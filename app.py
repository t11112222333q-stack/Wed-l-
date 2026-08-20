#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Leak Scanner Pro v5.0 – Web Single-File Edition
Gộp Flask + Scanner + UI vào 1 file. Chỉ cần:
  pip install flask aiohttp
  python app.py
Rồi mở trình duyệt: http://localhost:5000

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
import os, sys, re, json, time, random, asyncio, threading, queue, csv, io, ssl, socket
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse, urljoin
from functools import wraps
from collections import OrderedDict

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
                    allow_redirects=False, progress_cb=None, scan_js=True):
    start = time.time()
    target = validate_target(target)
    result = {
        "target": target, "timestamp": datetime.now(timezone.utc).isoformat(),
        "scanner_version": "v5.0",
        "main": {}, "leak": [], "robots": [], "links": [], "js_links": [],
        "forms": [], "dirs": [], "brute": [], "ports": [], "technologies": [],
        "waf": {}, "cdn": [], "cookies": [], "security_headers": [],
        "secrets": [], "ssl": {}, "subdomain_hints": [], "page_summary": "",
        "errors": [], "duration_seconds": 0, "stats": {},
    }
    parsed = urlparse(target)
    host = parsed.hostname
    base = f"{parsed.scheme}://{parsed.netloc}"

    async def prog(phase, msg, current=0, total=0, found=0):
        if progress_cb:
            await progress_cb({"phase": phase, "message": msg, "current": current,
                                "total": total, "found": found})

    if HAS_AIOHTTP:
        conn = aiohttp.TCPConnector(limit=80, limit_per_host=30, ssl=False)
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

            limit = 5 if waf["should_slow_down"] else 15

            # SSL info nếu HTTPS
            if parsed.scheme == "https":
                await prog("ssl", "Đ kiểm tra SSL/TLS cert...")
                result["ssl"] = get_ssl_info(host, 443, 5)

            # 2. Ports
            if host:
                await prog("ports", "Đang quét cổng...")
                result["ports"] = await scan_ports(host)
                await prog("ports_done", f"Cổng mở: {result['ports'] or 'Không có'}")

            # 3. Leak paths
            await prog("leak_scan", f"Kiểm tra {len(LEAK_PATHS)} paths...", 0, len(LEAK_PATHS), 0)
            sem = asyncio.Semaphore(limit)
            found_count = 0
            async def check_path(path):
                nonlocal found_count
                async with sem:
                    url = urljoin(base, path)
                    text, code, h, rt = await fetch(session, url, custom_headers, proxy, timeout)
                    if code in (200, 401, 403):
                        if code == 200:
                            found_count += 1
                        sev = score_finding(path, code)
                        return {
                            "path": path, "url": url, "code": code,
                            "size": len(text) if text else 0,
                            "preview": (text[:500]+"..." if len(text) > 500 else text) if code == 200 else "",
                            "headers": dict(h) if code == 200 else {},
                            "severity": sev,
                            "response_time_ms": rt,
                        }
                    return None
            tasks = [check_path(p) for p in LEAK_PATHS]
            done = 0
            for coro in asyncio.as_completed(tasks):
                item = await coro
                done += 1
                if item:
                    result["leak"].append(item)
                if done % 10 == 0 or done == len(LEAK_PATHS):
                    await prog("leak_scan", f"{done}/{len(LEAK_PATHS)} – Found {found_count}", done, len(LEAK_PATHS), found_count)
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

            # 5. Links + JS + Forms
            if main_text:
                await prog("links", "Trích xuất links / JS / forms...")
                links = set()
                for m in re.finditer(r'(?:href|src|action)\s*=\s*["\']([^"\']+)["\']', main_text, re.I):
                    u = m.group(1)
                    if u.startswith(("http://", "https://")):
                        links.add(u)
                    elif u.startswith("/") and not u.startswith("//"):
                        links.add(urljoin(base, u))
                    elif not u.startswith(("#", "javascript:", "mailto:", "data:", "tel:")):
                        links.add(urljoin(base, u))
                result["links"] = sorted([l for l in links if urlparse(l).netloc == parsed.netloc])[:80]
                result["js_links"] = extract_js_links(main_text, base)
                result["forms"] = extract_forms(main_text, base)

                # 6. Secrets trong main HTML
                await prog("secrets", "Quét secret patterns trong HTML...")
                html_secrets = scan_secrets(main_text, "main page HTML")
                result["secrets"].extend(html_secrets)

                # 7. Fetch + scan JS files
                if scan_js and result["js_links"]:
                    await prog("secrets_js", f"Quét {len(result['js_links'])} JS files...", 0, len(result["js_links"]))
                    js_sem = asyncio.Semaphore(5)
                    async def scan_one_js(url):
                        async with js_sem:
                            t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                            if c == 200 and t:
                                return scan_secrets(t, f"JS: {url}")
                            return []
                    done = 0
                    for coro in asyncio.as_completed([scan_one_js(u) for u in result["js_links"]]):
                        ss = await coro
                        result["secrets"].extend(ss)
                        done += 1
                        if done % 5 == 0 or done == len(result["js_links"]):
                            await prog("secrets_js", f"JS {done}/{len(result['js_links'])} – Secrets: {len(result['secrets'])}", done, len(result["js_links"]), len(result['secrets']))
                # Dedup secrets + sort
                seen = set(); deduped = []
                for s in result["secrets"]:
                    k = (s["type"], s["match_masked"], s["source"])
                    if k not in seen:
                        seen.add(k); deduped.append(s)
                result["secrets"] = deduped
                result["secrets"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))

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

            # 9. Brute-force common names
            await prog("brute", "Brute-force common files...")
            exts = [".php", ".html", ".txt", ".json", ".xml", ".bak", ".old", ".save", ".orig"]
            names = ["index", "admin", "login", "config", "test", "api", "backup",
                     "db", "database", "secret", "private", "key", "token", "user",
                     "users", "account", "accounts", "config.bak", "panel"]
            bsem = asyncio.Semaphore(10)
            async def brute_one(n, e):
                path = f"/{n}{e}"
                url = urljoin(base, path)
                async with bsem:
                    _, c, _, rt = await fetch(session, url, custom_headers, proxy, timeout)
                    if c in (200, 403, 401):
                        return {"path": path, "code": c, "severity": score_finding(path, c), "response_time_ms": rt}
                    return None
            result["brute"] = [r for r in await asyncio.gather(*[brute_one(n, e) for n in names for e in exts]) if r]
            result["brute"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))

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
    }
    result["duration_seconds"] = round(time.time()-start, 2)
    await prog("completed", f"Hoàn thành – {result['stats']['leak_count']} leaks, {result['stats']['secret_count']} secrets, {result['stats']['ports_open']} ports")
    return result

# ── SSE ──
progress_queues = {}
prog_lock = threading.Lock()
scan_results = {}
scan_history = []  # list of {scan_id, target, started_at, status, leak_count}

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

def fmt_sse(data):
    return f"data: {data}\n\n"

# ── HTML Template (PAGE) ──
PAGE_HTML = r"""
<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Leak Scanner Pro v5.0</title>
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
  <div class="nav-brand"><span>🔒</span><span>Web Leak Scanner <span class="version">v5.0</span></span></div>
  <div class="nav-right">
    <button class="theme-toggle" id="themeToggle" title="Đổi theme">🌙</button>
  </div>
</nav>
<main class="container">

<!-- Form -->
<div class="card">
  <h1>🕵️ Quét lỗ hổng thông tin rò rỉ</h1>
  <p class="subtitle">Async scanner: leak paths · ports · tech fingerprint · WAF/CDN · security headers · cookies · JS secrets · forms · severity scoring</p>
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
    <div class="form-group" style="display:flex;align-items:center;gap:8px">
      <input type="checkbox" name="redirect" value="yes" id="rd" checked>
      <label for="rd" style="margin:0">Theo dõi redirect</label>
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
  <h3>📡 Tiến trình quét</h3>
  <div class="progress-info"><span id="progressPhase">Khởi tạo...</span><span id="progressCount"></span></div>
  <div class="progress-bar-bg"><div id="progressBar" class="progress-bar-fill"></div></div>
  <div id="progressMessage" class="progress-msg"></div>
  <div id="progressFound" class="progress-found hidden"></div>
</div>

<!-- Results -->
<div id="resultsArea"></div>

</main>
<footer class="footer">Web Leak Scanner Pro v5.0 – Async Security Scanner · 16+ feature improvements</footer>
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
  f.addEventListener('input', ()=>{
    const q = f.value.toLowerCase();
    const sev = $('#filterSev').value;
    $$('.leak-item[data-sev]').forEach(el=>{
      const path = el.dataset.path.toLowerCase();
      const s = el.dataset.sev;
      const matchQ = !q || path.includes(q);
      const matchS = sev === 'all' || s === sev;
      el.style.display = (matchQ && matchS) ? '' : 'none';
    });
  });
  $('#filterSev').addEventListener('change', ()=>{
    $('#filterInput').dispatchEvent(new Event('input'));
  });
}

// Submit scan
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

  btn.disabled = true;
  $('.btn-text').classList.add('hidden');
  $('.btn-loading').classList.remove('hidden');
  progressPanel.classList.remove('hidden');
  resultsArea.innerHTML = '';
  bar.style.width = '0%';
  phase.textContent = 'Đang khởi tạo...';

  const formData = new FormData(this);
  try{
    const resp = await fetch('/scan', {method:'POST', body:formData});
    const data = await resp.json();
    if(data.error){ toast('❌ ' + data.error); resetBtn(); return; }
    const scanId = data.scan_id;

    const evtSource = new EventSource('/progress/' + scanId);
    evtSource.onmessage = function(e){
      try{
        const d = JSON.parse(e.data);
        if(d.phase) phase.textContent = d.phase;
        if(d.total > 0){ bar.style.width = Math.round((d.current/d.total)*100)+'%'; count.textContent = d.current+'/'+d.total; }
        else { count.textContent = ''; }
        if(d.message) msg.textContent = d.message;
        if(d.found !== undefined && d.found > 0){
          found.classList.remove('hidden');
          found.textContent = '🔍 Tìm thấy: ' + d.found;
        }
        if(d.phase === 'completed' || d.phase === 'error'){
          evtSource.close();
          loadResult(scanId).then(loadHistory);
        }
      }catch(err){}
    };
    evtSource.onerror = function(){
      evtSource.close();
      loadResult(scanId).then(loadHistory);
    };
  }catch(err){
    toast('❌ Lỗi mạng: ' + err.message);
    resetBtn();
  }
});

function resetBtn(){
  $('#scanBtn').disabled = false;
  $('.btn-text').classList.remove('hidden');
  $('.btn-loading').classList.add('hidden');
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
    </select>
  </div>
  {% if result.leak %}
    {% for item in result.leak %}
    {% set sev_class = 'crit' if item.severity == 'critical' else ('high' if item.severity == 'high' else ('med' if item.severity == 'medium' else '')) %}
    <div class="leak-item {{ sev_class }}" data-path="{{ item.path }}" data-sev="{{ item.severity }}">
      <div class="leak-header">
        <span class="code-badge code-{{ item.code }}">{{ item.code }}</span>
        <span class="sev-badge sev-{{ item.severity }}">{{ item.severity }}</span>
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

    scan_id = int(time.time() * 1000)

    with prog_lock:
        progress_queues[scan_id] = queue.Queue(maxsize=500)

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
                allow_redirects, progress_cb, scan_js
            ))
            scan_results[scan_id] = result
            # update history
            with prog_lock:
                for h in scan_history:
                    if h["scan_id"] == scan_id:
                        h["status"] = "done"
                        h["leak_count"] = len(result.get("leak", []))
                        h["duration_seconds"] = result.get("duration_seconds", 0)
                        break
            send_prog(scan_id, {"phase": "completed",
                                "message": f"Done in {result['duration_seconds']}s · {len(result['leak'])} leaks"})
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

@app.route("/download_json", methods=["POST"])
def download_json():
    d = request.form.get("json_data")
    if not d: return "No data", 400
    try:
        data = json.loads(d)
    except Exception:
        return "Invalid JSON", 400
    data["scanner"] = "Web Leak Scanner Pro v5.0"
    data["exported_at"] = datetime.now(timezone.utc).isoformat()
    return Response(json.dumps(data, indent=2, ensure_ascii=False),
                    mimetype="application/json",
                    headers={"Content-Disposition": "attachment; filename=scan_result_v5.json"})

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
                    headers={"Content-Disposition": "attachment; filename=scan_result_v5.csv"})

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
<h1>🔒 Web Leak Scanner Pro v5.0 — Standalone Report</h1>
<p><strong>Target:</strong> {data.get('target','')}</p>
<p><strong>Scanned at:</strong> {data.get('timestamp','')}</p>
<p><strong>Duration:</strong> {data.get('duration_seconds',0)}s</p>
{html}
</body></html>"""
    return Response(full.encode("utf-8"), mimetype="text/html",
                    headers={"Content-Disposition": "attachment; filename=scan_report_v5.html"})

# ── Main ──
if __name__ == "__main__":
    print("=" * 60)
    print(f"🔒 Web Leak Scanner Pro v5.0 – Web Edition")
    print(f"   URL: http://{HOST}:{PORT}")
    print(f"   Mở trình duyệt vào địa chỉ trên (Ctrl+C để dừng)")
    print(f"   New: Security Headers · Cookies · SSL · JS secrets")
    print(f"   New: Forms · CDN · Severity scoring · Tabs UI · CSV/HTML export")
    print("=" * 60)
    app.run(host=HOST, port=PORT, debug=False, threaded=True)
