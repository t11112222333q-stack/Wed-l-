#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Leak Scanner Pro v8.0 – Web Single-File Edition
Gộp Flask + Scanner + UI vào 1 file. Chỉ cần:
  pip install flask aiohttp
  python app.py
Rồi mở trình duyệt: http://localhost:5000

Cài thêm (optional):
  pip install dnspython         # cho DNS enum + DNS records
  pip install playwright && playwright install chromium   # cho screenshot

Changelog v8.0 (so với v7.0):
  + 🕰️ Wayback Machine: fetch paths lịch sử từ web.archive.org CDX API
    (limit 200), test lại trên target hiện tại, phát hiện paths cũ đã bị xoá.
  + 🌐 DNS subdomain enumeration thật: async resolve 60 subdomain candidate
    qua dnspython, trả A records (IP). Cần `pip install dnspython`.
  + 📡 DNS records: query A/AAAA/MX/NS/TXT/SOA cho main domain.
  + 📸 Playwright screenshot: chụp màn hình main page (1280x800), lưu vào
    /tmp/wlscan_screenshot_<id>.png, hiển thị trong UI qua /screenshot/<id>.
    Cần `pip install playwright && playwright install chromium`.
  + 🎯 Subdomain takeover check: với mỗi subdomain resolved, query CNAME,
    check pattern (heroku, github.io, s3.amazonaws.com, etc.) để phát hiện
    dịch vụ có thể bị takeover.
  + 🔒 CORS test: gửi `Origin: https://evil.com` tới main URL, kiểm tra
    reflection trong `Access-Control-Allow-Origin` header.
  + 🆕 Tab "Recon": gộp Wayback URLs + DNS subdomains + DNS records +
    takeover risks + CORS issues + screenshot.
  + 🆕 4 form toggle: Wayback / DNS enum / Screenshot / CORS test.
  + 🆕 Route GET /screenshot/<int:scan_id> serve ảnh PNG.
  + 📊 Stats mới: wayback_count, dns_subdomain_count, dns_record_count,
    takeover_risk_count, cors_issue_count.

Changelog v7.0 (so với v6.0):
  + 🕷️ Deep Crawl (recursive spider depth=2): đệ quy fetch links
    tìm được trên main page để khám phá thêm paths trên cùng domain.
  + 🗺️ Sitemap.xml deep parse: đọc sitemap.xml + sitemap index,
    parse <loc> URLs, add tất cả vào hàng đợi scan.
  + 🔌 API endpoint enumeration: tự tìm /api/v1/... /v2/.../graphql
    trong HTML và trong nội dung JS files.
  + 💬 HTML comments extraction: trích <!-- ... --> thường chứa
    debug info, TODO, version, developer notes.
  + 🔗 JS string URL extraction: tìm URL tuyệt đối + relative
    trong chuỗi JS (api endpoints, hidden routes, debug URLs).
  + 📚 +30 LEAK_PATHS mới (CMS-specific + framework-specific):
    WordPress /wp-json/wp/v2/users, /wp-content/debug.log,
    Drupal /sites/default/settings.php, Magento /app/etc/local.xml,
    Laravel /.env.example /storage/logs/laravel.log,
    Spring /actuator/heapdump, Django /admin/, etc.
  + 🔁 Recursive dir check: tìm /admin/ -> check /admin/login,
    /admin/config, /admin/backup, /admin/.env, etc.
  + ❓ Query param fuzzing: ?debug=1, ?test=1, ?source=1, ?dev=1,
    ?env=development, ?show_errors=1 trên main URL.
  + 🎯 2 UI tab mới: Crawled URLs, API Endpoints.
  + ⚙️ Form thêm toggle "Deep crawl (recursive, slower)".
  + 📊 Stats thêm: crawled_url_count, api_endpoint_count,
    comment_count, sitemap_url_count.

Changelog v6.0 (so với v5.0):
  + ⏱️ Real-time elapsed timer (mm:ss) + ETA ước tính còn lại.
  + ⚡ Requests/sec rate counter (số request hoàn thành/giây).
  + 🛑 Cancel Scan button + endpoint POST /cancel/<scan_id>.
  + 🎯 Soft-404 calibration: fetch 1 path random kỳ lạ trước,
    lưu size + signature, rồi filter các finding có pattern giống
    (giảm false positive khi target trả 200 cho mọi path).
  + 🚫 Ẩn phase "keepalive" và "connected" khỏi UI (chỉ là SSE heartbeat).
  + 📝 Phase human-readable tiếng Việt (snake_case -> "Đang quét leak paths...").
  + 📊 Sub-progress chi tiết: phase progress bar + ETA + rate ngay trong UI.
  + ⚡ Concurrency mặc định tăng: 15->25, WAF slow 5->8.
  + ⏱️ Timeout rút gọn cho brute-force (3s thay vì 10s) để scan nhanh hơn.
  + 📈 Mini stats live: requests/sec, found, elapsed, ETA, phase.
  + 🧹 Auto-dedup soft-404 khi render kết quả.

Changelog v5.0 (so với v4.0):
  + Security Headers Analysis (CSP, HSTS, X-Frame-Options, X-Content-Type-Options,
    Referrer-Policy, Permissions-Policy, X-XSS-Protection, X-Permitted-Cross-Domain-Policies).
  + Cookie Security Analysis (HttpOnly, Secure, SameSite, __Host- prefix).
  + HTTPS / SSL basic info (subject, issuer, days to expiry).
  + JavaScript file extraction + quét secret patterns trong nội dung JS
    (AWS keys, Google API key, Slack token, JWT, private key, …).
  + Sensitive Data Pattern Matching trong HTML (email, phone, JWT, AWS keys,
    private key, GitHub/Firebase/Stripe tokens).
  + Mở rộng WAF detection (Cloudflare, AWS WAF, Akamai, Imperva, Sucuri, F5,
    Wordfence, ModSecurity, Fastly, Barracuda, Fortinet, Datadome, PerimeterX).
  + Mở rộng LEAK_PATHS (+30 paths mới: .gitlab-ci.yml, firebase.json, .npmrc,
    service-account.json, id_rsa.pub, .dockerenv, .htpasswd, …).
  + Mở rộng TECH_SIGS (Next.js, Nuxt, Gatsby, SvelteKit, Express, Spring,
    Rails, Symfony, CodeIgniter, Craft CMS, Strapi, Ghost, Joomla, Magento, Shopify).
  + Form Detection (login forms, hidden inputs, file upload, CSRF tokens).
  + CDN Detection (Cloudflare, CloudFront, Akamai, Fastly, MaxCDN, BunnyCDN).
  + Auto-retry 429 (Too Many Requests) với exponential backoff.
  + Severity scoring (Critical/High/Medium/Low) cho từng finding.
  + Tabs UI (Summary / Leaks / Tech / Network / Sensitive / Raw).
  + Filter / search trong kết quả.
  + Export đa định dạng: JSON / CSV / standalone HTML.
  + Scan history (in-memory, 10 scan gần nhất).
  + Theme toggle Dark / Light.
  + Response time tracking từng request.
"""
import os, sys, re, json, time, random, asyncio, threading, queue, csv, io, ssl, socket, base64
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse, urljoin
from functools import wraps
from collections import OrderedDict

# ── v8.0 optional deps ──
try:
    import dns.asyncresolver
    import dns.resolver
    import dns.exception
    HAS_DNS = True
except ImportError:
    HAS_DNS = False

try:
    from playwright.async_api import async_playwright
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False


# ── Flask ──
from flask import Flask, request, render_template_string, jsonify, Response

app = Flask(__name__)
app.secret_key = os.urandom(32)

# ── Config ──
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
]
COMMON_PORTS = [80, 443, 8080, 8443, 3000, 5000, 8000, 8888, 9000, 9200, 21, 22, 25, 3306, 5432, 6379, 27017, 9090, 8161, 5601]
BLOCKED_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "::1", "169.254.169.254", "metadata.google.internal", "metadata"}
SCAN_HISTORY_MAX = 10

LEAK_PATHS = [
    # Common config / env
    "/robots.txt", "/sitemap.xml", "/.env", "/.env.local", "/.env.production",
    "/.env.development", "/.env.staging", "/.env.test", "/.env.example",
    "/.git/config", "/.git/HEAD", "/.git/index", "/.gitignore", "/.gitattributes",
    "/wp-config.php", "/config.php", "/configuration.php", "/settings.json",
    "/.htaccess", "/web.config", "/config.json", "/config.xml", "/config.yaml",
    "/config.yml", "/config.ini", "/appsettings.json", "/appsettings.Development.json",
    "/appsettings.Production.json", "/.htpasswd", "/.htaccess.bak", "/.htaccess.txt",
    # Backup / dumps
    "/backup.zip", "/backup.tar.gz", "/backup.tar", "/db.sql", "/dump.sql",
    "/database.sql", "/www.zip", "/www.tar.gz", "/site.zip", "/website.zip",
    "/backup.sql", "/backup.json", "/data.sql", "/data.json",
    # Admin panels
    "/admin/", "/administrator/", "/wp-admin/", "/phpmyadmin/", "/adminer.php",
    "/admin/login", "/manager/html", "/cpanel", "/.admin", "/wp-login.php",
    # Cloud / SSH / DevOps secrets
    "/.aws/credentials", "/.aws/config", "/.ssh/id_rsa", "/.ssh/id_rsa.pub",
    "/.ssh/authorized_keys", "/.ssh/known_hosts", "/.dockerenv", "/.dockercfg",
    "/.gitlab-ci.yml", "/.github/workflows/", "/firebase.json", "/service-account.json",
    "/google-services.json", "/GoogleService-Info.plist", "/.npmrc", "/.yarnrc",
    "/.netrc", "/.pypirc", "/.kube/config", "/.terraform.tfvars", "/terraform.tfstate",
    # API docs
    "/swagger.json", "/swagger.yaml", "/api-docs", "/openapi.json", "/openapi.yaml",
    "/swagger-ui/", "/swagger/", "/redoc", "/graphql", "/graphiql", "/altair",
    "/api/v1/", "/api/v2/", "/api/v3/", "/rest/", "/api/",
    # Package manifests
    "/package.json", "/package-lock.json", "/composer.json", "/composer.lock",
    "/Dockerfile", "/docker-compose.yml", "/docker-compose.yaml", "/Containerfile",
    "/Pipfile", "/Pipfile.lock", "/requirements.txt", "/Gemfile", "/Gemfile.lock",
    "/go.mod", "/go.sum", "/pom.xml", "/build.gradle", "/build.sbt",
    # History / debug
    "/.bash_history", "/.mysql_history", "/.psql_history", "/.viminfo",
    "/.phpstorm", "/.idea/", "/.vscode/", "/.DS_Store", "/Thumbs.db",
    "/phpinfo.php", "/info.php", "/_profiler/", "/symfony/", "/_debugbar/",
    "/actuator", "/actuator/health", "/actuator/env", "/actuator/mappings",
    "/actuator/heapdump", "/actuator/loggers", "/server-status", "/server-info",
    # VCS
    "/.svn/entries", "/.svn/wc.db", "/.hg/store", "/.bzr/", "/CVS/Root",
    # Misc
    "/install/", "/setup/", "/test/", "/temp/", "/tmp/", "/logs/", "/log/",
    "/old/", "/backup/", "/bak/", "/archive/", "/archives/", "/debug/",
    "/_files/", "/uploads/", "/files/", "/static/", "/public/",
    "/.well-known/security.txt", "/.well-known/openid-configuration",
    "/crossdomain.xml", "/clientaccesspolicy.xml", "/humans.txt", "/security.txt",
    "/.env~", "/.env.bak", "/.env.save", "/.env.sw", "/.env.swp", "/.env.old",
    "/error.log", "/access.log", "/debug.log", "/app.log",
]

TECH_SIGS = {
    "WordPress":   [("html", r'wp-content|wp-includes|wp-json|wordpress|xmlrpc\.php'), ("header", r'x-powered-by.*wordpress|wp-')],
    "Drupal":      [("html", r'drupal|sites/all|sites/default'), ("header", r'x-drupal|drupal\s')],
    "Joomla":      [("html", r'joomla|/media/jui/|/components/com_'), ("header", r'joomla')],
    "Magento":     [("html", r'magento|Mage\.|skin/frontend'), ("header", r'x-magento')],
    "Shopify":     [("html", r'cdn\.shopify\.com|Shopify\.theme')],
    "Laravel":     [("header", r'laravel_session'), ("html", r'laravel|csrf-token.*name="_token"')],
    "Symfony":     [("html", r'sf-container|symfony'), ("header", r'symfony')],
    "CodeIgniter": [("header", r'ci_session|codeigniter')],
    "Django":      [("header", r'csrftoken|django|csrfmiddlewaretoken'), ("html", r'csrfmiddlewaretoken')],
    "Flask":       [("header", r'flask|werkzeug'), ("cookie", r'session')],
    "Express":     [("header", r'x-powered-by.*express')],
    "Koa":         [("header", r'x-powered-by.*koa')],
    "Next.js":     [("html", r'__next|_next/static|next/dist'), ("header", r'x-powered-by.*next\.?js')],
    "Nuxt":        [("html", r'__nuxt|_nuxt/|nuxt-link')],
    "Gatsby":      [("html", r'gatsby|___gatsby')],
    "SvelteKit":   [("html", r'sveltekit|__sveltekit|svelte-')],
    "Vue.js":      [("html", r'vue[.-]\d|data-v-[a-z0-9]+|__VUE__|__NUXT__')],
    "React":       [("html", r'reactroot|data-react|react\.js|react-dom')],
    "Angular":     [("html", r'ng-\w+|angular[./]|ng-version')],
    "Svelte":      [("html", r'svelte-[a-z0-9]+')],
    "PHP":         [("header", r'x-powered-by.*php|php/'), ("html", r'\.php\?|phpsessid')],
    "ASP.NET":     [("header", r'x-aspnet|x-powered-by.*asp\.net|aspsessionid|aspnet'), ("cookie", r'asp\.net') , ("header", r'x-aspnetmvc')],
    "Ruby on Rails":[("header", r'x-powered-by.*rails|x-runtime|x-request-id'), ("cookie", r'_session|_rails')],
    "Spring Boot": [("header", r'x-application-context'), ("html", r'/actuator')],
    "Node.js":     [("header", r'x-powered-by.*nodejs|x-powered-by.*express')],
    "Nginx":       [("header", r'server.*nginx')],
    "Apache":      [("header", r'server.*apache')],
    "LiteSpeed":   [("header", r'server.*litespeed')],
    "IIS":         [("header", r'server.*microsoft-iis')],
    "Cloudflare":  [("header", r'cf-ray|cloudflare|cf-cache-status')],
    "jQuery":      [("html", r'jquery[.-]\d+\.\d+|jquery\.min\.js')],
    "Bootstrap":   [("html", r'bootstrap[./]|bootstrap\.min\.css')],
    "TailwindCSS": [("html", r'tailwind|tw-|\.bg-[\w-]+|\.flex|\.grid')],
    "Bulma":       [("html", r'bulma')],
    "Material-UI": [("html", r'mui-|material-ui|MuiButton')],
    "Ant Design":  [("html", r'ant-|ant-btn|ant-card')],
    "ElementUI":   [("html", r'el-button|el-input|element-ui')],
    "Vuetify":     [("html", r'vuetify|v-app|v-card')],
    "Ghost":       [("header", r'x-ghost'), ("html", r'ghost-')],
    "Strapi":      [("header", r'x-powered-by.*strapi'), ("html", r'strapi')],
    "Craft CMS":   [("html", r'craftcms|craft/app')],
}

WAF_SIGS = [
    ("Cloudflare",   [r'cf-ray', r'cloudflare', r'cf-cache-status', r'__cf_bm']),
    ("AWS WAF",      [r'x-amzn-requestid', r'x-amz-cf-id', r'awselb']),
    ("Akamai",       [r'akamai', r'akamaighost', r'ak_bmsc', r'_abck']),
    ("Imperva/Incapsula", [r'incap_ses', r'visid_incap', r'x-iinfo', r'incapsula']),
    ("Sucuri",       [r'x-sucuri-id', r'sucuri']),
    ("F5 BIG-IP",    [r'bigipserver', r'tmm_api', r'x-cnection']),
    ("Wordfence",    [r'wordfence', r'wf_']),
    ("ModSecurity",  [r'mod_security', r'nginx-mod-security', r'x-mod-security']),
    ("Fastly",       [r'fastly', r'x-served-by.*cache', r'x-fastly']),
    ("Barracuda",    [r'barracuda', r'barra']),
    ("Fortinet",     [r'fortinet', r'fortiweb']),
    ("Datadome",     [r'datadome', r'dd_cookie']),
    ("PerimeterX",   [r'pxhd', r'perimeterx', r'px-captcha']),
    ("Reblaze",      [r'rbzid', r'reblaze']),
    "Rate Limit (generic, HTTP 429)",
]

# Security headers to check (key, header_name, severity if missing)
SECURITY_HEADERS = [
    ("strict-transport-security", "Strict-Transport-Security (HSTS)", "high"),
    ("content-security-policy", "Content-Security-Policy (CSP)", "high"),
    ("x-frame-options", "X-Frame-Options", "medium"),
    ("x-content-type-options", "X-Content-Type-Options", "medium"),
    ("referrer-policy", "Referrer-Policy", "low"),
    ("permissions-policy", "Permissions-Policy", "low"),
    ("x-xss-protection", "X-XSS-Protection (legacy)", "info"),
    ("x-permitted-cross-domain-policies", "X-Permitted-Cross-Domain-Policies", "info"),
    ("cross-origin-opener-policy", "Cross-Origin-Opener-Policy", "medium"),
    ("cross-origin-resource-policy", "Cross-Origin-Resource-Policy", "medium"),
]

# Sensitive data patterns (name, regex, severity, description)
SECRET_PATTERNS = [
    ("AWS Access Key ID",      r'AKIA[0-9A-Z]{16}',                                "critical", "AWS Access Key - cho phép gọi API AWS"),
    ("AWS Secret Key",         r'aws_secret_access_key["\']?\s*[:=]\s*["\']?[A-Za-z0-9/+=]{40}', "critical", "AWS Secret Key"),
    ("Google API Key",         r'AIza[0-9A-Za-z_\-]{35}',                          "high",     "Google API Key"),
    ("Google OAuth Refresh",   r'1/[0-9A-Za-z_\-]{43}',                            "high",     "Google OAuth refresh token"),
    ("Slack Token",            r'xox[abprs]-[0-9A-Za-z-]{10,}',                    "high",     "Slack token"),
    ("Slack Webhook",          r'https://hooks\.slack\.com/services/T[A-Z0-9]+',    "high",     "Slack incoming webhook"),
    ("Stripe Secret Key",      r'sk_live_[0-9A-Za-z]{24,}',                        "critical", "Stripe secret key (live)"),
    ("Stripe Restricted Key",  r'rk_live_[0-9A-Za-z]{24,}',                        "critical", "Stripe restricted key"),
    ("GitHub Token",           r'gh[pousr]_[A-Za-z0-9]{36,}',                      "critical", "GitHub personal access token"),
    ("GitHub OAuth Token",      r'gho_[A-Za-z0-9]{36}',                             "critical", "GitHub OAuth token"),
    ("GitLab Token",           r'glpat-[A-Za-z0-9_\-]{20}',                        "high",     "GitLab personal access token"),
    ("Heroku API Key",         r'(?:heroku_api_key|heroku_api_token)["\']?\s*[:=]\s*["\']?[0-9a-fA-F]{32}', "high", "Heroku API key"),
    ("JWT Token",              r'eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}', "high", "JWT token - có thể leak claims"),
    ("Private Key PEM",        r'-----BEGIN (RSA|EC|DSA|OPENSSH|PGP) PRIVATE KEY-----', "critical", "Private key PEM"),
    ("Generic Secret",        r'(?:secret|api[_-]?key|token|passwd|password)["\']?\s*[:=]\s*["\']?[A-Za-z0-9+/=_\-]{16,}', "medium", "Generic secret / api key"),
    ("Firebase URL",          r'https?://[a-z0-9\-]+\.firebaseio\.com',            "high",     "Firebase realtime DB URL"),
    ("Firebase Config",        r'firebaseConfig\s*=\s*\{[^}]*?(?:apiKey|databaseURL|projectId)[^}]*?\}', "high", "Firebase client config"),
    ("Twilio SID",            r'AC[a-z0-9]{32}',                                  "high",     "Twilio Account SID"),
    ("Square OAuth Secret",   r'sq0csp-[0-9A-Za-z_\-]{43}',                       "high",     "Square OAuth secret"),
    ("Mailgun API Key",       r'key-[0-9a-zA-Z]{32}',                             "high",     "Mailgun API key"),
    ("SendGrid API Key",      r'SG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}',    "high",     "SendGrid API key"),
    ("Email Address",         r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "low", "Email address"),
    ("Internal IPv4",         r'\b(?:10|172\.(?:1[6-9]|2[0-9]|3[01])|192\.168)\.\d{1,3}\.\d{1,3}\b', "info", "Private/internal IPv4"),
    ("US Phone",              r'\+1\s?\(?[2-9]\d{2}\)?[\s.-]?[2-9]\d{2}[\s.-]?\d{4}', "info", "US phone (E.164-ish)"),
]

# CDN detection
CDN_SIGS = [
    ("Cloudflare",     [r'cf-ray', r'cloudflare', r'cf-cache-status']),
    ("AWS CloudFront", [r'x-amz-cf-id', r'x-amz-cf-pop', r'cloudfront']),
    ("Akamai",         [r'akamai', r'x-akamai-transformed']),
    ("Fastly",         [r'x-served-by.*cache', r'x-fastly', r'fastly']),
    ("MaxCDN",         [r'maxcdn', r'x-cdn']),
    ("BunnyCDN",       [r'bunnycdn', r'server.*bunny']),
    ("KeyCDN",         [r'x-edge-ip', r'keycdn']),
    ("CDN77",          [r'cdn77', r'x-77']),
    ("jsDelivr",       [r'jsdelivr']),
]

# Subdomain suggestions shown for recon (no network call – just hints)
COMMON_SUBDOMAINS = [
    "www", "mail", "remote", "blog", "shop", "dev", "test", "stage", "staging",
    "api", "app", "admin", "portal", "vpn", "m", "mobile", "secure", "secure2",
    "git", "gitlab", "jenkins", "jira", "wiki", "docs", "support", "help",
    "status", "cdn", "static", "assets", "media", "img", "images", "video",
    "sso", "auth", "login", "id", "account", "profile", "dashboard", "panel",
    "beta", "demo", "preview", "old", "new", "internal", "intranet", "extranet",
    "ns1", "ns2", "dns", "mx", "smtp", "imap", "pop", "ftp", "sftp",
]

# ── v7.0: CMS-specific & framework-specific leak paths ──
EXTRA_LEAK_PATHS_V7 = [
    # WordPress
    "/wp-json/wp/v2/users", "/wp-json/", "/wp-content/debug.log", "/wp-content/uploads/",
    "/wp-content/backups/", "/wp-content/backup-db/", "/readme.html", "/license.txt",
    "/wp-config.php.bak", "/wp-config.php.save", "/wp-config.php.old",
    "/wp-content/uploads/wpallimport/", "/wp-admin/install.php", "/wp-links-opml.php",
    "/wp-includes/version.php", "/wp-content/plugins/", "/wp-content/themes/",
    "/wp-content/upgrade/", "/wp-content/cache/", "/wp-content/wflogs/",
    # Joomla
    "/components/com_users/", "/administrator/manifests/files/joomla.xml",
    "/language/en-GB/en-GB.xml", "/templates/", "/modules/", "/plugins/",
    "/cache/", "/logs/joomla.log", "/configuration.php.bak",
    # Drupal
    "/sites/default/settings.php", "/sites/default/files/", "/sites/default/private/",
    "/core/CHANGELOG.txt", "/core/install.php", "/update.php", "/cron.php",
    "/xmlrpc.php", "/user/login", "/user/register", "/admin/config",
    # Magento
    "/app/etc/local.xml", "/var/log/exception.log", "/var/log/system.log",
    "/errors/", "/downloader/", "/shell/", "/media/import/",
    # Laravel / Symfony
    "/.env.example", "/storage/logs/laravel.log", "/storage/framework/cache/",
    "/vendor/", "/app/config/", "/bootstrap/cache/", "/routes/web.php",
    "/.env.backup", "/.env.dev", "/.env.staging",
    # Spring Boot actuator (already have some)
    "/actuator/heapdump", "/actuator/threaddump", "/actuator/mappings",
    "/actuator/configprops", "/actuator/beans", "/actuator/logfile",
    "/actuator/httptrace", "/actuator/auditevents", "/actuator/scheduledtasks",
    # Django / Flask
    "/admin/login/", "/admin/?next=/", "/static/admin/", "/media/",
    "/debug/", "/sentry/", "/__debug__/", "/config/settings.py.bak",
    # Rails
    "/rails/info", "/rails/info/routes", "/rails/mailers", "/Gemfile",
    # Express / Node
    "/node_modules/", "/.node_repl_history", "/yarn-error.log", "/yarn.lock",
    "/npm-debug.log", "/.pm2/", "/forever/", "/.pnp.cjs", "/.pnp.js",
    # DevOps / CI/CD
    "/.gitlab-ci.yml", "/.travis.yml", "/.circleci/config.yml",
    "/bitbucket-pipelines.yml", "/.github/workflows/ci.yml",
    "/azure-pipelines.yml", "/Jenkinsfile", "/.drone.yml",
    "/.dockerignore", "/Dockerfile", "/docker-compose.override.yml",
    # Cloud / buckets
    "/.s3/", "/.gs/", "/.azure/", "/.aliyun/", "/.do-spaces/",
    "/assets/", "/static/", "/public/", "/dist/", "/build/",
    # Common admin panels
    "/manager/", "/cpanel/", "/whm/", "/directadmin/", "/vesta/",
    "/cockpit/", "/webmin/", "/z-panel/", "/ispconfig/", "/virtualmin/",
    # Logs / debug files
    "/var/log/", "/var/log/nginx/access.log", "/var/log/apache2/access.log",
    "/var/log/mysql/error.log", "/var/log/auth.log", "/var/log/syslog",
    "/log/error.log", "/log/access.log", "/logs/error.log", "/debug/error.log",
    "/php_errors.log", "/error_log", "/stderr.log", "/stdout.log",
    # Common backup files
    "/backup/db_backup.sql", "/backup/db.sql", "/backup/site.zip",
    "/backup/www.tar.gz", "/backup/latest.zip", "/backup/database.sql.gz",
    # Container / k8s
    "/.docker/", "/.kubernetes/", "/run/secrets/", "/var/run/secrets/",
    "/etc/passwd", "/etc/shadow", "/etc/hosts", "/etc/hostname",
    "/proc/self/environ", "/proc/self/cmdline",
    # Other
    "/.well-known/openid-configuration", "/.well-known/jwks.json",
    "/.well-known/apple-app-site-association", "/apple-app-site-association",
    "/assetlinks.json", "/.well-known/assetlinks.json",
    "/BingSiteAuth.xml", "/yandex_*.html", "/google.html",
    "/sftp-config.json", "/rsync.conf", "/.vscode/sftp.json",
    "/composer.phar", "/phpunit.xml", "/phpunit.xml.dist",
    "/.phpunit.result.cache", "/.phpunit.cache/",
]

# Common API endpoint patterns (relative to base)
API_ENDPOINTS = [
    "/api", "/api/", "/api/v1", "/api/v1/", "/api/v2", "/api/v2/",
    "/api/v3", "/api/v3/", "/api/users", "/api/user", "/api/admin",
    "/api/auth", "/api/login", "/api/logout", "/api/register",
    "/api/products", "/api/orders", "/api/customers", "/api/items",
    "/api/posts", "/api/comments", "/api/articles", "/api/categories",
    "/api/files", "/api/upload", "/api/download", "/api/search",
    "/api/health", "/api/status", "/api/version", "/api/info",
    "/api/me", "/api/profile", "/api/account", "/api/settings",
    "/api/messages", "/api/notifications", "/api/sessions", "/api/tokens",
    "/api/key", "/api/keys", "/api/secrets", "/api/config",
    "/api/swagger", "/api/docs", "/api/openapi", "/api/spec",
    "/v1/users", "/v1/admin", "/v1/auth", "/v1/health", "/v1/status",
    "/v2/users", "/v2/admin", "/v2/auth", "/v2/health",
    "/rest/users", "/rest/admin", "/rest/auth", "/rest/health",
    "/graphql", "/graphiql", "/playground", "/altair",
    "/api/graphql", "/api/graphiql",
    "/users.json", "/admin.json", "/config.json", "/settings.json",
    "/api/.env", "/api/config.yml", "/api/swagger.json",
    "/internal/api", "/internal/health", "/internal/status",
    "/debug/status", "/debug/pprof", "/debug/vars",
    "/healthz", "/health", "/healthcheck", "/statusz",
    "/metrics", "/prometheus", "/grafana", "/api/metrics",
    "/api/v1/swagger.json", "/api/v1/openapi.json", "/api/v2/swagger.json",
]

# Query params fuzzing (test trên main URL)
QUERY_PARAM_FUZZ = [
    "?debug=1", "?test=1", "?dev=1", "?source=1", "?backup=1",
    "?admin=1", "?env=development", "?env=dev", "?show_errors=1",
    "?error=1", "?log=1", "?trace=1", "?verbose=1", "?detail=1",
    "?profile=1", "?profiling=1", "?debug=true", "?XDEBUG_SESSION_START=1",
    "?_method=DELETE", "?_method=PUT", "?_method=PATCH",
]

# Sub-paths thử khi tìm thấy 1 directory (recursive dir check)
RECURSIVE_DIR_PROBES = [
    "login", "config", "backup", ".env", "settings.php", "config.php",
    "admin", "users", "database", "db", "test", "panel", "dashboard",
    "settings", "credentials", "secret", "private", "log", "logs",
]

# Config cho spider
SPIDER_MAX_URLS = 50
SPIDER_MAX_DEPTH = 2
SITEMAP_MAX_URLS = 100

# v8.0: Wayback Machine
WAYBACK_MAX_URLS = 200

# v8.0: Subdomain takeover patterns (CNAME -> service). Nếu service không còn
# control bởi chủ sở hữu domain hiện tại → có thể takeover.
TAKEOVER_CNAME_PATTERNS = [
    (r'\.herokuapp\.com',           "Heroku (challenge CNAME)",              "high"),
    (r'\.herokudns\.com',           "Heroku DNS",                            "high"),
    (r'\.github\.io',               "GitHub Pages",                          "high"),
    (r'\.bitbucket\.io',            "Bitbucket Pages",                       "high"),
    (r'\.s3\.amazonaws\.com',       "AWS S3 bucket",                         "high"),
    (r'\.s3-website[\-\.].*\.amazonaws\.com', "AWS S3 website",              "high"),
    (r'stdente\.azurewebsites\.net', "Azure (StdEnv)",                        "high"),
    (r'\.azurewebsites\.net',       "Azure Web Apps",                        "high"),
    (r'\.cloudapp\.net',            "Azure CloudApp",                        "medium"),
    (r'\.trafficmanager\.net',      "Azure Traffic Manager",                 "medium"),
    (r'\.elasticbeanstalk\.com',    "AWS Elastic Beanstalk",                 "medium"),
    (r'\.cloudfront\.net',          "CloudFront (s3 origin)",                "medium"),
    (r'\.myshopify\.com',           "Shopify",                                "high"),
    (r'\.tumblr\.com',             "Tumblr",                                 "high"),
    (r'\.pantheon\.io',            "Pantheon",                               "high"),
    (r'\.ghost\.io',               "Ghost",                                  "high"),
    (r'\.wordpress\.com',          "WordPress.com",                          "high"),
    (r'\.surge\.sh',              "Surge.sh",                               "high"),
    (r'\.netlify\.app',           "Netlify",                                "high"),
    (r'\.vercel\.app',            "Vercel",                                 "high"),
    (r'\.firebaseapp\.com',       "Firebase",                               "high"),
    (r'\.web\.app',               "Firebase",                               "high"),
    (r'\.pagespeedmobilizer\.com', "Google PageSpeed",                      "high"),
    (r'\.ngrok\.io',              "ngrok",                                  "medium"),
    (r'\.ngrok\.app',             "ngrok",                                  "medium"),
    (r'\.teamwork\.com',          "Teamwork",                               "high"),
    (r'\.helpscoutdocs\.com',      "HelpScout",                             "high"),
    (r'\.feedpress\.me',          "FeedPress",                             "high"),
    (r'\.freshdesk\.com',         "Freshdesk",                              "high"),
    (r'\.zendesk\.com',           "Zendesk",                                "high"),
    (r'\.cargo\.site',            "Cargo",                                  "high"),
    (r'\.squarespace\.com',       "Squarespace",                            "high"),
    (r'\.webflow\.io',           "Webflow",                                 "high"),
    (r'\.cargocollective\.com',  "Cargo Collective",                       "high"),
    (r'\.smugmug\.com',          "Smugmug",                                "high"),
    (r'\.statuspage\.io',        "StatusPage",                             "high"),
    (r'\.status\.page',          "StatusPage",                             "high"),
    (r'\.fastly\.net',           "Fastly",                                 "medium"),
]

# v8.0: Screenshot directory
SCREENSHOT_DIR = "/tmp/wlscan_screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# ── Validators ──
import ipaddress

def validate_target(url):
    if not url:
        raise ValueError("URL không được để trống")
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    parsed = urlparse(url)
    if not parsed.hostname:
        raise ValueError("Hostname không hợp lệ")
    hn = parsed.hostname.lower()
    if hn in BLOCKED_HOSTS:
        raise ValueError(f"'{hn}' bị chặn (SSRF protection)")
    # IP literal checks (only if hostname IS an IP literal)
    try:
        ip = ipaddress.ip_address(hn)
    except ValueError:
        # not an IP literal (it's a DNS name) -> skip IP-based checks
        ip = None
    if ip is not None:
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            raise ValueError("IP private / loopback / link-local / reserved bị chặn (SSRF protection)")
    if "@" in parsed.netloc:
        raise ValueError("URL chứa '@' – bị chặn (anti-redirect trick)")
    if "\\" in url:
        raise ValueError("URL chứa backslash – bị chặn")
    return url

def parse_headers(raw):
    headers = {}
    if not raw:
        return headers
    for part in re.split(r'[;,]', raw):
        part = part.strip()
        if ":" in part:
            k, v = part.split(":", 1)
            headers[k.strip()] = v.strip()
    return headers

def get_ssl_info(host, port=443, timeout=5):
    """Returns dict with subject, issuer, not_after, days_remaining (or None on failure)."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                subject = dict(x[0] for x in cert.get("subject", [])) if cert else {}
                issuer = dict(x[0] for x in cert.get("issuer", [])) if cert else {}
                not_after = cert.get("notAfter") if cert else None
                days = None
                if not_after:
                    try:
                        end = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                        days = (end - datetime.utcnow()).days
                    except Exception:
                        pass
                return {
                    "subject": subject.get("commonName", ""),
                    "issuer": issuer.get("commonName", ""),
                    "not_after": not_after,
                    "days_remaining": days,
                }
    except Exception as e:
        return {"error": str(e)[:120]}

def severity_rank(s):
    return {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}.get(s, 0)

# ── Async Scanner ──
try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False
    print("[!] aiohttp chưa cài – pip install aiohttp")

async def fetch(session, url, headers=None, proxy=None, timeout=10, max_retries=2):
    """Fetch với auto-retry khi gặp 429 (exponential backoff)."""
    if not HAS_AIOHTTP:
        return "", 0, {}, 0
    last_err = None
    for attempt in range(max_retries + 1):
        start = time.time()
        try:
            async with session.get(url, headers=headers, proxy=proxy,
                                    timeout=aiohttp.ClientTimeout(total=timeout),
                                    ssl=False, allow_redirects=True) as r:
                text = await r.text(errors="replace")
                elapsed = round((time.time() - start) * 1000, 1)
                if r.status == 429 and attempt < max_retries:
                    backoff = (2 ** attempt) + random.uniform(0, 0.5)
                    await asyncio.sleep(backoff)
                    continue
                return text, r.status, dict(r.headers), elapsed
        except Exception as e:
            elapsed = round((time.time() - start) * 1000, 1)
            last_err = e
            if attempt < max_retries:
                await asyncio.sleep(0.4 * (attempt + 1))
                continue
    return str(last_err)[:100] if last_err else "", 0, {}, 0

async def scan_ports(host):
    if not HAS_AIOHTTP:
        return []
    async def check(p):
        try:
            r, w = await asyncio.wait_for(asyncio.open_connection(host, p), timeout=1.2)
            try:
                w.close(); await w.wait_closed()
            except Exception:
                pass
            return p
        except Exception:
            return None
    return sorted([p for p in await asyncio.gather(*[check(p) for p in COMMON_PORTS]) if p])

def detect_tech(html, headers, cookies=None):
    techs = []
    hl = {k.lower(): str(v).lower() for k, v in headers.items()}
    cl = [c.lower() for c in (cookies or [])]
    html_l = (html or "").lower()
    for tech, sigs in TECH_SIGS.items():
        for st, pat in sigs:
            if st == "header":
                if any(re.search(pat, v, re.I) for v in hl.values()):
                    techs.append(tech); break
            elif st == "cookie":
                if any(re.search(pat, c, re.I) for c in cl):
                    techs.append(tech); break
            elif st == "html" and re.search(pat, html_l, re.I):
                techs.append(tech); break
    return sorted(set(techs))

def detect_waf(headers, code, text):
    hs = json.dumps(headers).lower()
    wafs, recs = [], []
    for sig in WAF_SIGS:
        if isinstance(sig, str):
            # Rate Limit (generic)
            if code == 429 and "Rate Limit" not in wafs:
                wafs.append(sig)
                recs.append("Server trả 429 Too Many Requests – giảm concurrency, tăng delay")
            continue
        name, pats = sig
        if name in wafs:
            continue
        for p in pats:
            if re.search(p, hs, re.I):
                wafs.append(name)
                if name == "Cloudflare":
                    recs.append("Cloudflare: giảm concurrent xuống 5-8, xoay UA, tránh /admin/ liệt kê")
                elif name in ("AWS WAF", "Akamai", "Imperva/Incapsula", "F5 BIG-IP"):
                    recs.append(f"{name}: Dùng token bucket, giới hạn 3-5 req/giây")
                else:
                    recs.append(f"{name}: Giảm tốc, dùng retry backoff, có thể cần CAPTCHA")
                break
    return {"detected": wafs, "recommendations": recs, "should_slow_down": len(wafs) > 0}

def detect_cdn(headers):
    hs = json.dumps(headers).lower()
    cdns = []
    for name, pats in CDN_SIGS:
        if any(re.search(p, hs, re.I) for p in pats):
            cdns.append(name)
    return sorted(set(cdns))

def analyze_security_headers(headers):
    """Trả về list of {header, present, value, severity}."""
    hl = {k.lower(): v for k, v in headers.items()}
    out = []
    for hname, display, sev in SECURITY_HEADERS:
        v = hl.get(hname)
        out.append({
            "header": display,
            "present": v is not None,
            "value": (v[:200] + "...") if v and len(v) > 200 else (v or ""),
            "severity": sev if v is None else "info",
            "missing": v is None,
        })
    return out

def analyze_cookies(headers):
    """Phân tích Set-Cookie flags (HttpOnly, Secure, SameSite, prefix)."""
    out = []
    raw = headers.get("Set-Cookie") or headers.get("set-cookie")
    if not raw:
        return out
    # Gom nhiều set-cookie (Flask gộp thành một list nếu là from aiohttp)
    if isinstance(raw, str):
        cookies = [c.strip() for c in raw.split(",") if "=" in c.split(";")[0]]
    else:
        cookies = list(raw)
    for c in cookies:
        if "=" not in c:
            continue
        name, _, rest = c.partition("=")
        name = name.strip()
        val = rest.split(";")[0]
        attrs = [a.strip().lower() for a in rest.split(";")[1:]]
        flags = {
            "httponly":  "httponly" in attrs,
            "secure":    "secure" in attrs,
            "samesite":  next((a.split("=",1)[1] for a in attrs if a.startswith("samesite")), None),
            "host_prefix": name.startswith("__host-"),
            "secure_prefix": name.startswith("__secure-"),
        }
        issues = []
        if not flags["httponly"]:
            issues.append("Thiếu HttpOnly (XSS cookie theft)")
        if not flags["secure"]:
            issues.append("Thiếu Secure (leak qua HTTP)")
        if not flags["samesite"]:
            issues.append("Thiếu SameSite (CSRF)")
        out.append({
            "name": name,
            "value_preview": val[:40] + ("..." if len(val) > 40 else ""),
            "flags": flags,
            "issues": issues,
        })
    return out

def scan_secrets(text, label):
    """Quét text tìm các secret patterns. Trả về list of {type, severity, match, label}."""
    out = []
    if not text:
        return out
    for name, pat, sev, desc in SECRET_PATTERNS:
        for m in re.finditer(pat, text, re.I):
            snippet = m.group(0)
            # Che bớt một phần để tránh leak hoàn toàn khi export
            masked = snippet[:8] + "*" * (max(0, len(snippet) - 12)) + snippet[-4:] if len(snippet) > 16 else snippet[:2] + "***"
            out.append({
                "type": name,
                "severity": sev,
                "match_masked": masked,
                "description": desc,
                "source": label,
            })
    # Dedup theo (type, masked)
    seen = set()
    deduped = []
    for s in out:
        k = (s["type"], s["match_masked"])
        if k not in seen:
            seen.add(k); deduped.append(s)
    return deduped

def extract_js_links(html, base):
    """Trích link file .js từ HTML. Trả về list of absolute URLs (unique)."""
    if not html:
        return []
    links = set()
    for m in re.finditer(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)["\']', html, re.I):
        u = m.group(1)
        if u.startswith(("http://", "https://", "//")):
            links.add(u if u.startswith("http") else ("https:" + u))
        elif u.startswith("/"):
            links.add(urljoin(base, u))
        else:
            links.add(urljoin(base + "/", u))
    return sorted(links)[:30]

def extract_forms(html, base):
    """Trích <form> từ HTML. Trả về list of dicts."""
    if not html:
        return []
    forms = []
    for m in re.finditer(r'<form[^>]*>(.*?)</form>', html, re.I | re.S):
        block = m.group(0)
        action = re.search(r'action=["\']([^"\']*)["\']', block, re.I)
        method = re.search(r'method=["\']([^"\']*)["\']', block, re.I)
        action_url = action.group(1) if action else ""
        if action_url and not action_url.startswith(("http://", "https://", "//")):
            action_url = urljoin(base, action_url) if action_url.startswith("/") else urljoin(base + "/", action_url)
        meth = (method.group(1) if method else "GET").upper()
        # detect inputs
        inputs = re.findall(r'<input[^>]*>', block, re.I)
        input_summary = []
        has_password = False
        has_file = False
        has_hidden = False
        has_csrf = False
        for inp in inputs:
            name = re.search(r'name=["\']([^"\']*)["\']', inp, re.I)
            type_ = re.search(r'type=["\']([^"\']*)["\']', inp, re.I)
            t = (type_.group(1).lower() if type_ else "text")
            n = (name.group(1) if name else "")
            if t == "password":
                has_password = True
            elif t == "file":
                has_file = True
            elif t == "hidden":
                has_hidden = True
                if re.search(r'csrf|_token|authenticity', n, re.I):
                    has_csrf = True
            input_summary.append({"name": n, "type": t})
        form_type = "login" if has_password else ("upload" if has_file else "generic")
        forms.append({
            "action": action_url,
            "method": meth,
            "type": form_type,
            "has_password": has_password,
            "has_file": has_file,
            "has_hidden": has_hidden,
            "has_csrf_token": has_csrf,
            "input_count": len(input_summary),
            "inputs_preview": input_summary[:10],
        })
    return forms

# ── v7.0: Spider & discovery helpers ──

def extract_all_links(html, base, target_netloc=None):
    """Trích TẤT CẢ link từ HTML: href, src, action + URL trong JS inline
    + meta refresh + canonical. Trả về list of absolute URLs (unique, same domain)."""
    if not html:
        return []
    parsed_base = urlparse(base)
    target_netloc = target_netloc or parsed_base.netloc
    links = set()

    # 1. href / src / action / data-src / data-url / poster
    for m in re.finditer(r'(?:href|src|action|poster|data-src|data-url|data-href|data-action)\s*=\s*["\']([^"\']+)["\']', html, re.I):
        u = m.group(1).strip()
        _add_link(links, u, base, target_netloc)

    # 2. Meta refresh
    for m in re.finditer(r'<meta[^>]+http-equiv=["\']?refresh["\']?[^>]*content=["\']?[^"\';]+;\s*url=([^"\']+)["\']', html, re.I):
        _add_link(links, m.group(1), base, target_netloc)

    # 3. Canonical
    for m in re.finditer(r'<link[^>]+rel=["\']?canonical["\']?[^>]+href=["\']?([^"\'>\s]+)', html, re.I):
        _add_link(links, m.group(1), base, target_netloc)

    # 4. URL trong JS inline (string literals)
    for m in re.finditer(r'["\'](/[A-Za-z0-9_\-./?=&%+#]*)["\']', html):
        u = m.group(1)
        if u.startswith('/') and not u.startswith('//') and len(u) > 2:
            _add_link(links, u, base, target_netloc)

    # 5. Absolute URLs in JS
    for m in re.finditer(r'(?:https?:)//([A-Za-z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]+)', html):
        u = m.group(0)
        if urlparse(u).netloc == target_netloc:
            links.add(u)

    return sorted(links)

def _add_link(links_set, u, base, target_netloc):
    """Helper: thêm u vào links_set nếu cùng domain và hợp lệ."""
    if not u or u.startswith(("#", "javascript:", "mailto:", "data:", "tel:", "sms:", "blob:", "about:")):
        return
    if u.startswith(("http://", "https://")):
        if urlparse(u).netloc == target_netloc:
            links_set.add(u)
    elif u.startswith("//"):
        # protocol-relative
        full = "https:" + u
        if urlparse(full).netloc == target_netloc:
            links_set.add(full)
    elif u.startswith("/"):
        links_set.add(urljoin(base, u))
    else:
        links_set.add(urljoin(base + "/", u))

def parse_sitemap(xml_text, base):
    """Parse sitemap.xml hoặc sitemap index. Trả về list of URLs (max SITEMAP_MAX_URLS)."""
    if not xml_text:
        return []
    urls = []
    # Standard sitemap: <url><loc>...</loc></url>
    for m in re.finditer(r'<loc>\s*([^<]+?)\s*</loc>', xml_text, re.I):
        u = m.group(1).strip()
        if u and u.startswith(("http://", "https://")):
            urls.append(u)
        elif u and u.startswith("/"):
            urls.append(urljoin(base, u))
        if len(urls) >= SITEMAP_MAX_URLS:
            break
    # Dedup + sort
    return sorted(set(urls))

def extract_html_comments(html, max_count=30):
    """Trích <!-- ... --> comments. Bỏ qua các comment quá ngắn hoặc boilerplate."""
    if not html:
        return []
    out = []
    for m in re.finditer(r'<!--(.*?)-->', html, re.S):
        c = m.group(1).strip()
        if not c:
            continue
        # Bỏ comment boilerplate (DOCTYPE-ish, conditional IE, empty)
        if c.lower().startswith(("doctype", "[if", "[endif", "end")):
            continue
        if len(c) < 3:
            continue
        # Giới hạn độ dài
        c_short = c[:300] + ("..." if len(c) > 300 else "")
        out.append(c_short)
        if len(out) >= max_count:
            break
    return out

def extract_api_endpoints(text, base, target_netloc=None):
    """Tìm API endpoint patterns trong text (HTML hoặc JS)."""
    if not text:
        return []
    parsed_base = urlparse(base)
    target_netloc = target_netloc or parsed_base.netloc
    endpoints = set()

    # Pattern 1: /api/..., /v1/..., /v2/..., /rest/..., /graphql, /internal/...
    # Path chars chỉ gồm chữ/số/gạch/underline/chấm/dấu hỏi/, — KHÔNG có ')', '('
    pattern = r'["\']((?:/api(?:/v\d+)?(?:/[A-Za-z0-9_\-./?=&%]+)?|/v\d+/[A-Za-z0-9_\-./?=&%]+|/rest/[A-Za-z0-9_\-./?=&%]+|/graphql|/internal/[A-Za-z0-9_\-./?=&%]+|/debug/(?:pprof|vars|status)))(?:["\']|[?\s]|$)'
    for m in re.finditer(pattern, text, re.I):
        path = m.group(1).rstrip('.,;)')
        if len(path) > 2 and not path.startswith("//"):
            full = urljoin(base, path)
            endpoints.add((path, full))

    # Pattern 2: absolute URLs có /api/ hoặc /v1/ /v2/ hoặc /graphql cùng domain
    # Sử dụng pattern hẹp - chỉ ký tự URL hợp lệ, sau đó strip trailing punctuation
    abs_pat = r'https?://[A-Za-z0-9\-._~:/?#@!$&+,%=]+'
    for m in re.finditer(abs_pat, text):
        u = m.group(0).rstrip('.,;)\'"')
        try:
            pu = urlparse(u)
            if pu.netloc == target_netloc and re.search(r'/api/|/v\d+/|/graphql|/rest/|/internal/', pu.path):
                endpoints.add((pu.path + (("?" + pu.query) if pu.query else ""), u))
        except Exception:
            pass

    # Format output
    return [{"path": p, "url": u} for (p, u) in sorted(endpoints)[:50]]

def extract_urls_from_text(text, base, target_netloc=None):
    """Tìm TẤT CẢ URL tuyệt đối trong text (JS, comment) cùng domain."""
    if not text:
        return []
    parsed_base = urlparse(base)
    target_netloc = target_netloc or parsed_base.netloc
    urls = set()
    abs_pat = r'https?://[A-Za-z0-9\-._~:/?#@!$&+,%=]+'
    for m in re.finditer(abs_pat, text):
        u = m.group(0).rstrip('.,;)\'"')
        try:
            pu = urlparse(u)
            if pu.netloc == target_netloc and pu.path and pu.path != "/":
                urls.add(u)
        except Exception:
            pass
    return sorted(urls)[:80]

# ── v8.0: Wayback / DNS / Screenshot helpers ──

async def wayback_fetch_paths(session, domain, limit=WAYBACK_MAX_URLS):
    """Fetch paths lịch sử từ Wayback Machine CDX API.
    Trả về list of unique URLs đã từng được archive."""
    api_url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&limit={limit}&fl=original&collapse=urlkey"
    try:
        async with session.get(api_url, timeout=aiohttp.ClientTimeout(total=20), ssl=False) as r:
            if r.status != 200:
                return []
            text = await r.text()
            data = json.loads(text)
            if len(data) < 2:
                return []
            # Row 0 = header, row 1+ = URLs
            urls = list(set(row[0] for row in data[1:] if row))
            return urls[:limit]
    except Exception:
        return []

async def dns_get_records(domain):
    """Query A/AAAA/MX/NS/TXT/SOA cho domain. Cần dnspython."""
    if not HAS_DNS:
        return {}, "dnspython chưa cài – pip install dnspython"
    records = {}
    resolver = dns.asyncresolver.Resolver()
    resolver.lifetime = 3.0
    resolver.timeout = 2.0
    async def query(qtype):
        try:
            answers = await resolver.resolve(domain, qtype, lifetime=3)
            return [str(r) for r in answers]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            return []
        except dns.resolver.LifetimeTimeout:
            return ["<timeout>"]
        except Exception:
            return []
    for qtype in ("A", "AAAA", "MX", "NS", "TXT", "SOA"):
        records[qtype] = await query(qtype)
    return records, None

async def dns_subdomain_enum(domain, wordlist, max_concurrent=20):
    """Async resolve A records cho các subdomain candidate.
    Trả về list of {subdomain, ips}."""
    if not HAS_DNS:
        return [], "dnspython chưa cài – pip install dnspython"
    resolver = dns.asyncresolver.Resolver()
    resolver.lifetime = 2.0
    resolver.timeout = 1.5
    sem = asyncio.Semaphore(max_concurrent)

    async def resolve_one(sub):
        subdomain = f"{sub}.{domain}"
        async with sem:
            try:
                answers = await resolver.resolve(subdomain, "A", lifetime=2)
                ips = [rdata.address for rdata in answers]
                return {"subdomain": subdomain, "ips": ips, "alive": True}
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.DNSException):
                return None
            except Exception:
                return None
    results = await asyncio.gather(*[resolve_one(s) for s in wordlist])
    return [r for r in results if r], None

async def dns_check_takeover(subdomains):
    """Với mỗi subdomain resolved, query CNAME và check pattern takeover.
    Trả về list of {subdomain, cname, service, severity}."""
    if not HAS_DNS:
        return [], "dnspython chưa cài"
    resolver = dns.asyncresolver.Resolver()
    resolver.lifetime = 2.0
    sem = asyncio.Semaphore(15)

    async def check_one(s):
        async with sem:
            try:
                answers = await resolver.resolve(s["subdomain"], "CNAME", lifetime=2)
                for rdata in answers:
                    cname = str(rdata.target).rstrip(".")
                    for pat, service, sev in TAKEOVER_CNAME_PATTERNS:
                        if re.search(pat, cname, re.I):
                            return {
                                "subdomain": s["subdomain"],
                                "cname": cname,
                                "service": service,
                                "severity": sev,
                                "takeover_possible": True,
                            }
                    # CNAME trỏ ra ngoài domain → check tay
                    return None
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException):
                return None
            except Exception:
                return None
            return None
    results = await asyncio.gather(*[check_one(s) for s in subdomains])
    return [r for r in results if r], None

async def take_screenshot(url, scan_id):
    """Chụp screenshot main page với Playwright (chromium headless).
    Lưu file PNG vào SCREENSHOT_DIR, trả về path + base64 preview."""
    if not HAS_PLAYWRIGHT:
        return None, "playwright chưa cài – pip install playwright && playwright install chromium"
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
            context = await browser.new_context(viewport={"width": 1280, "height": 800})
            page = await context.new_page()
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=15000)
            except Exception:
                pass
            try:
                await page.wait_for_load_state("networkidle", timeout=5000)
            except Exception:
                pass
            path = os.path.join(SCREENSHOT_DIR, f"scan_{scan_id}.png")
            await page.screenshot(path=path, full_page=False)
            await browser.close()
            # Đọc + return base64 preview
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            return {"path": path, "size_bytes": os.path.getsize(path), "base64_preview": b64}, None
    except Exception as e:
        return None, f"playwright error: {str(e)[:200]}"

async def check_cors(session, url, custom_headers=None, proxy=None, timeout=10):
    """Test CORS: gửi Origin: https://evil.com, check Access-Control-Allow-Origin reflection."""
    evil_origin = "https://evil.com"
    test_headers = dict(custom_headers or {})
    test_headers["Origin"] = evil_origin
    try:
        async with session.get(url, headers=test_headers, proxy=proxy,
                                timeout=aiohttp.ClientTimeout(total=timeout), ssl=False) as r:
            acao = r.headers.get("Access-Control-Allow-Origin") or r.headers.get("access-control-allow-origin")
            acac = r.headers.get("Access-Control-Allow-Credentials") or r.headers.get("access-control-allow-credentials")
            issues = []
            if acao:
                if acao == "*" and acac and acac.lower() == "true":
                    issues.append({
                        "type": "CORS Wildcard + Credentials",
                        "severity": "critical",
                        "detail": f"Server trả ACAO: * + ACAC: true (vô lý, browser sẽ chặn nhưng vẫn báo lỗi config)",
                    })
                elif acao == evil_origin:
                    issues.append({
                        "type": "CORS Origin Reflection",
                        "severity": "high",
                        "detail": f"Server reflect Origin header ({evil_origin}) vào ACAO – bất kỳ site nào cũng có thể đọc response",
                    })
                elif acao == "*":
                    issues.append({
                        "type": "CORS Wildcard",
                        "severity": "medium",
                        "detail": "ACAO: * – mọi site có thể đọc response (nếu không cần credentials)",
                    })
            return {
                "acao": acao,
                "acac": acac,
                "issues": issues,
            }
    except Exception as e:
        return {"error": str(e)[:100], "issues": []}

def score_finding(path, code):
    """Severity cho 1 path leak."""
    p = path.lower()
    # Critical
    if any(k in p for k in ["/.ssh/id_rsa", "/.aws/credentials", "/service-account.json",
                           "/firebase.json", "/.netrc", "/.kube/config", "/.terraform.tfvars",
                           "/terraform.tfstate", "private key", "/.env", "wp-config.php",
                           "/config.php", "/configuration.php"]):
        return "critical"
    # High
    if any(k in p for k in ["/db.sql", "/dump.sql", "/database.sql", "/backup.zip",
                            "/backup.tar.gz", "/www.zip", "/site.zip", "/.git/config",
                            "/.git/HEAD", "/.gitlab-ci.yml", "/.github/workflows/",
                            "/.npmrc", "/.pypirc", "/.netrc", "/.ssh/authorized_keys",
                            "/phpmyadmin/", "/adminer.php", "/swagger.json",
                            "/openapi.json", "/actuator/env", "/actuator/heapdump",
                            "/error.log", "/access.log", "/.bash_history"]):
        return "high"
    # Medium
    if code == 401 or code == 403:
        return "medium"
    if any(k in p for k in ["/admin/", "/administrator/", "/wp-admin/", "/wp-login.php",
                            "/install/", "/setup/", "/phpinfo.php", "/info.php",
                            "/server-status", "/.idea/", "/.vscode/", "/.DS_Store",
                            "/Thumbs.db"]):
        return "medium"
    return "low"

def get_main_page_summary(html, max_chars=400):
    if not html:
        return ""
    # Strip scripts + tags
    t = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.I | re.S)
    t = re.sub(r'<style[^>]*>.*?</style>', ' ', t, flags=re.I | re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:max_chars] + ("..." if len(t) > max_chars else "")

async def deep_scan(target, custom_headers=None, proxy=None, timeout=10,
                    allow_redirects=False, progress_cb=None, scan_js=True,
                    scan_id=None, deep_crawl=False,
                    scan_wayback=False, dns_enum=False,
                    take_shot=False, scan_cors=False):
    start = time.time()
    target = validate_target(target)
    # Mở rộng LEAK_PATHS với v7 CMS/framework paths
    ALL_LEAK_PATHS = list(LEAK_PATHS) + [p for p in EXTRA_LEAK_PATHS_V7 if p not in LEAK_PATHS]
    result = {
        "target": target, "timestamp": datetime.now(timezone.utc).isoformat(),
        "scanner_version": "v8.0",
        "main": {}, "leak": [], "robots": [], "links": [], "js_links": [],
        "forms": [], "dirs": [], "brute": [], "ports": [], "technologies": [],
        "waf": {}, "cdn": [], "cookies": [], "security_headers": [],
        "secrets": [], "ssl": {}, "subdomain_hints": [], "page_summary": "",
        "errors": [], "duration_seconds": 0, "stats": {},
        "soft_404_filtered": 0, "cancelled": False,
        # v7.0 fields
        "crawled_urls": [], "api_endpoints": [], "comments": [],
        "sitemap_urls": [], "query_param_hits": [], "recursive_dirs": [],
        "deep_crawl_enabled": deep_crawl,
        # v8.0 fields
        "wayback_urls": [], "wayback_hits": [],
        "dns_subdomains": [], "dns_records": {}, "dns_error": None,
        "takeover_risks": [], "cors": {}, "screenshot": None,
        "scan_wayback_enabled": scan_wayback, "dns_enum_enabled": dns_enum,
        "screenshot_enabled": take_shot, "cors_enabled": scan_cors,
        "has_dns_module": HAS_DNS, "has_playwright": HAS_PLAYWRIGHT,
    }
    parsed = urlparse(target)
    host = parsed.hostname
    base = f"{parsed.scheme}://{parsed.netloc}"

    def cancelled():
        return scan_id is not None and is_cancelled(scan_id)

    async def prog(phase, msg, current=0, total=0, found=0):
        if progress_cb:
            # Tính ETA dựa trên elapsed + current/total
            elapsed = time.time() - start
            eta = None
            if total > 0 and current > 0:
                rate = current / elapsed if elapsed > 0 else 0
                if rate > 0:
                    eta = max(0, round((total - current) / rate))
            display = phase_display(phase)
            await progress_cb({
                "phase": phase,
                "phase_display": display,
                "message": msg,
                "current": current, "total": total, "found": found,
                "elapsed": round(elapsed, 1),
                "eta": eta,
                "rate": round(current / elapsed, 1) if elapsed > 0 else 0,
            })

    if HAS_AIOHTTP:
        # Concurrency tăng nhẹ, brute-force timeout ngắn để scan nhanh hơn
        conn = aiohttp.TCPConnector(limit=100, limit_per_host=40, ssl=False)
        async with aiohttp.ClientSession(connector=conn,
                                          headers={"User-Agent": random.choice(USER_AGENTS)}) as session:
            # 1. Main page
            await prog("main_page", "Đang tải trang chính...")
            main_text, main_code, main_headers, main_rt = await fetch(session, target, custom_headers, proxy, timeout)
            result["main"] = {
                "code": main_code,
                "length": len(main_text) if main_text else 0,
                "headers": dict(main_headers),
                "response_time_ms": main_rt,
            }
            result["page_summary"] = get_main_page_summary(main_text)
            if main_code == 0:
                result["errors"].append(f"Kết nối thất bại: {main_text[:120]}")
                result["duration_seconds"] = round(time.time()-start, 2)
                return result

            # Cookies + security headers
            await prog("security_headers", "Phân tích security headers & cookies...")
            result["cookies"] = analyze_cookies(main_headers)
            result["security_headers"] = analyze_security_headers(main_headers)

            # Technologies + WAF + CDN
            cookie_names = [c.get("name","") for c in result["cookies"]]
            techs = detect_tech(main_text, main_headers, cookie_names)
            result["technologies"] = techs
            await prog("fingerprint", f"Tech: {', '.join(techs) if techs else 'Không xác định'}")
            waf = detect_waf(main_headers, main_code, main_text or "")
            result["waf"] = waf
            result["cdn"] = detect_cdn(main_headers)
            if waf["should_slow_down"]:
                await prog("waf", f"WAF: {', '.join(waf['detected'])} – Giảm tốc")

            limit = 8 if waf["should_slow_down"] else 25

            # SSL info nếu HTTPS
            if parsed.scheme == "https":
                await prog("ssl", "Đ kiểm tra SSL/TLS cert...")
                result["ssl"] = get_ssl_info(host, 443, 5)

            # v8.0: Screenshot (chạy sớm để không block các phase sau)
            if take_shot and not cancelled():
                await prog("screenshot", "Đang chụp screenshot main page (Playwright)...")
                shot, shot_err = await take_screenshot(target, scan_id)
                if shot:
                    result["screenshot"] = shot
                    await prog("screenshot", f"Screenshot OK – {shot['size_bytes']} bytes")
                else:
                    result["errors"].append(f"Screenshot fail: {shot_err}")
                    await prog("screenshot", f"Screenshot fail: {shot_err}")

            # v8.0: CORS test
            if scan_cors and not cancelled():
                await prog("cors", "Test CORS (Origin: https://evil.com)...")
                result["cors"] = await check_cors(session, target, custom_headers, proxy, timeout)
                if result["cors"].get("issues"):
                    await prog("cors", f"CORS issues: {len(result['cors']['issues'])} – severity cao nhất: {result['cors']['issues'][0]['severity']}")

            # v8.0: DNS records (A/AAAA/MX/NS/TXT/SOA) cho main domain
            if HAS_DNS and not cancelled():
                await prog("dns_records", f"Query DNS records cho {host}...")
                records, dns_err = await dns_get_records(host)
                result["dns_records"] = records
                if dns_err:
                    result["dns_error"] = dns_err
                await prog("dns_records", f"DNS records: A={len(records.get('A',[]))} MX={len(records.get('MX',[]))} NS={len(records.get('NS',[]))} TXT={len(records.get('TXT',[]))}")

            # v8.0: DNS subdomain enumeration
            if dns_enum and HAS_DNS and not cancelled():
                await prog("dns_enum", f"DNS subdomain enum ({len(COMMON_SUBDOMAINS)} candidates)...", 0, len(COMMON_SUBDOMAINS))
                subs, dns_err = await dns_subdomain_enum(host, COMMON_SUBDOMAINS, max_concurrent=20)
                if dns_err:
                    result["dns_error"] = dns_err
                result["dns_subdomains"] = subs
                await prog("dns_enum", f"DNS resolved: {len(subs)} subdomains")

                # v8.0: Subdomain takeover check
                if subs and not cancelled():
                    await prog("takeover", f"Check takeover cho {len(subs)} subdomains...", 0, len(subs))
                    risks, _ = await dns_check_takeover(subs)
                    result["takeover_risks"] = risks
                    await prog("takeover", f"Takeover risks: {len(risks)}")

            # v8.0: Wayback Machine
            if scan_wayback and not cancelled():
                await prog("wayback", f"Fetch Wayback Machine paths cho {host}...")
                wb_urls = await wayback_fetch_paths(session, host, WAYBACK_MAX_URLS)
                result["wayback_urls"] = wb_urls
                await prog("wayback", f"Wayback URLs: {len(wb_urls)}")

                # Test wayback paths trên target hiện tại (lấy tối đa 30 để tránh slow)
                if wb_urls and not cancelled():
                    await prog("wayback_test", f"Test {min(30, len(wb_urls))} wayback paths trên target...", 0, min(30, len(wb_urls)))
                    sem_wb = asyncio.Semaphore(8)
                    async def check_wayback(wb_url):
                        if cancelled(): return None
                        async with sem_wb:
                            # Convert về path trên current target
                            wb_parsed = urlparse(wb_url)
                            if not wb_parsed.path or wb_parsed.path == "/":
                                return None
                            test_url = urljoin(base, wb_parsed.path)
                            if test_url in (target, base + "/"):
                                return None
                            t, c, h, rt = await fetch(session, test_url, custom_headers, proxy, min(timeout, 5))
                            if c in (200, 401, 403):
                                path = wb_parsed.path
                                sev = score_finding(path, c)
                                return {
                                    "path": path, "url": test_url, "code": c,
                                    "size": len(t) if t else 0, "preview": "",
                                    "headers": {}, "severity": sev,
                                    "response_time_ms": rt,
                                    "soft_404": False, "from_wayback": True,
                                }
                            return None
                    to_test = wb_urls[:30]
                    wb_done = 0
                    wb_hits = []
                    for coro in asyncio.as_completed([check_wayback(u) for u in to_test]):
                        item = await coro
                        wb_done += 1
                        if item:
                            wb_hits.append(item)
                            result["leak"].append(item)
                        if wb_done % 5 == 0 or wb_done == len(to_test):
                            await prog("wayback_test", f"{wb_done}/{len(to_test)} – Hits: {len(wb_hits)}", wb_done, len(to_test), len(wb_hits))
                    result["wayback_hits"] = wb_hits
                    # Sort lại leak list
                    result["leak"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))

            # 2. Ports
            if host:
                await prog("ports", "Đang quét cổng...")
                result["ports"] = await scan_ports(host)
                await prog("ports_done", f"Cổng mở: {result['ports'] or 'Không có'}")

            # 3. Leak paths — soft-404 calibration trước
            await prog("leak_scan", f"Soft-404 calibration...", 0, len(ALL_LEAK_PATHS), 0)
            # Fetch 1 path random kỳ lạ -> nếu status 200 thì đây là soft-404 signature
            calib_paths = [
                f"/__wlscan_calib_{random.randint(10**8, 10**9 - 1)}__.html",
                f"/__wlscan_calib_{random.randint(10**8, 10**9 - 1)}__.php",
                f"/__wlscan_calib_{random.randint(10**8, 10**9 - 1)}__/",
            ]
            soft_404_sizes = set()
            soft_404_hashes = set()
            soft_404_codes = set()
            for cp in calib_paths:
                t, c, _, _ = await fetch(session, urljoin(base, cp), custom_headers, proxy, timeout)
                if c == 200 and t:
                    sz = len(t)
                    soft_404_sizes.add(sz)
                    # Hash nhanh: dùng 4 sample positions
                    try:
                        import hashlib
                        soft_404_hashes.add(hashlib.md5(t.encode('utf-8','replace')).hexdigest()[:12])
                    except Exception:
                        pass
                    soft_404_codes.add(c)
            if soft_404_sizes:
                await prog("leak_scan", f"Soft-404 baseline: {len(soft_404_sizes)} size(s) – sẽ filter", 0, len(ALL_LEAK_PATHS), 0)

            await prog("leak_scan", f"Quét {len(ALL_LEAK_PATHS)} paths...", 0, len(ALL_LEAK_PATHS), 0)
            sem = asyncio.Semaphore(limit)
            found_count = 0
            soft_filtered_count = 0
            async def check_path(path):
                nonlocal found_count, soft_filtered_count
                if cancelled():
                    return None
                async with sem:
                    url = urljoin(base, path)
                    text, code, h, rt = await fetch(session, url, custom_headers, proxy, timeout)
                    if code in (200, 401, 403):
                        sev = score_finding(path, code)
                        size = len(text) if text else 0
                        is_soft_404 = False
                        if code == 200 and size in soft_404_sizes and size > 0:
                            # Có thể là soft-404 — hash check
                            try:
                                import hashlib
                                h_ = hashlib.md5((text or "").encode('utf-8','replace')).hexdigest()[:12]
                                if h_ in soft_404_hashes:
                                    is_soft_404 = True
                            except Exception:
                                # fallback: chỉ dựa vào size
                                is_soft_404 = True
                        if is_soft_404:
                            soft_filtered_count += 1
                            # Vẫn giữ lại nhưng đánh dấu soft_404 + severity info
                            return {
                                "path": path, "url": url, "code": code,
                                "size": size, "preview": "", "headers": {},
                                "severity": "info", "response_time_ms": rt,
                                "soft_404": True,
                            }
                        if code == 200:
                            found_count += 1
                        return {
                            "path": path, "url": url, "code": code,
                            "size": size,
                            "preview": (text[:500]+"..." if len(text) > 500 else text) if code == 200 else "",
                            "headers": dict(h) if code == 200 else {},
                            "severity": sev,
                            "response_time_ms": rt,
                            "soft_404": False,
                        }
                    return None
            tasks = [check_path(p) for p in ALL_LEAK_PATHS]
            done = 0
            for coro in asyncio.as_completed(tasks):
                item = await coro
                done += 1
                if item:
                    result["leak"].append(item)
                if done % 10 == 0 or done == len(ALL_LEAK_PATHS):
                    await prog("leak_scan", f"{done}/{len(ALL_LEAK_PATHS)} – Found {found_count} (soft-404 filtered: {soft_filtered_count})", done, len(ALL_LEAK_PATHS), found_count)
            result["soft_404_filtered"] = soft_filtered_count
            if cancelled():
                result["cancelled"] = True
                result["errors"].append("Scan bị huỷ bởi user")
                result["duration_seconds"] = round(time.time()-start, 2)
                return result
            # Sort by severity
            result["leak"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))

            # 4. robots.txt
            await prog("robots", "Phân tích robots.txt...")
            rt, rc, _, _ = await fetch(session, urljoin(base, "/robots.txt"), custom_headers, proxy, timeout)
            if rc == 200 and rt:
                paths = []
                for line in rt.splitlines():
                    line = line.strip()
                    if line.startswith(("Allow:", "Disallow:")):
                        parts = line.split(":", 1)
                        if len(parts) == 2:
                            p = parts[1].strip()
                            if p and p.startswith("/"):
                                paths.append(p)
                result["robots"] = list(set(paths))
                for rp in paths[:15]:
                    full = urljoin(base, rp)
                    _, c, _, _ = await fetch(session, full, custom_headers, proxy, timeout)
                    if c == 200:
                        result["leak"].append({
                            "path": rp, "url": full, "code": 200, "size": 0,
                            "preview": "[from robots.txt]", "headers": {},
                            "severity": score_finding(rp, 200), "response_time_ms": 0,
                        })

            # 5. Links + JS + Forms + Comments + API endpoints (v7.0)
            if main_text:
                await prog("links", "Trích xuất links / JS / forms / comments / API endpoints...")
                # v7.0: dùng extract_all_links thay vì regex thủ công
                all_links = extract_all_links(main_text, base, parsed.netloc)
                result["links"] = [l for l in all_links if l != target][:SPIDER_MAX_URLS]
                result["js_links"] = extract_js_links(main_text, base)
                result["forms"] = extract_forms(main_text, base)
                # v7.0: HTML comments
                result["comments"] = extract_html_comments(main_text)
                # v7.0: API endpoints từ HTML
                result["api_endpoints"] = extract_api_endpoints(main_text, base, parsed.netloc)

                # 6. Secrets trong main HTML
                await prog("secrets", "Quét secret patterns trong HTML...")
                html_secrets = scan_secrets(main_text, "main page HTML")
                result["secrets"].extend(html_secrets)

                # 7. Fetch + scan JS files (cũng extract API endpoints từ JS)
                if scan_js and result["js_links"]:
                    await prog("secrets_js", f"Quét {len(result['js_links'])} JS files...", 0, len(result["js_links"]))
                    js_sem = asyncio.Semaphore(5)
                    async def scan_one_js(url):
                        async with js_sem:
                            t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                            if c == 200 and t:
                                secrets = scan_secrets(t, f"JS: {url}")
                                return (t, secrets)
                            return (None, [])
                    done = 0
                    for coro in asyncio.as_completed([scan_one_js(u) for u in result["js_links"]]):
                        js_text, ss = await coro
                        result["secrets"].extend(ss)
                        # v7.0: API endpoints từ JS
                        if js_text:
                            result["api_endpoints"].extend(extract_api_endpoints(js_text, base, parsed.netloc))
                        done += 1
                        if done % 5 == 0 or done == len(result["js_links"]):
                            await prog("secrets_js", f"JS {done}/{len(result['js_links'])} – Secrets: {len(result['secrets'])} – APIs: {len(result['api_endpoints'])}", done, len(result["js_links"]), len(result['secrets']))
                # Dedup secrets + sort
                seen = set(); deduped = []
                for s in result["secrets"]:
                    k = (s["type"], s["match_masked"], s["source"])
                    if k not in seen:
                        seen.add(k); deduped.append(s)
                result["secrets"] = deduped
                result["secrets"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))
                # Dedup API endpoints
                seen_apis = set(); deduped_apis = []
                for a in result["api_endpoints"]:
                    if a["url"] not in seen_apis:
                        seen_apis.add(a["url"]); deduped_apis.append(a)
                result["api_endpoints"] = deduped_apis[:80]

                # v7.0: Sitemap.xml deep parse
                if not cancelled():
                    await prog("sitemap", "Đọc sitemap.xml + sitemap index...")
                    sm_text, sm_code, _, _ = await fetch(session, urljoin(base, "/sitemap.xml"), custom_headers, proxy, timeout)
                    if sm_code == 200 and sm_text:
                        sm_urls = parse_sitemap(sm_text, base)
                        result["sitemap_urls"] = sm_urls
                        # Nếu là sitemap index, fetch sitemap con
                        if "<sitemapindex" in sm_text.lower():
                            await prog("sitemap", f"Sitemap index, fetching {min(5, len(sm_urls))} sitemaps con...")
                            sub_urls = set()
                            for sub_sm_url in sm_urls[:5]:
                                st, sc, _, _ = await fetch(session, sub_sm_url, custom_headers, proxy, timeout)
                                if sc == 200 and st:
                                    sub_urls.update(parse_sitemap(st, base))
                            result["sitemap_urls"] = sorted(set(sm_urls) | sub_urls)[:SITEMAP_MAX_URLS]
                        await prog("sitemap", f"Sitemap: {len(result['sitemap_urls'])} URLs")

                # v7.0: Deep crawl (recursive spider)
                if deep_crawl and not cancelled():
                    await prog("crawl", f"Deep crawl depth={SPIDER_MAX_DEPTH}...", 0, SPIDER_MAX_URLS)
                    crawled = set()
                    to_visit = list(result["links"])[:SPIDER_MAX_URLS]
                    visited = set([target])
                    crawl_sem = asyncio.Semaphore(8)
                    async def crawl_one(url, depth):
                        if url in visited or len(crawled) >= SPIDER_MAX_URLS:
                            return []
                        visited.add(url)
                        async with crawl_sem:
                            t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                            if c == 200 and t:
                                new_links = extract_all_links(t, base, parsed.netloc)
                                # Quét secret trong crawled page
                                page_secrets = scan_secrets(t, f"Crawled: {url}")
                                return (new_links, page_secrets)
                            return ([], [])
                    done = 0
                    for depth in range(SPIDER_MAX_DEPTH):
                        if not to_visit or cancelled():
                            break
                        batch = to_visit[:20]
                        to_visit = to_visit[20:]
                        next_batch = []
                        for url in batch:
                            if cancelled():
                                break
                            new_links, page_secrets = await crawl_one(url, depth)
                            crawled.add(url)
                            if page_secrets:
                                result["secrets"].extend(page_secrets)
                            next_batch.extend([u for u in new_links if u not in visited and u not in crawled and u not in to_visit])
                            done += 1
                            await prog("crawl", f"Crawled {done}/{len(result['links'])} – Found {len(next_batch)} new", done, len(result['links']), len(crawled))
                        to_visit.extend(next_batch[:SPIDER_MAX_URLS])
                    result["crawled_urls"] = sorted(crawled)
                    await prog("crawl", f"Deep crawl xong: {len(crawled)} pages")

                # v7.0: Query param fuzzing trên main URL
                if not cancelled():
                    await prog("query_fuzz", f"Test {len(QUERY_PARAM_FUZZ)} query params...", 0, len(QUERY_PARAM_FUZZ))
                    qf_hits = []
                    q_sem = asyncio.Semaphore(5)
                    async def check_q(qs):
                        if cancelled(): return None
                        async with q_sem:
                            full = target + qs
                            t, c, _, _ = await fetch(session, full, custom_headers, proxy, timeout)
                            if c == 200 and t:
                                # So sánh size với main page để xem có khác biệt
                                main_size = result["main"].get("length", 0)
                                size = len(t) if t else 0
                                # Nếu size khác biệt đáng kể hoặc status khác
                                if abs(size - main_size) > 200:
                                    return {"query": qs, "code": c, "size": size,
                                            "size_diff": size - main_size,
                                            "preview": (t[:300]+"...") if len(t)>300 else t}
                            return None
                    q_done = 0
                    for coro in asyncio.as_completed([check_q(qs) for qs in QUERY_PARAM_FUZZ]):
                        h = await coro
                        q_done += 1
                        if h:
                            qf_hits.append(h)
                        if q_done % 5 == 0 or q_done == len(QUERY_PARAM_FUZZ):
                            await prog("query_fuzz", f"{q_done}/{len(QUERY_PARAM_FUZZ)} – Hits: {len(qf_hits)}", q_done, len(QUERY_PARAM_FUZZ), len(qf_hits))
                    result["query_param_hits"] = qf_hits

            # 8. Directory listing
            await prog("dirs", "Kiểm tra directory listing...")
            dirs = ["/backup/", "/temp/", "/tmp/", "/admin/", "/uploads/", "/files/",
                    "/logs/", "/config/", "/static/", "/public/", "/_files/", "/media/"]
            async def check_dir(d):
                url = urljoin(base, d)
                t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                if c == 200 and t and ("<title>Index of" in t or "Parent Directory" in t or "<h1>Index of" in t):
                    return {"url": url, "type": "dirlist"}
                return None
            result["dirs"] = [r for r in await asyncio.gather(*[check_dir(d) for d in dirs]) if r]

            # v7.0: Recursive dir check — với mỗi directory 200 tìm được, thử sub-paths
            if result["dirs"] and not cancelled():
                await prog("recursive_dirs", f"Recursive check {len(result['dirs'])} dirs...", 0, len(result["dirs"]))
                rec_hits = []
                rec_sem = asyncio.Semaphore(8)
                async def check_subpath(parent_url, sub):
                    if cancelled(): return None
                    async with rec_sem:
                        url = urljoin(parent_url + "/" if not parent_url.endswith("/") else parent_url, sub)
                        url = url.replace("//", "/")  # avoid // in middle
                        t, c, _, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 4))
                        if c in (200, 401, 403):
                            if c == 200 and t and len(t) in soft_404_sizes:
                                return None
                            return {
                                "parent": parent_url, "sub": sub, "url": url,
                                "code": c, "severity": score_finding("/" + sub, c),
                                "response_time_ms": rt,
                            }
                        return None
                tasks_rec = []
                for d in result["dirs"]:
                    for sub in RECURSIVE_DIR_PROBES:
                        tasks_rec.append(check_subpath(d["url"], sub))
                rec_done = 0
                for coro in asyncio.as_completed(tasks_rec):
                    item = await coro
                    rec_done += 1
                    if item:
                        rec_hits.append(item)
                    if rec_done % 10 == 0 or rec_done == len(tasks_rec):
                        await prog("recursive_dirs", f"{rec_done}/{len(tasks_rec)} – Found {len(rec_hits)}", rec_done, len(tasks_rec), len(rec_hits))
                result["recursive_dirs"] = sorted(rec_hits, key=lambda x: -severity_rank(x.get("severity", "low")))

            # v7.0: API endpoint enumeration — test response của từng API endpoint đã tìm thấy
            if not cancelled():
                # Combine endpoints từ result["api_endpoints"] (đã discover) + API_ENDPOINTS (predefined)
                discovered = set(a["path"] for a in result.get("api_endpoints", []))
                to_test = list(set(API_ENDPOINTS) | discovered)
                await prog("api_scan", f"Test {len(to_test)} API endpoints...", 0, len(to_test))
                api_hits = []
                api_sem = asyncio.Semaphore(10)
                async def check_api(path):
                    if cancelled(): return None
                    async with api_sem:
                        url = urljoin(base, path)
                        t, c, h, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 5))
                        if c in (200, 401, 403, 500):
                            if c == 200 and t and len(t) in soft_404_sizes:
                                return None
                            return {
                                "path": path, "url": url, "code": c,
                                "size": len(t) if t else 0,
                                "content_type": (h.get("Content-Type") or h.get("content-type") or "")[:60],
                                "severity": "high" if c == 200 else ("medium" if c == 401 else "low"),
                                "response_time_ms": rt,
                            }
                        return None
                a_done = 0
                for coro in asyncio.as_completed([check_api(p) for p in to_test]):
                    h = await coro
                    a_done += 1
                    if h:
                        api_hits.append(h)
                    if a_done % 10 == 0 or a_done == len(to_test):
                        await prog("api_scan", f"{a_done}/{len(to_test)} – Hits: {len(api_hits)}", a_done, len(to_test), len(api_hits))
                # Merge vào leak list với tag api
                for h in api_hits:
                    result["leak"].append({
                        "path": h["path"], "url": h["url"], "code": h["code"],
                        "size": h["size"], "preview": "", "headers": {},
                        "severity": h["severity"],
                        "response_time_ms": h["response_time_ms"],
                        "soft_404": False, "is_api": True,
                    })
                # Sort lại leak list
                result["leak"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))

            # 9. Brute-force common names — timeout ngắn để scan nhanh
            if not cancelled():
                brute_total = 9 * 20  # 180
                await prog("brute", "Brute-force common files...", 0, brute_total)
                exts = [".php", ".html", ".txt", ".json", ".xml", ".bak", ".old", ".save", ".orig"]
                names = ["index", "admin", "login", "config", "test", "api", "backup",
                         "db", "database", "secret", "private", "key", "token", "user",
                         "users", "account", "accounts", "config.bak", "panel"]
                bsem = asyncio.Semaphore(15)
                brute_timeout = min(timeout, 4)  # rút gọn timeout cho brute
                b_done = 0
                async def brute_one(n, e):
                    nonlocal b_done
                    if cancelled():
                        return None
                    path = f"/{n}{e}"
                    url = urljoin(base, path)
                    async with bsem:
                        t, c, _, rt = await fetch(session, url, custom_headers, proxy, brute_timeout)
                        b_done += 1
                        if c in (200, 403, 401):
                            # Soft-404 check cho brute
                            if c == 200 and t and len(t) in soft_404_sizes:
                                return None
                            return {"path": path, "code": c, "severity": score_finding(path, c), "response_time_ms": rt}
                        return None
                result["brute"] = [r for r in await asyncio.gather(*[brute_one(n, e) for n in names for e in exts]) if r]
                result["brute"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))
                await prog("brute", f"Brute xong: {len(result['brute'])} hits", b_done, brute_total, len(result['brute']))

            # 10. Subdomain hints (no network call)
            result["subdomain_hints"] = [f"{s}.{host}" for s in COMMON_SUBDOMAINS[:30]]
    else:
        import requests
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.get(target, headers={"User-Agent": random.choice(USER_AGENTS)},
                             timeout=timeout, verify=False, allow_redirects=True)
            main_text, main_code, main_headers = r.text, r.status_code, dict(r.headers)
        except Exception as e:
            main_text, main_code, main_headers = str(e), 0, {}
        result["main"] = {"code": main_code, "length": len(main_text),
                          "headers": main_headers, "response_time_ms": 0}
        result["page_summary"] = get_main_page_summary(main_text)
        result["cookies"] = analyze_cookies(main_headers)
        result["security_headers"] = analyze_security_headers(main_headers)
        result["technologies"] = detect_tech(main_text, main_headers, [c.get("name","") for c in result["cookies"]])
        result["waf"] = detect_waf(main_headers, main_code, main_text)
        result["cdn"] = detect_cdn(main_headers)
        if parsed.scheme == "https":
            result["ssl"] = get_ssl_info(host, 443, 5)
        result["secrets"] = scan_secrets(main_text, "main page HTML")
        result["errors"].append("Chế độ đồng bộ – cài aiohttp để có async scan đầy đủ")

    # Final stats
    result["stats"] = {
        "leak_count": len(result["leak"]),
        "critical_count": sum(1 for x in result["leak"] if x.get("severity") == "critical"),
        "high_count": sum(1 for x in result["leak"] if x.get("severity") == "high"),
        "medium_count": sum(1 for x in result["leak"] if x.get("severity") == "medium"),
        "low_count": sum(1 for x in result["leak"] if x.get("severity") == "low"),
        "secret_count": len(result["secrets"]),
        "secret_critical": sum(1 for x in result["secrets"] if x.get("severity") == "critical"),
        "secret_high": sum(1 for x in result["secrets"] if x.get("severity") == "high"),
        "ports_open": len(result["ports"]),
        "dir_listings": len(result["dirs"]),
        "tech_count": len(result["technologies"]),
        "waf_detected": len(result.get("waf", {}).get("detected", [])),
        "missing_security_headers": sum(1 for h in result["security_headers"] if h["missing"]),
        "insecure_cookies": sum(1 for c in result["cookies"] if c.get("issues")),
        "js_files_scanned": len(result.get("js_links", [])),
        "forms_found": len(result.get("forms", [])),
        "soft_404_filtered": result.get("soft_404_filtered", 0),
        "real_leak_count": sum(1 for x in result.get("leak", []) if not x.get("soft_404")),
        "cancelled": result.get("cancelled", False),
        # v7.0 stats
        "crawled_url_count": len(result.get("crawled_urls", [])),
        "api_endpoint_count": len(result.get("api_endpoints", [])),
        "api_hit_count": sum(1 for x in result.get("leak", []) if x.get("is_api")),
        "comment_count": len(result.get("comments", [])),
        "sitemap_url_count": len(result.get("sitemap_urls", [])),
        "query_param_hit_count": len(result.get("query_param_hits", [])),
        "recursive_dir_count": len(result.get("recursive_dirs", [])),
        "total_paths_tested": len(LEAK_PATHS) + len(EXTRA_LEAK_PATHS_V7) + len(API_ENDPOINTS),
        # v8.0 stats
        "wayback_count": len(result.get("wayback_urls", [])),
        "wayback_hit_count": len(result.get("wayback_hits", [])),
        "dns_subdomain_count": len(result.get("dns_subdomains", [])),
        "dns_record_count": sum(len(v) for v in (result.get("dns_records") or {}).values()),
        "takeover_risk_count": len(result.get("takeover_risks", [])),
        "cors_issue_count": len((result.get("cors") or {}).get("issues", [])),
        "has_screenshot": bool(result.get("screenshot")),
    }
    result["duration_seconds"] = round(time.time()-start, 2)
    s = result['stats']
    await prog("completed", f"Hoàn thành – {s['real_leak_count']} leaks (soft-404: {s['soft_404_filtered']}), {s['secret_count']} secrets, {s['ports_open']} ports, {s['api_endpoint_count']} APIs, {s['crawled_url_count']} crawled, {s['wayback_count']} wayback, {s['dns_subdomain_count']} subdomains, {s['takeover_risk_count']} takeover risks, {s['cors_issue_count']} CORS issues")
    return result

# ── SSE ──
progress_queues = {}
prog_lock = threading.Lock()
scan_results = {}
scan_history = []  # list of {scan_id, target, started_at, status, leak_count}
scan_cancels = set()  # set of scan_id that user wants to cancel
scan_starts = {}  # scan_id -> start timestamp (for ETA calc)

def push_history(item):
    scan_history.insert(0, item)
    if len(scan_history) > SCAN_HISTORY_MAX:
        scan_history.pop()

def send_prog(scan_id, data):
    with prog_lock:
        q = progress_queues.get(scan_id)
        if q:
            try:
                q.put_nowait(json.dumps(data))
            except:
                pass

def is_cancelled(scan_id):
    with prog_lock:
        return scan_id in scan_cancels

def fmt_sse(data):
    return f"data: {data}\n\n"

# Phase name translation (snake_case -> tiếng Việt human-readable)
PHASE_NAMES = {
    "main_page": "🌐 Tải trang chính",
    "security_headers": "📜 Phân tích security headers",
    "fingerprint": "🛠️ Nhận diện công nghệ",
    "waf": "🛡️ Phát hiện WAF",
    "ssl": "🔒 Kiểm tra SSL/TLS",
    "ports": "🔌 Quét cổng",
    "ports_done": "✅ Xong quét cổng",
    "leak_scan": "📁 Quét leak paths",
    "robots": "🤖 Phân tích robots.txt",
    "links": "🔗 Trích xuất links/JS/forms",
    "secrets": "🔐 Quét secret trong HTML",
    "secrets_js": "📜 Quét secret trong JS files",
    "dirs": "📂 Kiểm tra directory listing",
    "brute": "🔍 Brute-force common files",
    "completed": "✅ Hoàn thành",
    "error": "❌ Lỗi",
    "cancelling": "🛑 Đang huỷ...",
    "cancelled": "🛑 Đã huỷ",
    # v7.0 phases
    "sitemap": "🗺️ Đọc sitemap.xml",
    "crawl": "🕷️ Deep crawl (recursive spider)",
    "query_fuzz": "❓ Test query params",
    "recursive_dirs": "🔁 Recursive dir check",
    "api_scan": "🔌 Test API endpoints",
    # v8.0 phases
    "screenshot": "📸 Chụp screenshot (Playwright)",
    "cors": "🔒 Test CORS",
    "dns_records": "📡 Query DNS records",
    "dns_enum": "🌐 DNS subdomain enum",
    "takeover": "🎯 Subdomain takeover check",
    "wayback": "🕰️ Fetch Wayback Machine",
    "wayback_test": "🕰️ Test wayback paths",
    # Internal — không hiển thị cho user
    "connected": None,
    "keepalive": None,
}

def phase_display(phase):
    """Trả về tên hiển thị cho phase, hoặc None nếu là internal heartbeat."""
    return PHASE_NAMES.get(phase, phase if phase else "")

# ── HTML Template (PAGE) ──
PAGE_HTML = r"""
<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Leak Scanner Pro v8.0</title>
<style>
:root{
  --bg:#0f0f1a; --bg2:#16213e; --bg3:#1a1a2e; --border:#2d3561;
  --text:#e0e0e0; --muted:#a0a0b0; --dim:#888;
  --accent:#00d4aa; --accent2:#54a0ff; --warn:#feca57;
  --danger:#ff6b6b; --ok:#1dd1a1;
}
[data-theme="light"]{
  --bg:#f5f7fa; --bg2:#ffffff; --bg3:#eef1f6; --border:#d0d7e2;
  --text:#1a1a2e; --muted:#5b6478; --dim:#8793a8;
  --accent:#00b894; --accent2:#0984e3; --warn:#f0932b;
  --danger:#eb4d4b; --ok:#2ecc71;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh;transition:background .3s,color .3s}
.navbar{background:var(--bg3);border-bottom:1px solid var(--border);padding:0 16px;display:flex;justify-content:space-between;align-items:center;height:54px;position:sticky;top:0;z-index:100;backdrop-filter:blur(8px)}
.nav-brand{display:flex;align-items:center;gap:8px;font-weight:700;font-size:16px}
.version{background:var(--accent);color:var(--bg);padding:2px 8px;border-radius:12px;font-size:11px;font-weight:800}
.nav-right{display:flex;align-items:center;gap:10px}
.theme-toggle{background:var(--bg3);border:1px solid var(--border);color:var(--text);padding:6px 10px;border-radius:8px;cursor:pointer;font-size:14px}
.theme-toggle:hover{background:var(--bg2)}
.container{max-width:1100px;margin:0 auto;padding:16px}
.card{background:var(--bg2);border:1px solid var(--border);border-radius:12px;padding:18px;margin-bottom:16px;transition:border-color .2s}
.card:hover{border-color:var(--accent)}
.card h1,.card h2{font-size:20px;margin-bottom:8px;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.card h3{font-size:16px;margin-bottom:10px}
.subtitle{color:var(--muted);font-size:14px;margin-bottom:16px}
.form-group{margin-bottom:14px}
.form-group label{display:block;font-size:13px;color:var(--muted);font-weight:600;margin-bottom:6px}
.form-group input,.form-group select{width:100%;padding:10px 12px;background:var(--bg);border:1px solid var(--border);border-radius:10px;color:var(--text);font-size:14px;outline:none;font-family:inherit}
.form-group input:focus,.form-group select:focus{border-color:var(--accent);box-shadow:0 0 0 2px rgba(0,212,170,.15)}
.form-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.form-row-2{display:grid;grid-template-columns:1fr 2fr;gap:12px}
.btn{padding:10px 18px;border:none;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;display:inline-flex;align-items:center;gap:6px;text-decoration:none;border:1px solid transparent;font-family:inherit}
.btn-primary{background:linear-gradient(135deg,var(--accent),#00b894);color:var(--bg)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,212,170,.25)}
.btn-primary:disabled{opacity:.5;cursor:not-allowed;transform:none}
.btn-secondary{background:var(--bg3);color:var(--accent);border-color:var(--accent)}
.btn-secondary:hover{background:var(--accent);color:var(--bg)}
.btn-ghost{background:transparent;color:var(--muted);border:1px solid var(--border)}
.btn-ghost:hover{color:var(--text);border-color:var(--accent)}
.progress-card{border-left:3px solid var(--accent)}
.progress-info{display:flex;justify-content:space-between;font-size:13px;color:var(--muted);margin-bottom:8px}
.progress-bar-bg{width:100%;height:6px;background:var(--bg);border-radius:3px;overflow:hidden;margin-bottom:10px}
.progress-bar-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;transition:width .3s;width:0%}
.progress-msg{font-size:13px;color:var(--muted)}
.progress-found{font-size:13px;font-weight:700;color:var(--ok);margin-top:4px}
.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin-bottom:16px}
.stat-box{text-align:center;padding:12px 6px;background:var(--bg3);border:1px solid var(--border);border-radius:10px}
.stat-number{font-size:22px;font-weight:800;color:var(--accent)}
.stat-label{font-size:10px;color:var(--dim);margin-top:2px;text-transform:uppercase;letter-spacing:.5px}
.sev-crit{color:var(--danger)!important}
.sev-high{color:#feca57!important}
.sev-med{color:#ff9f43!important}
.tabs{display:flex;gap:4px;margin-bottom:14px;border-bottom:1px solid var(--border);overflow-x:auto}
.tab{padding:10px 14px;background:none;border:none;color:var(--muted);cursor:pointer;font-size:14px;font-weight:600;border-bottom:2px solid transparent;white-space:nowrap;font-family:inherit}
.tab.active{color:var(--accent);border-bottom-color:var(--accent)}
.tab:hover{color:var(--text)}
.tab-panel{display:none}
.tab-panel.active{display:block;animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.section-title{font-size:14px;font-weight:700;margin:14px 0 10px;display:flex;align-items:center;gap:6px;color:var(--text)}
.section-title .count{background:var(--bg3);color:var(--muted);padding:1px 8px;border-radius:10px;font-size:11px;margin-left:6px}
.tech-tag{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;margin:2px;background:rgba(0,212,170,.1);color:var(--accent);border:1px solid rgba(0,212,170,.3)}
.port-badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:700;margin:2px;background:rgba(84,160,255,.15);color:var(--accent2);border:1px solid rgba(84,160,255,.3)}
.cdn-badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;margin:2px;background:rgba(254,202,87,.12);color:var(--warn);border:1px solid rgba(254,202,87,.3)}
.sev-badge{padding:2px 8px;border-radius:4px;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.5px}
.sev-critical{background:rgba(255,107,107,.2);color:var(--danger)}
.sev-high{background:rgba(254,202,87,.2);color:var(--warn)}
.sev-medium{background:rgba(255,159,64,.2);color:#ff9f43}
.sev-low{background:rgba(0,212,170,.15);color:var(--accent)}
.sev-info{background:rgba(160,160,176,.15);color:var(--dim)}
.leak-item{padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;margin-bottom:8px;transition:all .2s}
.leak-item:hover{border-color:var(--accent)}
.leak-item.crit{border-left:3px solid var(--danger)}
.leak-item.high{border-left:3px solid var(--warn)}
.leak-item.med{border-left:3px solid #ff9f43}
.leak-header{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.code-badge{padding:2px 8px;border-radius:4px;font-size:12px;font-weight:800;min-width:36px;text-align:center}
.code-200{background:rgba(29,209,161,.2);color:var(--ok)}
.code-403{background:rgba(254,202,87,.2);color:var(--warn)}
.code-401{background:rgba(255,107,107,.2);color:var(--danger)}
.code-404{background:rgba(160,160,176,.2);color:var(--dim)}
.leak-path{font-family:ui-monospace,'SFMono-Regular',Menlo,monospace;font-weight:700;font-size:13px;color:var(--text);word-break:break-all}
.leak-size{font-size:11px;color:var(--dim)}
.leak-url{font-size:11px;color:var(--dim);word-break:break-all;margin-top:2px}
.leak-rt{font-size:10px;color:var(--dim);margin-left:auto}
.leak-preview summary{cursor:pointer;color:var(--accent);font-size:12px;font-weight:600}
.leak-preview pre{background:var(--bg);padding:10px;border-radius:8px;font-size:12px;overflow-x:auto;margin-top:6px;max-height:240px;overflow-y:auto;color:#aed581;font-family:ui-monospace,monospace;white-space:pre-wrap;word-break:break-all}
.robots-content{background:var(--bg);padding:10px;border-radius:8px;font-family:ui-monospace,monospace;font-size:12px;max-height:240px;overflow-y:auto;white-space:pre-wrap}
.waf-info{background:rgba(255,107,107,.05);border:1px solid rgba(255,107,107,.2);border-radius:8px;padding:12px}
.alert{padding:12px;border-radius:8px;margin-bottom:12px;font-size:14px}
.alert-error{background:rgba(255,107,107,.1);border:1px solid rgba(255,107,107,.3);color:var(--danger)}
.alert-warn{background:rgba(254,202,87,.1);border:1px solid rgba(254,202,87,.3);color:var(--warn)}
.alert-info{background:rgba(84,160,255,.1);border:1px solid rgba(84,160,255,.3);color:var(--accent2)}
.empty-state{text-align:center;padding:24px;color:var(--dim)}
.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;margin:2px}
.badge-time{background:rgba(84,160,255,.12);color:var(--accent2)}
.badge-waf{background:rgba(255,107,107,.12);color:var(--danger)}
.badge-ssl-ok{background:rgba(29,209,161,.15);color:var(--ok)}
.badge-ssl-warn{background:rgba(254,202,87,.15);color:var(--warn)}
.badge-ssl-err{background:rgba(255,107,107,.15);color:var(--danger)}
.filter-bar{margin-bottom:12px;display:flex;gap:8px;flex-wrap:wrap}
.filter-bar input{flex:1;min-width:200px;padding:8px 12px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text);font-size:13px;font-family:inherit}
.filter-bar select{padding:8px 12px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text);font-size:13px;font-family:inherit}
.cookie-item{padding:8px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;margin-bottom:6px;font-size:13px}
.cookie-name{font-family:monospace;font-weight:700;color:var(--accent)}
.cookie-flag{display:inline-block;padding:1px 6px;border-radius:4px;font-size:10px;margin-left:4px}
.flag-ok{background:rgba(29,209,161,.2);color:var(--ok)}
.flag-bad{background:rgba(255,107,107,.2);color:var(--danger)}
.sec-header-row{display:flex;justify-content:space-between;align-items:center;padding:8px;background:var(--bg3);border:1px solid var(--border);border-radius:6px;margin-bottom:4px;font-size:13px}
.sec-header-missing{border-left:3px solid var(--danger)}
.sec-header-present{border-left:3px solid var(--ok)}
.sec-header-name{font-family:monospace;font-weight:600;color:var(--text)}
.sec-header-value{font-family:monospace;font-size:11px;color:var(--muted);word-break:break-all;max-width:55%;text-align:right}
.form-item{padding:8px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;margin-bottom:6px;font-size:13px}
.form-action{font-family:monospace;color:var(--accent);word-break:break-all}
.form-tag{display:inline-block;padding:1px 6px;border-radius:4px;font-size:10px;font-weight:700;margin-left:4px;text-transform:uppercase}
.form-tag-login{background:rgba(255,107,107,.15);color:var(--danger)}
.form-tag-upload{background:rgba(254,202,87,.15);color:var(--warn)}
.form-tag-csrf{background:rgba(84,160,255,.15);color:var(--accent2)}
.history-list{display:flex;flex-direction:column;gap:6px}
.history-item{display:flex;justify-content:space-between;align-items:center;padding:8px 10px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;cursor:pointer;font-size:13px;transition:all .2s}
.history-item:hover{border-color:var(--accent);background:var(--bg2)}
.history-target{font-family:monospace;color:var(--accent);word-break:break-all}
.history-meta{font-size:11px;color:var(--dim)}
.footer{text-align:center;padding:16px;color:var(--dim);font-size:12px;border-top:1px solid var(--border);margin-top:16px}
.hidden{display:none!important}
.toast{position:fixed;bottom:20px;right:20px;background:var(--bg2);border:1px solid var(--accent);color:var(--text);padding:10px 16px;border-radius:8px;font-size:13px;z-index:200;box-shadow:0 4px 12px rgba(0,0,0,.3);opacity:0;transform:translateY(10px);transition:all .3s}
.toast.show{opacity:1;transform:none}
@media(max-width:768px){
  .form-row{grid-template-columns:1fr}
  .stats-grid{grid-template-columns:repeat(3,1fr)}
  .container{padding:12px}
}
</style>
</head>
<body>
<nav class="navbar">
  <div class="nav-brand"><span>🔒</span><span>Web Leak Scanner <span class="version">v8.0</span></span></div>
  <div class="nav-right">
    <button class="theme-toggle" id="themeToggle" title="Đổi theme">🌙</button>
  </div>
</nav>
<main class="container">

<!-- Form -->
<div class="card">
  <h1>🕵️ Quét lỗ hổng thông tin rò rỉ</h1>
  <p class="subtitle">Async scanner: leak paths · deep crawl · wayback · DNS enum · screenshot · CORS · takeover · soft-404 filter · ETA · cancel</p>
  <form id="scanForm" method="post" action="/scan">
    <div class="form-group"><label>🌐 URL mục tiêu</label><input type="text" name="target" placeholder="https://example.com" required></div>
    <div class="form-row">
      <div class="form-group"><label>⏱️ Timeout (s)</label><input type="number" name="timeout" value="10" min="1" max="60"></div>
      <div class="form-group"><label>🔀 Proxy</label><input type="text" name="proxy" placeholder="http://proxy:8080"></div>
      <div class="form-group"><label>🔎 Quét JS files</label>
        <select name="scan_js"><option value="yes" selected>Có (deep)</option><option value="no">Không (nhanh)</option></select>
      </div>
    </div>
    <div class="form-group"><label>📋 Custom Headers</label><input type="text" name="headers" placeholder="User-Agent: MyBot; X-Forwarded-For: 1.2.3.4"></div>
    <div class="form-group" style="display:flex;align-items:center;gap:18px;flex-wrap:wrap">
      <div style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" name="redirect" value="yes" id="rd" checked>
        <label for="rd" style="margin:0">Theo dõi redirect</label>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" name="deep_crawl" value="yes" id="dc">
        <label for="dc" style="margin:0" title="Spider recursive depth=2 + parse sitemap + API endpoint enumeration">🕷️ Deep crawl</label>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" name="wayback" value="yes" id="wb">
        <label for="wb" style="margin:0" title="Fetch paths lịch sử từ web.archive.org + test trên target">🕰️ Wayback</label>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" name="dns_enum" value="yes" id="dn">
        <label for="dn" style="margin:0" title="DNS subdomain enum thật (cần dnspython) + takeover check">🌐 DNS enum</label>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" name="cors" value="yes" id="co">
        <label for="co" style="margin:0" title="Gửi Origin: https://evil.com, check ACAO reflection">🔒 CORS test</label>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <input type="checkbox" name="screenshot" value="yes" id="sc">
        <label for="sc" style="margin:0" title="Chụp screenshot main page (cần playwright)">📸 Screenshot</label>
      </div>
    </div>
    <button type="submit" class="btn btn-primary" id="scanBtn">
      <span class="btn-text">🔍 Bắt đầu quét</span>
      <span class="btn-loading hidden">⏳ Đang quét...</span>
    </button>
  </form>
</div>

<!-- History -->
<div class="card" id="historyCard" style="display:none">
  <h3>🕘 Lịch sử quét gần đây</h3>
  <div class="history-list" id="historyList"></div>
</div>

<!-- Progress -->
<div id="progressPanel" class="card progress-card hidden">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:8px">
    <h3 style="margin:0">📡 Tiến trình quét</h3>
    <div style="display:flex;gap:6px;align-items:center">
      <span class="badge badge-time" id="elapsedBadge" title="Thời gian đã trôi qua">⏱️ 00:00</span>
      <span class="badge" id="etaBadge" style="background:rgba(254,202,87,.12);color:#feca57;display:none" title="Còn lại (ước tính)">⌛ ETA --:--</span>
      <span class="badge" id="rateBadge" style="background:rgba(84,160,255,.12);color:#54a0ff;display:none" title="Tốc độ">⚡ -- req/s</span>
      <button class="btn btn-ghost" id="cancelBtn" style="padding:4px 10px;font-size:12px">🛑 Huỷ</button>
    </div>
  </div>
  <div class="progress-info"><span id="progressPhase">Khởi tạo...</span><span id="progressCount"></span></div>
  <div class="progress-bar-bg"><div id="progressBar" class="progress-bar-fill"></div></div>
  <div id="progressMessage" class="progress-msg"></div>
  <div id="progressFound" class="progress-found hidden"></div>
</div>

<!-- Results -->
<div id="resultsArea"></div>

</main>
<footer class="footer">Web Leak Scanner Pro v8.0 – Async Security Scanner · deep crawl · wayback · DNS enum · screenshot · CORS · takeover · soft-404 filter · ETA · cancel</footer>
<div id="toast" class="toast"></div>

<script>
const $ = (s)=>document.querySelector(s);
const $$ = (s)=>document.querySelectorAll(s);

// Theme toggle
const THEME_KEY = 'wlsv5_theme';
function applyTheme(t){
  document.documentElement.setAttribute('data-theme', t);
  $('#themeToggle').textContent = t === 'dark' ? '🌙' : '☀️';
  localStorage.setItem(THEME_KEY, t);
}
applyTheme(localStorage.getItem(THEME_KEY) || 'dark');
$('#themeToggle').addEventListener('click', ()=>{
  const cur = document.documentElement.getAttribute('data-theme');
  applyTheme(cur === 'dark' ? 'light' : 'dark');
});

// Toast
function toast(msg){
  const t = $('#toast'); t.textContent = msg; t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'), 2200);
}

// History
async function loadHistory(){
  try{
    const r = await fetch('/history');
    const d = await r.json();
    if(!d.history || !d.history.length){ $('#historyCard').style.display='none'; return; }
    $('#historyCard').style.display='';
    const list = $('#historyList');
    list.innerHTML = d.history.map(h=>`
      <div class="history-item" data-scan-id="${h.scan_id}">
        <div>
          <div class="history-target">${h.target}</div>
          <div class="history-meta">${new Date(h.started_at).toLocaleString()} · ${h.leak_count} leaks · ${h.duration_seconds}s</div>
        </div>
        <span class="badge badge-time">↻ Reload</span>
      </div>
    `).join('');
    $$('.history-item').forEach(el=>{
      el.addEventListener('click', async ()=>{
        const id = el.dataset.scanId;
        await loadResult(id);
      });
    });
  }catch(e){}
}

// Tabs
function initTabs(){
  $$('.tab').forEach(t=>{
    t.addEventListener('click', ()=>{
      const target = t.dataset.tab;
      $$('.tab').forEach(x=>x.classList.remove('active'));
      $$('.tab-panel').forEach(x=>x.classList.remove('active'));
      t.classList.add('active');
      const panel = document.getElementById('tab-' + target);
      if(panel) panel.classList.add('active');
    });
  });
}

// Filter
function initFilter(){
  const f = $('#filterInput');
  if(!f) return;
  function applyFilter(){
    const q = f.value.toLowerCase();
    const sev = $('#filterSev').value;
    const hideS404 = $('#hideSoft404') ? $('#hideSoft404').checked : false;
    $$('.leak-item[data-sev]').forEach(el=>{
      const path = (el.dataset.path || '').toLowerCase();
      const s = el.dataset.sev;
      const isSoft = el.dataset.soft404 === 'true';
      const matchQ = !q || path.includes(q);
      let matchS = sev === 'all' || s === sev;
      // Nếu chọn info -> chỉ hiện soft-404
      if(sev === 'info') matchS = isSoft;
      // Ẩn soft-404 nếu user tick
      const matchHide = !(hideS404 && isSoft);
      el.style.display = (matchQ && matchS && matchHide) ? '' : 'none';
    });
  }
  f.addEventListener('input', applyFilter);
  $('#filterSev').addEventListener('change', applyFilter);
  const hideChk = $('#hideSoft404');
  if(hideChk) hideChk.addEventListener('change', applyFilter);
  // Apply ngay lần đầu
  applyFilter();
}

// Submit scan
let timerInterval = null;
let scanStartTs = 0;

function fmtTime(s){
  s = Math.max(0, Math.floor(s));
  const m = Math.floor(s / 60);
  const sec = s % 60;
  return String(m).padStart(2,'0') + ':' + String(sec).padStart(2,'0');
}

function startTimer(){
  scanStartTs = Date.now();
  const elapsed = $('#elapsedBadge');
  const eta = $('#etaBadge');
  const rate = $('#rateBadge');
  elapsed.style.display = '';
  eta.style.display = 'none';
  rate.style.display = 'none';
  if(timerInterval) clearInterval(timerInterval);
  timerInterval = setInterval(()=>{
    const e = (Date.now() - scanStartTs) / 1000;
    elapsed.textContent = '⏱️ ' + fmtTime(e);
  }, 250);
}

function stopTimer(){
  if(timerInterval){ clearInterval(timerInterval); timerInterval = null; }
}

// Phase translation fallback (dùng nếu backend không gửi phase_display)
const PHASE_FALLBACK = {
  'main_page':'🌐 Tải trang chính',
  'security_headers':'📜 Phân tích security headers',
  'fingerprint':'🛠️ Nhận diện công nghệ',
  'waf':'🛡️ Phát hiện WAF',
  'ssl':'🔒 Kiểm tra SSL/TLS',
  'ports':'🔌 Quét cổng',
  'ports_done':'✅ Xong quét cổng',
  'leak_scan':'📁 Quét leak paths',
  'robots':'🤖 Phân tích robots.txt',
  'links':'🔗 Trích xuất links/JS/forms',
  'secrets':'🔐 Quét secret trong HTML',
  'secrets_js':'📜 Quét secret trong JS files',
  'dirs':'📂 Kiểm tra directory listing',
  'brute':'🔍 Brute-force common files',
  'completed':'✅ Hoàn thành',
  'error':'❌ Lỗi',
  'cancelling':'🛑 Đang huỷ',
  'cancelled':'🛑 Đã huỷ',
  // v7.0 phases
  'sitemap':'🗺️ Đọc sitemap.xml',
  'crawl':'🕷️ Deep crawl',
  'query_fuzz':'❓ Test query params',
  'recursive_dirs':'🔁 Recursive dir check',
  'api_scan':'🔌 Test API endpoints',
  // v8.0 phases
  'screenshot':'📸 Chụp screenshot',
  'cors':'🔒 Test CORS',
  'dns_records':'📡 Query DNS records',
  'dns_enum':'🌐 DNS subdomain enum',
  'takeover':'🎯 Subdomain takeover check',
  'wayback':'🕰️ Fetch Wayback Machine',
  'wayback_test':'🕰️ Test wayback paths',
};

// Phases internal — KHÔNG hiển thị cho user
const INTERNAL_PHASES = new Set(['connected', 'keepalive']);

$('#scanForm').addEventListener('submit', async function(e){
  e.preventDefault();
  const btn = $('#scanBtn');
  const progressPanel = $('#progressPanel');
  const resultsArea = $('#resultsArea');
  const bar = $('#progressBar');
  const phase = $('#progressPhase');
  const count = $('#progressCount');
  const msg = $('#progressMessage');
  const found = $('#progressFound');
  const cancelBtn = $('#cancelBtn');

  btn.disabled = true;
  $('.btn-text').classList.add('hidden');
  $('.btn-loading').classList.remove('hidden');
  cancelBtn.disabled = false;
  progressPanel.classList.remove('hidden');
  resultsArea.innerHTML = '';
  bar.style.width = '0%';
  phase.textContent = 'Đang khởi tạo...';
  startTimer();

  let currentScanId = null;

  // Cancel button handler
  cancelBtn.onclick = async ()=>{
    if(!currentScanId) return;
    cancelBtn.disabled = true;
    cancelBtn.textContent = '⏳ Đang huỷ...';
    try{
      await fetch('/cancel/' + currentScanId, {method:'POST'});
      toast('🛑 Đã gửi yêu cầu huỷ');
    }catch(err){ toast('Lỗi huỷ: ' + err.message); }
  };

  const formData = new FormData(this);
  try{
    const resp = await fetch('/scan', {method:'POST', body:formData});
    const data = await resp.json();
    if(data.error){ toast('❌ ' + data.error); resetBtn(); stopTimer(); return; }
    const scanId = data.scan_id;
    currentScanId = scanId;

    const evtSource = new EventSource('/progress/' + scanId);
    evtSource.onmessage = function(e){
      try{
        const d = JSON.parse(e.data);
        // Bỏ qua internal heartbeats
        if(d.phase && INTERNAL_PHASES.has(d.phase)) return;

        // Phase display — ưu tiên phase_display từ backend, fallback translation
        if(d.phase || d.phase_display){
          const display = d.phase_display || PHASE_FALLBACK[d.phase] || d.phase || '';
          if(display) phase.textContent = display;
        }

        // Progress bar + count
        if(d.total > 0){
          const pct = Math.round((d.current/d.total)*100);
          bar.style.width = pct + '%';
          count.textContent = d.current + '/' + d.total + ' (' + pct + '%)';
        } else {
          count.textContent = '';
        }

        // Message
        if(d.message) msg.textContent = d.message;

        // Found counter
        if(d.found !== undefined && d.found > 0){
          found.classList.remove('hidden');
          found.textContent = '🔍 Tìm thấy: ' + d.found;
        }

        // Elapsed (từ backend, chính xác hơn timer local)
        const elapsedBadge = $('#elapsedBadge');
        const etaBadge = $('#etaBadge');
        const rateBadge = $('#rateBadge');
        if(d.elapsed !== undefined){
          elapsedBadge.textContent = '⏱️ ' + fmtTime(d.elapsed);
          // Hiện eta + rate nếu có
          if(d.eta !== null && d.eta !== undefined && d.total > 0){
            etaBadge.style.display = '';
            etaBadge.textContent = '⌛ ETA ' + fmtTime(d.eta);
          }
          if(d.rate !== undefined && d.rate > 0){
            rateBadge.style.display = '';
            rateBadge.textContent = '⚡ ' + d.rate + ' req/s';
          }
        }

        // Terminal phases
        if(d.phase === 'completed' || d.phase === 'error' || d.phase === 'cancelled'){
          evtSource.close();
          stopTimer();
          cancelBtn.style.display = 'none';
          if(d.phase === 'cancelled'){
            // vẫn load result để xem partial
            setTimeout(()=>loadResult(scanId).then(loadHistory), 200);
          } else {
            loadResult(scanId).then(loadHistory);
          }
        }
      }catch(err){}
    };
    evtSource.onerror = function(){
      evtSource.close();
      stopTimer();
      loadResult(scanId).then(loadHistory);
    };
  }catch(err){
    toast('❌ Lỗi mạng: ' + err.message);
    resetBtn();
    stopTimer();
  }
});

function resetBtn(){
  $('#scanBtn').disabled = false;
  $('.btn-text').classList.remove('hidden');
  $('.btn-loading').classList.add('hidden');
  $('#cancelBtn').style.display = '';
  $('#cancelBtn').disabled = false;
  $('#cancelBtn').textContent = '🛑 Huỷ';
}

async function loadResult(scanId){
  const resp = await fetch('/result/' + scanId);
  const html = await resp.text();
  $('#resultsArea').innerHTML = html;
  resetBtn();
  initTabs();
  initFilter();
  // Smooth scroll
  $('#resultsArea').scrollIntoView({behavior:'smooth', block:'start'});
}

loadHistory();
</script>
</body>
</html>
"""

# ── HTML Template (RESULT) ──
RESULT_HTML = r"""
{% if result %}
<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
  <h2 style="margin:0">📊 Kết quả cho {{ result.target }}</h2>
  <div>
    {% if result.duration_seconds %}<span class="badge badge-time">⏱️ {{ result.duration_seconds }}s</span>{% endif %}
    {% if result.cancelled %}<span class="badge" style="background:rgba(255,107,107,.15);color:#ff6b6b">🛑 Đã huỷ</span>{% endif %}
    {% if result.stats and result.stats.soft_404_filtered %}<span class="badge" style="background:rgba(160,160,176,.15);color:#a0a0b0">🎯 Soft-404 filter: {{ result.stats.soft_404_filtered }}</span>{% endif %}
    {% if result.waf.detected %}<span class="badge badge-waf">🛡️ WAF: {{ result.waf.detected|join(", ") }}</span>{% endif %}
    {% if result.cdn %}<span class="badge" style="background:rgba(254,202,87,.12);color:#feca57">☁️ CDN: {{ result.cdn|join(", ") }}</span>{% endif %}
    {% if result.ssl %}
      {% if result.ssl.days_remaining is defined and result.ssl.days_remaining != None %}
        {% if result.ssl.days_remaining > 30 %}
          <span class="badge badge-ssl-ok">🔒 SSL {{ result.ssl.days_remaining }}d còn lại</span>
        {% elif result.ssl.days_remaining > 0 %}
          <span class="badge badge-ssl-warn">🔒 SSL sắp hết ({{ result.ssl.days_remaining }}d)</span>
        {% else %}
          <span class="badge badge-ssl-err">🔓 SSL ĐÃ HẾT HẠN</span>
        {% endif %}
      {% endif %}
    {% endif %}
  </div>
</div>

{% if result.error %}
<div class="alert alert-error"><strong>❌ Lỗi:</strong> {{ result.error }}</div>
{% else %}

<!-- Stats grid -->
<div class="stats-grid">
  <div class="stat-box"><div class="stat-number">{{ result.main.code }}</div><div class="stat-label">Main code</div></div>
  <div class="stat-box"><div class="stat-number sev-crit">{{ result.stats.critical_count|default(0) }}</div><div class="stat-label">Critical</div></div>
  <div class="stat-box"><div class="stat-number sev-high">{{ result.stats.high_count|default(0) }}</div><div class="stat-label">High</div></div>
  <div class="stat-box"><div class="stat-number">{{ result.leak|length }}</div><div class="stat-label">Leaks</div></div>
  <div class="stat-box"><div class="stat-number sev-crit">{{ result.stats.secret_critical|default(0) }}</div><div class="stat-label">Secrets crit</div></div>
  <div class="stat-box"><div class="stat-number">{{ result.ports|length }}</div><div class="stat-label">Open ports</div></div>
</div>

<!-- Tabs -->
<div class="tabs">
  <button class="tab active" data-tab="summary">📋 Tóm tắt</button>
  <button class="tab" data-tab="leaks">📁 Leaks <span class="count">{{ result.leak|length }}</span></button>
  <button class="tab" data-tab="secrets">🔐 Secrets <span class="count">{{ result.secrets|length }}</span></button>
  <button class="tab" data-tab="crawled">🕷️ Crawled <span class="count">{{ result.crawled_urls|length + result.sitemap_urls|length }}</span></button>
  <button class="tab" data-tab="apis">🔌 APIs <span class="count">{{ result.api_endpoints|length }}</span></button>
  <button class="tab" data-tab="recon">🛰️ Recon <span class="count">{{ result.wayback_urls|length + result.dns_subdomains|length + result.takeover_risks|length }}</span></button>
  <button class="tab" data-tab="tech">🛠️ Tech & WAF</button>
  <button class="tab" data-tab="network">🌐 Network</button>
  <button class="tab" data-tab="headers">📜 Headers & Cookies</button>
  <button class="tab" data-tab="forms">📝 Forms <span class="count">{{ result.forms|length }}</span></button>
  <button class="tab" data-tab="raw">🔎 Raw</button>
</div>

<!-- Tab: Summary -->
<div class="tab-panel active" id="tab-summary">
  {% if result.stats.missing_security_headers %}
  <div class="alert alert-warn">⚠️ Thiếu <strong>{{ result.stats.missing_security_headers }}</strong> security header(s) quan trọng</div>
  {% endif %}
  {% if result.stats.insecure_cookies %}
  <div class="alert alert-warn">🍪 Có <strong>{{ result.stats.insecure_cookies }}</strong> cookie thiếu flag bảo mật</div>
  {% endif %}
  {% if result.stats.secret_critical %}
  <div class="alert alert-error">🚨 Phát hiện <strong>{{ result.stats.secret_critical }}</strong> secret mức CRITICAL (AWS/Stripe/GitHub/private key...)</div>
  {% endif %}
  {% if result.stats.critical_count %}
  <div class="alert alert-error">🚨 Có <strong>{{ result.stats.critical_count }}</strong> leak path mức CRITICAL (.env, .aws, .ssh, terraform...)</div>
  {% endif %}
  {% if result.waf.detected %}
  <div class="alert alert-info">🛡️ WAF phát hiện: <strong>{{ result.waf.detected|join(", ") }}</strong>. Nên giảm tốc độ scan.</div>
  {% endif %}

  {% if result.page_summary %}
  <div class="section-title">📄 Tóm tắt nội dung trang</div>
  <div style="background:var(--bg3);padding:10px;border-radius:8px;font-size:13px;color:var(--muted)">{{ result.page_summary }}</div>
  {% endif %}

  {% if result.technologies %}
  <div class="section-title">🛠️ Công nghệ phát hiện</div>
  <div>{% for t in result.technologies %}<span class="tech-tag">{{ t }}</span>{% endfor %}</div>
  {% endif %}

  {% if result.cdn %}
  <div class="section-title">☁️ CDN / Edge</div>
  <div>{% for c in result.cdn %}<span class="cdn-badge">{{ c }}</span>{% endfor %}</div>
  {% endif %}

  {% if result.ssl and result.ssl.subject %}
  <div class="section-title">🔒 SSL/TLS Certificate</div>
  <div style="background:var(--bg3);padding:10px;border-radius:8px;font-family:monospace;font-size:12px">
    <div><strong>Subject:</strong> {{ result.ssl.subject }}</div>
    <div><strong>Issuer:</strong> {{ result.ssl.issuer }}</div>
    <div><strong>Valid until:</strong> {{ result.ssl.not_after }}</div>
    {% if result.ssl.days_remaining != None %}
      <div><strong>Days remaining:</strong> {{ result.ssl.days_remaining }}</div>
    {% endif %}
  </div>
  {% endif %}

  {% if result.waf.detected %}
  <div class="section-title">🛡️ WAF / Bảo vệ</div>
  <div class="waf-info">
    <p><strong>Phát hiện:</strong> {{ result.waf.detected|join(", ") }}</p>
    {% if result.waf.recommendations %}
    <ul style="margin-top:6px;margin-left:16px;color:var(--muted);font-size:13px">
      {% for r in result.waf.recommendations %}<li>{{ r }}</li>{% endfor %}
    </ul>
    {% endif %}
  </div>
  {% endif %}

  {% if result.subdomain_hints %}
  <div class="section-title">🌐 Gợi ý subdomain (cần DNS check ngoài)</div>
  <div style="max-height:120px;overflow-y:auto;font-size:12px;color:var(--muted)">
    {% for s in result.subdomain_hints %}<div style="padding:2px 0;font-family:monospace">{{ s }}</div>{% endfor %}
  </div>
  {% endif %}
</div>

<!-- Tab: Leaks -->
<div class="tab-panel" id="tab-leaks">
  <div class="filter-bar">
    <input id="filterInput" placeholder="🔎 Lọc theo path...">
    <select id="filterSev">
      <option value="all">Tất cả severity</option>
      <option value="critical">🔴 Critical</option>
      <option value="high">🟠 High</option>
      <option value="medium">🟡 Medium</option>
      <option value="low">🟢 Low</option>
      <option value="info">⚪ Info (soft-404)</option>
    </select>
    <label style="font-size:12px;color:var(--muted);display:flex;align-items:center;gap:4px;cursor:pointer">
      <input type="checkbox" id="hideSoft404" checked> Ẩn soft-404
    </label>
  </div>
  {% if result.leak %}
    {% for item in result.leak %}
    {% set sev_class = 'crit' if item.severity == 'critical' else ('high' if item.severity == 'high' else ('med' if item.severity == 'medium' else '')) %}
    <div class="leak-item {{ sev_class }} {% if item.soft_404 %}soft404{% endif %}" data-path="{{ item.path }}" data-sev="{{ item.severity }}" data-soft404="{{ 'true' if item.soft_404 else 'false' }}" {% if item.soft_404 %}style="opacity:.5"{% endif %}>
      <div class="leak-header">
        <span class="code-badge code-{{ item.code }}">{{ item.code }}</span>
        <span class="sev-badge sev-{{ item.severity }}">{{ item.severity }}</span>
        {% if item.soft_404 %}<span class="sev-badge sev-info">SOFT-404</span>{% endif %}
        {% if item.is_api %}<span class="sev-badge sev-info">API</span>{% endif %}
        {% if item.from_wayback %}<span class="sev-badge sev-info">WAYBACK</span>{% endif %}
        <span class="leak-path">{{ item.path }}</span>
        {% if item.size > 0 %}<span class="leak-size">{{ item.size }} bytes</span>{% endif %}
        {% if item.response_time_ms %}<span class="leak-rt">{{ item.response_time_ms }}ms</span>{% endif %}
      </div>
      <div class="leak-url">{{ item.url }}</div>
      {% if item.preview %}<details class="leak-preview"><summary>Xem trước ({{ item.preview|length }} chars)</summary><pre>{{ item.preview }}</pre></details>{% endif %}
    </div>
    {% endfor %}
  {% else %}
    <p class="empty-state">Không phát hiện file nhạy cảm. ✅</p>
  {% endif %}
</div>

<!-- Tab: Secrets -->
<div class="tab-panel" id="tab-secrets">
  {% if result.secrets %}
    {% for s in result.secrets %}
    <div class="leak-item {{ 'crit' if s.severity == 'critical' else ('high' if s.severity == 'high' else '') }}">
      <div class="leak-header">
        <span class="sev-badge sev-{{ s.severity }}">{{ s.severity }}</span>
        <strong>{{ s.type }}</strong>
        <span style="font-family:monospace;font-size:12px;color:var(--muted)">{{ s.match_masked }}</span>
      </div>
      <div style="font-size:12px;color:var(--dim);margin-top:4px">📍 {{ s.source }}</div>
      <div style="font-size:11px;color:var(--muted);margin-top:2px">{{ s.description }}</div>
    </div>
    {% endfor %}
  {% else %}
    <p class="empty-state">Không phát hiện secret pattern. ✅</p>
  {% endif %}
</div>

<!-- v7.0 Tab: Crawled URLs -->
<div class="tab-panel" id="tab-crawled">
  {% if result.sitemap_urls %}
  <div class="section-title">🗺️ Sitemap URLs <span class="count">{{ result.sitemap_urls|length }}</span></div>
  <div style="max-height:240px;overflow-y:auto;background:var(--bg3);padding:10px;border-radius:8px;font-family:monospace;font-size:12px">
    {% for u in result.sitemap_urls %}
    <div style="padding:2px 0;word-break:break-all"><a href="{{ u }}" target="_blank" style="color:var(--accent2);text-decoration:none">{{ u }}</a></div>
    {% endfor %}
  </div>
  {% endif %}

  <div class="section-title">🕷️ Crawled pages (recursive) <span class="count">{{ result.crawled_urls|length }}</span></div>
  {% if result.crawled_urls %}
  <div style="max-height:300px;overflow-y:auto;background:var(--bg3);padding:10px;border-radius:8px;font-family:monospace;font-size:12px">
    {% for u in result.crawled_urls %}
    <div style="padding:2px 0;word-break:break-all"><a href="{{ u }}" target="_blank" style="color:var(--accent);text-decoration:none">{{ u }}</a></div>
    {% endfor %}
  </div>
  {% else %}
    <p class="empty-state">Không có crawled URLs (tick "Deep crawl" trong form để bật spider).</p>
  {% endif %}

  {% if result.links %}
  <div class="section-title">🔗 Links phát hiện (main page) <span class="count">{{ result.links|length }}</span></div>
  <div style="max-height:200px;overflow-y:auto">
    {% for link in result.links %}
    <div style="padding:3px 0;font-size:12px"><a href="{{ link }}" target="_blank" style="color:var(--accent2);text-decoration:none;word-break:break-all">{{ link }}</a></div>
    {% endfor %}
  </div>
  {% endif %}

  {% if result.recursive_dirs %}
  <div class="section-title">🔁 Recursive dir probes <span class="count">{{ result.recursive_dirs|length }}</span></div>
  {% for r in result.recursive_dirs %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="code-badge code-{{ r.code }}">{{ r.code }}</span>
      <span class="sev-badge sev-{{ r.severity }}">{{ r.severity }}</span>
      <span class="leak-path">{{ r.sub }}</span>
      <span style="font-size:11px;color:var(--dim)">from {{ r.parent }}</span>
    </div>
    <div class="leak-url">{{ r.url }}</div>
  </div>
  {% endfor %}
  {% endif %}

  {% if result.query_param_hits %}
  <div class="section-title">❓ Query param hits <span class="count">{{ result.query_param_hits|length }}</span></div>
  {% for q in result.query_param_hits %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="code-badge code-{{ q.code }}">{{ q.code }}</span>
      <span class="sev-badge sev-medium">PARAM</span>
      <span class="leak-path">{{ q.query }}</span>
      <span class="leak-size">{{ q.size }} bytes (diff: {{ q.size_diff }})</span>
    </div>
    <details class="leak-preview"><summary>Xem trước</summary><pre>{{ q.preview }}</pre></details>
  </div>
  {% endfor %}
  {% endif %}

  {% if result.comments %}
  <div class="section-title">💬 HTML comments <span class="count">{{ result.comments|length }}</span></div>
  <pre class="robots-content" style="max-height:200px">{% for c in result.comments %}{{ loop.index }}. {{ c }}
———————————————————————————
{% endfor %}</pre>
  {% endif %}
</div>

<!-- v7.0 Tab: API Endpoints -->
<div class="tab-panel" id="tab-apis">
  {% if result.api_endpoints %}
  <div class="section-title">🔌 API Endpoints phát hiện (regex từ HTML/JS) <span class="count">{{ result.api_endpoints|length }}</span></div>
  {% for a in result.api_endpoints %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="sev-badge sev-info">API</span>
      <span class="leak-path">{{ a.path }}</span>
    </div>
    <div class="leak-url"><a href="{{ a.url }}" target="_blank" style="color:var(--accent2);text-decoration:none">{{ a.url }}</a></div>
  </div>
  {% endfor %}
  {% else %}
    <p class="empty-state">Không phát hiện API endpoint pattern trong HTML/JS.</p>
  {% endif %}

  {% if result.stats and result.stats.api_hit_count %}
  <div class="section-title">✅ API Endpoints HTTP hits ({{ result.stats.api_hit_count }})</div>
  <p style="font-size:13px;color:var(--muted)">Xem chi tiết trong tab Leaks — các API có code 200/401/403 được merge vào leak list với badge severity.</p>
  {% endif %}
</div>

<!-- v8.0 Tab: Recon -->
<div class="tab-panel" id="tab-recon">
  {% if result.screenshot %}
  <div class="section-title">📸 Screenshot main page ({{ result.screenshot.size_bytes }} bytes)</div>
  <div style="background:var(--bg3);padding:10px;border-radius:8px;text-align:center">
    <img src="/screenshot/{{ result.screenshot.path.split('_')[-1].replace('.png','') }}" alt="screenshot" style="max-width:100%;border-radius:8px;border:1px solid var(--border)">
    <div style="font-size:11px;color:var(--dim);margin-top:6px">Click chuột phải → "Save image as..." để tải</div>
  </div>
  {% elif result.screenshot_enabled %}
    <div class="alert alert-warn">⚠️ Screenshot được yêu cầu nhưng không có kết quả — có thể Playwright chưa cài. Chạy: <code>pip install playwright && playwright install chromium</code></div>
  {% endif %}

  {% if result.cors and result.cors.issues %}
  <div class="section-title">🔒 CORS Issues <span class="count">{{ result.cors.issues|length }}</span></div>
  {% for issue in result.cors.issues %}
  <div class="leak-item {{ 'crit' if issue.severity == 'critical' else ('high' if issue.severity == 'high' else '') }}">
    <div class="leak-header">
      <span class="sev-badge sev-{{ issue.severity }}">{{ issue.severity }}</span>
      <strong>{{ issue.type }}</strong>
    </div>
    <div style="font-size:12px;color:var(--muted);margin-top:4px">{{ issue.detail }}</div>
    {% if result.cors.acao %}<div style="font-size:11px;color:var(--dim);margin-top:4px;font-family:monospace">ACAO: {{ result.cors.acao }} | ACAC: {{ result.cors.acac or '—' }}</div>{% endif %}
  </div>
  {% endfor %}
  {% elif result.cors_enabled %}
    <div class="alert alert-info">✅ CORS an toàn — server không reflect Origin header.</div>
  {% endif %}

  {% if result.dns_records %}
  <div class="section-title">📡 DNS Records ({{ result.dns_records.keys()|list|length }} types)</div>
  <pre class="robots-content" style="max-height:200px">{% for qtype, vals in result.dns_records.items() %}{{ qtype }}:
{% for v in vals %}  {{ v }}
{% endfor %}{% endfor %}</pre>
  {% endif %}

  {% if result.dns_error %}
  <div class="alert alert-warn">⚠️ DNS module error: {{ result.dns_error }}</div>
  {% endif %}

  {% if result.dns_subdomains %}
  <div class="section-title">🌐 DNS Subdomains resolved <span class="count">{{ result.dns_subdomains|length }}</span></div>
  <div style="max-height:240px;overflow-y:auto">
    {% for s in result.dns_subdomains %}
    <div class="leak-item">
      <div class="leak-header">
        <span class="sev-badge sev-info">A</span>
        <span class="leak-path">{{ s.subdomain }}</span>
      </div>
      <div class="leak-url">{% for ip in s.ips %}{{ ip }}{% if not loop.last %} · {% endif %}{% endfor %}</div>
    </div>
    {% endfor %}
  </div>
  {% elif result.dns_enum_enabled %}
    <div class="alert alert-warn">⚠️ DNS enum được yêu cầu nhưng không có kết quả — kiểm tra HAS_DNS hoặc cài dnspython.</div>
  {% endif %}

  {% if result.takeover_risks %}
  <div class="section-title">🎯 Subdomain Takeover Risks <span class="count">{{ result.takeover_risks|length }}</span></div>
  {% for r in result.takeover_risks %}
  <div class="leak-item {{ 'crit' if r.severity == 'critical' else ('high' if r.severity == 'high' else '') }}">
    <div class="leak-header">
      <span class="sev-badge sev-{{ r.severity }}">{{ r.severity }}</span>
      <span class="leak-path">{{ r.subdomain }}</span>
    </div>
    <div class="leak-url">→ CNAME: <strong>{{ r.cname }}</strong></div>
    <div style="font-size:11px;color:var(--warn);margin-top:4px">⚠️ Service: {{ r.service }} — có thể bị takeover nếu CNAME không còn control bởi domain hiện tại.</div>
  </div>
  {% endfor %}
  {% endif %}

  {% if result.wayback_urls %}
  <div class="section-title">🕰️ Wayback Machine URLs <span class="count">{{ result.wayback_urls|length }}</span></div>
  <details>
    <summary style="cursor:pointer;color:var(--accent);font-weight:600">Hiện {{ result.wayback_urls|length }} URLs lịch sử</summary>
    <div style="max-height:300px;overflow-y:auto;background:var(--bg3);padding:10px;border-radius:8px;font-family:monospace;font-size:11px">
      {% for u in result.wayback_urls %}
      <div style="padding:2px 0;word-break:break-all"><a href="{{ u }}" target="_blank" style="color:var(--accent2);text-decoration:none">{{ u }}</a></div>
      {% endfor %}
    </div>
  </details>

  {% if result.wayback_hits %}
  <div class="section-title">✅ Wayback paths vẫn còn truy cập được <span class="count">{{ result.wayback_hits|length }}</span></div>
  <p style="font-size:13px;color:var(--muted)">Đã merge vào tab Leaks với badge severity + tag "from_wayback".</p>
  {% endif %}
  {% elif result.scan_wayback_enabled %}
    <div class="empty-state">Không có URL lịch sử trên Wayback Machine cho domain này.</div>
  {% endif %}

  {% if not result.has_dns_module %}
  <div class="alert alert-warn">⚠️ <code>dnspython</code> chưa cài — DNS enum và DNS records sẽ không chạy. Cài: <code>pip install dnspython</code></div>
  {% endif %}
  {% if not result.has_playwright %}
  <div class="alert alert-warn">⚠️ <code>playwright</code> chưa cài — screenshot sẽ không chạy. Cài: <code>pip install playwright && playwright install chromium</code></div>
  {% endif %}
</div>

<!-- Tab: Tech & WAF -->
<div class="tab-panel" id="tab-tech">
  <div class="section-title">🛠️ Công nghệ ({{ result.technologies|length }})</div>
  {% if result.technologies %}
    <div>{% for t in result.technologies %}<span class="tech-tag">{{ t }}</span>{% endfor %}</div>
  {% else %}<p class="empty-state">Không xác định được tech.</p>{% endif %}

  <div class="section-title">🛡️ WAF</div>
  {% if result.waf.detected %}
    <div class="waf-info">
      <p><strong>Phát hiện:</strong> {{ result.waf.detected|join(", ") }}</p>
      {% if result.waf.recommendations %}
      <ul style="margin-top:6px;margin-left:16px;color:var(--muted);font-size:13px">
        {% for r in result.waf.recommendations %}<li>{{ r }}</li>{% endfor %}
      </ul>
      {% endif %}
    </div>
  {% else %}<p class="empty-state">Không phát hiện WAF.</p>{% endif %}

  <div class="section-title">☁️ CDN</div>
  {% if result.cdn %}<div>{% for c in result.cdn %}<span class="cdn-badge">{{ c }}</span>{% endfor %}</div>
  {% else %}<p class="empty-state">Không phát hiện CDN.</p>{% endif %}

  {% if result.robots %}
  <div class="section-title">🤖 robots.txt paths ({{ result.robots|length }})</div>
  <pre class="robots-content">{{ result.robots|join("\n") }}</pre>
  {% endif %}
</div>

<!-- Tab: Network -->
<div class="tab-panel" id="tab-network">
  {% if result.ports %}
  <div class="section-title">🔌 Cổng mở ({{ result.ports|length }})</div>
  <div>{% for p in result.ports %}<span class="port-badge">{{ p }}</span>{% endfor %}</div>
  {% else %}<p class="empty-state">Không có cổng mở trong danh sách check.</p>{% endif %}

  {% if result.dirs %}
  <div class="section-title">📂 Directory Listing ({{ result.dirs|length }})</div>
  {% for d in result.dirs %}
    <div class="leak-item"><div class="leak-header"><span>📂</span><a href="{{ d.url }}" target="_blank" style="color:var(--accent);text-decoration:none;word-break:break-all">{{ d.url }}</a><span style="font-size:11px;color:var(--warn)">({{ d.type }})</span></div></div>
  {% endfor %}
  {% endif %}

  {% if result.brute %}
  <div class="section-title">🔍 Brute-force common files ({{ result.brute|length }})</div>
  {% for f in result.brute %}
    <div style="padding:4px 0;font-size:13px"><span class="code-badge code-{{ f.code }}">{{ f.code }}</span> <span class="sev-badge sev-{{ f.severity }}">{{ f.severity }}</span> <span style="font-family:monospace">{{ f.path }}</span> {% if f.response_time_ms %}<span style="font-size:11px;color:var(--dim)">{{ f.response_time_ms }}ms</span>{% endif %}</div>
  {% endfor %}
  {% endif %}

  {% if result.links %}
  <div class="section-title">🔗 Liên kết cùng domain ({{ result.links|length }})</div>
  <div style="max-height:240px;overflow-y:auto">
    {% for link in result.links %}
    <div style="padding:4px 0;font-size:12px"><a href="{{ link }}" target="_blank" style="color:var(--accent2);text-decoration:none;word-break:break-all">{{ link }}</a></div>
    {% endfor %}
  </div>
  {% endif %}
</div>

<!-- Tab: Headers & Cookies -->
<div class="tab-panel" id="tab-headers">
  <div class="section-title">📜 Security Headers ({{ result.security_headers|length }})</div>
  {% for h in result.security_headers %}
  <div class="sec-header-row {{ 'sec-header-missing' if h.missing else 'sec-header-present' }}">
    <div>
      <span class="sec-header-name">{{ h.header }}</span>
      {% if h.missing %}<span class="sev-badge sev-{{ h.severity }}" style="margin-left:6px">MISSING</span>{% endif %}
    </div>
    <div class="sec-header-value">{{ h.value or '—' }}</div>
  </div>
  {% endfor %}

  <div class="section-title">🍪 Cookies ({{ result.cookies|length }})</div>
  {% if result.cookies %}
    {% for c in result.cookies %}
    <div class="cookie-item">
      <span class="cookie-name">{{ c.name }}</span>
      <span style="font-family:monospace;font-size:11px;color:var(--dim)">{{ c.value_preview }}</span><br>
      {% if c.flags.httponly %}<span class="cookie-flag flag-ok">HttpOnly</span>{% else %}<span class="cookie-flag flag-bad">!HttpOnly</span>{% endif %}
      {% if c.flags.secure %}<span class="cookie-flag flag-ok">Secure</span>{% else %}<span class="cookie-flag flag-bad">!Secure</span>{% endif %}
      {% if c.flags.samesite %}<span class="cookie-flag flag-ok">SameSite={{ c.flags.samesite }}</span>{% else %}<span class="cookie-flag flag-bad">!SameSite</span>{% endif %}
      {% if c.flags.host_prefix %}<span class="cookie-flag flag-ok">__Host-</span>{% endif %}
      {% if c.flags.secure_prefix %}<span class="cookie-flag flag-ok">__secure-</span>{% endif %}
      {% if c.issues %}<div style="font-size:11px;color:var(--danger);margin-top:4px">⚠️ {{ c.issues|join("; ") }}</div>{% endif %}
    </div>
    {% endfor %}
  {% else %}<p class="empty-state">Không có cookie.</p>{% endif %}

  <div class="section-title">📡 Main Response Headers</div>
  <pre class="robots-content">{% for k, v in result.main.headers.items() %}{{ k }}: {{ v }}
{% endfor %}</pre>
</div>

<!-- Tab: Forms -->
<div class="tab-panel" id="tab-forms">
  {% if result.forms %}
    {% for f in result.forms %}
    <div class="form-item">
      <div><strong>{{ f.method }}</strong> <span class="form-action">{{ f.action or "(same page)" }}</span>
        {% if f.type == 'login' %}<span class="form-tag form-tag-login">LOGIN</span>{% endif %}
        {% if f.type == 'upload' %}<span class="form-tag form-tag-upload">UPLOAD</span>{% endif %}
        {% if f.has_csrf_token %}<span class="form-tag form-tag-csrf">CSRF</span>{% endif %}
      </div>
      <div style="font-size:11px;color:var(--dim);margin-top:4px">Inputs: {{ f.input_count }}{% if f.has_hidden %} · có hidden field{% endif %}{% if f.has_password %} · có password{% endif %}{% if f.has_file %} · có file upload{% endif %}</div>
    </div>
    {% endfor %}
  {% else %}<p class="empty-state">Không phát hiện form.</p>{% endif %}

  {% if result.js_links %}
  <div class="section-title">📜 JS Files ({{ result.js_links|length }})</div>
  <div style="max-height:200px;overflow-y:auto">
    {% for j in result.js_links %}
    <div style="padding:3px 0;font-size:12px"><a href="{{ j }}" target="_blank" style="color:var(--accent2);text-decoration:none;word-break:break-all">{{ j }}</a></div>
    {% endfor %}
  </div>
  {% endif %}
</div>

<!-- Tab: Raw -->
<div class="tab-panel" id="tab-raw">
  <details>
    <summary style="cursor:pointer;color:var(--accent);font-weight:600">📜 Full JSON result (click to expand)</summary>
    <pre class="robots-content" style="max-height:500px">{{ result|tojson(indent=2)|forceescape }}</pre>
  </details>
</div>

<!-- Actions -->
<div class="actions">
  <form method="post" action="/download_json" style="display:inline">
    <input type="hidden" name="json_data" value="{{ result|tojson|forceescape }}">
    <button type="submit" class="btn btn-secondary">⬇️ JSON</button>
  </form>
  <form method="post" action="/download_csv" style="display:inline">
    <input type="hidden" name="json_data" value="{{ result|tojson|forceescape }}">
    <button type="submit" class="btn btn-secondary">⬇️ CSV</button>
  </form>
  <form method="post" action="/download_html" style="display:inline">
    <input type="hidden" name="json_data" value="{{ result|tojson|forceescape }}">
    <button type="submit" class="btn btn-secondary">⬇️ HTML report</button>
  </form>
  <button class="btn btn-ghost" onclick="navigator.clipboard.writeText('{{ result.target }}').then(()=>{});">📋 Copy URL</button>
</div>

{% endif %}
</div>
{% endif %}
"""

# ── Routes ──
@app.route("/")
def index():
    return render_template_string(PAGE_HTML)

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target", "").strip()
    if not target:
        return jsonify({"scan_id": None, "error": "URL trống"})

    custom_headers = parse_headers(request.form.get("headers", ""))
    proxy = request.form.get("proxy", "").strip() or None
    try:
        timeout = int(request.form.get("timeout", 10))
        if not (1 <= timeout <= 60): timeout = 10
    except Exception:
        timeout = 10
    allow_redirects = request.form.get("redirect") == "yes"
    scan_js = request.form.get("scan_js", "yes") == "yes"
    deep_crawl = request.form.get("deep_crawl", "no") == "yes"
    scan_wayback = request.form.get("wayback", "no") == "yes"
    dns_enum = request.form.get("dns_enum", "no") == "yes"
    take_shot = request.form.get("screenshot", "no") == "yes"
    scan_cors = request.form.get("cors", "no") == "yes"

    scan_id = int(time.time() * 1000)

    with prog_lock:
        progress_queues[scan_id] = queue.Queue(maxsize=500)
        scan_starts[scan_id] = time.time()

    push_history({
        "scan_id": scan_id,
        "target": target,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "status": "running",
        "leak_count": 0,
        "duration_seconds": 0,
    })

    async def progress_cb(data):
        send_prog(scan_id, data)

    def do_scan():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(deep_scan(
                target, custom_headers, proxy, timeout,
                allow_redirects, progress_cb, scan_js, scan_id, deep_crawl,
                scan_wayback, dns_enum, take_shot, scan_cors
            ))
            scan_results[scan_id] = result
            # update history
            with prog_lock:
                for h in scan_history:
                    if h["scan_id"] == scan_id:
                        h["status"] = "cancelled" if result.get("cancelled") else "done"
                        h["leak_count"] = result.get("stats", {}).get("real_leak_count", 0)
                        h["duration_seconds"] = result.get("duration_seconds", 0)
                        break
            send_prog(scan_id, {
                "phase": "cancelled" if result.get("cancelled") else "completed",
                "phase_display": "🛑 Đã huỷ" if result.get("cancelled") else "✅ Hoàn thành",
                "message": f"Done in {result['duration_seconds']}s · {result.get('stats',{}).get('real_leak_count',0)} real leaks (soft-404 filter: {result.get('soft_404_filtered',0)})",
            })
        except Exception as e:
            scan_results[scan_id] = {
                "target": target, "error": str(e),
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_seconds": 0, "stats": {}, "leak": [], "secrets": [],
                "ports": [], "dirs": [], "brute": [], "technologies": [],
                "waf": {"detected": [], "recommendations": [], "should_slow_down": False},
                "cdn": [], "cookies": [], "security_headers": [],
                "links": [], "js_links": [], "forms": [], "robots": [],
                "main": {}, "subdomain_hints": [], "page_summary": "",
                "errors": [str(e)], "scanner_version": "v5.0",
            }
            with prog_lock:
                for h in scan_history:
                    if h["scan_id"] == scan_id:
                        h["status"] = "error"
                        break
            send_prog(scan_id, {"phase": "error", "message": str(e)})
        finally:
            time.sleep(120)
            with prog_lock:
                progress_queues.pop(scan_id, None)
                scan_cancels.discard(scan_id)
                scan_starts.pop(scan_id, None)
            scan_results.pop(scan_id, None)

    threading.Thread(target=do_scan, daemon=True).start()
    return jsonify({"scan_id": scan_id})

@app.route("/progress/<int:scan_id>")
def progress_stream(scan_id):
    def stream():
        time.sleep(0.2)
        with prog_lock:
            q = progress_queues.get(scan_id)
        if not q:
            yield fmt_sse(json.dumps({"phase": "completed",
                                       "message": "Scan đã hoàn thành hoặc không tồn tại"}))
            return
        yield fmt_sse(json.dumps({"phase": "connected", "message": "SSE connected"}))
        while True:
            try:
                msg = q.get(timeout=20)
                yield fmt_sse(msg)
                try:
                    d = json.loads(msg)
                    if d.get("phase") in ("completed", "error"):
                        break
                except Exception:
                    pass
            except queue.Empty:
                yield fmt_sse(json.dumps({"phase": "keepalive"}))
    return Response(stream(), mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache",
                             "X-Accel-Buffering": "no"})

@app.route("/result/<int:scan_id>")
def result(scan_id):
    result = scan_results.get(scan_id, {})
    return render_template_string(RESULT_HTML, result=result)

@app.route("/history")
def history():
    with prog_lock:
        # only return finished scans for history list
        items = [{"scan_id": h["scan_id"], "target": h["target"],
                  "started_at": h["started_at"], "leak_count": h.get("leak_count", 0),
                  "duration_seconds": h.get("duration_seconds", 0),
                  "status": h.get("status", "")} for h in scan_history]
    return jsonify({"history": items})

@app.route("/screenshot/<int:scan_id>")
def screenshot(scan_id):
    """Serve screenshot PNG từ /tmp/wlscan_screenshots/scan_<id>.png."""
    path = os.path.join(SCREENSHOT_DIR, f"scan_{scan_id}.png")
    if not os.path.exists(path):
        return "Not found", 404
    with open(path, "rb") as f:
        data = f.read()
    return Response(data, mimetype="image/png",
                    headers={"Cache-Control": "no-cache",
                             "Content-Disposition": f"inline; filename=scan_{scan_id}.png"})

@app.route("/cancel/<int:scan_id>", methods=["POST"])
def cancel_scan(scan_id):
    with prog_lock:
        scan_cancels.add(scan_id)
    # Push ngay 1 event để UI thấy ngay
    send_prog(scan_id, {
        "phase": "cancelling",
        "phase_display": "🛑 Đang huỷ...",
        "message": "Đã nhận yêu cầu huỷ, sẽ dừng ở phase tiếp theo",
    })
    return jsonify({"ok": True, "scan_id": scan_id, "status": "cancelling"})

@app.route("/download_json", methods=["POST"])
def download_json():
    d = request.form.get("json_data")
    if not d: return "No data", 400
    try:
        data = json.loads(d)
    except Exception:
        return "Invalid JSON", 400
    data["scanner"] = "Web Leak Scanner Pro v8.0"
    data["exported_at"] = datetime.now(timezone.utc).isoformat()
    return Response(json.dumps(data, indent=2, ensure_ascii=False),
                    mimetype="application/json",
                    headers={"Content-Disposition": "attachment; filename=scan_result_v8.json"})

@app.route("/download_csv", methods=["POST"])
def download_csv():
    d = request.form.get("json_data")
    if not d: return "No data", 400
    try:
        data = json.loads(d)
    except Exception:
        return "Invalid JSON", 400
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["Section", "Field", "Value"])
    # Stats
    for k, v in (data.get("stats") or {}).items():
        w.writerow(["stats", k, v])
    # Main
    main = data.get("main") or {}
    w.writerow(["main", "code", main.get("code")])
    w.writerow(["main", "length", main.get("length")])
    w.writerow(["main", "response_time_ms", main.get("response_time_ms")])
    # Leak
    for item in data.get("leak", []):
        w.writerow(["leak", item.get("severity"), f"{item.get('code')} {item.get('path')} ({item.get('size')}b)"])
    # Secrets
    for s in data.get("secrets", []):
        w.writerow(["secret", s.get("severity"), f"{s.get('type')}: {s.get('match_masked')} @ {s.get('source')}"])
    # Ports
    w.writerow(["ports", "open", ", ".join(str(p) for p in data.get("ports", []))])
    # Tech
    w.writerow(["tech", "list", ", ".join(data.get("technologies", []))])
    # WAF
    w.writerow(["waf", "detected", ", ".join((data.get("waf") or {}).get("detected", []))])
    # CDN
    w.writerow(["cdn", "list", ", ".join(data.get("cdn", []))])
    # Security headers
    for h in data.get("security_headers", []):
        w.writerow(["sec_header", h.get("severity") if h.get("missing") else "ok",
                    f"{'MISSING' if h.get('missing') else 'OK'} {h.get('header')}"])
    # Cookies
    for c in data.get("cookies", []):
        w.writerow(["cookie", "issues" if c.get("issues") else "ok",
                    f"{c.get('name')} | issues: {'; '.join(c.get('issues', [])) or 'none'}"])
    # Forms
    for f in data.get("forms", []):
        w.writerow(["form", f.get("type"), f"{f.get('method')} {f.get('action')} (inputs: {f.get('input_count')})"])
    payload = out.getvalue().encode("utf-8")
    return Response(payload, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=scan_result_v8.csv"})

@app.route("/download_html", methods=["POST"])
def download_html():
    d = request.form.get("json_data")
    if not d: return "No data", 400
    try:
        data = json.loads(d)
    except Exception:
        return "Invalid JSON", 400
    html = render_template_string(RESULT_HTML, result=data)
    full = f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8">
<title>Scan Report - {data.get('target','')}</title>
<style>
body{{font-family:system-ui,sans-serif;background:#0f0f1a;color:#e0e0e0;padding:20px;margin:0}}
.card{{background:#16213e;border:1px solid #2d3561;border-radius:12px;padding:18px;margin-bottom:16px}}
h2{{background:linear-gradient(90deg,#00d4aa,#54a0affff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.badge{{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;margin:2px}}
.badge-time{{background:rgba(84,160,255,.12);color:#54a0ff}}
.badge-waf{{background:rgba(255,107,107,.12);color:#ff6b6b}}
code,pre{{font-family:monospace;background:#0a0a12;padding:8px;border-radius:6px;display:block;white-space:pre-wrap;word-break:break-all}}
</style>
</head><body>
<h1>🔒 Web Leak Scanner Pro v8.0 — Standalone Report</h1>
<p><strong>Target:</strong> {data.get('target','')}</p>
<p><strong>Scanned at:</strong> {data.get('timestamp','')}</p>
<p><strong>Duration:</strong> {data.get('duration_seconds',0)}s</p>
{html}
</body></html>"""
    return Response(full.encode("utf-8"), mimetype="text/html",
                    headers={"Content-Disposition": "attachment; filename=scan_report_v8.html"})

# ── Main ──
if __name__ == "__main__":
    print("=" * 60)
    print(f"🔒 Web Leak Scanner Pro v8.0 – Web Edition")
    print(f"   URL: http://{HOST}:{PORT}")
    print(f"   Mở trình duyệt vào địa chỉ trên (Ctrl+C để dừng)")
    print(f"   v5.0: Security Headers · Cookies · SSL · JS secrets")
    print(f"   v5.0: Forms · CDN · Severity scoring · Tabs UI · CSV/HTML export")
    print(f"   v6.0: Elapsed timer · ETA · Cancel · Soft-404 filter")
    print(f"   v6.0: Phase human-readable · Concurrency boost · Brute timeout")
    print(f"   v7.0: Deep crawl (spider depth=2) · Sitemap parse · API endpoint enum")
    print(f"   v7.0: HTML comments · JS URL extraction · Recursive dir probe · Query fuzz")
    print(f"   v8.0: Wayback Machine · DNS subdomain enum · DNS records")
    print(f"   v8.0: Playwright screenshot · CORS test · Subdomain takeover")
    print("=" * 60)
    app.run(host=HOST, port=PORT, debug=False, threaded=True)
