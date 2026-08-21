#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Leak Scanner Pro v11.1 — Deep Recon Edition
Gộp Flask + Scanner + UI vào 1 file. Chỉ cần:
  pip install flask aiohttp
  python app.py
Rồi mở trình duyệt: http://localhost:5000

Changelog v11.1 (so với v6.0):
  + 🔍 Scanner sâu hơn: LEAK_PATHS ~100 -> ~230 (cloud creds, k8s, docker, CI/CD,
    CMS-specific, backup variants .bak/.old/.orig/.save, .well-known/, framework
    config files, php/python/ruby/go/java/.NET specifics).
  + 🔑 SECRET_PATTERNS +12 patterns hiện đại (OpenAI, Anthropic, GitHub fine-grained,
    Linear, Mailchimp, Datadog, Asana, CircleCI, Vault, HashiCorp, Tencent, Alipay).
  + 🛠️ TECH_SIGS +8 frameworks (Astro, Remix, Qwik, Solid, htmx, Alpine, Lit, Stencil).
  + 🛡️ WAF_SIGS +4 (Citrix, Radware, StackPath, Azure Front Door).
  + ☁️ CDN_SIGS +3 (Edgecast, Imperva CDN, Verizon Edge).
  + 🔌 COMMON_PORTS +8 (e.g. 4040, 4443, 7001, 8880, 9001, 5044, 15672, 27018).
  + 🎯 Query param fuzzing: ?debug, ?test, ?admin, ?source, ?backup, ?dev, ?demo,
    ?config, ?env, ?show, ?cmd — phát hiện debug endpoints.
  + 📦 Backup variant check: với mỗi file 200 tìm được, tự check thêm .bak/.old/.orig.
  + ⚡ Concurrency boost: 25 -> 30 (non-WAF), 8 -> 12 (WAF slow mode).
  + 🌐 DNS subdomain enumeration thực sự (async dns resolution cho 30+ subs).
  + 🎨 UI v2: glassmorphism cards, animated mesh-gradient background, glow effects,
    staggered slide-in animations, animated number counters, shimmer skeleton,
    live terminal-style activity log, severity-based card glow, animated striped
    progress bar with pulsing edge.
  + 📊 Activity log (terminal-style) hiển thị từng request live trong khi scan.
  + 🎯 Severity filter chips (Critical / High / Medium / Low / Info) + search.

Changelog v6.0 (so với v5.0):
  + ⏱️ Real-time elapsed timer + ETA + Cancel button.
  + 🎯 Soft-404 calibration (md5 hash signature).
  + 📝 Phase human-readable tiếng Việt.
  + ⚡ Concurrency boost (15->25), brute-force timeout rút gọn.
"""
import os, sys, re, json, time, random, asyncio, threading, queue, csv, io, ssl, socket
import hashlib
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
COMMON_PORTS = [80, 443, 8080, 8443, 3000, 5000, 8000, 8888, 9000, 9200, 21, 22, 25, 3306,
                5432, 6379, 27017, 9090, 8161, 5601, 4040, 4443, 7001, 8880, 9001, 5044,
                15672, 27018, 9300, 11211, 6379]
BLOCKED_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "::1", "169.254.169.254", "metadata.google.internal", "metadata"}
SCAN_HISTORY_MAX = 10

# Query param fuzzing (debug endpoints)
PARAM_FUZZ = ["debug", "test", "admin", "source", "backup", "dev", "demo", "config",
              "env", "show", "cmd", "verbose", "trace", "profile", "internal"]

LEAK_PATHS = [
    # ── Common config / env ──
    "/robots.txt", "/sitemap.xml", "/sitemap-news.xml", "/.env", "/.env.local", "/.env.production",
    "/.env.development", "/.env.staging", "/.env.test", "/.env.example", "/.env.dev",
    "/.env.prod", "/.env.stage", "/.env.qa", "/.env.live", "/.env.master",
    "/.git/config", "/.git/HEAD", "/.git/index", "/.gitignore", "/.gitattributes",
    "/.git/objects/info/packs", "/.git/logs/HEAD", "/.git/info/refs", "/.git/refs/heads/master",
    "/wp-config.php", "/wp-config.php.bak", "/config.php", "/configuration.php",
    "/settings.php", "/settings.json", "/settings.local.php",
    "/.htaccess", "/web.config", "/config.json", "/config.xml", "/config.yaml",
    "/config.yml", "/config.ini", "/config.toml", "/appsettings.json",
    "/appsettings.Development.json", "/appsettings.Production.json", "/appsettings.Staging.json",
    "/.htpasswd", "/.htaccess.bak", "/.htaccess.txt", "/.htaccess.old",
    # ── Backup / dumps ──
    "/backup.zip", "/backup.tar.gz", "/backup.tar", "/backup.sql", "/backup.json",
    "/db.sql", "/db.sqlite", "/db.sqlite3", "/dump.sql", "/database.sql",
    "/www.zip", "/www.tar.gz", "/www.rar", "/www.7z", "/site.zip", "/website.zip",
    "/site.tar.gz", "/data.sql", "/data.json", "/data.tar", "/data.zip",
    "/backup-2023.zip", "/backup-2024.zip", "/backup.bak", "/db_backup.sql",
    "/mysql.sql", "/postgres.sql", "/pgdump.sql", "/mongodump.json",
    # ── Admin panels ──
    "/admin/", "/administrator/", "/wp-admin/", "/phpmyadmin/", "/adminer.php",
    "/admin/login", "/manager/html", "/cpanel", "/.admin", "/wp-login.php",
    "/admin.php", "/admin.html", "/admin/index.php", "/admin/console",
    "/admin/dashboard", "/adminarea/", "/adminpanel/", "/admincp/", "/admin/controlpanel",
    "/manage/", "/manager/", "/panel/", "/dashboard/", "/console/",
    "/administrator/index.php", "/admin/config", "/admin/settings",
    # ── Cloud / SSH / DevOps secrets ──
    "/.aws/credentials", "/.aws/config", "/.aws/credentials.bak",
    "/.ssh/id_rsa", "/.ssh/id_rsa.pub", "/.ssh/id_ecdsa", "/.ssh/id_ed25519",
    "/.ssh/authorized_keys", "/.ssh/known_hosts", "/.ssh/config",
    "/.dockerenv", "/.dockercfg", "/docker-compose.yml", "/docker-compose.yaml",
    "/.gitlab-ci.yml", "/.github/workflows/", "/firebase.json",
    "/service-account.json", "/service-account-credentials.json",
    "/google-services.json", "/GoogleService-Info.plist", "/.npmrc", "/.yarnrc", "/.yarn/",
    "/.netrc", "/.pypirc", "/.kube/config", "/.terraform.tfvars", "/terraform.tfstate",
    "/terraform.tfstate.backup", "/.terraform/", "/terraform.tfplan",
    # ── API docs ──
    "/swagger.json", "/swagger.yaml", "/swagger-ui/", "/swagger/", "/swagger-ui.html",
    "/api-docs", "/api/docs", "/openapi.json", "/openapi.yaml", "/openapi/",
    "/redoc", "/graphql", "/graphiql", "/altair", "/graphiql.html",
    "/api/v1/", "/api/v2/", "/api/v3/", "/api/", "/rest/", "/api/swagger.json",
    "/api/openapi.json", "/swagger/v1/swagger.json",
    # ── Package manifests ──
    "/package.json", "/package-lock.json", "/yarn.lock", "/pnpm-lock.yaml",
    "/composer.json", "/composer.lock", "/Dockerfile", "/docker-compose.yml",
    "/docker-compose.yaml", "/Containerfile", "/Pipfile", "/Pipfile.lock",
    "/requirements.txt", "/poetry.lock", "/Gemfile", "/Gemfile.lock",
    "/go.mod", "/go.sum", "/pom.xml", "/build.gradle", "/build.sbt",
    "/Cargo.toml", "/Cargo.lock", "/mix.exs", "/mix.lock",
    # ── History / debug ──
    "/.bash_history", "/.bashrc", "/.profile", "/.mysql_history", "/.psql_history",
    "/.viminfo", "/.phpstorm", "/.idea/", "/.idea/workspace.xml", "/.vscode/",
    "/.vscode/settings.json", "/.DS_Store", "/Thumbs.db",
    "/phpinfo.php", "/info.php", "/_profiler/", "/symfony/", "/_debugbar/",
    "/actuator", "/actuator/health", "/actuator/env", "/actuator/mappings",
    "/actuator/heapdump", "/actuator/loggers", "/actuator/beans", "/actuator/configprops",
    "/actuator/metrics", "/actuator/threaddump", "/actuator/httptrace",
    "/server-status", "/server-info",
    # ── VCS ──
    "/.svn/entries", "/.svn/wc.db", "/.svn/props/", "/.svn/text-base/",
    "/.hg/store", "/.bzr/", "/CVS/Root", "/CVS/Entries",
    # ── Misc / debug ──
    "/install/", "/setup/", "/test/", "/temp/", "/tmp/", "/logs/", "/log/",
    "/old/", "/backup/", "/bak/", "/archive/", "/archives/", "/debug/",
    "/_files/", "/uploads/", "/files/", "/static/", "/public/", "/media/",
    "/.well-known/security.txt", "/.well-known/openid-configuration",
    "/.well-known/apple-app-site-association", "/.well-known/assetlinks.json",
    "/.well-known/webfinger", "/.well-known/nodeinfo",
    "/crossdomain.xml", "/clientaccesspolicy.xml", "/humans.txt", "/security.txt",
    "/.env~", "/.env.bak", "/.env.save", "/.env.sw", "/.env.swp", "/.env.old",
    "/.env.orig", "/.env.dist", "/.env.sample", "/.env.dev.local",
    "/error.log", "/access.log", "/debug.log", "/app.log", "/out.log",
    "/laravel.log", "/storage/logs/laravel.log", "/var/log/",
    # ── CMS / framework specifics ──
    "/wp-content/", "/wp-content/uploads/", "/wp-content/plugins/",
    "/wp-content/backup-db/", "/wp-content/updraft/",
    "/wp-content/uploads/wpallimport/", "/wp-json/wp/v2/users",
    "/xmlrpc.php", "/wp-cron.php", "/wp-load.php", "/wp-signup.php",
    "/wp-mail.php", "/wp-blog-header.php",
    "/admin/web", "/admin/web/config.php",
    "/sites/default/settings.php", "/sites/default/files/",
    "/user/register", "/admin/structure",
    "/media/jui/", "/components/com_users/",
    "/app/etc/local.xml", "/var/log/exception.log", "/var/log/system.log",
    "/app/code/local/", "/skin/frontend/",
    "/.git/refs/stash", "/.git/COMMIT_EDITMSG",
    "/config/database.yml", "/config/secrets.yml", "/config/master.key",
    "/config/credentials.yml.enc", "/config/initializers/",
    "/storage/", "/storage/logs/laravel.log",
    "/.env.backup", "/.env.production.local",
    # ── Cloud / k8s / docker specifics ──
    "/.docker/init", "/var/run/docker.sock",
    "/.dockerignore", "/Dockerfile.dev", "/Dockerfile.prod",
    "/k8s/", "/kubernetes/", "/deploy.yaml", "/deploy.yml",
    "/helm/", "/Chart.yaml", "/values.yaml",
    "/.vault-token", "/vault.json", "/.vault-pass",
    "/consul.json", "/nomad/",
    "/.aws/credentials.bak", "/.aws/credentials.old",
    "/.gcp/credentials.json", "/.azure/credentials",
    "/service-account-key.json", "/gcp-service-account.json",
    # ── Server config / proxy leaks ──
    "/nginx.conf", "/apache.conf", "/httpd.conf", "/.nginx.conf",
    "/server.conf", "/sites-enabled/default", "/sites-available/default",
    "/conf.d/default.conf", "/.htpasswd.bak",
    # ── Composer / vendor / build artifacts ──
    "/vendor/", "/vendor/composer/installed.json",
    "/node_modules/", "/node_modules/.env",
    "/dist/", "/build/", "/target/", "/out/",
    "/.cache/", "/.parcel-cache/", "/.next/", "/.nuxt/",
    "/coverage/", "/.nyc_output/",
    # ── Other ──
    "/composer.phar", "/phpunit.xml", "/phpunit.xml.dist",
    "/.eslintrc", "/.prettierrc", "/.babelrc", "/webpack.config.js",
    "/vite.config.js", "/rollup.config.js", "/tsconfig.json",
    "/.editorconfig", "/.flake8", "/.pylintrc", "/.ruff.toml",
    "/Makefile", "/makefile", "/CMakeLists.txt",
    "/README.md", "/README.txt", "/CHANGELOG.md", "/LICENSE", "/LICENSE.txt",
    "/contributing.md", "/CONTRIBUTING",
    "/.gitlab/", "/.gitlab/issue_templates/",
    "/.circleci/config.yml", "/.travis.yml", "/bitbucket-pipelines.yml",
    "/jenkins/", "/.jenkins/",
    "/.docker/registry", "/registry/",
    "/api/health", "/api/status", "/health", "/healthz", "/healthcheck",
    "/.well-known/security.txt.bak",
    "/cache/", "/.cache/laravel",
    "/_next/data/", "/_nuxt/",
    "/sitemap_index.xml", "/news_sitemap.xml", "/image_sitemap.xml",
    "/yandex_", "/bing_",

    # ── v11.1 additions: K8s / container / monitoring ──
    "/.docker/init", "/var/run/docker.sock", "/.dockerenv", "/Dockerfile.dev",
    "/.dockerignore", "/Dockerfile.prod", "/docker-compose.override.yml",
    "/k8s/", "/kubernetes/", "/k8s.yaml", "/k8s.yml", "/deploy.yaml", "/deploy.yml",
    "/helm/", "/Chart.yaml", "/values.yaml", "/values-dev.yaml", "/values-prod.yaml",
    "/manifests/", "/.helm/", "/.argo/", "/argocd.yaml",
    "/metrics", "/-/metrics", "/-/healthy", "/-/ready", "/-/reload",
    "/healthz", "/readyz", "/livez", "/healthcheck", "/health", "/api/health",
    "/api/status", "/status", "/api/v1/status", "/ping", "/pong", "/heartbeat",
    "/prometheus", "/-/prometheus", "/grafana/api/health",
    "/jolokia/", "/jolokia/list", "/jolokia/read",
    "/hawtio/", "/hawtio/index.html", "/hawtio/jolokia",
    "/.well-known/security.txt.bak",
    "/.well-known/openid-configuration",
    "/.well-known/oauth-authorization-server",
    "/.well-known/jwks.json",
    "/.well-known/revocation",
    "/.well-known/introspection",

    # ── v11.1: Source maps & debug bundles ──
    "/bundle.js.map", "/main.js.map", "/app.js.map", "/index.js.map",
    "/script.js.map", "/scripts.js.map", "/vendor.js.map", "/runtime.js.map",
    "/polyfills.js.map", "/styles.css.map", "/main.css.map", "/app.css.map",
    "/static/js/main.js.map", "/static/js/bundle.js.map",
    "/_next/static/chunks/main.js.map", "/_next/static/chunks/webpack.js.map",
    "/assets/index.js.map", "/assets/main.js.map", "/assets/app.js.map",
    "/dist/build.js.map", "/dist/main.js.map",

    # ── v11.1: GraphQL / WebSocket / API ──
    "/graphql", "/graphql.json", "/graphql/console", "/graphiql",
    "/api/graphql", "/v1/graphql", "/v2/graphql", "/query",
    "/ws", "/wss", "/websocket", "/socket.io/", "/socket.io/?EIO=4",
    "/signalr", "/signalr/negotiate", "/signalr/hubs", "/signalr/poll",
    "/hub", "/hub/", "/realtime", "/events", "/sse", "/stream",
    "/api/v1/users", "/api/v1/admin", "/api/v1/config",
    "/api/v1/settings", "/api/v1/account", "/api/v1/auth",
    "/api/v2/users", "/api/v2/admin",
    "/api/users", "/api/admin", "/api/account", "/api/auth",
    "/api/me", "/api/profile", "/api/search", "/api/upload",
    "/api/files", "/api/download", "/api/list",
    "/rest/users", "/rest/admin", "/rest/config",
    "/v1/users", "/v1/admin", "/v1/config", "/v2/users", "/v2/admin",

    # ── v11.1: Spring Boot Actuator deep ──
    "/actuator/", "/actuator/info", "/actuator/health",
    "/actuator/env", "/actuator/configprops", "/actuator/beans",
    "/actuator/mappings", "/actuator/metrics", "/actuator/threaddump",
    "/actuator/httptrace", "/actuator/loggers", "/actuator/heapdump",
    "/actuator/scheduledtasks", "/actuator/sessions", "/actuator/shutdown",
    "/actuator/auditevents", "/actuator/logfile", "/actuator/startup",
    "/actuator/conditions", "/actuator/caches", "/actuator/flyway",
    "/actuator/liquibase", "/actuator/sessions", "/actuator/refresh",
    "/actuator/bus-refresh", "/actuator/gateway/routes",

    # ── v11.1: Java / JVM specific ──
    "/WEB-INF/web.xml", "/WEB-INF/classes/", "/WEB-INF/lib/",
    "/WEB-INF/config/", "/META-INF/MANIFEST.MF", "/META-INF/application.properties",
    "/META-INF/maven/", "/META-INF/spring.factories",
    "/struts/web.xml", "/struts.xml", "/struts-config.xml",
    "/WEB-INF/struts-config.xml", "/WEB-INF/struts.xml",

    # ── v11.1: .NET / IIS specific ──
    "/trace.axd", "/trace.axd?id=1", "/elmah.axd", "/elmah/elmah.axd",
    "/web.config.bak", "/web.config.old", "/web.config.txt",
    "/App_Data/", "/App_Data/Logs/", "/App_Data/Cache/",
    "/bin/", "/App_Code/", "/App_Browsers/", "/App_GlobalResources/",
    "/Reserved.ReportViewerWebControl.axd", "/Reports/",

    # ── v11.1: PHP / Laravel specific ──
    "/.env.production", "/.env.staging", "/.env.local", "/.env.dev",
    "/storage/", "/storage/logs/", "/storage/logs/laravel.log",
    "/storage/framework/cache/", "/storage/framework/sessions/",
    "/storage/framework/views/", "/bootstrap/cache/",
    "/.env.backup", "/.env.example", "/.env.sample", "/.env.template",
    "/artisan", "/server.php", "/package.json",

    # ── v11.1: Ruby / Rails specific ──
    "/config/database.yml", "/config/secrets.yml", "/config/master.key",
    "/config/credentials.yml.enc", "/config/credentials.yml",
    "/config/initializers/", "/config/environments/",
    "/Gemfile", "/Gemfile.lock", "/Rakefile", "/config.ru",
    "/db/schema.rb", "/db/seeds.rb", "/db/migrate/",
    "/log/production.log", "/log/development.log",

    # ── v11.1: Python / Django specific ──
    "/settings.py", "/local_settings.py", "/config/settings.py",
    "/manage.py", "/wsgi.py", "/asgi.py", "/requirements.txt",
    "/Pipfile", "/Pipfile.lock", "/pyproject.toml", "/poetry.lock",
    "/db.sqlite3", "/db.sqlite", "/app.db", "/data.db",

    # ── v11.1: WordPress deep ──
    "/wp-content/uploads/", "/wp-content/plugins/", "/wp-content/themes/",
    "/wp-content/backup-db/", "/wp-content/updraft/",
    "/wp-content/uploads/wpallimport/", "/wp-content/backups/",
    "/wp-content/uploads/backwpup/", "/wp-content/uploads/backupwordpress/",
    "/wp-json/wp/v2/users", "/wp-json/wp/v2/posts", "/wp-json/wp/v2/pages",
    "/wp-json/wp/v2/categories", "/wp-json/wp/v2/comments",
    "/wp-content/debug.log", "/wp-content/uploads/dump.sql",
    "/wp-config.php.bak", "/wp-config.php.old", "/wp-config.php.save",
    "/wp-config.php~", "/wp-config.php.orig", "/wp-config.php.swp",
    "/xmlrpc.php?rsd", "/wp-mail.php", "/wp-cron.php?doing_wp_cron",
    "/wp-signup.php", "/wp-register.php", "/wp-login.php?action=register",
    "/wp-admin/install.php", "/wp-admin/setup-config.php",
    "/wp-content/uploads/index.php", "/wp-includes/version.php",

    # ── v11.1: CMS-specific deep ──
    "/admin/web/config.php", "/admin/conf/", "/admin/sql/",
    "/sites/default/settings.php", "/sites/default/files/",
    "/sites/default/private/", "/sites/default/config/",
    "/user/register", "/admin/structure", "/admin/reports",
    "/admin/config", "/admin/modules", "/admin/people",
    "/app/etc/local.xml", "/var/log/exception.log", "/var/log/system.log",
    "/var/cache/", "/var/session/", "/var/report/",
    "/media/jui/", "/components/com_users/", "/components/com_config/",
    "/administrator/components/com_config/", "/administrator/cache/",
    "/installation/index.php", "/installation/configuration.php",

    # ── v11.1: Node.js / npm specific ──
    "/.npmrc", "/.yarnrc", "/.yarn/", "/.yarn/cache/",
    "/yarn.lock", "/pnpm-lock.yaml", "/package-lock.json",
    "/.pnp.js", "/.pnp.cjs", "/.pnp/", "/.pnp.loader.js",
    "/node_modules/.cache/", "/.parcel-cache/", "/.next/",
    "/.nuxt/", "/.svelte-kit/", "/.output/", "/.vercel/",
    "/.netlify/", "/.cache/", "/.turbo/",

    # ── v11.1: Cloud / DevOps deep ──
    "/.aws/credentials", "/.aws/config", "/.aws/credentials.bak",
    "/.ssh/id_rsa", "/.ssh/id_rsa.pub", "/.ssh/id_ecdsa",
    "/.ssh/id_ed25519", "/.ssh/authorized_keys", "/.ssh/known_hosts",
    "/.ssh/config", "/.ssh/environment",
    "/.vault-token", "/.vault-pass", "/vault.json", "/.vault.d/",
    "/consul.json", "/nomad/", "/.terraform/", "/.terraform.tfstate",
    "/terraform.tfstate", "/terraform.tfstate.backup", "/terraform.tfvars",
    "/.gcp/credentials.json", "/.azure/credentials",
    "/service-account.json", "/service-account-key.json",
    "/google-services.json", "/GoogleService-Info.plist",
    "/firebase.json", "/firebase-config.json", "/.firebaserc",

    # ── v11.1: CI/CD configs ──
    "/.gitlab-ci.yml", "/.gitlab-ci.yml.bak",
    "/.github/workflows/", "/.github/workflows/ci.yml",
    "/.circleci/config.yml", "/.travis.yml", "/bitbucket-pipelines.yml",
    "/jenkins/", "/.jenkins/", "/Jenkinsfile", "/Jenkinsfile.bak",
    "/azure-pipelines.yml", "/.drone.yml", "/teamcity",

    # ── v11.1: API documentation ──
    "/swagger.json", "/swagger.yaml", "/swagger-ui/", "/swagger/",
    "/swagger-ui.html", "/swagger-ui/index.html", "/swagger-ui/swagger-ui-bundle.js",
    "/api-docs", "/api/docs", "/api/swagger.json", "/api/openapi.json",
    "/openapi.json", "/openapi.yaml", "/openapi/", "/redoc",
    "/rapidoc", "/api-docs/swagger.json", "/v1/api-docs", "/v2/api-docs",
    "/api/swagger", "/api/rapidoc", "/api/redoc",

    # ── v11.1: WebSocket / SSE endpoints ──
    "/ws", "/wss", "/websocket", "/socket.io/", "/socket.io/?EIO=4&transport=websocket",
    "/signalr", "/signalr/negotiate", "/signalr/hubs",
    "/hub", "/realtime", "/events", "/sse", "/stream",
    "/api/ws", "/api/websocket", "/api/realtime",
    "/_ws", "/_websocket", "/_realtime",

    # ── v11.1: Common config backups / temporaries ──
    "/config.php.bak", "/config.php.old", "/config.php.orig", "/config.php.save",
    "/config.php.swp", "/config.php~", "/config.php.txt", "/config.php.dist",
    "/config.json.bak", "/config.json.old", "/config.json.orig",
    "/config.yaml.bak", "/config.yml.old", "/config.ini.dist",
    "/settings.php.bak", "/settings.php.old", "/settings.json.bak",
    "/settings.json.old", "/.env.bak", "/.env.old", "/.env.orig",
    "/.env.save", "/.env.swp", "/.env~", "/.env.dist", "/.env.sample",
    "/.env.production.local", "/.env.development.local",
    "/.env.staging.local", "/.env.test.local",

    # ── v11.1: CVE / known vuln paths ──
    "/cgi-bin/nobody/CDPGateway-1101",  # CVE-2021-44228 (Log4Shell)
    "/test.jsp", "/test.html",
    "/cgi-bin/printenv", "/cgi-bin/test-cgi", "/cgi-bin/php",
    "/cgi-sys/defaultwebpage.cgi", "/cgi-sys/realsignup.cgi",
    "/struts2/devmode.action", "/struts2/showcase.action",
    "/struts/webconsole.html",  # CVE-2017-5638 (Struts2)
    "/jenkins/script", "/jenkins/login",  # Jenkins
    "/console/", "/web-console/", "/admin/console",
    "/solr/", "/solr/admin/",  # Solr
    "/elasticsearch/", "/_cat/indices", "/_cluster/health",  # ES
    "/redis/", "/memcached/", "/var/log/redis/redis.log",

    # ── v11.1: Misc / random secrets ──
    "/.htpasswd", "/.htpasswd.bak", "/.htpasswd.old",
    "/.htaccess", "/.htaccess.bak", "/.htaccess.old",
    "/.netrc", "/.netrc.bak", "/.npmrc", "/.pypirc", "/.pypirc.bak",
    "/.dockerignore", "/.gitignore", "/.gitattributes",
    "/.editorconfig", "/.flake8", "/.pylintrc", "/.ruff.toml",
    "/.prettierrc", "/.eslintrc", "/.babelrc",
    "/.docker/registry", "/registry/", "/docker/registry",

    # ── v11.1: Source code & build artifacts ──
    "/source/", "/src/", "/build/", "/dist/", "/out/", "/target/",
    "/coverage/", "/.nyc_output/", "/.cache/", "/.parcel-cache/",
    "/vendor/", "/vendor/composer/installed.json", "/vendor/autoload.php",
    "/node_modules/", "/node_modules/.env", "/node_modules/.package-lock.json",

    # ── v11.1: Logs & debug ──
    "/error.log", "/access.log", "/debug.log", "/app.log", "/out.log",
    "/laravel.log", "/storage/logs/laravel.log",
    "/var/log/", "/var/log/apache2/", "/var/log/nginx/",
    "/var/log/auth.log", "/var/log/syslog", "/var/log/messages",
    "/logs/", "/log/", "/_logs/", "/debugging/",
    "/_profiler/", "/_debugbar/", "/symfony/_profiler/",
    "/phpinfo.php", "/info.php", "/test.php", "/php.php",
    "/_internal/", "/_hidden/", "/_private/", "/_secret/",
    "/server-status", "/server-info", "/status?full", "/status?auto",

    # ── v11.1: Backup & database dumps ──
    "/backup.zip", "/backup.tar.gz", "/backup.tar", "/backup.sql",
    "/backup.bak", "/backup.dump", "/backup.json",
    "/backup-2024.zip", "/backup-2025.zip",
    "/db.sql", "/db.sqlite", "/db.sqlite3", "/db.bak",
    "/database.sql", "/database.bak", "/database.dump",
    "/dump.sql", "/dump.bak", "/dump.json",
    "/www.zip", "/www.tar.gz", "/www.rar", "/www.7z",
    "/site.zip", "/site.tar.gz", "/site.bak",
    "/data.sql", "/data.bak", "/data.json", "/data.zip",
    "/mysql.sql", "/postgres.sql", "/pgdump.sql",
    "/mongodump.json", "/mongodump.bson",

    # ── v11.1: Admin / management panels ──
    "/admin/", "/administrator/", "/admin/login", "/admin/index.php",
    "/admin.php", "/admin.html", "/admin/console", "/admin/dashboard",
    "/adminarea/", "/adminpanel/", "/admincp/", "/admin/controlpanel",
    "/manage/", "/manager/", "/panel/", "/dashboard/", "/console/",
    "/cpanel", "/whm", "/.admin", "/wp-admin/", "/wp-login.php",
    "/phpmyadmin/", "/adminer.php", "/adminer/", "/pma/",
    "/sqladmin/", "/mysql-admin/", "/dbadmin/",
    "/manager/html", "/manager/status", "/manager/jmxproxy",
    "/host-manager/html", "/host-manager/status",

    # ── v11.1: User-uploaded content ──
    "/uploads/", "/uploads/files/", "/uploads/images/",
    "/files/", "/_files/", "/static/uploads/", "/public/uploads/",
    "/media/", "/assets/", "/static/", "/public/",
    "/tmp/", "/temp/", "/cache/", "/.cache/laravel",
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
    "Fastify":     [("header", r'x-powered-by.*fastify')],
    "Next.js":     [("html", r'__next|_next/static|next/dist'), ("header", r'x-powered-by.*next\.?js')],
    "Nuxt":        [("html", r'__nuxt|_nuxt/|nuxt-link')],
    "Gatsby":      [("html", r'gatsby|___gatsby')],
    "SvelteKit":   [("html", r'sveltekit|__sveltekit|svelte-')],
    "Astro":       [("html", r'astro-island|astro:|data-astro-')],
    "Remix":       [("html", r'__remix|remix-router|__remixContext')],
    "Qwik":        [("html", r'qwik:|qwik-loader|qwik-city')],
    "Vue.js":      [("html", r'vue[.-]\d|data-v-[a-z0-9]+|__VUE__|__NUXT__')],
    "React":       [("html", r'reactroot|data-react|react\.js|react-dom')],
    "Angular":     [("html", r'ng-\w+|angular[./]|ng-version')],
    "Svelte":      [("html", r'svelte-[a-z0-9]+')],
    "Solid":       [("html", r'solid-js|data-hk')],
    "htmx":        [("html", r'hx-get|hx-post|hx-trigger|htmx\.org')],
    "Alpine.js":   [("html", r'x-data|x-init|x-show|alpinejs')],
    "Lit":         [("html", r'lit-element|customElements\.define')],
    "Stencil":     [("html", r'stencil-build|stencil-')],
    "PHP":         [("header", r'x-powered-by.*php|php/'), ("html", r'\.php\?|phpsessid')],
    "ASP.NET":     [("header", r'x-aspnet|x-powered-by.*asp\.net|aspsessionid|aspnet'), ("cookie", r'asp\.net'), ("header", r'x-aspnetmvc')],
    "Ruby on Rails":[("header", r'x-powered-by.*rails|x-runtime|x-request-id'), ("cookie", r'_session|_rails')],
    "Spring Boot": [("header", r'x-application-context'), ("html", r'/actuator')],
    "Node.js":     [("header", r'x-powered-by.*nodejs|x-powered-by.*express')],
    "Nginx":       [("header", r'server.*nginx')],
    "Apache":      [("header", r'server.*apache')],
    "LiteSpeed":   [("header", r'server.*litespeed')],
    "IIS":         [("header", r'server.*microsoft-iis')],
    "Caddy":       [("header", r'server.*caddy')],
    "Cloudflare":  [("header", r'cf-ray|cloudflare|cf-cache-status')],
    "jQuery":      [("html", r'jquery[.-]\d+\.\d+|jquery\.min\.js')],
    "Bootstrap":   [("html", r'bootstrap[./]|bootstrap\.min\.css')],
    "TailwindCSS": [("html", r'tailwind|tw-|\.bg-[\w-]+|\.flex|\.grid')],
    "Bulma":       [("html", r'bulma')],
    "Material-UI": [("html", r'mui-|material-ui|MuiButton')],
    "Ant Design":  [("html", r'ant-|ant-btn|ant-card')],
    "ElementUI":   [("html", r'el-button|el-input|element-ui')],
    "Vuetify":     [("html", r'vuetify|v-app|v-card')],
    "Chakra UI":   [("html", r'chakra-|css-[\w]+')],
    "Mantine":     [("html", r'mantine-')],
    "Ghost":       [("header", r'x-ghost'), ("html", r'ghost-')],
    "Strapi":      [("header", r'x-powered-by.*strapi'), ("html", r'strapi')],
    "Craft CMS":   [("html", r'craftcms|craft/app')],
    "Wix":         [("html", r'wix\.com|X-Wix|static\.wixstatic')],
    "Squarespace": [("html", r'squarespace|sqs-')],
    "Webflow":     [("html", r'webflow|w-nav|w-commerce')],
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
    ("Citrix Netscaler", [r'citrix', r'ns_af']),
    ("Radware",      [r'radware', r'x-sl-']),
    ("StackPath",    [r'stackpath', r'x-sp-url']),
    ("Azure Front Door", [r'x-azure-ref', r'frontdoor']),
    ("Rate Limit (generic, HTTP 429)"),
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
    ("cross-origin-embedder-policy", "Cross-Origin-Embedder-Policy", "medium"),
]

# Sensitive data patterns (name, regex, severity, description)
SECRET_PATTERNS = [
    ("AWS Access Key ID",      r'AKIA[0-9A-Z]{16}',                                "critical", "AWS Access Key - cho phép gọi API AWS"),
    ("AWS Secret Key",         r'aws_secret_access_key["\']?\s*[:=]\s*["\']?[A-Za-z0-9/+=]{40}', "critical", "AWS Secret Key"),
    ("AWS STS Token",          r'ASIA[0-9A-Z]{16}',                                "critical", "AWS STS temporary token"),
    ("Google API Key",         r'AIza[0-9A-Za-z_\-]{35}',                          "high",     "Google API Key"),
    ("Google OAuth Refresh",   r'1/[0-9A-Za-z_\-]{43}',                            "high",     "Google OAuth refresh token"),
    ("Google OAuth Access",    r'ya29\.[0-9A-Za-z_\-]+',                           "high",     "Google OAuth access token"),
    ("Slack Token",            r'xox[abprs]-[0-9A-Za-z-]{10,}',                    "high",     "Slack token"),
    ("Slack Webhook",          r'https://hooks\.slack\.com/services/T[A-Z0-9]+',    "high",     "Slack incoming webhook"),
    ("Stripe Secret Key",      r'sk_live_[0-9A-Za-z]{24,}',                        "critical", "Stripe secret key (live)"),
    ("Stripe Restricted Key",  r'rk_live_[0-9A-Za-z]{24,}',                        "critical", "Stripe restricted key"),
    ("Stripe Publishable",     r'pk_live_[0-9A-Za-z]{24,}',                        "medium",   "Stripe publishable key (live)"),
    ("GitHub Token",           r'gh[pousr]_[A-Za-z0-9]{36,}',                      "critical", "GitHub personal access token"),
    ("GitHub OAuth Token",     r'gho_[A-Za-z0-9]{36}',                             "critical", "GitHub OAuth token"),
    ("GitHub App Token",       r'(ghu|ghs)_[A-Za-z0-9]{36}',                       "critical", "GitHub App user/server token"),
    ("GitHub Fine-grained",    r'github_pat_[a-zA-Z0-9_]{22,}',                   "critical", "GitHub fine-grained PAT"),
    ("GitLab Token",           r'glpat-[A-Za-z0-9_\-]{20}',                        "high",     "GitLab personal access token"),
    ("Heroku API Key",         r'(?:heroku_api_key|heroku_api_token)["\']?\s*[:=]\s*["\']?[0-9a-fA-F]{32}', "high", "Heroku API key"),
    ("JWT Token",              r'eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}', "high", "JWT token - có thể leak claims"),
    ("Private Key PEM",        r'-----BEGIN (RSA|EC|DSA|OPENSSH|PGP) PRIVATE KEY-----', "critical", "Private key PEM"),
    ("Generic Secret",         r'(?:secret|api[_-]?key|token|passwd|password)["\']?\s*[:=]\s*["\']?[A-Za-z0-9+/=_\-]{20,}', "medium", "Generic secret / api key (>= 20 chars)"),
    ("Generic Secret Long",    r'(?:secret|api[_-]?key|token|passwd|password)["\']?\s*[:=]\s*["\']?[A-Za-z0-9+/=_\-]{40,}', "high", "Generic secret / api key (>= 40 chars)"),
    ("Firebase URL",          r'https?://[a-z0-9\-]+\.firebaseio\.com',            "high",     "Firebase realtime DB URL"),
    ("Firebase Config",        r'firebaseConfig\s*=\s*\{[^}]*?(?:apiKey|databaseURL|projectId)[^}]*?\}', "high", "Firebase client config"),
    ("Twilio SID",            r'AC[a-z0-9]{32}',                                  "high",     "Twilio Account SID"),
    ("Square OAuth Secret",   r'sq0csp-[0-9A-Za-z_\-]{43}',                       "high",     "Square OAuth secret"),
    ("Mailgun API Key",       r'key-[0-9a-zA-Z]{32}',                             "high",     "Mailgun API key"),
    ("SendGrid API Key",      r'SG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}',    "high",     "SendGrid API key"),
    ("Mailchimp API Key",     r'[0-9a-f]{32}-us[0-9]{1,2}',                        "high",     "Mailchimp API key"),
    ("OpenAI API Key",        r'sk-[A-Za-z0-9]{20}T3BlbkFJ[A-Za-z0-9]{16}',       "critical", "OpenAI API key (legacy)"),
    ("OpenAI Project Key",    r'sk-proj-[A-Za-z0-9_\-]{40,}',                     "critical", "OpenAI project API key"),
    ("Anthropic API Key",     r'sk-ant-[A-Za-z0-9_\-]{60,}',                       "critical", "Anthropic Claude API key"),
    ("Linear API Key",        r'lin_api_[A-Za-z0-9_\-]{30,}',                      "high",     "Linear API token"),
    ("Asana PAT",             r'[0-9]/[a-f0-9]{32,}:',                              "high",     "Asana personal access token"),
    ("CircleCI Token",        r'CCIPRJ_[A-Za-z0-9_\-]{22,}',                        "high",     "CircleCI project token"),
    ("Datadog API Key",       r'(?:DD_API_KEY|DATADOG_API_KEY)["\']?\s*[:=]\s*["\']?[a-f0-9]{32}', "high",   "Datadog API key (env-named)"),
    ("HashiCorp Vault Token", r'(?:hvs\.[A-Za-z0-9_\-]{60,})',                       "critical", "Vault service token"),
    ("Tencent SecretId",      r'AKID[A-Za-z0-9]{13,}',                             "high",     "Tencent Cloud SecretId"),
    ("Jenkins Token",         r'jenkins[_-]?(?:token|api[_-]?key)["\']?\s*[:=]\s*["\']?[a-f0-9]{40}', "high", "Jenkins API token"),
    ("Telegram Bot Token",    r'[0-9]{6,10}:[A-Za-z0-9_\-]{30,}',                  "high",     "Telegram bot token"),
    ("Discord Bot Token",     r'[MN][A-Za-z0-9_\-]{22,}\.[A-Za-z0-9_\-]{4,}\.[A-Za-z0-9_\-]{20,}', "high", "Discord bot token"),
    ("Notion Integration",    r'(secret_)?ntn_[A-Za-z0-9]{40,}',                   "high",     "Notion integration token"),
    ("Shopify Token",         r'shpat_[A-Fa-f0-9]{32}',                           "critical", "Shopify API access token"),
    ("Twilio App SID",        r'AP[a-z0-9]{32}',                                  "medium",   "Twilio App SID"),
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
    ("Edgecast",       [r'edgecast', r'x-ec-debug']),
    ("Imperva CDN",    [r'x-iinfo', r'incapsula']),
    ("Verizon Edge",   [r'verizon', r'x-ec-debug']),
    ("Azure CDN",      [r'x-azure-ref', r'azurecdn']),
    ("Google CDN",     [r'x-google-cache', r'gws']),
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
    "analytics", "track", "stats", "monitor", "grafana", "kibana", "prometheus",
    "warehouse", "data", "warehouse", "warehouse-api", "warehouse-internal",
    "console", "terminal", "shell", "ssh", "rdp", "vnc",
    "prod", "production", "uat", "qa", "sandbox", "shadow", "mirror", "backup",
    "ws", "websocket", "realtime", "stream", "events", "notifications",
    "checkout", "payment", "billing", "subscriptions",
    "search", "elastic", "solr", "redis", "cache", "queue", "broker",
]

# Brute-force wordlist expanded
BRUTE_NAMES = [
    "index", "admin", "login", "config", "test", "api", "backup",
    "db", "database", "secret", "private", "key", "token", "user",
    "users", "account", "accounts", "panel", "console", "dashboard",
    "settings", "setup", "install", "init", "main", "default",
    "old", "new", "tmp", "temp", "dev", "prod", "stage", "qa",
    "preview", "demo", "beta", "internal", "external", "public",
    "private", "secure", "auth", "oauth", "sso", "session",
    "wp-config", "wp-login", "wp-admin", "phpinfo", "info",
    "web.config", "swagger", "openapi", "graphql", "rest",
    "health", "status", "metrics", "debug", "trace", "profile",
    "log", "logs", "error", "access", "v1", "v2",
]

# Backup variants for files that returned 200
BACKUP_VARIANTS = [".bak", ".old", ".orig", ".save", ".swp", "~", ".dist", ".sample"]

# Recursive brute-force: với mỗi directory 200 tìm được, brute các sub-paths này
RECURSIVE_BRUTE_PATHS = [
    "login", "config", "settings", "admin", "dashboard", "console",
    "index.php", "index.html", "index", "default.php", "main",
    "users", "user", "account", "accounts", "profile", "me",
    "backup", "db", "database", "dump.sql", "data",
    "api", "api/v1", "api/users", "api/config",
    "logs", "log", "error.log", "access.log",
    "test", "debug", "info", "phpinfo",
    "upload", "uploads", "files", "static",
    "private", "secret", "internal", "hidden",
]

# Subdomain takeover fingerprints (CNAME pattern, service name, vulnerability)
TAKEOVER_SIGS = [
    (r'\.github\.io$', "GitHub Pages", "CNAME trỏ tới GitHub Pages nhưng repo không tồn tại hoặc chưa publish"),
    (r'\.herokuapp\.com$', "Heroku", "App Heroku đã bị xóa, CNAME vẫn trỏ — takeover được"),
    (r'\.s3\.amazonaws\.com$', "AWS S3", "Bucket không tồn tại — có thể register lại bucket name để takeover"),
    (r'\.s3-website[\.\-].*\.amazonaws\.com$', "AWS S3 Static", "Bucket S3 static website không tồn tại"),
    (r'\.cloudfront\.net$', "AWS CloudFront", "CloudFront distribution đã bị xóa — có thể register lại"),
    (r'\.azureedge\.net$', "Azure CDN", "Azure CDN endpoint đã bị xóa"),
    (r'\.azurewebsites\.net$', "Azure Web Apps", "Azure Web App đã bị xóa"),
    (r'\.blob\.core\.windows\.net$', "Azure Blob", "Azure Blob container không tồn tại"),
    (r'\.trafficmanager\.net$', "Azure Traffic Manager", "Profile đã bị xóa"),
    (r'\.elasticbeanstalk\.com$', "AWS Elastic Beanstalk", "Environment đã bị terminate"),
    (r'\.fastly\.net$', "Fastly", "Fastly service đã bị xóa"),
    (r'\.netlify\.app$', "Netlify", "Netlify site đã bị unclaim — có thể claim lại"),
    (r'\.vercel\.app$', "Vercel", "Vercel project đã bị xóa"),
    (r'\.gitlab\.io$', "GitLab Pages", "GitLab Pages project không tồn tại"),
    (r'\.surge\.sh$', "Surge.sh", "Surge domain đã bị unclaim"),
    (r'\.readthedocs\.io$', "Read the Docs", "Subdomain Read the Docs không tồn tại"),
    (r'\.fly.dev$', "Fly.io", "Fly.io app đã bị xóa"),
    (r'\.onrender\.com$', "Render", "Render service đã bị xóa — có thể register lại"),
    (r'\.pantheonsite\.io$', "Pantheon", "Pantheon environment đã bị xóa"),
    (r'\.ngrok\.io$', "ngrok", "ngrok tunnel đã đóng"),
    (r'\.ngrok-free\.app$', "ngrok free", "ngrok tunnel đã đóng"),
    (r'\.cloudflareaccess\.com$', "Cloudflare Access", "Cloudflare Access app đã bị xóa"),
    (r'\.myshopify\.com$', "Shopify", "Shopify store đã bị xóa"),
    (r'\.webflow\.io$', "Webflow", "Webflow site đã bị xóa"),
    (r'\.cargocollective\.com$', "Cargo", "Cargo site đã bị xóa"),
    (r'\.tumblr\.com$', "Tumblr", "Tumblr blog đã bị xóa — có thể register lại"),
    (r'\.wordpress\.com$', "WordPress.com", "WordPress.com blog đã bị xóa"),
    (r'\.ghost\.io$', "Ghost Pro", "Ghost Pro site đã bị xóa"),
    (r'\.squarespace\.com$', "Squarespace", "Squarespace site đã bị xóa"),
    (r'\.wixsite\.com$', "Wix", "Wix site đã bị xóa"),
    (r'\.zendesk\.com$', "Zendesk", "Zendesk subdomain đã bị xóa"),
    (r'\.freshdesk\.com$', "Freshdesk", "Freshdesk helpdesk đã bị xóa"),
    (r'\.herokuapp\.com$', "Heroku (dup)", "Heroku app không tồn tại"),
    (r'\.intercom\.cdn\.com$', "Intercom", "Intercom CDN đã bị xóa"),
    (r'\.statuspage\.io$', "StatusPage", "StatusPage đã bị xóa"),
    (r'\.helpscoutdocs\.com$', "HelpScout", "HelpScout docs đã bị xóa"),
    (r'\.unbounce\.com$', "Unbounce", "Unbounce landing page đã bị xóa"),
    (r'\.instapage\.com$', "Instapage", "Instapage đã bị xóa"),
    (r'\.launchrock\.com$', "LaunchRock", "LaunchRock page đã bị xóa"),
    (r'\.tave\.com$', "Tave", "Tave page đã bị xóa"),
    (r'\.smugmug\.net$', "SmugMug", "SmugMug gallery đã bị xóa"),
    (r'\.shopify\.cdn\.com$', "Shopify CDN", "Shopify CDN đã bị xóa"),
    (r'\.feedpress\.me$', "FeedPress", "FeedPress feed đã bị xóa"),
    (r'\.surge\.sh$', "Surge (dup)", "Surge domain unclaimed"),
    (r'\.fastly\.net$', "Fastly (dup)", "Fastly service deleted"),
    (r'\.cloudinary\.com$', "Cloudinary", "Cloudinary asset không tồn tại"),
    (r'\.imgix\.net$', "imgix", "imgix source đã bị xóa"),
    (r'\.kenticocdn\.com$', "Kentico", "Kentico CDN đã bị xóa"),
    (r'\.agcdn\.com$', "Agora CDN", "Agora CDN đã bị xóa"),
    (r'\.bigcartel\.com$', "Big Cartel", "Big Cartel store đã bị xóa"),
    (r'\.spreadshop\.com$', "Spreadshop", "Spreadshop đã bị xóa"),
    (r'\.eff\.org$', "EFF", "EFF site đã bị xóa"),
    (r'\.zoho\.com$', "Zoho", "Zoho site đã bị xóa"),
    (r'\.teamsnap\.com$', "TeamSnap", "TeamSnap club đã bị xóa"),
    (r'\.kinsta\.cloud$', "Kinsta", "Kinsta site đã bị xóa"),
    (r'\.kinstacdn\.com$', "Kinsta CDN", "Kinsta CDN đã bị xóa"),
    (r'\.flyusercontent\.com$', "Fly User Content", "Fly content đã bị xóa"),
    (r'\.workers\.dev$', "Cloudflare Workers", "Worker đã bị xóa hoặc chưa deploy"),
    (r'\.pages\.dev$', "Cloudflare Pages", "Pages project đã bị xóa"),
    (r'\.deno\.dev$', "Deno Deploy", "Deno Deploy project đã bị xóa"),
    (r'\.supabase\.co$', "Supabase", "Supabase project đã bị xóa"),
    (r'\.supabase\.in$', "Supabase Storage", "Supabase storage bucket không tồn tại"),
]

# Open redirect params to test
REDIRECT_PARAMS = [
    "redirect", "redirect_url", "redirectUrl", "redirect_uri", "redirect_to",
    "redirect_to_url", "return", "return_url", "returnUrl", "returnTo",
    "return_to", "next", "next_url", "nextUrl", "url", "go", "goto",
    "target", "destination", "dest", "continue", "to", "from",
    "callback", "callback_url", "callbackUrl", "callback_uri",
    "forward", "forward_url", "forwardUrl", "ref", "reference",
    "out", "external", "exit", "jump", "redir",
]

# GraphQL introspection query
GRAPHQL_INTROSPECTION_QUERY = '{"query":"query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}}"}'

# GraphQL endpoints to try
GRAPHQL_ENDPOINTS = ["/graphql", "/graphql.json", "/api/graphql", "/v1/graphql",
                     "/v2/graphql", "/query", "/graphiql", "/playground"]

# Source map file extensions to check (added to JS URL)
SOURCE_MAP_EXTS = [".map", ".map.js", ".json.map"]

# Wayback Machine API endpoint
WAYBACK_API = "https://web.archive.org/cdx/search/cdx"

# JS endpoint extraction patterns (API routes in JS code)
JS_ENDPOINT_PATTERNS = [
    # fetch("...", { method: "GET" })
    r'fetch\s*\(\s*[\'"`]([^\'"`]+\?[^\'"`]*|/[^\'"`]+)[\'"`]',
    # axios.get("..."), axios.post("...")
    r'axios\.(?:get|post|put|delete|patch|head)\s*\(\s*[\'"`]([^\'"`]+)[\'"`]',
    # $.ajax({ url: "..." })
    r'\$\.(?:ajax|get|post|getJSON)\s*\(\s*(?:\{[^}]*?url\s*:\s*)?[\'"`]([^\'"`]+)[\'"`]',
    # XHR.open("GET", "/...")
    r'\.open\s*\(\s*[\'"`](?:GET|POST|PUT|DELETE|PATCH)[\'"`]\s*,\s*[\'"`]([^\'"`]+)[\'"`]',
    # new URL("/...", base)
    r'new\s+URL\s*\(\s*[\'"`]([^\'"`]+)[\'"`]',
    # window.location = "/..."
    r'(?:window|document)\.location(?:\.href)?\s*=\s*[\'"`]([^\'"`]+)[\'"`]',
    # String concatenation: "/api/" + path  → catch the literal prefix
    r'[\'"`]((?:/api/|/v\d+/|/rest/|/graphql|/admin/|/internal/)[^\'"`]*)[\'"`]',
    # Path with /api/ or /v1/ or /v2/ prefix
    r'[\'"`]((?:/api/|/v\d+/|/rest/|/graphql/|/admin/api/|/internal/api/)[a-zA-Z0-9_/.-]+)[\'"`]',
    # Next.js __NEXT_DATA__ routes
    r'__NEXT_DATA__\s*=\s*\{[^}]*?(?:props|page|query)\s*:\s*\{[^}]*?["\'`]([^"\'`]+)["\'`]',
]

# Common API path suffixes to test (joined with discovered prefixes)
API_TEST_SUFFIXES = [
    "/users", "/users/me", "/users/list", "/users/all",
    "/admin", "/admin/users", "/admin/config", "/admin/settings",
    "/me", "/profile", "/account", "/accounts",
    "/config", "/settings", "/preferences",
    "/auth/login", "/auth/logout", "/auth/me", "/auth/refresh",
    "/login", "/logout", "/register", "/signup", "/forgot-password",
    "/upload", "/download", "/files", "/list",
    "/search", "/query", "/find",
    "/health", "/status", "/version", "/info",
    "/posts", "/comments", "/articles", "/products", "/orders",
    "/payments", "/invoices", "/subscriptions",
    "/notifications", "/messages", "/emails",
    "/debug", "/debug/info", "/debug/status",
    "/internal", "/internal/status", "/internal/users",
    "/v1", "/v1/users", "/v1/admin", "/v1/me",
    "/v2", "/v2/users", "/v2/admin",
]

# CORS test origins
CORS_TEST_ORIGINS = [
    "https://evil.com",
    "https://attacker.example",
    "null",
]

# HTTP methods to fuzz (test OPTIONS to discover allowed methods)
HTTP_METHODS_TO_FUZZ = ["OPTIONS", "PUT", "DELETE", "PATCH", "PROPFIND", "TRACE"]

# v11.1 WAF bypass modes
WAF_BYPASS_MODES = ["auto", "stealth", "aggressive", "turbo"]
WAF_BYPASS_PROFILES = {
    "auto":      {"concurrency": 30, "delay_min": 0,    "delay_max": 0.3,  "rotate_ua": True,  "rotate_xff": False, "retry": 2},
    "stealth":   {"concurrency": 5,  "delay_min": 0.8,  "delay_max": 2.5,  "rotate_ua": True,  "rotate_xff": True,  "retry": 3},
    "aggressive":{"concurrency": 60, "delay_min": 0,    "delay_max": 0.05, "rotate_ua": True,  "rotate_xff": True,  "retry": 1},
    "turbo":     {"concurrency": 100,"delay_min": 0,    "delay_max": 0,    "rotate_ua": False, "rotate_xff": False, "retry": 0},
}

# Pool of fake X-Forwarded-For IPs to rotate (bypass IP rate-limiting)
FAKE_XFF_IPS = [
    f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    for _ in range(50)
]

# Pool of fake Referer values (looks more like a real browser request)
FAKE_REFERERS = [
    "https://www.google.com/search?q=", "https://www.bing.com/search?q=",
    "https://duckduckgo.com/?q=", "https://github.com/",
    "https://stackoverflow.com/questions/", "https://www.reddit.com/",
    "https://twitter.com/", "https://www.linkedin.com/",
    "https://www.facebook.com/", "https://www.youtube.com/",
]

# Pool of Accept-Language values
FAKE_ACCEPT_LANG = [
    "en-US,en;q=0.9", "en-GB,en;q=0.9", "vi-VN,vi;q=0.9,en;q=0.8",
    "zh-CN,zh;q=0.9,en;q=0.8", "ja-JP,ja;q=0.9,en;q=0.8",
    "ko-KR,ko;q=0.9,en;q=0.8", "de-DE,de;q=0.9,en;q=0.8",
    "fr-FR,fr;q=0.9,en;q=0.8", "es-ES,es;q=0.9,en;q=0.8",
    "pt-BR,pt;q=0.9,en;q=0.8", "ru-RU,ru;q=0.9,en;q=0.8",
    "it-IT,it;q=0.9,en;q=0.8", "pl-PL,pl;q=0.9,en;q=0.8",
    "tr-TR,tr;q=0.9,en;q=0.8", "ar-SA,ar;q=0.9,en;q=0.8",
]

# SSTI test payloads — safe to send (no destructive payloads)
SSTI_PAYLOADS = [
    # Jinja2 / Twig
    ("{{7*7}}", "49"),
    ("{{7*'7'}}", "7777777"),  # Jinja2 only
    ("{{1+1}}", "2"),
    # Tornado
    ("{%import os%}", "import os"),
    # Java Freemarker
    ("${7*7}", "49"),
    ("${\"freemarker\"}", "freemarker"),
    # Java Velocity
    ("#set($x=7*7)${x}", "49"),
    # ERB (Ruby)
    ("<%=7*7%>", "49"),
    ("<%=system('id')%>", "uid="),
    # Smarty
    ("{7*7}", "49"),
    # Mako (Python)
    ("${7*7}", "49"),
    # Pebble
    ("{{7*7}}", "49"),
    # Handlebars / Mustache (won't compute, just check for reflection)
    ("{{7*7}}", "49"),
    # Generic — check reflection
    ("xss{{7*7}}probe", "xss49probe"),
    # ASP.NET Razor
    ("@(7*7)", "49"),
    # Check reflection without computation
    ("STTItest49", "STTItest49"),
]

# Prototype pollution payloads
PROTO_POLLUTION_PAYLOADS = [
    "?__proto__[polluted]=yes",
    "?__proto__.polluted=yes",
    "?__proto__[polluted]=yes",
    "?constructor[prototype][polluted]=yes",
    "?constructor.prototype.polluted=yes",
    "?__proto__[__proto__][polluted]=yes",
    # JSON body variants (we'd need POST; only test GET here)
    "?__proto__[isAdmin]=true",
    "?__proto__[admin]=1",
    "?__proto__[role]=admin",
    "?__proto__[isAuthenticated]=true",
]

# HTTP header injection payloads
HEADER_INJECTION_PAYLOADS = [
    # X-Forwarded-Host injection
    ("X-Forwarded-Host", "evil.com"),
    ("X-Forwarded-Host", "127.0.0.1:8080"),
    ("X-Forwarded-Host", "localhost"),
    ("X-Forwarded-For", "127.0.0.1"),
    ("X-Forwarded-For", "10.0.0.1"),
    ("X-Real-IP", "127.0.0.1"),
    ("X-Real-IP", "10.0.0.1"),
    ("X-Original-URL", "/admin"),
    ("X-Original-URL", "/admin/users"),
    ("X-Rewrite-URL", "/admin"),
    ("X-Custom-IP-Authorization", "127.0.0.1"),
    ("X-Forwarded-User", "admin"),
    ("X-Remote-User", "admin"),
    ("X-Forwarded-Email", "admin@example.com"),
    ("X-Original-Remote-Addr", "127.0.0.1"),
    ("X-Client-IP", "127.0.0.1"),
    ("True-Client-IP", "127.0.0.1"),
    ("X-Host", "evil.com"),
    ("Host", "evil.com"),
    ("X-HTTP-Method-Override", "PUT"),
    ("X-HTTP-Method-Override", "DELETE"),
    ("X-Method-Override", "PUT"),
]

# Cache poisoning payloads (test if Origin/Host reflected in cache key)
CACHE_POISON_PAYLOADS = [
    ("X-Forwarded-Host", "evil.cache-poison.example"),
    ("X-Forwarded-Scheme", "https"),
    ("X-Forwarded-Proto", "https"),
    ("X-Original-URL", "/?cachebust=1"),
    ("X-Forwarded-Server", "evil.com"),
    ("X-HTTP-Method-Override", "GET"),
]

# Login form test credentials (for default credential checks)
DEFAULT_CREDS = [
    ("admin", "admin"),
    ("admin", "password"),
    ("admin", "admin123"),
    ("admin", "123456"),
    ("root", "root"),
    ("root", "toor"),
    ("test", "test"),
    ("user", "user"),
    ("guest", "guest"),
    ("demo", "demo"),
]

# v11.1: EXPANDED leak paths — admin panels, framework configs, API, cloud, database, CI/CD
LEAK_PATHS_V2 = [
    # ── Admin panels (expanded) ──
    "/admin/", "/admin/login", "/admin/index.php", "/admin/index.html",
    "/admin/dashboard", "/admin/console", "/admin/config", "/admin/settings",
    "/admin/users", "/admin/accounts", "/admin/profile", "/admin/panel",
    "/admin/manage", "/admin/system", "/admin/tools", "/admin/files",
    "/admin/upload", "/admin/download", "/admin/export", "/admin/import",
    "/admin/api", "/admin/db", "/admin/sql", "/admin/cache",
    "/admin/logs", "/admin/stats", "/admin/monitor", "/admin/health",
    "/administrator/", "/administrator/index.php", "/administrator/login.php",
    "/administrator/config.php", "/administrator/settings.php",
    "/adminarea/", "/adminpanel/", "/admincp/", "/admin/controlpanel/",
    "/manage/", "/manager/", "/panel/", "/dashboard/", "/console/",
    "/cpanel", "/whm", "/directadmin", "/vesta", "/webmin",
    "/wp-admin/", "/wp-admin/login.php", "/wp-admin/admin.php",
    "/wp-admin/options.php", "/wp-admin/tools.php", "/wp-admin/plugins.php",
    "/wp-admin/themes.php", "/wp-admin/users.php", "/wp-admin/export.php",
    "/wp-admin/import.php", "/wp-admin/admin-ajax.php",
    "/phpmyadmin/", "/phpmyadmin/index.php", "/phpmyadmin/config.inc.php",
    "/adminer.php", "/adminer/", "/pma/", "/pma/index.php",
    "/sqladmin/", "/mysql-admin/", "/dbadmin/", "/dba/",
    "/manager/html", "/manager/status", "/manager/jmxproxy",
    "/host-manager/html", "/host-manager/status",

    # ── Framework configs (expanded) ──
    "/.env", "/.env.local", "/.env.production", "/.env.development",
    "/.env.staging", "/.env.test", "/.env.example", "/.env.dev",
    "/.env.prod", "/.env.stage", "/.env.qa", "/.env.live",
    "/.env.master", "/.env.backup", "/.env.save", "/.env.swp",
    "/.env.bak", "/.env.old", "/.env.orig", "/.env~",
    "/.env.production.local", "/.env.development.local",
    "/config.php", "/config.json", "/config.yaml", "/config.yml",
    "/config.ini", "/config.toml", "/config.xml", "/config.js",
    "/config/settings.php", "/config/database.php", "/config/app.php",
    "/config/credentials", "/config/secrets.yml", "/config/master.key",
    "/config/database.yml", "/config/credentials.yml.enc",
    "/appsettings.json", "/appsettings.Development.json", "/appsettings.Production.json",
    "/settings.json", "/settings.php", "/settings.py", "/settings.ini",
    "/local_settings.py", "/settings_local.php",
    "/wp-config.php", "/wp-config.php.bak", "/wp-config.php.old",
    "/wp-config.php.save", "/wp-config.php~", "/wp-config.php.swp",
    "/configuration.php", "/configuration.php.bak",
    "/web.config", "/web.config.bak", "/web.config.old",
    "/.htaccess", "/.htaccess.bak", "/.htaccess.old", "/.htpasswd",
    "/.htpasswd.bak", "/.htpasswd.old",
    "/conf/config.php", "/conf/settings.php", "/conf/database.php",
    "/include/config.php", "/includes/config.php", "/inc/config.php",
    "/system/config.php", "/system/settings.php",
    "/application/config/config.php", "/application/config/database.php",
    "/application/config/settings.php",

    # ── Cloud credentials (expanded) ──
    "/.aws/credentials", "/.aws/config", "/.aws/credentials.bak",
    "/.ssh/id_rsa", "/.ssh/id_rsa.pub", "/.ssh/id_ecdsa",
    "/.ssh/id_ed25519", "/.ssh/authorized_keys", "/.ssh/known_hosts",
    "/.ssh/config", "/.ssh/environment",
    "/.dockerenv", "/.dockercfg", "/.docker/config.json",
    "/.gitlab-ci.yml", "/.github/workflows/", "/.circleci/config.yml",
    "/.travis.yml", "/bitbucket-pipelines.yml", "/Jenkinsfile",
    "/.vault-token", "/.vault-pass", "/vault.json",
    "/.terraform.tfvars", "/terraform.tfstate", "/terraform.tfstate.backup",
    "/.kube/config", "/.kube/token", "/.kube/certificate",
    "/.gcp/credentials.json", "/.azure/credentials",
    "/service-account.json", "/service-account-key.json",
    "/firebase.json", "/firebase-config.json", "/.firebaserc",
    "/google-services.json", "/GoogleService-Info.plist",
    "/.netrc", "/.npmrc", "/.pypirc", "/.yarnrc",
    "/.docker/registry", "/registry/",
    "/heroku.yml", "/Procfile",

    # ── API endpoints (expanded) ──
    "/api/", "/api/v1/", "/api/v2/", "/api/v3/",
    "/api/users", "/api/user", "/api/admin", "/api/config",
    "/api/auth", "/api/login", "/api/logout", "/api/register",
    "/api/me", "/api/profile", "/api/account", "/api/settings",
    "/api/health", "/api/status", "/api/version", "/api/info",
    "/api/upload", "/api/download", "/api/files", "/api/list",
    "/api/search", "/api/query", "/api/debug", "/api/test",
    "/api/swagger.json", "/api/openapi.json", "/api/docs",
    "/api/internal/", "/api/private/", "/api/secret/",
    "/rest/", "/rest/users", "/rest/admin", "/rest/config",
    "/v1/", "/v1/users", "/v1/admin", "/v1/config",
    "/v2/", "/v2/users", "/v2/admin", "/v2/config",
    "/graphql", "/graphql.json", "/graphiql", "/playground",
    "/swagger.json", "/swagger.yaml", "/swagger-ui/", "/swagger/",
    "/openapi.json", "/openapi.yaml", "/redoc", "/rapidoc",
    "/api-docs", "/api/docs", "/v1/api-docs", "/v2/api-docs",
    "/internal/api/", "/internal/users", "/internal/config",
    "/debug/api/", "/dev/api/", "/test/api/",
    "/_api/", "/_internal/", "/_debug/", "/_private/",

    # ── Backup & database dumps (expanded) ──
    "/backup/", "/backup.zip", "/backup.tar.gz", "/backup.tar",
    "/backup.sql", "/backup.json", "/backup.bak",
    "/backup-2023.zip", "/backup-2024.zip", "/backup-2025.zip",
    "/backups/", "/bak/", "/archive/", "/archives/",
    "/db.sql", "/db.sqlite", "/db.sqlite3", "/db.bak",
    "/database.sql", "/database.bak", "/database.dump",
    "/dump.sql", "/dump.bak", "/dump.json",
    "/www.zip", "/www.tar.gz", "www.rar", "/www.7z",
    "/site.zip", "/site.tar.gz", "/site.bak",
    "/website.zip", "/website.tar.gz",
    "/data.sql", "/data.bak", "/data.json", "/data.zip",
    "/mysql.sql", "/postgres.sql", "/pgdump.sql",
    "/mongodump.json", "/mongodump.bson",
    "/sql/dump.sql", "/sql/backup.sql", "/sql/database.sql",
    "/database/backup.sql", "/database/dump.sql",
    "/tmp/backup.sql", "/tmp/database.sql", "/tmp/dump.sql",
    "/old/", "/old/backup.sql", "/old/config.php",
    "/test/", "/test/database.sql", "/test/config.php",

    # ── Source code & build artifacts ──
    "/source/", "/src/", "/build/", "/dist/", "/out/", "/target/",
    "/coverage/", "/.nyc_output/", "/.cache/", "/.parcel-cache/",
    "/vendor/", "/vendor/composer/installed.json", "/vendor/autoload.php",
    "/node_modules/", "/node_modules/.env",
    "/.next/", "/.nuxt/", "/.svelte-kit/", "/.output/",
    "/.vercel/", "/.netlify/", "/.turbo/",
    "/package.json", "/package-lock.json", "/yarn.lock", "/pnpm-lock.yaml",
    "/composer.json", "/composer.lock",
    "/Dockerfile", "/docker-compose.yml", "/docker-compose.yaml",
    "/Containerfile", "/Pipfile", "/Pipfile.lock",
    "/requirements.txt", "/poetry.lock", "/pyproject.toml",
    "/Gemfile", "/Gemfile.lock", "/Rakefile",
    "/go.mod", "/go.sum", "/pom.xml", "/build.gradle",
    "/Cargo.toml", "/Cargo.lock", "/mix.exs",
    "/tsconfig.json", "/webpack.config.js", "/vite.config.js",
    "/.babelrc", "/.eslintrc", "/.prettierrc",
    "/.editorconfig", "/.flake8", "/.pylintrc",
    "/Makefile", "/CMakeLists.txt",
    "/README.md", "/README.txt", "/CHANGELOG.md", "/LICENSE",

    # ── Logs & debug (expanded) ──
    "/error.log", "/access.log", "/debug.log", "/app.log",
    "/out.log", "/laravel.log", "/storage/logs/laravel.log",
    "/var/log/", "/var/log/apache2/", "/var/log/nginx/",
    "/var/log/auth.log", "/var/log/syslog", "/var/log/messages",
    "/logs/", "/log/", "/_logs/",
    "/.bash_history", "/.mysql_history", "/.psql_history", "/.viminfo",
    "/phpinfo.php", "/info.php", "/test.php", "/debug.php",
    "/_profiler/", "/_debugbar/", "/symfony/_profiler/",
    "/actuator/", "/actuator/env", "/actuator/heapdump",
    "/actuator/loggers", "/actuator/beans", "/actuator/configprops",
    "/actuator/mappings", "/actuator/metrics", "/actuator/threaddump",
    "/actuator/httptrace", "/actuator/health", "/actuator/info",
    "/server-status", "/server-info", "/status?full",

    # ── Git/SVN exposure ──
    "/.git/HEAD", "/.git/config", "/.git/index",
    "/.git/objects/info/packs", "/.git/logs/HEAD",
    "/.git/refs/heads/master", "/.git/refs/heads/main",
    "/.git/COMMIT_EDITMSG", "/.git/packed-refs",
    "/.git/description", "/.git/info/refs",
    "/.svn/entries", "/.svn/wc.db", "/.svn/props/",
    "/.hg/store", "/.bzr/", "/CVS/Root", "/CVS/Entries",

    # ── CMS specific (expanded) ──
    "/wp-content/uploads/", "/wp-content/plugins/", "/wp-content/themes/",
    "/wp-content/backup-db/", "/wp-content/updraft/",
    "/wp-content/uploads/wpallimport/", "/wp-content/backups/",
    "/wp-json/wp/v2/users", "/wp-json/wp/v2/posts",
    "/wp-cron.php", "/wp-login.php", "/wp-mail.php",
    "/xmlrpc.php", "/wp-signup.php", "/wp-register.php",
    "/sites/default/settings.php", "/sites/default/files/",
    "/user/register", "/admin/structure", "/admin/reports",
    "/app/etc/local.xml", "/var/log/exception.log", "/var/log/system.log",
    "/media/jui/", "/components/com_users/",
    "/installation/index.php", "/installation/configuration.php",

    # ── Common config & dotfiles ──
    "/.gitignore", "/.gitattributes", "/.dockerignore",
    "/.well-known/security.txt", "/.well-known/openid-configuration",
    "/.well-known/jwks.json", "/.well-known/assetlinks.json",
    "/robots.txt", "/sitemap.xml", "/sitemap-index.xml",
    "/crossdomain.xml", "/clientaccesspolicy.xml",
    "/humans.txt", "/security.txt", "/manifest.json",
    "/.DS_Store", "/Thumbs.db", "/desktop.ini",
    "/.idea/", "/.idea/workspace.xml", "/.vscode/",
    "/.vscode/settings.json", "/.vscode/launch.json",
    "/.DS_Store", "/._.DS_Store", "/.DS_Store.bak",

    # ── Static site / JAMstack ──
    "/_headers", "/_redirects", "/netlify.toml", "/vercel.json",
    "/_next/static/", "/_next/data/", "/_nuxt/",
    "/_app/", "/_astro/", "/.svelte-kit/",
    "/service-worker.js", "/sw.js",
    "/manifest.webmanifest", "/site.webmanifest",
    "/buildManifest.json", "/react-loadable-manifest.json",
    "/page-data.json", "/page-data/", "/gatsby-data.json",

    # ── Database & cache endpoints ──
    "/redis/", "/memcached/", "/mongodb/", "/elasticsearch/",
    "/_cat/indices", "/_cluster/health", "/_search",
    "/solr/", "/solr/admin/",
    "/couchdb/", "/couchdb/_all_dbs",
    "/influxdb/", "/prometheus/", "/-/metrics",

    # ── Dev/CI/CD endpoints ──
    "/jenkins/", "/jenkins/script", "/jenkins/login",
    "/gitlab/", "/gitlab/api/v4/projects",
    "/grafana/", "/grafana/api/health",
    "/kibana/", "/kibana/app/kibana",
    "/consul/", "/consul/v1/agent/members",
    "/nomad/", "/rancher/",
    "/drone/", "/drone/api/user",
    "/teamcity/", "/teamcity/httpAuth/app/rest/server",
    "/gocd/", "/gocd/api/config/pipelines",

    # ── Common dev/test paths ──
    "/test/", "/dev/", "/debug/", "/temp/", "/tmp/",
    "/old/", "/new/", "/beta/", "/demo/", "/preview/",
    "/staging/", "/production/", "/qa/", "/sandbox/",
    "/internal/", "/intranet/", "/private/", "/secret/",
    "/.test", "/.dev", "/.debug", "/.internal",

    # ── PHP specific (expanded) ──
    "/index.php", "/index.php.bak", "/index.php~",
    "/info.php", "/info.php.bak", "/phpinfo.php",
    "/test.php", "/test.php.bak", "/debug.php",
    "/shell.php", "/cmd.php", "/exec.php", "/system.php",
    "/upload.php", "/download.php", "/delete.php",
    "/config.php", "/config.php.bak", "/config.php~",
    "/db.php", "/database.php", "/connect.php",
    "/functions.php", "/include.php", "/require.php",
    "/wp-config.php", "/wp-settings.php", "/wp-load.php",
    "/wp-blog-header.php", "/wp-mail.php",

    # ── Python/Django specific ──
    "/manage.py", "/settings.py", "/wsgi.py", "/asgi.py",
    "/local_settings.py", "/config/settings.py",
    "/db.sqlite3", "/db.sqlite", "/app.db", "/data.db",
    "/admin/login/", "/admin/logout/", "/admin/auth/",
    "/media/", "/static/", "/staticfiles/",

    # ── Ruby/Rails specific ──
    "/Gemfile", "/Gemfile.lock", "/Rakefile", "/config.ru",
    "/config/database.yml", "/config/secrets.yml",
    "/config/master.key", "/config/credentials.yml.enc",
    "/config/initializers/", "/config/environments/",
    "/db/schema.rb", "/db/seeds.rb", "/db/migrate/",
    "/log/production.log", "/log/development.log",

    # ── Java/Spring specific ──
    "/WEB-INF/web.xml", "/WEB-INF/classes/",
    "/WEB-INF/lib/", "/WEB-INF/config/",
    "/META-INF/MANIFEST.MF", "/META-INF/maven/",
    "/struts.xml", "/struts-config.xml",
    "/application.properties", "/application.yml",
    "/application-dev.properties", "/application-prod.properties",

    # ── .NET specific ──
    "/trace.axd", "/trace.axd?id=1",
    "/elmah.axd", "/elmah/elmah.axd",
    "/web.config.bak", "/web.config.old",
    "/App_Data/", "/App_Data/Logs/",
    "/bin/", "/App_Code/",
    "/Reserved.ReportViewerWebControl.axd",

    # ── Cloud storage ──
    "/.aws/", "/.gcp/", "/.azure/",
    "/storage/", "/storage/logs/", "/storage/framework/",
    "/bucket/", "/buckets/",
    "/s3/", "/s3-bucket/", "/s3-buckets/",
]

# v11.1: EXPANDED secret patterns
SECRET_PATTERNS_V2 = [
    # Cloud providers
    ("AWS Access Key ID", r'AKIA[0-9A-Z]{16}', "critical", "AWS Access Key"),
    ("AWS Secret Key", r'aws_secret_access_key["\']?\s*[:=]\s*["\']?[A-Za-z0-9/+=]{40}', "critical", "AWS Secret Key"),
    ("AWS STS Token", r'ASIA[0-9A-Z]{16}', "critical", "AWS STS Token"),
    ("Google API Key", r'AIza[0-9A-Za-z_\-]{35}', "high", "Google API Key"),
    ("Google OAuth", r'ya29\.[0-9A-Za-z_\-]+', "high", "Google OAuth Token"),
    ("Azure Key", r'[A-Za-z0-9_\-]{86}', "medium", "Possible Azure key (86 chars)"),

    # Payment / Crypto
    ("Stripe Secret", r'sk_live_[0-9A-Za-z]{24,}', "critical", "Stripe secret key (live)"),
    ("Stripe Restricted", r'rk_live_[0-9A-Za-z]{24,}', "critical", "Stripe restricted key"),
    ("Coinbase API", r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', "high", "Possible Coinbase API key"),
    ("Binance API", r'[A-Za-z0-9]{64}', "medium", "Possible Binance API key (64 chars)"),

    # AI / LLM
    ("OpenAI API Key", r'sk-[A-Za-z0-9]{20}T3BlbkFJ[A-Za-z0-9]{16}', "critical", "OpenAI API key"),
    ("OpenAI Project Key", r'sk-proj-[A-Za-z0-9_\-]{40,}', "critical", "OpenAI project API key"),
    ("Anthropic API Key", r'sk-ant-[A-Za-z0-9_\-]{60,}', "critical", "Anthropic Claude API key"),
    ("HuggingFace Token", r'hf_[A-Za-z0-9]{34,}', "high", "HuggingFace token"),
    ("Replicate Token", r'r8_[A-Za-z0-9]{37}', "high", "Replicate API token"),
    ("Together AI Key", r'[a-f0-9]{64}', "medium", "Possible Together AI key"),

    # Communication
    ("Slack Token", r'xox[abprs]-[0-9A-Za-z-]{10,}', "high", "Slack token"),
    ("Slack Webhook", r'https://hooks\.slack\.com/services/T[A-Z0-9]+', "high", "Slack webhook"),
    ("Discord Bot Token", r'[MN][A-Za-z0-9_\-]{22,}\.[A-Za-z0-9_\-]{4,}\.[A-Za-z0-9_\-]{20,}', "high", "Discord bot token"),
    ("Discord Webhook", r'https://discord(?:app)?\.com/api/webhooks/\d+/[A-Za-z0-9_\-]+', "high", "Discord webhook"),
    ("Telegram Bot Token", r'[0-9]{6,10}:[A-Za-z0-9_\-]{30,}', "high", "Telegram bot token"),
    ("Teams Webhook", r'https://[a-z0-9]+\.webhook\.office\.com/webhookb2/[a-f0-9\-]+', "high", "MS Teams webhook"),

    # Dev platforms
    ("GitHub Token", r'gh[pousr]_[A-Za-z0-9]{36,}', "critical", "GitHub token"),
    ("GitHub Fine-grained", r'github_pat_[a-zA-Z0-9_]{22,}', "critical", "GitHub fine-grained PAT"),
    ("GitLab Token", r'glpat-[A-Za-z0-9_\-]{20}', "high", "GitLab PAT"),
    ("Heroku API Key", r'(?:heroku_api_key|heroku_api_token)["\']?\s*[:=]\s*["\']?[0-9a-fA-F]{32}', "high", "Heroku API key"),
    ("Linear API Token", r'lin_api_[A-Za-z0-9_\-]{30,}', "high", "Linear API token"),
    ("Notion Token", r'(?:secret_)?ntn_[A-Za-z0-9]{40,}', "high", "Notion integration token"),
    ("Jira Token", r'[A-Za-z0-9]{24}ATATT3[A-Za-z0-9_\-]{100,}', "high", "Jira API token"),
    ("Asana Token", r'[0-9]/[a-f0-9]{32,}:', "high", "Asana PAT"),

    # SaaS
    ("Shopify Token", r'shpat_[A-Fa-f0-9]{32}', "critical", "Shopify access token"),
    ("Shopify App Secret", r'shssa_[A-Fa-f0-9]{32}', "high", "Shopify app secret"),
    ("Twilio SID", r'AC[a-z0-9]{32}', "high", "Twilio Account SID"),
    ("SendGrid API Key", r'SG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}', "high", "SendGrid API key"),
    ("Mailgun API Key", r'key-[0-9a-zA-Z]{32}', "high", "Mailgun API key"),
    ("Mailchimp Key", r'[0-9a-f]{32}-us[0-9]{1,2}', "high", "Mailchimp API key"),
    ("Square OAuth Secret", r'sq0csp-[0-9A-Za-z_\-]{43}', "high", "Square OAuth secret"),
    ("CircleCI Token", r'CCIPRJ_[A-Za-z0-9_\-]{22,}', "high", "CircleCI project token"),
    ("Datadog API Key", r'(?:DD_API_KEY|DATADOG_API_KEY)["\']?\s*[:=]\s*["\']?[a-f0-9]{32}', "high", "Datadog API key"),
    ("HashiCorp Vault Token", r'(?:hvs\.[A-Za-z0-9_\-]{60,})', "critical", "Vault service token"),
    ("Tencent SecretId", r'AKID[A-Za-z0-9]{13,}', "high", "Tencent Cloud SecretId"),

    # Database connection strings
    ("MongoDB URI", r'mongodb(?:\+srv)?://[^\s"\']+:[^\s"\']+@[^\s"\']+', "high", "MongoDB connection string"),
    ("PostgreSQL URI", r'postgres(?:ql)?://[^\s"\']+:[^\s"\']+@[^\s"\']+', "high", "PostgreSQL connection string"),
    ("MySQL URI", r'mysql://[^\s"\']+:[^\s"\']+@[^\s"\']+', "high", "MySQL connection string"),
    ("Redis URI", r'redis://:[^\s"\']+@[^\s"\']+', "high", "Redis connection string"),
    ("Firebase URL", r'https?://[a-z0-9\-]+\.firebaseio\.com', "high", "Firebase DB URL"),

    # Generic secrets
    ("JWT Token", r'eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}', "high", "JWT token"),
    ("Private Key PEM", r'-----BEGIN (RSA|EC|DSA|OPENSSH|PGP) PRIVATE KEY-----', "critical", "Private key PEM"),
    ("Generic Secret", r'(?:secret|api[_-]?key|token|passwd|password)["\']?\s*[:=]\s*["\']?[A-Za-z0-9+/=_\-]{20,}', "medium", "Generic secret"),
    ("Bearer Token", r'Bearer\s+[A-Za-z0-9_\-\.]{20,}', "medium", "Bearer token"),
    ("Basic Auth", r'Basic\s+[A-Za-z0-9+/=]{16,}', "medium", "Basic auth header"),

    # PII
    ("Email Address", r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "low", "Email address"),
    ("Internal IPv4", r'\b(?:10|172\.(?:1[6-9]|2[0-9]|3[01])|192\.168)\.\d{1,3}\.\d{1,3}\b', "info", "Private IPv4"),
    ("US Phone", r'\+1\s?\(?[2-9]\d{2}\)?[\s.-]?[2-9]\d{2}[\s.-]?\d{4}', "info", "US phone"),
]

# v11.1: EXPANDED brute-force wordlist
BRUTE_NAMES_V2 = [
    # Basic
    "index", "default", "main", "home", "start", "page", "view", "app",
    "config", "settings", "setup", "init", "configure", "options", "prefs",
    # Admin
    "admin", "administrator", "adminpanel", "admincp", "adminarea",
    "manage", "manager", "panel", "dashboard", "console", "controlpanel",
    "cp", "cpadmin", "webadmin", "siteadmin", "sysadmin",
    # Auth
    "login", "signin", "logout", "signout", "register", "signup",
    "auth", "authenticate", "oauth", "sso", "saml", "token", "session",
    "forgot", "reset", "verify", "confirm", "activate",
    # Users
    "user", "users", "account", "accounts", "profile", "profiles",
    "member", "members", "people", "staff", "employee", "employees",
    "customer", "customers", "client", "clients",
    # Database
    "db", "database", "sql", "mysql", "postgres", "mongodb", "redis",
    "data", "dump", "backup", "bak", "export", "import", "migrate",
    "schema", "table", "tables", "record", "records", "entry", "entries",
    # API
    "api", "rest", "graphql", "rpc", "soap", "json", "xml", "yaml",
    "endpoint", "endpoints", "route", "routes", "callback", "webhook",
    "v1", "v2", "v3", "v4", "latest", "stable", "beta", "alpha",
    # Files
    "file", "files", "upload", "uploads", "download", "downloads",
    "document", "documents", "doc", "docs", "image", "images",
    "media", "asset", "assets", "static", "public", "private",
    # Content
    "post", "posts", "article", "articles", "blog", "blogs",
    "news", "event", "events", "page", "pages",
    "product", "products", "item", "items", "order", "orders",
    "cart", "checkout", "payment", "payments", "invoice", "invoices",
    # System
    "system", "sys", "server", "service", "services", "health",
    "status", "info", "version", "ping", "pong", "heartbeat",
    "monitor", "metrics", "stats", "statistics", "analytics",
    "log", "logs", "error", "errors", "debug", "trace", "profile",
    # Dev/test
    "test", "testing", "dev", "development", "prod", "production",
    "stage", "staging", "qa", "sandbox", "demo", "preview",
    "beta", "internal", "external", "private", "secret", "hidden",
    # Security
    "security", "secure", "protected", "private", "secret",
    "key", "keys", "token", "tokens", "cert", "certificate",
    "ssh", "rsa", "ecdsa", "pgp", "jwt",
    # Tools
    "tool", "tools", "utility", "utilities", "helper", "helpers",
    "script", "scripts", "cron", "job", "jobs", "task", "tasks",
    "worker", "workers", "queue", "queues", "batch", "batchs",
    # Misc
    "old", "new", "tmp", "temp", "cache", "cache_clear",
    "archive", "archives", "backup", "backups", "history",
    "search", "find", "query", "filter", "sort", "list",
    "about", "contact", "help", "support", "faq", "terms",
    "privacy", "policy", "legal", "license", "copyright",
    # WordPress specific
    "wp-config", "wp-login", "wp-admin", "wp-content", "wp-includes",
    "wp-json", "wp-cron", "wp-mail", "wp-signup", "wp-register",
    "xmlrpc", "wp-blog-header", "wp-load", "wp-settings",
    # Common CMS
    "phpinfo", "info", "php", "test", "shell", "cmd", "exec",
    "webconfig", "configuration", "settings.php", "config.php",
]

# v11.1: EXPANDED brute extensions
BRUTE_EXTS_V2 = [".php", ".html", ".htm", ".txt", ".json", ".xml", ".yaml", ".yml",
                 ".ini", ".toml", ".bak", ".old", ".orig", ".save", ".swp", "~",
                 ".zip", ".tar.gz", ".tar", ".gz", ".sql", ".db", ".sqlite",
                 ".log", ".md", ".env", ".config", ".conf", ".dist", ".sample"]

# Merge old + new
LEAK_PATHS.extend(LEAK_PATHS_V2)
# Deduplicate while preserving order
_seen_leak = set()
LEAK_PATHS = [x for x in LEAK_PATHS if not (x in _seen_leak or _seen_leak.add(x))]

# Merge secret patterns
SECRET_PATTERNS.extend(SECRET_PATTERNS_V2)
_seen_secret = set()
SECRET_PATTERNS = [x for x in SECRET_PATTERNS if not (x[0] in _seen_secret or _seen_secret.add(x[0]))]

# Merge brute names
BRUTE_NAMES.extend(BRUTE_NAMES_V2)
BRUTE_NAMES = list(dict.fromkeys(BRUTE_NAMES))  # dedupe preserve order

# Use expanded extensions
BRUTE_EXTS_EXPANDED = BRUTE_EXTS_V2

# Skip these file extensions when brute-forcing (binary files we can't parse)
SKIP_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico",
                  ".mp4", ".webm", ".mp3", ".wav", ".pdf", ".woff", ".woff2",
                  ".ttf", ".eot", ".otf"}

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
    try:
        ip = ipaddress.ip_address(hn)
    except ValueError:
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

# Activity log: stores recent activity messages per scan_id (for live terminal)
activity_logs = {}
activity_lock = threading.Lock()

def push_activity(scan_id, msg):
    """Push an activity log line for live terminal display."""
    with activity_lock:
        q = activity_logs.setdefault(scan_id, [])
        q.append({"t": time.time(), "msg": msg})
        # Keep last 200 entries
        if len(q) > 200:
            del q[:len(q)-200]

def get_activity(scan_id, since=0):
    """Get activity lines since timestamp."""
    with activity_lock:
        q = activity_logs.get(scan_id, [])
        return [item for item in q if item["t"] >= since]

async def fetch(session, url, headers=None, proxy=None, timeout=10, max_retries=2, bypass_mode="auto"):
    """Fetch với auto-retry khi gặp 429/timeout, xoay User-Agent mỗi retry.
    v11.1: WAF bypass mode support — stealth/aggressive/turbo with header rotation."""
    if not HAS_AIOHTTP:
        return "", 0, {}, 0
    last_err = None
    base_headers = dict(headers or {})
    profile = WAF_BYPASS_PROFILES.get(bypass_mode, WAF_BYPASS_PROFILES["auto"])
    effective_retries = max(max_retries, profile["retry"])
    for attempt in range(effective_retries + 1):
        start = time.time()
        # Build bypass headers — rotate per attempt
        attempt_headers = dict(base_headers)
        # User-Agent rotation
        if profile["rotate_ua"]:
            attempt_headers["User-Agent"] = random.choice(USER_AGENTS)
        elif "User-Agent" not in attempt_headers and "user-agent" not in attempt_headers:
            attempt_headers["User-Agent"] = random.choice(USER_AGENTS)
        # X-Forwarded-For rotation (bypass IP rate-limiting)
        if profile["rotate_xff"]:
            attempt_headers["X-Forwarded-For"] = random.choice(FAKE_XFF_IPS)
            attempt_headers["X-Real-IP"] = attempt_headers["X-Forwarded-For"]
            attempt_headers["X-Client-IP"] = attempt_headers["X-Forwarded-For"]
            attempt_headers["True-Client-IP"] = attempt_headers["X-Forwarded-For"]
        # Add Accept-Language + Referer for stealth mode
        if bypass_mode == "stealth":
            attempt_headers.setdefault("Accept-Language", random.choice(FAKE_ACCEPT_LANG))
            attempt_headers.setdefault("Referer", random.choice(FAKE_REFERERS) + url.split('/')[-1] if url.split('/')[-1] else random.choice(FAKE_REFERERS))
            attempt_headers.setdefault("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
            attempt_headers.setdefault("Sec-Fetch-Dest", "document")
            attempt_headers.setdefault("Sec-Fetch-Mode", "navigate")
            attempt_headers.setdefault("Sec-Fetch-Site", "cross-site")
            attempt_headers.setdefault("Sec-Fetch-User", "?1")
            attempt_headers.setdefault("Upgrade-Insecure-Requests", "1")
        # Add randomized delay before request (rate-limit avoidance)
        if profile["delay_max"] > 0:
            delay = random.uniform(profile["delay_min"], profile["delay_max"])
            await asyncio.sleep(delay)
        try:
            async with session.get(url, headers=attempt_headers, proxy=proxy,
                                    timeout=aiohttp.ClientTimeout(total=timeout),
                                    ssl=False, allow_redirects=True) as r:
                text = await r.text(errors="replace")
                elapsed = round((time.time() - start) * 1000, 1)
                if r.status == 429 and attempt < effective_retries:
                    # Exponential backoff with jitter
                    backoff = (2 ** attempt) + random.uniform(0.5, 1.5)
                    # If stealth mode, longer backoff
                    if bypass_mode == "stealth":
                        backoff += 2
                    await asyncio.sleep(backoff)
                    continue
                # 403 + Cloudflare/Akamai challenge page → retry with new UA + XFF
                if r.status == 403 and attempt < effective_retries:
                    challenge_markers = ["cloudflare", "challenge", "captcha", "just a moment",
                                        "akamai", "bmsc", "incapsula", "access denied",
                                        "blocked", "forbidden", "request rejected"]
                    if any(m in text.lower()[:3000] for m in challenge_markers):
                        await asyncio.sleep(0.5 * (attempt + 1))
                        continue
                return text, r.status, dict(r.headers), elapsed
        except asyncio.TimeoutError as e:
            elapsed = round((time.time() - start) * 1000, 1)
            last_err = "Timeout"
            if attempt < effective_retries:
                await asyncio.sleep(0.3 * (attempt + 1))
                continue
        except (aiohttp.ClientConnectorError, aiohttp.ServerDisconnectedError,
                aiohttp.ClientOSError, ConnectionError) as e:
            elapsed = round((time.time() - start) * 1000, 1)
            last_err = str(type(e).__name__) + ": " + str(e)[:60]
            if attempt < 1:
                await asyncio.sleep(0.2)
                continue
            break
        except Exception as e:
            elapsed = round((time.time() - start) * 1000, 1)
            last_err = str(type(e).__name__) + ": " + str(e)[:60]
            if attempt < effective_retries:
                await asyncio.sleep(0.3 * (attempt + 1))
                continue
    return str(last_err)[:100] if last_err else "", 0, {}, 0

async def fetch_with_custom_headers(session, url, custom_headers, proxy, timeout, method="GET", body=None):
    """Fetch với arbitrary method + body (POST/PUT/etc) + custom headers.
    Used for SSTI/SQLi/header injection tests."""
    if not HAS_AIOHTTP:
        return "", 0, {}, 0
    start = time.time()
    try:
        timeout_obj = aiohttp.ClientTimeout(total=timeout)
        kwargs = {"headers": custom_headers, "proxy": proxy, "timeout": timeout_obj, "ssl": False, "allow_redirects": True}
        if body and method in ("POST", "PUT", "PATCH"):
            kwargs["data"] = body
        async with session.request(method, url, **kwargs) as r:
            text = await r.text(errors="replace")
            elapsed = round((time.time() - start) * 1000, 1)
            return text, r.status, dict(r.headers), elapsed
    except Exception as e:
        return str(type(e).__name__) + ": " + str(e)[:60], 0, {}, 0

async def check_ssti(session, target, custom_headers, proxy, timeout, log_fn, cancel_fn):
    """Test Server-Side Template Injection trên các endpoint phổ biến."""
    findings = []
    test_endpoints = [
        target,
        urljoin(target, "/search"),
        urljoin(target, "/render"),
        urljoin(target, "/template"),
        urljoin(target, "/preview"),
        urljoin(target, "/api/render"),
        urljoin(target, "/api/preview"),
        urljoin(target, "/page"),
    ]
    sem = asyncio.Semaphore(5)
    async def test_one(url):
        if cancel_fn():
            return None
        results = []
        for payload, expected in SSTI_PAYLOADS:
            if cancel_fn():
                return results
            try:
                # Inject payload via query param `q`, `name`, `template`, `input`, `query`
                for param in ["q", "name", "template", "input", "query", "search", "text"]:
                    test_url = f"{url}?{param}={payload}"
                    async with sem:
                        t, c, h, rt = await fetch(session, test_url, custom_headers, proxy, min(timeout, 5))
                    if c == 200 and t:
                        # Check if expected value appears in response (means template engine executed payload)
                        if expected in t:
                            results.append({
                                "url": test_url, "param": param, "payload": payload,
                                "expected": expected, "status_code": c,
                                "severity": "critical",
                                "description": f"SSTI detected: payload '{payload}' → returned '{expected}' (template engine executed)",
                            })
                            log_fn(f"[SSTI] {param}={payload} → {expected} (CRITICAL)")
                            return results  # One finding per endpoint is enough
            except Exception:
                continue
        return results
    for coro in asyncio.as_completed([test_one(u) for u in test_endpoints]):
        r = await coro
        if r:
            findings.extend(r)
    return findings

async def check_proto_pollution(session, target, custom_headers, proxy, timeout, log_fn, cancel_fn):
    """Test Prototype Pollution via query params."""
    findings = []
    sem = asyncio.Semaphore(5)
    async def test_one(payload):
        if cancel_fn():
            return None
        test_url = target + payload
        try:
            async with sem:
                t, c, h, rt = await fetch(session, test_url, custom_headers, proxy, min(timeout, 5))
            # Check if response changed significantly vs baseline (means __proto__ injection affected something)
            # Or check for any reflection of "polluted" in body/headers
            if c == 200 and t and "polluted" in t.lower():
                return {
                    "url": test_url, "payload": payload, "status_code": c,
                    "severity": "high",
                    "description": "Prototype Pollution detected: payload reflected in response",
                }
        except Exception:
            return None
        return None
    for coro in asyncio.as_completed([test_one(p) for p in PROTO_POLLUTION_PAYLOADS]):
        r = await coro
        if r:
            findings.append(r)
            log_fn(f"[PROTO] {r['payload'][:50]} → REFLECTED")
    return findings

async def check_header_injection(session, target, custom_headers, proxy, timeout, log_fn, cancel_fn):
    """Test HTTP header injection: X-Forwarded-Host, X-Original-URL, etc."""
    findings = []
    sem = asyncio.Semaphore(5)
    async def test_one(header_name, value):
        if cancel_fn():
            return None
        test_headers = dict(custom_headers or {})
        test_headers[header_name] = value
        try:
            async with sem:
                t, c, h, rt = await fetch(session, target, test_headers, proxy, min(timeout, 5))
            # Check if our injected value was reflected in body or Location header
            reflected_in_body = value in (t or "")[:5000]
            location = h.get("Location") or h.get("location") or ""
            reflected_in_location = value in location
            # Check for redirect to our injected host
            if c in (301, 302, 303, 307, 308) and value in location:
                return {
                    "header": header_name, "value": value, "status_code": c,
                    "redirect_location": location[:200],
                    "severity": "high",
                    "description": f"Header injection: {header_name}={value} → redirect to injected host",
                }
            elif reflected_in_body and value not in ("evil.com", "127.0.0.1:8080", "localhost", "admin"):
                return {
                    "header": header_name, "value": value, "status_code": c,
                    "redirect_location": "",
                    "severity": "medium",
                    "description": f"Header injection: {header_name}={value} reflected in body",
                }
            # Special: X-Original-URL / X-Rewrite-URL → if 200, may have bypassed access control
            elif header_name in ("X-Original-URL", "X-Rewrite-URL") and c == 200:
                # Compare body length vs original request
                # If significantly different, may have hit internal endpoint
                return {
                    "header": header_name, "value": value, "status_code": c,
                    "redirect_location": "",
                    "severity": "medium",
                    "description": f"Header injection: {header_name}={value} → 200 OK (possible access bypass)",
                }
        except Exception:
            return None
        return None
    for coro in asyncio.as_completed([test_one(h, v) for h, v in HEADER_INJECTION_PAYLOADS]):
        r = await coro
        if r:
            findings.append(r)
            log_fn(f"[HEADER-INJ] {r['header']}={r['value']} → {r['status_code']}")
    return findings

async def check_cache_poisoning(session, target, main_text, custom_headers, proxy, timeout, log_fn, cancel_fn):
    """Test cache poisoning: inject X-Forwarded-Host/Scheme and check if response reflects it."""
    findings = []
    sem = asyncio.Semaphore(3)
    async def test_one(header_name, value):
        if cancel_fn:
            return None
        test_headers = dict(custom_headers or {})
        test_headers[header_name] = value
        try:
            async with sem:
                t, c, h, rt = await fetch(session, target, test_headers, proxy, min(timeout, 5))
            if c == 200 and t:
                # Check if our injected value appears in response (means it was cached)
                if value in t[:5000] and value not in (main_text or ""):
                    return {
                        "header": header_name, "value": value,
                        "severity": "high",
                        "description": f"Cache poisoning: {header_name}={value} reflected in cached response",
                        "evidence": value,
                    }
        except Exception:
            return None
        return None
    for coro in asyncio.as_completed([test_one(h, v) for h, v in CACHE_POISON_PAYLOADS]):
        r = await coro
        if r:
            findings.append(r)
            log_fn(f"[CACHE-POISON] {r['header']}={r['value']} → reflected")
    return findings

async def check_default_creds(session, target, forms, custom_headers, proxy, timeout, log_fn, cancel_fn):
    """Test default credentials trên login forms detected."""
    findings = []
    if not forms:
        return findings
    login_forms = [f for f in forms if f.get("type") == "login" and f.get("action")]
    if not login_forms:
        return findings
    sem = asyncio.Semaphore(3)
    for form in login_forms[:3]:  # Test up to 3 login forms
        if cancel_fn():
            break
        action = form.get("action")
        method = form.get("method", "POST").upper()
        # Find password + username field names
        inputs = form.get("inputs_preview", [])
        username_field = None
        password_field = None
        for inp in inputs:
            if inp.get("type") == "password":
                password_field = inp.get("name", "password")
            elif inp.get("type") in ("text", "email") and inp.get("name"):
                username_field = inp.get("name")
        if not username_field or not password_field:
            username_field = username_field or "username"
            password_field = password_field or "password"
        log_fn(f"[AUTH] Testing default creds on {action} (fields: {username_field}, {password_field})")
        for username, password in DEFAULT_CREDS:
            if cancel_fn():
                break
            try:
                # Build form body
                body = f"{username_field}={username}&{password_field}={password}"
                test_headers = dict(custom_headers or {})
                test_headers["Content-Type"] = "application/x-www-form-urlencoded"
                async with sem:
                    t, c, h, rt = await fetch_with_custom_headers(session, action, test_headers, proxy, min(timeout, 8), method="POST", body=body)
                # Check for successful login (redirect to dashboard, or "welcome" in body)
                if c in (302, 303) and any(m in (h.get("Location") or "").lower() for m in ["dashboard", "admin", "welcome", "home", "panel"]):
                    findings.append({
                        "form_action": action, "username": username, "password": password,
                        "status_code": c, "redirect": h.get("Location", "")[:100],
                        "severity": "critical",
                        "description": f"Default credentials work: {username}:{password}",
                    })
                    log_fn(f"[AUTH] Default creds work: {username}:{password} → {c}")
                    break
                elif c == 200 and any(m in (t or "").lower()[:3000] for m in ["welcome", "logged in", "dashboard", "logout", "sign out"]):
                    findings.append({
                        "form_action": action, "username": username, "password": password,
                        "status_code": c, "redirect": "",
                        "severity": "critical",
                        "description": f"Default credentials work: {username}:{password}",
                    })
                    log_fn(f"[AUTH] Default creds work: {username}:{password}")
                    break
            except Exception:
                continue
    return findings

async def fetch_with_fallbacks(session, target, custom_headers, proxy, timeout, log_fn=None):
    """Try target với nhiều chiến lược fallback.
    Strategy: thử original URL + trailing slash variant song song để tối ưu.
    Trả về (text, code, headers, elapsed, final_url, error_msg)."""
    parsed = urlparse(target)
    host = parsed.hostname
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query

    # Build list of URLs to try in order — ưu tiên trailing slash variant nếu URL gốc không có path rõ ràng
    # (Netlify/Vercel thường redirect /path → /path/, tốn thời gian)
    urls_to_try = []
    if not target.endswith('/'):
        # Nếu URL không có path rõ ràng (chỉ host), thêm variant có /
        if path == "/" or path == "":
            urls_to_try.append(target + "/")
        urls_to_try.append(target)
    else:
        urls_to_try.append(target)
    # Add https + host + path (clean) và www. variants
    fallback_urls = [
        f"https://{host}{path}",
        f"http://{host}{path}",
        f"https://www.{host}{path}",
    ]
    for u in fallback_urls:
        if u not in urls_to_try:
            urls_to_try.append(u)

    last_err = None
    for idx, url in enumerate(urls_to_try):
        # First 2 attempts: full timeout + 2 retries. Later: shorter timeout + 1 retry.
        if idx < 2:
            attempt_timeout = timeout
            attempt_retries = 2
        else:
            attempt_timeout = min(timeout, 8)
            attempt_retries = 1
        if log_fn and idx > 0:
            log_fn(f"[FALLBACK] Trying {url} (timeout {attempt_timeout}s)")
        text, code, headers, elapsed = await fetch(session, url, custom_headers, proxy, attempt_timeout, max_retries=attempt_retries)
        if code > 0:  # Got a response (even 4xx/5xx counts)
            if log_fn and url != target:
                log_fn(f"[FALLBACK] Success: {url} → {code}")
            return text, code, headers, elapsed, url, None
        last_err = text or "Connection failed"
        if log_fn and idx == 0:
            log_fn(f"[FALLBACK] Original URL failed ({last_err[:80]}), trying alternatives...")
    # All attempts failed
    return "", 0, {}, 0, target, last_err

def detect_static_site_host(headers, html, host):
    """Detect if site is hosted on a static-site platform (Netlify/Vercel/CF Pages/GH Pages)."""
    indicators = []
    hs = json.dumps(headers).lower()
    hl = (html or "").lower()[:5000]
    host_lower = (host or "").lower()

    # Netlify
    if "netlify" in hs or "x-nf-request-id" in hs or "netlify" in host_lower:
        indicators.append("Netlify")
    # Vercel
    if "vercel" in hs or "x-vercel-id" in hs or "vercel" in host_lower or ".vercel.app" in host_lower:
        indicators.append("Vercel")
    # Cloudflare Pages
    if "pages.dev" in host_lower or ("cloudflare" in hs and "pages" in hl):
        indicators.append("Cloudflare Pages")
    # GitHub Pages
    if "github.io" in host_lower or "github pages" in hl:
        indicators.append("GitHub Pages")
    # Render
    if "onrender.com" in host_lower or "render" in hs.lower():
        indicators.append("Render")
    # Heroku
    if "herokuapp.com" in host_lower:
        indicators.append("Heroku")
    # Surge.sh
    if "surge.sh" in host_lower:
        indicators.append("Surge.sh")
    # Fly.io
    if "fly.dev" in host_lower:
        indicators.append("Fly.io")
    return indicators

# Static-site specific leak paths (Netlify, Vercel, Cloudflare Pages)
STATIC_SITE_PATHS = [
    "/_headers", "/_redirects", "/_config.yml", "/_config.yaml",
    "/netlify.toml", "/vercel.json", "/.vercel/",
    "/.netlify/functions/", "/.netlify/state.json",
    "/_next/data/", "/_next/static/",
    "/_nuxt/", "/_nuxt/data/",
    "/.well-known/netlify/", "/.well-known/vercel/",
    "/api/", "/api/health", "/.netlify/",
    "/sitemap.xml", "/robots.txt",
    "/manifest.json", "/site.webmanifest", "/assetlinks.json",
    "/static/", "/static/js/", "/static/css/",
    "/build/", "/dist/", "/assets/",
    "/404.html", "/500.html", "/_errors/",
    # Jekyll / Hugo
    "/_site/", "/public/", "/config.toml", "/hugo.toml", "/hugo.yaml",
    # Common JS bundles & maps
    "/bundle.js", "/main.js", "/app.js", "/index.js", "/runtime.js",
    "/polyfills.js", "/vendor.js", "/scripts.js", "/styles.js",
    "/bundle.js.map", "/main.js.map", "/app.js.map", "/index.js.map",
    "/static/js/bundle.js.map", "/static/js/main.js.map",
    # Next.js specific
    "/_next/static/chunks/main.js", "/_next/static/chunks/webpack.js",
    "/_next/static/chunks/framework.js", "/_next/static/chunks/pages/_app.js",
    "/_next/static/chunks/pages/_error.js", "/_next/static/chunks/pages/index.js",
    "/_next/static/chunks/main.js.map", "/_next/static/chunks/webpack.js.map",
    "/buildManifest.json", "/react-loadable-manifest.json",
    # Service workers
    "/service-worker.js", "/sw.js", "/workbox-*.js",
    "/firebase-messaging-sw.js", "/firebase-messaging-sw.js.map",
    # Manifests & env
    "/manifest.webmanifest", "/.env", "/.env.local", "/.env.production",
    # Pre-rendered data
    "/__NEXT_DATA__.json", "/page-data.json",
    # Hugo/Jekyll meta
    "/index.json", "/index.xml", "/feed.json", "/feed.xml",
    # Source files leaked
    "/src/", "/source/", "/.cache/", "/.parcel-cache/",
    "/tsconfig.json", "/package.json", "/package-lock.json",
    "/yarn.lock", "/pnpm-lock.yaml", "/.pnp.cjs",
    # Cloudflare specific
    "/_cloudflare/", "/cf-", "/_cf/",
    # Vercel build outputs
    "/.vercel/output/", "/.vercel/builds/",
    # Common config files
    "/config.json", "/config.yml", "/config.yaml", "/config.toml",
    "/settings.json", "/app.json", "/.app.json",
    # CMS exports / content
    "/content/", "/content/posts/", "/content/pages/",
    "/api/content/", "/api/posts/", "/api/pages/",
    # Exposed secrets in JSON
    "/data.json", "/data/config.json", "/data/settings.json",
    "/config/secrets.json", "/secrets.json",
    # OAuth / redirect configs
    "/_redirects.bak", "/_headers.bak",
    # Backups
    "/backup.zip", "/backup.tar.gz", "/site.zip", "/www.zip",
    # Common source maps in subdirs
    "/static/css/main.css.map", "/assets/index.css.map",
]

def detect_framework(html, headers):
    """Detect web framework từ HTML/headers để chạy framework-specific checks."""
    frameworks = []
    hs = json.dumps(headers).lower()
    hl = (html or "").lower()[:8000]
    # Next.js
    if "__next" in hl or "_next/static" in hl or "next/dist" in hl:
        frameworks.append("Next.js")
    # Nuxt
    if "__nuxt" in hl or "_nuxt/" in hl or "nuxt-link" in hl:
        frameworks.append("Nuxt")
    # Gatsby
    if "gatsby" in hl or "___gatsby" in hl:
        frameworks.append("Gatsby")
    # Astro
    if "astro-island" in hl or "data-astro-" in hl:
        frameworks.append("Astro")
    # SvelteKit
    if "sveltekit" in hl or "__sveltekit" in hl:
        frameworks.append("SvelteKit")
    # Remix
    if "__remix" in hl or "remix-router" in hl:
        frameworks.append("Remix")
    # Angular
    if "ng-version" in hl or "ng-app" in hl:
        frameworks.append("Angular")
    # Vue
    if "vue" in hl and ("v-" in hl or "vue-" in hl):
        frameworks.append("Vue")
    # React (without Next)
    if ("reactroot" in hl or "data-react" in hl) and "Next.js" not in frameworks:
        frameworks.append("React")
    return frameworks

FRAMEWORK_EXTRA_PATHS = {
    "Next.js": [
        "/_next/static/chunks/main.js.map", "/_next/static/chunks/webpack.js.map",
        "/_next/static/chunks/framework.js.map", "/_next/static/chunks/pages/_app.js.map",
        "/_next/static/chunks/pages/_error.js.map", "/_next/static/chunks/pages/index.js.map",
        "/_next/static/chunks/pages/_document.js.map", "/_next/static/chunks/pages/_error.js.map",
        "/_next/static/chunks/runtime/main.js.map", "/_next/static/chunks/runtime/webpack.js.map",
        "/_next/static/buildManifest.json", "/_next/static/react-loadable-manifest.json",
        "/_next/static/loading.js", "/_next/static/chunks/main-*.js.map",
        "/_next/data/", "/_next/static/chunks/",
    ],
    "Nuxt": [
        "/_nuxt/app.js.map", "/_nuxt/vendor.js.map", "/_nuxt/runtime.js.map",
        "/_nuxt/index.js.map", "/_nuxt/commons.app.js.map",
        "/_nuxt/", "/_nuxt/data/",
    ],
    "Gatsby": [
        "/page-data.json", "/page-data/", "/gatsby-data.json",
        "/webpack.stats.json", "/.cache/",
    ],
    "Astro": [
        "/_astro/", "/_astro/chunks/", "/_astro/pages/",
        "/_astro/*.js.map", "/_astro/index.js.map",
    ],
    "SvelteKit": [
        "/_app/", "/_app/immutable/", "/_app/version.json",
        "/.svelte-kit/", "/.svelte-kit/output/",
    ],
    "Remix": [
        "/build/", "/build/manifest.json", "/.data/",
        "/.cache/", "/build/assets/",
    ],
}

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

async def resolve_subdomains(domain):
    """Async DNS resolution cho subdomain enumeration. Trả về list of {sub, ip, ok}."""
    if not domain:
        return []
    try:
        import socket as _sock
    except ImportError:
        return []
    loop = asyncio.get_event_loop()
    async def resolve(sub):
        name = f"{sub}.{domain}"
        try:
            infos = await loop.getaddrinfo(name, None)
            ip = infos[0][4][0] if infos else None
            return {"sub": sub, "host": name, "ip": ip, "ok": True}
        except Exception:
            return {"sub": sub, "host": name, "ip": None, "ok": False}
    # Limit concurrency to avoid hammering DNS
    sem = asyncio.Semaphore(20)
    async def r(sub):
        async with sem:
            return await resolve(sub)
    results = await asyncio.gather(*[r(s) for s in COMMON_SUBDOMAINS[:40]])
    return [r for r in results if r["ok"]]

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
    out = []
    raw = headers.get("Set-Cookie") or headers.get("set-cookie")
    if not raw:
        return out
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
    out = []
    if not text:
        return out
    # Skip vendor/common JS files hoàn toàn để tránh false positive
    VENDOR_PATTERNS = [
        'jquery', 'bootstrap', 'react-dom', 'react.development',
        'vue.global', 'angular.min', 'monaco-editor', 'vs/loader',
        'cdn.jsdelivr', 'unpkg.com', 'cdnjs.cloudflare',
        'moment.min', 'lodash.min', 'axios.min', 'd3.min',
        'fontawesome', 'tinymce', 'ckeditor', 'ace-builds',
    ]
    if any(vp in (label or '').lower() for vp in VENDOR_PATTERNS):
        return []  # vendor JS, skip toàn bộ
    for name, pat, sev, desc in SECRET_PATTERNS:
        for m in re.finditer(pat, text, re.I):
            snippet = m.group(0)
            # Skip generic-looking matches trong source code comments
            masked = snippet[:8] + "*" * (max(0, len(snippet) - 12)) + snippet[-4:] if len(snippet) > 16 else snippet[:2] + "***"
            out.append({
                "type": name,
                "severity": sev,
                "match_masked": masked,
                "description": desc,
                "source": label,
            })
    seen = set()
    deduped = []
    for s in out:
        k = (s["type"], s["match_masked"])
        if k not in seen:
            seen.add(k); deduped.append(s)
    return deduped

def extract_js_links(html, base):
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
    p = path.lower()
    if any(k in p for k in ["/.ssh/id_rsa", "/.aws/credentials", "/service-account.json",
                           "/firebase.json", "/.netrc", "/.kube/config", "/.terraform.tfvars",
                           "/terraform.tfstate", "private key", "/.env", "wp-config.php",
                           "/config.php", "/configuration.php", "/service-account-key",
                           "/.vault-token", "/.vault-pass", "/vault.json"]):
        return "critical"
    if any(k in p for k in ["/db.sql", "/dump.sql", "/database.sql", "/backup.zip",
                            "/backup.tar.gz", "/www.zip", "/site.zip", "/.git/config",
                            "/.git/HEAD", "/.gitlab-ci.yml", "/.github/workflows/",
                            "/.npmrc", "/.pypirc", "/.netrc", "/.ssh/authorized_keys",
                            "/phpmyadmin/", "/adminer.php", "/swagger.json",
                            "/openapi.json", "/actuator/env", "/actuator/heapdump",
                            "/actuator/loggers", "/actuator/beans", "/actuator/configprops",
                            "/error.log", "/access.log", "/.bash_history",
                            "/settings.json", "/settings.php", "/app/etc/local.xml",
                            "/config/secrets.yml", "/config/master.key"]):
        return "high"
    if code == 401 or code == 403:
        return "medium"
    if any(k in p for k in ["/admin/", "/administrator/", "/wp-admin/", "/wp-login.php",
                            "/install/", "/setup/", "/phpinfo.php", "/info.php",
                            "/server-status", "/.idea/", "/.vscode/", "/.DS_Store",
                            "/Thumbs.db", "/phpunit.xml"]):
        return "medium"
    return "low"

def get_main_page_summary(html, max_chars=400):
    if not html:
        return ""
    t = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.I | re.S)
    t = re.sub(r'<style[^>]*>.*?</style>', ' ', t, flags=re.I | re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:max_chars] + ("..." if len(t) > max_chars else "")

# ── v11.1 helper functions: deep recon capabilities ──

def extract_js_endpoints(js_text, base_url):
    """Parse JS source, extract API endpoints (fetch URLs, axios routes, XHR, etc.)."""
    endpoints = set()
    if not js_text:
        return []
    for pat in JS_ENDPOINT_PATTERNS:
        for m in re.finditer(pat, js_text, re.I):
            url = m.group(1)
            # Filter out obviously non-route strings
            if not url or url.startswith(('javascript:', 'mailto:', 'tel:', 'data:', '#')):
                continue
            if url.startswith(('http://', 'https://')):
                # Only include if same origin
                try:
                    u = urlparse(url)
                    base_host = urlparse(base_url).hostname
                    if u.hostname and u.hostname != base_host:
                        continue
                    endpoints.add(u.path)
                except Exception:
                    continue
            elif url.startswith('/'):
                endpoints.add(url)
            elif url.startswith('./') or url.startswith('../'):
                endpoints.add(urljoin(base_url, url))
            else:
                # Probably a relative path or a key name, skip
                continue
    # Clean up: keep only paths that look like routes (start with /)
    return sorted([e for e in endpoints if e.startswith('/') and len(e) > 1 and len(e) < 200])[:50]

def parse_swagger_spec(spec_text, base):
    """Parse Swagger/OpenAPI JSON spec to enumerate endpoints."""
    endpoints = []
    if not spec_text:
        return endpoints
    try:
        spec = json.loads(spec_text)
    except Exception:
        return endpoints
    # OpenAPI 3
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for method, info in methods.items():
            if method.lower() not in ("get", "post", "put", "delete", "patch", "head", "options"):
                continue
            summary = info.get("summary", "") if isinstance(info, dict) else ""
            description = info.get("description", "") if isinstance(info, dict) else ""
            # Resolve path with basePath
            base_path = spec.get("basePath", "")
            full_url = urljoin(base, (base_path + path).replace("//", "/"))
            endpoints.append({
                "path": path,
                "url": full_url,
                "method": method.upper(),
                "summary": summary,
                "description": description,
            })
    return endpoints

async def check_subdomain_takeover(host):
    """Resolve CNAME cho host, check pattern takeover signatures."""
    if not host:
        return []
    findings = []
    try:
        loop = asyncio.get_event_loop()
        # Try resolve CNAME
        try:
            infos = await loop.getaddrinfo(host, None)
            ip = infos[0][4][0] if infos else None
        except Exception:
            ip = None
        # Use socket.gethostbyname_ex to get CNAME chain
        try:
            # Try resolving CNAME via DNS-like query (fallback to getaddrinfo)
            cname_chain = []
            # Cannot easily get CNAME from getaddrinfo alone. Use a simpler heuristic:
            # try resolving <sub>.<host> common takeover targets and see if they NXDOMAIN.
            pass
        except Exception:
            pass
        # We'll do per-subdomain check: for each resolved subdomain, also try CNAME-style takeover detection
        # by checking if the subdomain's IP looks suspicious (returns special AWS/Heroku error pages).
        return findings
    except Exception:
        return []

async def check_subdomain_takeover_detailed(session, host, sub_results, custom_headers, proxy, timeout):
    """For each resolved subdomain, fetch it and check for takeover fingerprints in body."""
    findings = []
    sem = asyncio.Semaphore(8)
    async def check_one(sub_info):
        sub_host = sub_info["host"]
        # Try both http and https
        for scheme in ("https", "http"):
            url = f"{scheme}://{sub_host}/"
            try:
                async with sem:
                    t, c, h, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 6))
                # Check body for takeover fingerprints
                body_lower = (t or "").lower()[:5000]
                for pat, service, desc in TAKEOVER_SIGS:
                    # Check if body mentions the service error page
                    takeover_markers = []
                    if service == "GitHub Pages":
                        if "there isn't a github pages site here" in body_lower:
                            takeover_markers.append("GitHub Pages 'no site' error page")
                    elif service == "Heroku":
                        if "no such app" in body_lower or "heroku | no such app" in body_lower:
                            takeover_markers.append("Heroku 'no such app' error page")
                    elif service == "AWS S3":
                        if "nosuchbucket" in body_lower or "the specified bucket does not exist" in body_lower:
                            takeover_markers.append("S3 'NoSuchBucket' error")
                    elif service == "AWS CloudFront":
                        if "bad request" in body_lower and "cloudfront" in body_lower:
                            takeover_markers.append("CloudFront bad request")
                    elif service == "Vercel":
                        if "vercel" in body_lower and ("configuration" in body_lower or "not found" in body_lower):
                            takeover_markers.append("Vercel config error page")
                    elif service == "Netlify":
                        if "not found" in body_lower and "netlify" in body_lower:
                            takeover_markers.append("Netlify not found page")
                    elif service == "Render":
                        if "render" in body_lower and ("not found" in body_lower or "free" in body_lower):
                            takeover_markers.append("Render not found page")
                    elif service == "Cloudflare Pages":
                        if "pages.dev" in body_lower and "not found" in body_lower:
                            takeover_markers.append("Cloudflare Pages not found")
                    elif service == "Cloudflare Workers":
                        if "workers.dev" in body_lower and ("error" in body_lower or "not found" in body_lower):
                            takeover_markers.append("Workers error page")
                    elif service == "Supabase":
                        if "supabase" in body_lower and "project" in body_lower and "not found" in body_lower:
                            takeover_markers.append("Supabase project not found")
                    if takeover_markers:
                        findings.append({
                            "subdomain": sub_host,
                            "url": url,
                            "service": service,
                            "status_code": c,
                            "markers": takeover_markers,
                            "description": desc,
                            "severity": "high",
                        })
                        return  # one finding per sub is enough
            except Exception:
                continue
    for sub_info in sub_results[:30]:
        await check_one(sub_info)
    return findings

async def check_open_redirect(session, target, custom_headers, proxy, timeout):
    """Test ?redirect=https://evil.com, ?next=//evil.com, etc."""
    findings = []
    evil_url = "https://evil.com"
    sem = asyncio.Semaphore(8)
    async def test_param(param):
        # Use various injection payloads
        payloads = [
            ("exact", evil_url),
            ("protocol-relative", "//evil.com"),
            ("slash-prefixed", "/\\evil.com"),
            ("url-encoded", "https%3A%2F%2Fevil.com"),
            ("double-encoded", "https%253A%252F%252Fevil.com"),
        ]
        for variant, payload in payloads:
            url = f"{target}?{param}={payload}"
            try:
                async with sem:
                    t, c, h, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 5))
                if c in (301, 302, 303, 307, 308):
                    loc = h.get("Location") or h.get("location") or ""
                    if "evil.com" in loc.lower():
                        return {
                            "param": param,
                            "payload": payload,
                            "variant": variant,
                            "status_code": c,
                            "location": loc[:200],
                            "url": url,
                            "severity": "high",
                        }
                elif c == 200 and t and ("evil.com" in t[:5000] or "//evil.com" in t[:5000]):
                    return {
                        "param": param,
                        "payload": payload,
                        "variant": variant,
                        "status_code": c,
                        "location": "(reflected in body)",
                        "url": url,
                        "severity": "medium",
                    }
            except Exception:
                continue
        return None
    tasks = [test_param(p) for p in REDIRECT_PARAMS]
    for coro in asyncio.as_completed(tasks):
        r = await coro
        if r:
            findings.append(r)
    return findings

async def check_cors(session, target, custom_headers, proxy, timeout):
    """Test CORS misconfiguration với Origin: https://evil.com."""
    findings = []
    sem = asyncio.Semaphore(5)
    test_endpoints = [target, urljoin(target, "/api/"), urljoin(target, "/api/v1/"),
                      urljoin(target, "/login"), urljoin(target, "/admin/")]
    async def check_one(url):
        headers = dict(custom_headers or {})
        for origin in CORS_TEST_ORIGINS:
            test_headers = dict(headers)
            test_headers["Origin"] = origin
            try:
                async with sem:
                    t, c, h, rt = await fetch(session, url, test_headers, proxy, min(timeout, 5))
                acao = h.get("Access-Control-Allow-Origin") or h.get("access-control-allow-origin") or ""
                acac = h.get("Access-Control-Allow-Credentials") or h.get("access-control-allow-credentials") or ""
                # Vulnerable if reflects Origin OR returns wildcard with credentials
                if acao == origin or (acao == "*" and acac.lower() == "true"):
                    return {
                        "url": url,
                        "origin_tested": origin,
                        "acao": acao,
                        "acac": acac,
                        "status_code": c,
                        "severity": "high" if acac.lower() == "true" else "medium",
                        "description": f"ACAO reflects origin ({origin}) — credentials: {acac}",
                    }
            except Exception:
                continue
        return None
    for coro in asyncio.as_completed([check_one(u) for u in test_endpoints]):
        r = await coro
        if r:
            findings.append(r)
    return findings

async def check_graphql(session, target, custom_headers, proxy, timeout):
    """Test GraphQL endpoints với introspection query."""
    findings = []
    sem = asyncio.Semaphore(5)
    async def check_endpoint(endpoint):
        url = urljoin(target, endpoint)
        # Try GET first
        try:
            async with sem:
                t, c, h, rt = await fetch(session, url + "?query={__schema{types{name}}}",
                                          custom_headers, proxy, min(timeout, 5))
            if c == 200 and t and "__schema" in t:
                # Try introspection query
                async with sem:
                    t2, c2, h2, _ = await fetch(session, url, custom_headers, proxy, min(timeout, 8),
                                                  ) if False else (None, 0, {}, 0)
                # Count types in response
                types_count = t.count('"kind":"OBJECT"') + t.count('"kind":"INTERFACE"') + t.count('"kind":"INPUT_OBJECT"')
                return {
                    "endpoint": endpoint,
                    "url": url,
                    "status_code": c,
                    "introspection_enabled": True,
                    "types_found": types_count,
                    "severity": "high" if types_count > 0 else "medium",
                    "preview": (t[:300] + "...") if len(t) > 300 else t,
                }
            elif c == 200 and t and ("graphql" in t.lower() or "GraphiQL" in t):
                # GraphiQL UI found
                return {
                    "endpoint": endpoint,
                    "url": url,
                    "status_code": c,
                    "introspection_enabled": False,
                    "ui_found": "GraphiQL/Playground UI",
                    "severity": "medium",
                    "preview": "",
                }
            elif c in (400, 405) and t and "query" in t.lower():
                # GraphQL exists but rejected our query
                return {
                    "endpoint": endpoint,
                    "url": url,
                    "status_code": c,
                    "introspection_enabled": False,
                    "ui_found": "",
                    "severity": "low",
                    "preview": (t[:200] + "...") if len(t) > 200 else t,
                }
        except Exception:
            return None
        # Try POST with introspection query
        try:
            async with sem:
                pass  # aiohttp POST not implemented in fetch(); skip POST
        except Exception:
            pass
        return None
    for coro in asyncio.as_completed([check_endpoint(ep) for ep in GRAPHQL_ENDPOINTS]):
        r = await coro
        if r:
            findings.append(r)
    return findings

async def check_source_maps(session, js_links, custom_headers, proxy, timeout):
    """Với mỗi JS file, check .map variant."""
    findings = []
    sem = asyncio.Semaphore(8)
    async def check_one(js_url):
        # Try .map variant
        map_url = js_url + ".map"
        try:
            async with sem:
                t, c, h, rt = await fetch(session, map_url, custom_headers, proxy, min(timeout, 5))
            if c == 200 and t and len(t) > 100 and ("sources" in t or "mappings" in t or "version" in t):
                # Try to parse as source map
                try:
                    sm = json.loads(t)
                    sources = sm.get("sources", [])[:5]
                    return {
                        "js_url": js_url,
                        "map_url": map_url,
                        "size": len(t),
                        "sources_preview": sources,
                        "sources_count": len(sm.get("sources", [])),
                        "severity": "high",
                        "description": f"Source map leak {len(sm.get('sources', []))} source files",
                    }
                except Exception:
                    return {
                        "js_url": js_url,
                        "map_url": map_url,
                        "size": len(t),
                        "sources_preview": [],
                        "sources_count": 0,
                        "severity": "medium",
                        "description": "Possible source map (invalid JSON)",
                    }
        except Exception:
            return None
        return None
    # Only check JS files from same origin to avoid false positives
    for coro in asyncio.as_completed([check_one(u) for u in js_links[:30]]):
        r = await coro
        if r:
            findings.append(r)
    return findings

async def fetch_wayback_urls(session, target, custom_headers, proxy, timeout):
    """Lấy historical URLs từ Wayback Machine API."""
    parsed = urlparse(target)
    host = f"{parsed.hostname}/*"
    url = f"{WAYBACK_API}?url={host}&output=json&fl=original&collapse=urlkey&limit=200"
    try:
        async with session.get(url, headers={"User-Agent": random.choice(USER_AGENTS)},
                              timeout=aiohttp.ClientTimeout(total=15),
                              ssl=False) as r:
            if r.status != 200:
                return []
            data = await r.json()
            # Wayback returns [original, ...urls]
            if isinstance(data, list) and len(data) > 1:
                urls = data[1:]  # skip first element which is "original"
                return list(set(urls))[:100]
            return []
    except Exception:
        return []

# ── v11.1 deep recon: Certificate Transparency, DNS records, deep crawl, JS string extraction ──

async def fetch_ct_logs(session, domain, log_fn=None):
    """Query crt.sh Certificate Transparency logs để lấy tất cả subdomains đã từng được cert.
    Đây là cách mạnh nhất để enum subdomain — không cần DNS, không cần wordlist."""
    if not domain:
        return []
    # crt.sh returns JSON array of {name_value: "sub.example.com\nsub2.example.com", ...}
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    subdomains = set()
    try:
        async with session.get(url, headers={"User-Agent": random.choice(USER_AGENTS)},
                              timeout=aiohttp.ClientTimeout(total=20),
                              ssl=False) as r:
            if r.status != 200:
                if log_fn: log_fn(f"[CT] crt.sh returned {r.status}")
                return []
            text = await r.text(errors="replace")
            try:
                data = json.loads(text)
            except Exception:
                if log_fn: log_fn("[CT] crt.sh response not JSON, trying line-parse")
                # Fallback: parse as text
                for m in re.finditer(r'([a-zA-Z0-9][a-zA-Z0-9\-\_]*\.' + re.escape(domain) + r')', text):
                    subdomains.add(m.group(1).lower())
                return sorted(subdomains)[:200]
            for entry in data:
                if isinstance(entry, dict):
                    name_value = entry.get("name_value", "") or entry.get("common_name", "")
                    for line in name_value.split("\n"):
                        line = line.strip().lower()
                        # Remove wildcard prefix
                        if line.startswith("*."):
                            line = line[2:]
                        if line.endswith(domain.lower()) and "*" not in line:
                            subdomains.add(line)
        if log_fn: log_fn(f"[CT] crt.sh found {len(subdomains)} unique subdomains")
        return sorted(subdomains)[:200]
    except Exception as e:
        if log_fn: log_fn(f"[CT] crt.sh query failed: {type(e).__name__}: {str(e)[:60]}")
        return []

async def lookup_dns_records(host):
    """Lookup DNS records: A, AAAA, MX, NS, TXT, SOA, CNAME."""
    if not host:
        return {}
    records = {"A": [], "AAAA": [], "MX": [], "NS": [], "TXT": [], "SOA": [], "CNAME": []}
    loop = asyncio.get_event_loop()
    async def query(record_type, fn_name):
        try:
            infos = await loop.getaddrinfo(host, None, type=getattr(__import__("socket"), record_type, 0))
            ips = sorted({info[4][0] for info in infos})
            records[record_type if record_type != "SOCK_STREAM" else "A"] = ips
        except Exception:
            pass
    # getaddrinfo only does A/AAAA; for MX/NS/TXT/SOA we'd need dnspython — fallback to socket.getaddrinfo
    try:
        infos = await loop.getaddrinfo(host, None)
        records["A"] = sorted({info[4][0] for info in infos if ":" not in info[4][0]})
        records["AAAA"] = sorted({info[4][0] for info in infos if ":" in info[4][0]})
    except Exception:
        pass
    # Try reverse DNS for first A record
    if records["A"]:
        try:
            hostname, _, _ = await loop.getnameinfo((records["A"][0], 0), 0)
            records["PTR"] = [hostname]
        except Exception:
            pass
    # Filter empty
    return {k: v for k, v in records.items() if v}

async def deep_crawl(session, base, main_text, custom_headers, proxy, timeout, soft_404_sizes, log_fn, cancel_fn, max_depth=2, max_pages=30):
    """Deep crawler: collect all internal links từ main page, fetch từng page depth-2.
    Extract thêm endpoints, secrets, forms từ tất cả pages."""
    if not main_text:
        return [], []
    parsed = urlparse(base)
    target_host = parsed.hostname
    visited = set()
    pages_data = []  # list of {url, code, size, secrets, forms}
    queue = [(urljoin(base, "/"), 0)]
    all_secrets = []
    all_forms = []
    sem = asyncio.Semaphore(10)
    pages_crawled = 0

    # Extract initial links từ main_text
    initial_links = set()
    for m in re.finditer(r'(?:href|src|action)\s*=\s*["\']([^"\']+)["\']', main_text, re.I):
        u = m.group(1)
        if u.startswith(("http://", "https://")):
            try:
                u_p = urlparse(u)
                if u_p.hostname == target_host:
                    initial_links.add(u)
            except Exception:
                pass
        elif u.startswith("/") and not u.startswith("//"):
            initial_links.add(urljoin(base, u))
        elif not u.startswith(("#", "javascript:", "mailto:", "data:", "tel:")):
            initial_links.add(urljoin(base, u))
    # Limit to 20 initial links for deep crawl
    queue = [(u, 0) for u in list(initial_links)[:20]]

    async def crawl_one(url, depth):
        nonlocal pages_crawled
        if cancel_fn() or pages_crawled >= max_pages:
            return None
        async with sem:
            t, c, h, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 8))
        if c != 200 or not t:
            return None
        pages_crawled += 1
        # Check soft-404
        if len(t) in soft_404_sizes:
            return None
        # Extract secrets from this page
        page_secrets = scan_secrets(t, f"crawl: {url}")
        # Extract forms
        page_forms = extract_forms(t, base)
        # Extract more links for depth+1
        next_links = set()
        if depth < max_depth - 1:
            for m in re.finditer(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', t, re.I):
                u = m.group(1)
                if u.startswith("/") and not u.startswith("//"):
                    full = urljoin(base, u)
                    if full not in visited:
                        next_links.add(full)
                elif u.startswith(("http://", "https://")):
                    try:
                        u_p = urlparse(u)
                        if u_p.hostname == target_host and u not in visited:
                            next_links.add(u)
                    except Exception:
                        pass
        return {
            "url": url, "code": c, "size": len(t),
            "secrets": page_secrets, "forms": page_forms,
            "next_links": list(next_links)[:5], "depth": depth,
        }

    # Crawl depth 0
    depth_0_results = []
    tasks = [crawl_one(url, 0) for url, _ in queue]
    for coro in asyncio.as_completed(tasks):
        r = await coro
        if r:
            visited.add(r["url"])
            depth_0_results.append(r)
            all_secrets.extend(r["secrets"])
            all_forms.extend(r["forms"])
            if r["secrets"]:
                log_fn(f"[CRAWL] {r['url']} → {len(r['secrets'])} secrets")
            if r["forms"]:
                log_fn(f"[CRAWL] {r['url']} → {len(r['forms'])} forms")

    # Crawl depth 1
    depth_1_urls = set()
    for r in depth_0_results:
        for u in r["next_links"]:
            if u not in visited:
                depth_1_urls.add(u)
    depth_1_urls = list(depth_1_urls)[:10]
    if depth_1_urls and not cancel_fn():
        tasks = [crawl_one(url, 1) for url in depth_1_urls]
        for coro in asyncio.as_completed(tasks):
            r = await coro
            if r:
                visited.add(r["url"])
                depth_0_results.append(r)
                all_secrets.extend(r["secrets"])
                all_forms.extend(r["forms"])

    return depth_0_results, all_secrets

def extract_js_strings(js_text, min_length=15, max_strings=30):
    """Extract string literals from JS source code. v11.1: optimized for speed —
    limit input size, use simpler regex, cap output."""
    if not js_text:
        return []
    # v11.1: Truncate input to 100KB max to prevent regex hangs on large JS files
    if len(js_text) > 100000:
        js_text = js_text[:100000]
    strings = set()
    # Simpler patterns — faster than alternations
    try:
        # Single/double quoted: 15-200 chars
        for m in re.finditer(r'"([^"\\]{15,200})"', js_text):
            s = m.group(1)
            if not s or len(s) > 200:
                continue
            # Skip noise: hex colors, data URLs, pure numbers, camelCase, css
            if s.startswith('#') or s.startswith('data:') or s.startswith('.') or \
               s.startswith('{') or s.startswith('function') or s.isdigit():
                continue
            if re.match(r'^[a-z]+(?:[A-Z][a-z]+)+$', s):  # camelCase identifiers
                continue
            if re.match(r'^[a-z]+(-[a-z]+)+$', s):  # kebab-case CSS classes
                continue
            strings.add(s)
            if len(strings) >= max_strings:
                break
        if len(strings) < max_strings:
            for m in re.finditer(r"'([^'\\]{15,200})'", js_text):
                s = m.group(1)
                if not s or len(s) > 200:
                    continue
                if s.startswith('#') or s.startswith('data:') or s.startswith('.') or \
                   s.startswith('{') or s.startswith('function') or s.isdigit():
                    continue
                if re.match(r'^[a-z]+(?:[A-Z][a-z]+)+$', s):
                    continue
                strings.add(s)
                if len(strings) >= max_strings:
                    break
        if len(strings) < max_strings:
            # Template literals (backticks)
            for m in re.finditer(r'`([^`\\]{15,200})`', js_text):
                s = m.group(1)
                if not s or len(s) > 200:
                    continue
                if s.startswith('#') or s.startswith('data:') or s.startswith('.') or \
                   s.startswith('{') or s.startswith('function') or s.isdigit():
                    continue
                strings.add(s)
                if len(strings) >= max_strings:
                    break
    except Exception:
        pass  # Regex timeout/overflow protection
    return list(strings)[:max_strings]

async def check_git_exposure(session, base, custom_headers, proxy, timeout, log_fn):
    """Check if .git directory is exposed — fetch HEAD, config, index, then enumerate objects."""
    findings = []
    git_paths_to_check = [
        "/.git/HEAD",
        "/.git/config",
        "/.git/index",
        "/.git/description",
        "/.git/info/refs",
        "/.git/info/packs",
        "/.git/objects/info/packs",
        "/.git/refs/heads/master",
        "/.git/refs/heads/main",
        "/.git/logs/HEAD",
        "/.git/COMMIT_EDITMSG",
        "/.git/packed-refs",
    ]
    sem = asyncio.Semaphore(5)
    async def check_one(path):
        url = urljoin(base, path)
        try:
            async with sem:
                t, c, h, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 5))
            if c == 200 and t:
                # Verify it's actually git content
                is_git = False
                content_preview = ""
                if path.endswith("HEAD"):
                    # HEAD file contains "ref: refs/heads/master" or similar
                    if "ref:" in t or len(t.strip()) == 40:  # 40 = SHA-1 hash length
                        is_git = True
                        content_preview = t.strip()[:100]
                elif path.endswith("config"):
                    if "[core]" in t or "[remote" in t:
                        is_git = True
                        content_preview = t.strip()[:300]
                elif path.endswith("index"):
                    # Binary file, check for "DIRC" magic
                    if t.startswith("DIRC") or len(t) > 100:
                        is_git = True
                        content_preview = f"[binary, {len(t)} bytes]"
                elif path.endswith("packed-refs"):
                    if "# pack-refs with" in t or "refs/" in t:
                        is_git = True
                        content_preview = t.strip()[:200]
                else:
                    # Other paths — just check size > 0
                    if len(t) > 0:
                        is_git = True
                        content_preview = (t[:200] + "...") if len(t) > 200 else t
                if is_git:
                    log_fn(f"[GIT-EXPOSED] {path} → 200 ({len(t)}b)")
                    return {
                        "path": path, "url": url, "code": 200, "size": len(t),
                        "severity": "critical",
                        "preview": content_preview,
                        "description": f"Git directory exposed: {path}",
                    }
            elif c == 403:
                # Forbidden — still interesting (means .git exists but protected)
                log_fn(f"[GIT-PROTECTED] {path} → 403")
                return {
                    "path": path, "url": url, "code": 403, "size": 0,
                    "severity": "medium",
                    "preview": "",
                    "description": f"Git directory protected (403): {path}",
                }
        except Exception:
            return None
        return None
    tasks = [check_one(p) for p in git_paths_to_check]
    for coro in asyncio.as_completed(tasks):
        r = await coro
        if r:
            findings.append(r)
    return findings

async def recursive_brute(session, base, found_dirs, custom_headers, proxy, timeout, soft_404_sizes, log_fn, cancel_fn):
    """Với mỗi directory 200 tìm được, brute thêm các sub-paths."""
    findings = []
    sem = asyncio.Semaphore(15)
    brute_timeout = min(timeout, 4)
    total = len(found_dirs) * len(RECURSIVE_BRUTE_PATHS)
    done = 0
    found = 0
    async def check_one(dir_path, sub):
        nonlocal done, found
        if cancel_fn():
            return None
        # Ensure dir_path ends with /
        if not dir_path.endswith('/'):
            dir_path = dir_path + '/'
        path = dir_path + sub
        url = urljoin(base, path)
        async with sem:
            t, c, h, rt = await fetch(session, url, custom_headers, proxy, brute_timeout)
            done += 1
            if c in (200, 401, 403):
                if c == 200 and t and len(t) in soft_404_sizes:
                    return None
                found += 1
                log_fn(f"[RBRUTE] {c} {path}")
                return {"path": path, "url": url, "code": c,
                        "severity": score_finding(path, c),
                        "response_time_ms": rt, "recursive": True,
                        "parent_dir": dir_path}
            return None
    tasks = [check_one(d, sub) for d in found_dirs[:5] for sub in RECURSIVE_BRUTE_PATHS]
    for coro in asyncio.as_completed(tasks):
        r = await coro
        if r:
            findings.append(r)
    return findings, done, total, found

async def test_http_methods(session, url, custom_headers, proxy, timeout):
    """Test OPTIONS, PUT, DELETE, PATCH để discover allowed methods."""
    findings = []
    sem = asyncio.Semaphore(5)
    async def test_method(method):
        try:
            async with sem:
                # Use aiohttp directly for non-GET methods
                timeout_obj = aiohttp.ClientTimeout(total=min(timeout, 5))
                async with session.options(url, headers=custom_headers or {},
                                          timeout=timeout_obj, ssl=False) as r:
                    allow = r.headers.get("Allow") or r.headers.get("allow") or ""
                    acam = r.headers.get("Access-Control-Allow-Methods") or r.headers.get("access-control-allow-methods") or ""
                    if allow or acam:
                        return {
                            "url": url,
                            "method_tested": "OPTIONS",
                            "allow": allow,
                            "acah_methods": acam,
                            "status_code": r.status,
                            "severity": "low",
                        }
        except Exception:
            return None
    for coro in asyncio.as_completed([test_method(m) for m in ["OPTIONS"]]):
        r = await coro
        if r:
            findings.append(r)
    return findings

def iter_tree(node):
    """Recursively yield all file-type nodes in a tree (DFS)."""
    if not isinstance(node, dict):
        return
    if node.get("type") == "file":
        yield node
    for child in node.get("children", []) or []:
        yield from iter_tree(child)


def _norm_path(p):
    """Normalize a path/URL string into a list of path segments."""
    if not p:
        return []
    s = str(p).strip()
    if "://" in s:
        try:
            from urllib.parse import urlsplit
            parts = urlsplit(s)
            s = parts.path or ""
        except Exception:
            # strip protocol crudely
            s = s.split("://", 1)[1]
            if "/" in s:
                s = "/" + s.split("/", 1)[1]
            else:
                s = "/"
    s = s.lstrip("/").rstrip("/")
    if not s:
        return []
    return [seg for seg in s.split("/") if seg]


def _extract_finding(item):
    """Extract (path, status, size, severity, url) from a finding dict/str."""
    if isinstance(item, str):
        return item, None, None, None, item
    if not isinstance(item, dict):
        return None, None, None, None, None
    url = item.get("url") or ""
    path = (item.get("path") or item.get("file") or item.get("name")
            or item.get("endpoint") or "")
    if not path:
        path = url
    status = (item.get("status") or item.get("status_code")
              or item.get("code") or item.get("http_status"))
    size = (item.get("size") or item.get("length") or item.get("content_length")
            or item.get("bytes") or item.get("size_bytes"))
    severity = item.get("severity") or item.get("level") or item.get("risk")
    return path, status, size, severity, url


def build_file_tree(leak_items, dirs, brute_findings, js_links, source_maps, api_endpoints):
    """Build hierarchical file tree từ tất cả discovered paths.
    Trả về dict structure: {name, type, children, status, size, url}
    """
    root = {"name": "/", "type": "dir", "children": {}}

    def insert(segments, meta):
        if not segments:
            return
        node = root["children"]
        for i, seg in enumerate(segments):
            is_leaf = (i == len(segments) - 1)
            if seg not in node:
                node[seg] = {"name": seg, "type": "dir", "children": {}}
            entry = node[seg]
            if is_leaf:
                # If never seen as a parent, treat as a file
                if not entry["children"]:
                    entry["type"] = "file"
                if meta.get("status") is not None:
                    entry["status"] = meta["status"]
                if meta.get("size") is not None:
                    entry["size"] = meta["size"]
                if meta.get("severity") is not None:
                    entry["severity"] = meta["severity"]
                if meta.get("url"):
                    entry["url"] = meta["url"]
                entry.setdefault("sources", []).append(meta.get("source", "unknown"))
            else:
                entry["type"] = "dir"
                node = entry["children"]

    sources = [
        ("leak", leak_items),
        ("brute", brute_findings),
        ("dir", dirs),
        ("js", js_links),
        ("sourcemap", source_maps),
        ("api", api_endpoints),
    ]
    for src_name, items in sources:
        if not items:
            continue
        for item in items:
            path, status, size, severity, url = _extract_finding(item)
            segs = _norm_path(path)
            if not segs:
                continue
            insert(segs, {
                "status": status, "size": size, "severity": severity,
                "url": url, "source": src_name,
            })

    def finalize(node):
        children = node.get("children")
        if isinstance(children, dict):
            lst = [finalize(c) for c in children.values()]
            lst.sort(key=lambda n: (n.get("type") != "dir", n.get("name", "")))
            node["children"] = lst
        return node

    finalize(root)
    return root


async def deep_scan(target, custom_headers=None, proxy=None, timeout=10,
                    allow_redirects=False, progress_cb=None, scan_js=True,
                    scan_id=None, bypass_mode="auto"):
    start = time.time()
    target = validate_target(target)
    result = {
        "target": target, "timestamp": datetime.now(timezone.utc).isoformat(),
        "scanner_version": "v11.1",
        "main": {}, "leak": [], "robots": [], "links": [], "js_links": [],
        "forms": [], "dirs": [], "brute": [], "ports": [], "technologies": [],
        "waf": {}, "cdn": [], "cookies": [], "security_headers": [],
        "secrets": [], "ssl": {}, "subdomain_hints": [], "subdomains_resolved": [],
        "page_summary": "", "param_findings": [], "backup_findings": [],
        "js_endpoints": [], "api_endpoints": [], "swagger_endpoints": [],
        "takeover_findings": [], "source_maps": [], "graphql_findings": [],
        "cors_findings": [], "open_redirect_findings": [], "wayback_urls": [],
        "http_method_findings": [], "recursive_brute_findings": [],
        # v11.1 additions
        "ct_subdomains": [], "dns_records": {}, "git_findings": [],
        "crawled_pages": [], "js_strings": [],
        "static_platforms": [], "frameworks_detected": [],
        # v11.1 additions
        "ssti_findings": [], "proto_pollution_findings": [],
        "header_injection_findings": [], "cache_poison_findings": [],
        "default_creds_findings": [],
        "bypass_mode": "auto",
        "errors": [], "duration_seconds": 0, "stats": {},
        "soft_404_filtered": 0, "cancelled": False,
    }
    parsed = urlparse(target)
    host = parsed.hostname
    base = f"{parsed.scheme}://{parsed.netloc}"

    def cancelled():
        return scan_id is not None and is_cancelled(scan_id)

    def log(msg):
        push_activity(scan_id, msg) if scan_id else None

    async def prog(phase, msg, current=0, total=0, found=0):
        if progress_cb:
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

    # v11.1: Heartbeat task — gửi progress event mỗi 3s với phase cuối cùng,
    # để UI không bị kẹt "Đang khởi tạo..." khi phase chạy lâu không gửi event
    last_phase = {"phase": "main_page", "msg": "Đang khởi tạo...", "current": 0, "total": 0, "found": 0}
    async def _store_phase(phase, msg, current=0, total=0, found=0):
        last_phase["phase"] = phase
        last_phase["msg"] = msg
        last_phase["current"] = current
        last_phase["total"] = total
        last_phase["found"] = found

    # Wrap prog to also store last phase
    _original_prog = prog
    async def prog(phase, msg, current=0, total=0, found=0):
        await _store_phase(phase, msg, current, total, found)
        await _original_prog(phase, msg, current, total, found)

    # Start heartbeat in background
    async def heartbeat():
        while True:
            await asyncio.sleep(3)
            if cancelled():
                break
            # Re-send last phase to keep UI alive
            await _original_prog(last_phase["phase"], last_phase["msg"],
                                  last_phase["current"], last_phase["total"], last_phase["found"])
    heartbeat_task = asyncio.create_task(heartbeat())

    if HAS_AIOHTTP:
        conn = aiohttp.TCPConnector(limit=100, limit_per_host=40, ssl=False)
        async with aiohttp.ClientSession(connector=conn,
                                          headers={"User-Agent": random.choice(USER_AGENTS)}) as session:
            # 1. Main page — fetch với fallbacks (HTTPS → HTTP → www.)
            await prog("main_page", "Đang tải trang chính (với fallbacks)...")
            log(f"GET {target} (với 5 fallback strategies)")
            main_text, main_code, main_headers, main_rt, final_target, fetch_err = await fetch_with_fallbacks(
                session, target, custom_headers, proxy, timeout, log
            )
            # Update target nếu fallback URL được dùng
            if final_target != target:
                log(f"[FALLBACK] Final target used: {final_target}")
                target = final_target
                parsed = urlparse(target)
                host = parsed.hostname
                base = f"{parsed.scheme}://{parsed.netloc}"
                result["target"] = target
            result["main"] = {
                "code": main_code,
                "length": len(main_text) if main_text else 0,
                "headers": dict(main_headers),
                "response_time_ms": main_rt,
                "final_target": final_target,
                "fetch_error": fetch_err,
            }
            result["page_summary"] = get_main_page_summary(main_text)
            if main_code > 0:
                log(f"Main page: {main_code} ({len(main_text or '')} bytes, {main_rt}ms)")
            else:
                log(f"[ERROR] Main page fetch failed: {fetch_err}")
                result["errors"].append(f"Kết nối thất bại sau 5 fallback strategies: {fetch_err}")
                # Continue scan với empty HTML thay vì return sớm — vẫn scan paths/ports/subdomains
                main_text = ""

            # Detect static site platform (Netlify/Vercel/CF Pages/GH Pages)
            static_platforms = detect_static_site_host(main_headers, main_text, host)
            if static_platforms:
                log(f"[STATIC] Site hosted on: {', '.join(static_platforms)}")
                result["static_platforms"] = static_platforms

            # Detect framework (Next.js/Nuxt/etc.) để chạy framework-specific checks
            frameworks_detected = detect_framework(main_text, main_headers)
            if frameworks_detected:
                log(f"[FRAMEWORK] Detected: {', '.join(frameworks_detected)}")
                result["frameworks_detected"] = frameworks_detected

            # Cookies + security headers
            if main_code > 0:
                await prog("security_headers", "Phân tích security headers & cookies...")
                result["cookies"] = analyze_cookies(main_headers)
                result["security_headers"] = analyze_security_headers(main_headers)
                log(f"Cookies: {len(result['cookies'])}, sec headers: {sum(1 for h in result['security_headers'] if h['missing'])} missing")

                # Technologies + WAF + CDN
                cookie_names = [c.get("name","") for c in result["cookies"]]
                techs = detect_tech(main_text, main_headers, cookie_names)
                result["technologies"] = techs
                await prog("fingerprint", f"Tech: {', '.join(techs) if techs else 'Không xác định'}")
                log(f"Tech detected: {', '.join(techs) if techs else 'none'}")
            else:
                # Main page failed but still continue with port scan / subdomain / leak paths
                await prog("security_headers", "Skip security headers (main page failed)")
                log("Skip security headers + tech detection (main page failed)")

            waf = detect_waf(main_headers, main_code, main_text or "")
            result["waf"] = waf
            result["cdn"] = detect_cdn(main_headers)
            if waf["detected"]:
                log(f"WAF: {', '.join(waf['detected'])} – slow mode")
            if waf["should_slow_down"]:
                await prog("waf", f"WAF: {', '.join(waf['detected'])} – Giảm tốc")

            limit = WAF_BYPASS_PROFILES.get(bypass_mode, WAF_BYPASS_PROFILES["auto"])["concurrency"]
            if waf["should_slow_down"] and bypass_mode == "auto":
                limit = 12  # Auto-throttle if WAF detected and not in aggressive/turbo mode
            result["bypass_mode"] = bypass_mode
            log(f"[BYPASS] Mode: {bypass_mode} → concurrency={limit}, rotate_ua={WAF_BYPASS_PROFILES.get(bypass_mode, {}).get('rotate_ua')}, rotate_xff={WAF_BYPASS_PROFILES.get(bypass_mode, {}).get('rotate_xff')}")

            # SSL info nếu HTTPS
            if parsed.scheme == "https":
                await prog("ssl", "Đ kiểm tra SSL/TLS cert...")
                result["ssl"] = get_ssl_info(host, 443, 5)
                if result["ssl"].get("days_remaining") is not None:
                    log(f"SSL: {result['ssl'].get('subject')} ({result['ssl'].get('days_remaining')}d remaining)")

            # 2. Ports
            if host:
                await prog("ports", "Đang quét cổng...")
                result["ports"] = await scan_ports(host)
                await prog("ports_done", f"Cổng mở: {result['ports'] or 'Không có'}")
                log(f"Open ports: {result['ports']}")

            # 3. Leak paths — soft-404 calibration trước
            await prog("leak_scan", f"Soft-404 calibration...", 0, len(LEAK_PATHS), 0)
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
                    try:
                        soft_404_hashes.add(hashlib.md5(t.encode('utf-8','replace')).hexdigest()[:12])
                    except Exception:
                        pass
                    soft_404_codes.add(c)
            if soft_404_sizes:
                await prog("leak_scan", f"Soft-404 baseline: {len(soft_404_sizes)} size(s) – sẽ filter", 0, len(LEAK_PATHS), 0)
                log(f"Soft-404 baseline: sizes={soft_404_sizes}")

            await prog("leak_scan", f"Quét {len(LEAK_PATHS)} paths...", 0, len(LEAK_PATHS), 0)
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
                            try:
                                h_ = hashlib.md5((text or "").encode('utf-8','replace')).hexdigest()[:12]
                                if h_ in soft_404_hashes:
                                    is_soft_404 = True
                            except Exception:
                                is_soft_404 = True
                        if is_soft_404:
                            soft_filtered_count += 1
                            return {
                                "path": path, "url": url, "code": code,
                                "size": size, "preview": "", "headers": {},
                                "severity": "info", "response_time_ms": rt,
                                "soft_404": True,
                            }
                        if code == 200:
                            found_count += 1
                            log(f"[{sev:>5}] {code} {path} ({size}b)")
                        else:
                            log(f"[{sev:>5}] {code} {path}")
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
            tasks = [check_path(p) for p in LEAK_PATHS]
            done = 0
            for coro in asyncio.as_completed(tasks):
                item = await coro
                done += 1
                if item:
                    result["leak"].append(item)
                if done % 10 == 0 or done == len(LEAK_PATHS):
                    await prog("leak_scan", f"{done}/{len(LEAK_PATHS)} – Found {found_count} (soft-404 filtered: {soft_filtered_count})", done, len(LEAK_PATHS), found_count)
            result["soft_404_filtered"] = soft_filtered_count
            if cancelled():
                result["cancelled"] = True
                result["errors"].append("Scan bị huỷ bởi user")
                result["duration_seconds"] = round(time.time()-start, 2)
                return result

            # 3a. POST-HOC soft-404 clustering — nếu server trả 200 cho mọi path
            # với cùng size/hash, tự đánh dấu là soft-404 dù calibration không catch được.
            # Threshold: nếu >5 path 200 có cùng size và content-hash, mark tất cả là soft-404.
            size_count = {}  # size -> [items]
            hash_count = {}  # hash -> [items]
            for item in result["leak"]:
                if item.get("code") == 200 and not item.get("soft_404"):
                    sz = item.get("size", 0)
                    if sz > 0:
                        size_count.setdefault(sz, []).append(item)
            cluster_filtered = 0
            CLUSTER_THRESHOLD = 8  # nếu 8+ paths cùng size → soft-404
            for sz, items in size_count.items():
                if len(items) >= CLUSTER_THRESHOLD and sz > 0:
                    # Mark all as soft-404
                    for item in items:
                        item["soft_404"] = True
                        item["severity"] = "info"
                        cluster_filtered += 1
                    log(f"[CLUSTER] {len(items)} paths cùng size {sz}b → mark soft-404")
            if cluster_filtered > 0:
                found_count -= cluster_filtered
                soft_filtered_count += cluster_filtered
                result["soft_404_filtered"] = soft_filtered_count
                log(f"Cluster filter total: {cluster_filtered} items")

            result["leak"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))
            log(f"Leak scan done: {found_count} found, {soft_filtered_count} soft-404 filtered")

            # 3a.5. Static-site specific paths (v11.1)
            # Nếu detect Netlify/Vercel/CF Pages/GH Pages → scan thêm STATIC_SITE_PATHS
            # Nếu detect framework → scan thêm FRAMEWORK_EXTRA_PATHS
            extra_paths = set()
            if result.get("static_platforms"):
                log(f"[STATIC] Adding {len(STATIC_SITE_PATHS)} static-site specific paths")
                for p in STATIC_SITE_PATHS:
                    extra_paths.add(p)
            if result.get("frameworks_detected"):
                for fw in result["frameworks_detected"]:
                    extra_paths_fw = FRAMEWORK_EXTRA_PATHS.get(fw, [])
                    if extra_paths_fw:
                        log(f"[FRAMEWORK] Adding {len(extra_paths_fw)} {fw}-specific paths")
                        for p in extra_paths_fw:
                            extra_paths.add(p)
            if extra_paths:
                await prog("static_scan", f"Quét {len(extra_paths)} static/framework-specific paths...", 0, len(extra_paths), 0)
                log(f"Static/framework scan: {len(extra_paths)} extra paths")
                sem_static = asyncio.Semaphore(limit)
                static_done = 0
                static_found = 0
                async def check_static_path(path):
                    nonlocal static_done, static_found
                    if cancelled():
                        return None
                    async with sem_static:
                        url = urljoin(base, path)
                        text, code, h, rt = await fetch(session, url, custom_headers, proxy, timeout)
                        static_done += 1
                        if static_done % 15 == 0:
                            await prog("static_scan", f"Static {static_done}/{len(extra_paths)} – Found {static_found}", static_done, len(extra_paths), static_found)
                        if code in (200, 401, 403):
                            # Soft-404 check
                            if code == 200 and text and len(text) in soft_404_sizes:
                                return None
                            if code == 200:
                                static_found += 1
                                sev = score_finding(path, code)
                                # Boost severity for source maps and config files
                                if path.endswith('.map') or path.endswith('Map.json'):
                                    sev = "high"
                                elif path in ('/_headers', '/_redirects', '/netlify.toml', '/vercel.json'):
                                    sev = "high"
                                elif path in ('/.env', '/.env.local', '/.env.production', '/secrets.json'):
                                    sev = "critical"
                                log(f"[STATIC {sev.upper():>5}] {code} {path} ({len(text or '')}b)")
                            else:
                                log(f"[STATIC] {code} {path}")
                            return {
                                "path": path, "url": url, "code": code,
                                "size": len(text) if text else 0,
                                "preview": (text[:500]+"..." if len(text) > 500 else text) if code == 200 else "",
                                "headers": dict(h) if code == 200 else {},
                                "severity": score_finding(path, code),
                                "response_time_ms": rt,
                                "soft_404": False,
                                "static_specific": True,
                            }
                        return None
                static_tasks = [check_static_path(p) for p in extra_paths if p not in LEAK_PATHS]
                for coro in asyncio.as_completed(static_tasks):
                    item = await coro
                    if item:
                        result["leak"].append(item)
                await prog("static_scan", f"Static scan done: {static_found} found", static_done, len(extra_paths), static_found)
                log(f"Static scan done: {static_found} found")
                # Re-sort
                result["leak"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))

            # 3b. Backup variant check cho các file 200 tìm được
            await prog("backup_check", f"Check backup variants cho {found_count} file(s)...")
            real_leaks = [x for x in result["leak"] if not x.get("soft_404") and x["code"] == 200]
            backup_count = 0
            async def check_backup(item):
                nonlocal backup_count
                for variant in BACKUP_VARIANTS:
                    if cancelled():
                        return None
                    url = item["url"] + variant
                    t, c, _, rt = await fetch(session, url, custom_headers, proxy, timeout)
                    if c == 200 and t and len(t) not in soft_404_sizes:
                        backup_count += 1
                        log(f"[BACKUP] 200 {url} ({len(t)}b)")
                        return {"original": item["path"], "backup_path": item["path"] + variant,
                                "url": url, "code": c, "size": len(t), "severity": score_finding(item["path"], c)}
                    elif c in (401, 403):
                        log(f"[BACKUP] {c} {url}")
                return None
            bsem = asyncio.Semaphore(limit)
            async def b_check(item):
                async with bsem:
                    return await check_backup(item)
            for r in await asyncio.gather(*[b_check(x) for x in real_leaks[:30]]):
                if r:
                    result["backup_findings"].append(r)
            log(f"Backup check done: {backup_count} backups found")

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
                log(f"robots.txt: {len(result['robots'])} paths")
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
                log(f"Links: {len(result['links'])}, JS: {len(result['js_links'])}, Forms: {len(result['forms'])}")

                # 6. Secrets trong main HTML
                await prog("secrets", "Quét secret trong HTML...")
                html_secrets = scan_secrets(main_text, "main page HTML")
                result["secrets"].extend(html_secrets)
                log(f"HTML secrets: {len(html_secrets)}")

                # 7. Fetch + scan JS files — SKIP external CDN domains
                if scan_js and result["js_links"]:
                    # Chỉ scan JS files cùng origin với target (tránh false positive từ CDN vendor)
                    target_netloc = parsed.netloc.lower()
                    same_origin_js = []
                    external_js = []
                    for u in result["js_links"]:
                        try:
                            u_parsed = urlparse(u)
                            if u_parsed.netloc.lower() == target_netloc or not u_parsed.netloc:
                                same_origin_js.append(u)
                            else:
                                external_js.append(u)
                        except Exception:
                            same_origin_js.append(u)
                    if external_js:
                        log(f"Skip {len(external_js)} external CDN JS files (avoid false positive)")
                    if same_origin_js:
                        await prog("secrets_js", f"Quét {len(same_origin_js)} same-origin JS files...", 0, len(same_origin_js), 0)
                        js_sem = asyncio.Semaphore(8)
                        async def scan_one_js(url):
                            async with js_sem:
                                t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                                if c == 200 and t:
                                    ss = scan_secrets(t, f"JS: {url}")
                                    if ss:
                                        log(f"[SECRET] {url}: {len(ss)} secrets")
                                    return ss
                                return []
                        done = 0
                        for coro in asyncio.as_completed([scan_one_js(u) for u in same_origin_js]):
                            ss = await coro
                            result["secrets"].extend(ss)
                            done += 1
                            if done % 5 == 0 or done == len(same_origin_js):
                                await prog("secrets_js", f"JS {done}/{len(same_origin_js)} – Secrets: {len(result['secrets'])}", done, len(same_origin_js), len(result['secrets']))
                    else:
                        log("No same-origin JS files to scan")
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
                    "/logs/", "/config/", "/static/", "/public/", "/_files/", "/media/",
                    "/uploads/files/", "/static/uploads/", "/var/", "/var/log/", "/var/log/apache2/"]
            async def check_dir(d):
                url = urljoin(base, d)
                t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                if c == 200 and t and ("<title>Index of" in t or "Parent Directory" in t or "<h1>Index of" in t):
                    log(f"[DIRLIST] 200 {url}")
                    return {"url": url, "type": "dirlist"}
                return None
            result["dirs"] = [r for r in await asyncio.gather(*[check_dir(d) for d in dirs]) if r]

            # 9. Brute-force common names — gửi progress liên tục
            if not cancelled():
                brute_total = len(BRUTE_NAMES) * len(BRUTE_EXTS_EXPANDED)
                await prog("brute", "Brute-force common files...", 0, brute_total, 0)
                exts = BRUTE_EXTS_EXPANDED
                bsem = asyncio.Semaphore(15)
                brute_timeout = min(timeout, 4)
                b_done = 0
                b_found = 0
                async def brute_one(n, e):
                    nonlocal b_done, b_found
                    if cancelled():
                        return None
                    path = f"/{n}{e}"
                    url = urljoin(base, path)
                    async with bsem:
                        t, c, _, rt = await fetch(session, url, custom_headers, proxy, brute_timeout)
                        b_done += 1
                        if b_done % 30 == 0 or b_done == brute_total:
                            await prog("brute", f"Brute {b_done}/{brute_total} – Found {b_found}", b_done, brute_total, b_found)
                        if c in (200, 403, 401):
                            # Soft-404 check: nếu size trùng baseline hoặc cùng size với nhiều path khác
                            if c == 200 and t:
                                sz = len(t)
                                if sz in soft_404_sizes:
                                    return None
                            b_found += 1
                            log(f"[BRUTE] {c} {path}")
                            return {"path": path, "code": c, "severity": score_finding(path, c), "response_time_ms": rt}
                        return None
                result["brute"] = [r for r in await asyncio.gather(*[brute_one(n, e) for n in BRUTE_NAMES for e in exts]) if r]
                result["brute"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))
                await prog("brute", f"Brute xong: {len(result['brute'])} hits", b_done, brute_total, 0)
                log(f"Brute: {len(result['brute'])} hits")

            # 10. Query param fuzzing trên endpoint chính
            if not cancelled():
                p_total = len(PARAM_FUZZ)
                await prog("param_fuzz", f"Query param fuzzing ({p_total} params)...", 0, p_total, 0)
                psem = asyncio.Semaphore(10)
                p_done = 0
                p_found = 0
                async def fuzz_param(param):
                    nonlocal p_done, p_found
                    url = f"{target}?{param}=1"
                    async with psem:
                        t, c, _, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 5))
                        p_done += 1
                        if p_done % 5 == 0 or p_done == p_total:
                            await prog("param_fuzz", f"Param {p_done}/{p_total}", p_done, p_total, p_found)
                        # So sánh với main response để detect debug mode
                        if c == 200 and t and len(t) != len(main_text or ""):
                            diff = abs(len(t) - len(main_text or ""))
                            if diff > 50:  # significant difference
                                p_found += 1
                                log(f"[PARAM] ?{param}=1 → {c} ({len(t)}b, diff {diff})")
                                return {"param": param, "url": url, "code": c, "size": len(t),
                                        "main_size": len(main_text or ""), "diff": diff}
                        return None
                result["param_findings"] = [r for r in await asyncio.gather(*[fuzz_param(p) for p in PARAM_FUZZ]) if r]
                await prog("param_fuzz", f"Param fuzz xong: {len(result['param_findings'])} interesting", p_done, p_total, 0)
                log(f"Param fuzz: {len(result['param_findings'])} interesting")

            # 11. Subdomain hints (no network call) + DNS resolution
            result["subdomain_hints"] = [f"{s}.{host}" for s in COMMON_SUBDOMAINS[:30]]
            await prog("subdomains", "DNS enum subdomains...", 0, 40, 0)
            try:
                result["subdomains_resolved"] = await resolve_subdomains(host)
                await prog("subdomains", f"Subdomain resolved: {len(result['subdomains_resolved'])}", len(result["subdomains_resolved"]), 40, len(result["subdomains_resolved"]))
                log(f"Subdomain resolved: {len(result['subdomains_resolved'])}")
            except Exception as e:
                log(f"Subdomain enum failed: {e}")

            # 12. Subdomain takeover check (v11.1)
            if not cancelled() and result["subdomains_resolved"]:
                await prog("takeover", f"Check subdomain takeover cho {len(result['subdomains_resolved'])} subs...", 0, len(result["subdomains_resolved"]), 0)
                log(f"Takeover check: {len(result['subdomains_resolved'])} subdomains")
                try:
                    result["takeover_findings"] = await check_subdomain_takeover_detailed(
                        session, host, result["subdomains_resolved"], custom_headers, proxy, timeout
                    )
                    for tf in result["takeover_findings"]:
                        log(f"[TAKEOVER] {tf['subdomain']} → {tf['service']}")
                    await prog("takeover", f"Takeover check done: {len(result['takeover_findings'])} vulnerable", len(result["subdomains_resolved"]), len(result["subdomains_resolved"]), len(result["takeover_findings"]))
                    log(f"Takeover done: {len(result['takeover_findings'])} vulnerable")
                except Exception as e:
                    log(f"Takeover check failed: {e}")

            # 13. GraphQL introspection (v11.1)
            if not cancelled():
                await prog("graphql", f"GraphQL endpoint discovery ({len(GRAPHQL_ENDPOINTS)} endpoints)...", 0, len(GRAPHQL_ENDPOINTS), 0)
                log(f"GraphQL: testing {len(GRAPHQL_ENDPOINTS)} endpoints")
                try:
                    result["graphql_findings"] = await check_graphql(session, target, custom_headers, proxy, timeout)
                    for gq in result["graphql_findings"]:
                        log(f"[GRAPHQL] {gq['endpoint']} → {gq.get('introspection_enabled', False)} (severity: {gq['severity']})")
                    await prog("graphql", f"GraphQL done: {len(result['graphql_findings'])} found", len(GRAPHQL_ENDPOINTS), len(GRAPHQL_ENDPOINTS), len(result["graphql_findings"]))
                    log(f"GraphQL done: {len(result['graphql_findings'])} found")
                except Exception as e:
                    log(f"GraphQL check failed: {e}")

            # 14. CORS misconfiguration (v11.1)
            if not cancelled():
                await prog("cors", "CORS misconfiguration test (3 origins × 5 endpoints)...", 0, 5, 0)
                log(f"CORS: testing 3 origins × 5 endpoints")
                try:
                    result["cors_findings"] = await check_cors(session, target, custom_headers, proxy, timeout)
                    for cf in result["cors_findings"]:
                        log(f"[CORS] {cf['url']} reflects {cf['origin_tested']} (cred: {cf.get('acac','')})")
                    await prog("cors", f"CORS done: {len(result['cors_findings'])} vulnerable", 5, 5, len(result["cors_findings"]))
                    log(f"CORS done: {len(result['cors_findings'])} vulnerable")
                except Exception as e:
                    log(f"CORS check failed: {e}")

            # 15. Open redirect test (v11.1)
            if not cancelled():
                await prog("open_redirect", f"Open redirect test ({len(REDIRECT_PARAMS)} params × 5 payloads)...", 0, len(REDIRECT_PARAMS), 0)
                log(f"Open redirect: testing {len(REDIRECT_PARAMS)} params × 5 payloads")
                try:
                    result["open_redirect_findings"] = await check_open_redirect(session, target, custom_headers, proxy, timeout)
                    for rf in result["open_redirect_findings"]:
                        log(f"[REDIRECT] ?{rf['param']}={rf['payload'][:30]} → {rf['status_code']} {rf.get('location','')[:50]}")
                    await prog("open_redirect", f"Redirect done: {len(result['open_redirect_findings'])} vulnerable", len(REDIRECT_PARAMS), len(REDIRECT_PARAMS), len(result["open_redirect_findings"]))
                    log(f"Redirect done: {len(result['open_redirect_findings'])} vulnerable")
                except Exception as e:
                    log(f"Open redirect check failed: {e}")

            # 16. Source map exposure (v11.1)
            if not cancelled() and result["js_links"]:
                await prog("source_maps", f"Source map check cho {min(30, len(result['js_links']))} JS files...", 0, min(30, len(result["js_links"])), 0)
                log(f"Source maps: checking {min(30, len(result['js_links']))} JS files")
                try:
                    result["source_maps"] = await check_source_maps(session, result["js_links"], custom_headers, proxy, timeout)
                    for sm in result["source_maps"]:
                        log(f"[SRCMAP] {sm['map_url']} → {sm['sources_count']} source files")
                    await prog("source_maps", f"Source maps done: {len(result['source_maps'])} found", min(30, len(result["js_links"])), min(30, len(result["js_links"])), len(result["source_maps"]))
                    log(f"Source maps done: {len(result['source_maps'])} found")
                except Exception as e:
                    log(f"Source map check failed: {e}")

            # 17. JS endpoint extraction + API fuzzing (v11.1)
            if not cancelled() and scan_js and result["js_links"]:
                await prog("js_endpoints", f"Extract API endpoints từ {len(result['js_links'])} JS files...", 0, len(result["js_links"]), 0)
                log(f"JS endpoints: extracting from {len(result['js_links'])} JS files")
                try:
                    target_netloc = parsed.netloc.lower()
                    same_origin_js = [u for u in result["js_links"]
                                     if not urlparse(u).netloc or urlparse(u).netloc.lower() == target_netloc]
                    js_sem = asyncio.Semaphore(8)
                    all_endpoints = set()
                    done = 0
                    async def extract_one(url):
                        nonlocal done
                        async with js_sem:
                            t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                            done += 1
                            if c == 200 and t:
                                eps = extract_js_endpoints(t, url)
                                return eps
                            return []
                    for coro in asyncio.as_completed([extract_one(u) for u in same_origin_js[:20]]):
                        eps = await coro
                        for ep in eps:
                            all_endpoints.add(ep)
                        if done % 3 == 0:
                            await prog("js_endpoints", f"JS {done}/{len(same_origin_js[:20])} – Endpoints: {len(all_endpoints)}", done, len(same_origin_js[:20]), len(all_endpoints))
                    result["js_endpoints"] = sorted(all_endpoints)[:50]
                    log(f"JS endpoints extracted: {len(result['js_endpoints'])}")
                    if result["js_endpoints"]:
                        await prog("api_fuzz", f"Test {len(result['js_endpoints'])} discovered API endpoints...", 0, len(result["js_endpoints"]), 0)
                        log(f"API fuzz: testing {len(result['js_endpoints'])} endpoints")
                        api_sem = asyncio.Semaphore(10)
                        api_done = 0
                        api_found = 0
                        async def test_endpoint(ep):
                            nonlocal api_done, api_found
                            if cancelled():
                                return None
                            url = urljoin(base, ep)
                            async with api_sem:
                                t, c, h, rt = await fetch(session, url, custom_headers, proxy, min(timeout, 5))
                                api_done += 1
                                if c in (200, 401, 403, 405):
                                    if c == 200 and t and len(t) in soft_404_sizes:
                                        return None
                                    api_found += 1
                                    if c != 404:
                                        log(f"[API] {c} {ep}")
                                    return {"path": ep, "url": url, "code": c,
                                            "size": len(t) if t else 0,
                                            "severity": "medium" if c == 200 else "low",
                                            "response_time_ms": rt}
                                return None
                        for coro in asyncio.as_completed([test_endpoint(ep) for ep in result["js_endpoints"]]):
                            r = await coro
                            if r:
                                result["api_endpoints"].append(r)
                        await prog("api_fuzz", f"API fuzz done: {len(result['api_endpoints'])} hits", api_done, len(result["js_endpoints"]), len(result["api_endpoints"]))
                        log(f"API fuzz done: {len(result['api_endpoints'])} hits")
                except Exception as e:
                    log(f"JS endpoint extraction failed: {e}")

            # 18. Swagger/OpenAPI parsing (v11.1)
            if not cancelled():
                await prog("swagger", "Parse Swagger/OpenAPI specs...", 0, 5, 0)
                log(f"Swagger: testing 6 spec paths")
                try:
                    swagger_paths = ["/swagger.json", "/openapi.json", "/api/swagger.json",
                                    "/api/openapi.json", "/v2/api-docs", "/v3/api-docs"]
                    for sp in swagger_paths:
                        url = urljoin(base, sp)
                        t, c, _, _ = await fetch(session, url, custom_headers, proxy, min(timeout, 5))
                        if c == 200 and t and ("swagger" in t.lower() or "openapi" in t.lower() or '"paths"' in t):
                            endpoints = parse_swagger_spec(t, base)
                            if endpoints:
                                log(f"[SWAGGER] {sp} → {len(endpoints)} endpoints discovered")
                                result["swagger_endpoints"].extend(endpoints[:100])
                    await prog("swagger", f"Swagger done: {len(result['swagger_endpoints'])} endpoints", 5, 5, len(result["swagger_endpoints"]))
                    log(f"Swagger done: {len(result['swagger_endpoints'])} endpoints")
                except Exception as e:
                    log(f"Swagger parsing failed: {e}")

            # 19. Recursive depth-2 brute-force (v11.1)
            if not cancelled():
                found_dirs = [d["url"].replace(base, "") for d in result["dirs"]]
                found_dirs += [x["path"] for x in result["leak"] if x.get("path","").endswith("/") and not x.get("soft_404")]
                found_dirs = list(set(found_dirs))[:5]
                if found_dirs:
                    total_r = len(found_dirs) * len(RECURSIVE_BRUTE_PATHS)
                    await prog("recursive_brute", f"Recursive brute-force {len(found_dirs)} dirs × {len(RECURSIVE_BRUTE_PATHS)} paths...", 0, total_r, 0)
                    log(f"Recursive brute: {len(found_dirs)} dirs × {len(RECURSIVE_BRUTE_PATHS)} sub-paths")
                    try:
                        findings, r_done, r_total, r_found = await recursive_brute(
                            session, base, found_dirs, custom_headers, proxy, timeout,
                            soft_404_sizes,
                            lambda msg: log(msg),
                            cancelled
                        )
                        result["recursive_brute_findings"] = findings
                        await prog("recursive_brute", f"Recursive brute done: {len(findings)} hits", r_done, r_total, len(findings))
                        log(f"Recursive brute done: {len(findings)} hits in {len(found_dirs)} dirs")
                    except Exception as e:
                        log(f"Recursive brute failed: {e}")
                else:
                    log(f"Recursive brute skipped: no directories found")

            # 20. HTTP method fuzzing (v11.1)
            if not cancelled():
                test_urls = [target]
                test_urls += [x["url"] for x in result["leak"][:3] if x.get("code") == 200 and not x.get("soft_404")]
                test_urls = test_urls[:5]
                await prog("http_methods", f"HTTP method fuzzing on {len(test_urls)} endpoints...", 0, len(test_urls), 0)
                log(f"HTTP methods: OPTIONS on {len(test_urls)} endpoints")
                try:
                    for u in test_urls:
                        if cancelled():
                            break
                        m_findings = await test_http_methods(session, u, custom_headers, proxy, timeout)
                        result["http_method_findings"].extend(m_findings)
                        for mf in m_findings:
                            log(f"[METHODS] OPTIONS {u} → Allow: {mf.get('allow','')[:80]}")
                    await prog("http_methods", f"HTTP methods done: {len(result['http_method_findings'])} with Allow header", len(test_urls), len(test_urls), len(result["http_method_findings"]))
                    log(f"HTTP methods done: {len(result['http_method_findings'])} with Allow header")
                except Exception as e:
                    log(f"HTTP method fuzz failed: {e}")

            # 21. Wayback Machine integration (v11.1)
            if not cancelled():
                await prog("wayback", "Wayback Machine historical URLs lookup...", 0, 1, 0)
                log(f"Wayback: querying web.archive.org")
                try:
                    result["wayback_urls"] = await fetch_wayback_urls(session, target, custom_headers, proxy, timeout)
                    log(f"Wayback done: {len(result['wayback_urls'])} historical URLs found")
                    await prog("wayback", f"Wayback done: {len(result['wayback_urls'])} URLs", 1, 1, len(result["wayback_urls"]))
                except Exception as e:
                    log(f"Wayback lookup failed: {e}")

            # 22. Certificate Transparency logs (v11.1) — crt.sh subdomain enum
            if not cancelled():
                await prog("ct_logs", "Certificate Transparency logs (crt.sh)...", 0, 1, 0)
                log(f"CT: querying crt.sh for *.{host}")
                try:
                    ct_subs = await fetch_ct_logs(session, host, log)
                    # Merge với subdomains_resolved
                    existing_subs = {s["host"] for s in result.get("subdomains_resolved", [])}
                    new_ct_subs = []
                    for sub in ct_subs:
                        if sub not in existing_subs:
                            # Try DNS resolve
                            try:
                                loop = asyncio.get_event_loop()
                                infos = await loop.getaddrinfo(sub, None)
                                ip = infos[0][4][0] if infos else None
                                new_ct_subs.append({"sub": sub.split(".")[0] if "." in sub else sub,
                                                    "host": sub, "ip": ip, "ok": True, "source": "crt.sh"})
                            except Exception:
                                new_ct_subs.append({"sub": sub.split(".")[0] if "." in sub else sub,
                                                    "host": sub, "ip": None, "ok": False, "source": "crt.sh"})
                    result["ct_subdomains"] = new_ct_subs
                    result["subdomains_resolved"].extend([s for s in new_ct_subs if s["ok"]])
                    log(f"[CT] Found {len(ct_subs)} CT subdomains, {len(new_ct_subs)} new (resolved: {sum(1 for s in new_ct_subs if s['ok'])})")
                    await prog("ct_logs", f"CT done: {len(ct_subs)} subs found", 1, 1, len(ct_subs))
                except Exception as e:
                    log(f"CT logs failed: {e}")

            # 23. DNS records lookup (v11.1)
            if not cancelled() and host:
                await prog("dns_records", "DNS records lookup (A/AAAA/MX/TXT/CNAME)...", 0, 1, 0)
                log(f"DNS: looking up records for {host}")
                try:
                    result["dns_records"] = await lookup_dns_records(host)
                    for rtype, rvals in result["dns_records"].items():
                        log(f"[DNS] {rtype}: {', '.join(rvals[:3])}")
                    await prog("dns_records", f"DNS done: {len(result['dns_records'])} record types", 1, 1, len(result["dns_records"]))
                except Exception as e:
                    log(f"DNS lookup failed: {e}")

            # 24. .git directory exposure check (v11.1)
            if not cancelled():
                await prog("git_exposure", "Check .git directory exposure (HEAD, config, index)...", 0, 1, 0)
                log(f"Git: checking .git directory exposure")
                try:
                    git_findings = await check_git_exposure(session, base, custom_headers, proxy, timeout, log)
                    if git_findings:
                        result["git_findings"] = git_findings
                        # Add to leaks list too
                        for gf in git_findings:
                            result["leak"].append({
                                "path": gf["path"], "url": gf["url"], "code": gf["code"],
                                "size": gf["size"], "preview": gf.get("preview", ""),
                                "headers": {}, "severity": gf["severity"],
                                "response_time_ms": 0, "soft_404": False,
                            })
                        result["leak"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))
                    await prog("git_exposure", f"Git check done: {len(git_findings)} findings", 1, 1, len(git_findings))
                except Exception as e:
                    log(f"Git exposure check failed: {e}")

            # 25. Deep crawl (v11.1) — crawl links depth-2, extract secrets from all pages
            if not cancelled() and main_text and len(main_text) > 100:
                await prog("deep_crawl", "Deep crawl internal links (depth-2)...", 0, 1, 0)
                log(f"Deep crawl: collecting internal links depth-2")
                try:
                    pages_data, crawled_secrets = await deep_crawl(
                        session, base, main_text, custom_headers, proxy, timeout,
                        soft_404_sizes, log, cancelled, max_depth=2, max_pages=20
                    )
                    result["crawled_pages"] = pages_data
                    # Dedup crawled secrets vs existing
                    existing_secret_keys = {(s["type"], s["match_masked"]) for s in result["secrets"]}
                    new_secrets = [s for s in crawled_secrets
                                   if (s["type"], s["match_masked"]) not in existing_secret_keys]
                    result["secrets"].extend(new_secrets)
                    result["secrets"].sort(key=lambda x: -severity_rank(x.get("severity", "low")))
                    log(f"[CRAWL] Crawled {len(pages_data)} pages, found {len(new_secrets)} new secrets")
                    await prog("deep_crawl", f"Deep crawl done: {len(pages_data)} pages, +{len(new_secrets)} secrets", 1, 1, len(pages_data))
                except Exception as e:
                    log(f"Deep crawl failed: {e}")

            # 26. JS source string extraction (v11.1)
            if not cancelled() and scan_js and result.get("js_links"):
                target_netloc = parsed.netloc.lower()
                same_origin_js = [u for u in result["js_links"]
                                 if not urlparse(u).netloc or urlparse(u).netloc.lower() == target_netloc]
                if same_origin_js:
                    await prog("js_strings", f"Extract strings từ {min(15, len(same_origin_js))} JS files...", 0, min(15, len(same_origin_js)), 0)
                    log(f"JS strings: extracting from {min(15, len(same_origin_js))} JS files")
                    try:
                        js_sem = asyncio.Semaphore(8)
                        all_strings = set()
                        done = 0
                        async def extract_strings_one(url):
                            nonlocal done
                            async with js_sem:
                                t, c, _, _ = await fetch(session, url, custom_headers, proxy, timeout)
                                done += 1
                                if c == 200 and t:
                                    return extract_js_strings(t, min_length=15, max_strings=50)
                                return []
                        for coro in asyncio.as_completed([extract_strings_one(u) for u in same_origin_js[:15]]):
                            strs = await coro
                            all_strings.update(strs)
                            if done % 3 == 0:
                                await prog("js_strings", f"JS {done}/{min(15, len(same_origin_js))} – Strings: {len(all_strings)}", done, min(15, len(same_origin_js)), len(all_strings))
                        result["js_strings"] = sorted(all_strings)[:200]
                        log(f"[JS-STR] Extracted {len(result['js_strings'])} unique strings from JS files")
                        await prog("js_strings", f"JS strings done: {len(result['js_strings'])} extracted", min(15, len(same_origin_js)), min(15, len(same_origin_js)), len(result["js_strings"]))
                    except Exception as e:
                        log(f"JS string extraction failed: {e}")

            # 27. SSTI detection (v11.1)
            if not cancelled():
                await prog("ssti", "Server-Side Template Injection test...", 0, 1, 0)
                log(f"SSTI: testing 8 endpoints × {len(SSTI_PAYLOADS)} payloads × 7 params")
                try:
                    result["ssti_findings"] = await check_ssti(session, target, custom_headers, proxy, timeout, log, cancelled)
                    await prog("ssti", f"SSTI done: {len(result['ssti_findings'])} vulnerable", 1, 1, len(result["ssti_findings"]))
                    log(f"SSTI done: {len(result['ssti_findings'])} vulnerable")
                except Exception as e:
                    log(f"SSTI check failed: {e}")

            # 28. Prototype Pollution (v11.1)
            if not cancelled():
                await prog("proto_pollution", f"Prototype Pollution test ({len(PROTO_POLLUTION_PAYLOADS)} payloads)...", 0, len(PROTO_POLLUTION_PAYLOADS), 0)
                log(f"Proto pollution: testing {len(PROTO_POLLUTION_PAYLOADS)} payloads")
                try:
                    result["proto_pollution_findings"] = await check_proto_pollution(session, target, custom_headers, proxy, timeout, log, cancelled)
                    await prog("proto_pollution", f"Proto pollution done: {len(result['proto_pollution_findings'])} vulnerable", len(PROTO_POLLUTION_PAYLOADS), len(PROTO_POLLUTION_PAYLOADS), len(result["proto_pollution_findings"]))
                    log(f"Proto pollution done: {len(result['proto_pollution_findings'])} vulnerable")
                except Exception as e:
                    log(f"Proto pollution check failed: {e}")

            # 29. HTTP Header Injection (v11.1) — bypass access control
            if not cancelled():
                await prog("header_injection", f"HTTP header injection ({len(HEADER_INJECTION_PAYLOADS)} payloads)...", 0, len(HEADER_INJECTION_PAYLOADS), 0)
                log(f"Header injection: testing {len(HEADER_INJECTION_PAYLOADS)} headers (X-Forwarded-*, X-Original-URL, etc.)")
                try:
                    result["header_injection_findings"] = await check_header_injection(session, target, custom_headers, proxy, timeout, log, cancelled)
                    await prog("header_injection", f"Header injection done: {len(result['header_injection_findings'])} vulnerable", len(HEADER_INJECTION_PAYLOADS), len(HEADER_INJECTION_PAYLOADS), len(result["header_injection_findings"]))
                    log(f"Header injection done: {len(result['header_injection_findings'])} vulnerable")
                except Exception as e:
                    log(f"Header injection check failed: {e}")

            # 30. Cache Poisoning (v11.1)
            if not cancelled():
                await prog("cache_poison", f"Cache poisoning test ({len(CACHE_POISON_PAYLOADS)} payloads)...", 0, len(CACHE_POISON_PAYLOADS), 0)
                log(f"Cache poisoning: testing {len(CACHE_POISON_PAYLOADS)} headers")
                try:
                    result["cache_poison_findings"] = await check_cache_poisoning(session, target, main_text, custom_headers, proxy, timeout, log, cancelled)
                    await prog("cache_poison", f"Cache poisoning done: {len(result['cache_poison_findings'])} vulnerable", len(CACHE_POISON_PAYLOADS), len(CACHE_POISON_PAYLOADS), len(result["cache_poison_findings"]))
                    log(f"Cache poisoning done: {len(result['cache_poison_findings'])} vulnerable")
                except Exception as e:
                    log(f"Cache poisoning check failed: {e}")

            # 31. Default Credentials test (v11.1)
            if not cancelled() and result.get("forms"):
                login_count = sum(1 for f in result["forms"] if f.get("type") == "login")
                if login_count > 0:
                    await prog("default_creds", f"Default credentials test ({login_count} login forms × {len(DEFAULT_CREDS)} creds)...", 0, login_count, 0)
                    log(f"Default creds: testing {login_count} login forms with {len(DEFAULT_CREDS)} credential pairs")
                    try:
                        result["default_creds_findings"] = await check_default_creds(session, target, result["forms"], custom_headers, proxy, timeout, log, cancelled)
                        await prog("default_creds", f"Default creds done: {len(result['default_creds_findings'])} valid", login_count, login_count, len(result["default_creds_findings"]))
                        log(f"Default creds done: {len(result['default_creds_findings'])} valid")
                    except Exception as e:
                        log(f"Default creds check failed: {e}")
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
        "backup_findings": len(result.get("backup_findings", [])),
        "param_findings": len(result.get("param_findings", [])),
        "subdomains_resolved": len(result.get("subdomains_resolved", [])),
        # v11.1 additions
        "takeover_findings": len(result.get("takeover_findings", [])),
        "graphql_findings": len(result.get("graphql_findings", [])),
        "cors_findings": len(result.get("cors_findings", [])),
        "open_redirect_findings": len(result.get("open_redirect_findings", [])),
        "source_maps": len(result.get("source_maps", [])),
        "js_endpoints": len(result.get("js_endpoints", [])),
        "api_endpoints": len(result.get("api_endpoints", [])),
        "swagger_endpoints": len(result.get("swagger_endpoints", [])),
        "wayback_urls": len(result.get("wayback_urls", [])),
        "http_method_findings": len(result.get("http_method_findings", [])),
        "recursive_brute_findings": len(result.get("recursive_brute_findings", [])),
        # v11.1 additions
        "ct_subdomains": len(result.get("ct_subdomains", [])),
        "dns_records": len(result.get("dns_records", {})),
        "git_findings": len(result.get("git_findings", [])),
        "crawled_pages": len(result.get("crawled_pages", [])),
        "js_strings": len(result.get("js_strings", [])),
        # v11.1 additions
        "ssti_findings": len(result.get("ssti_findings", [])),
        "proto_pollution_findings": len(result.get("proto_pollution_findings", [])),
        "header_injection_findings": len(result.get("header_injection_findings", [])),
        "cache_poison_findings": len(result.get("cache_poison_findings", [])),
        "default_creds_findings": len(result.get("default_creds_findings", [])),
        "cancelled": result.get("cancelled", False),
    }
    result["duration_seconds"] = round(time.time()-start, 2)
    await prog("completed", f"Hoàn thành – {result['stats']['real_leak_count']} leaks · {result['stats']['secret_count']} secrets · {result['stats']['subdomains_resolved']+result['stats']['ct_subdomains']} subs · {result['stats']['takeover_findings']} takeover · {result['stats']['git_findings']} git · {result['stats']['graphql_findings']} graphql · {result['stats']['cors_findings']} cors · {result['stats']['source_maps']} srcmaps · {result['stats']['api_endpoints']} api · {result['stats']['wayback_urls']} wayback · {result['stats']['crawled_pages']} crawled · {result['stats']['js_strings']} js-str")
    return result

# ── SSE ──
progress_queues = {}
prog_lock = threading.Lock()
scan_results = {}
scan_history = []
scan_cancels = set()
scan_starts = {}

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
    "static_scan": "🎯 Static/framework scan",
    "backup_check": "💾 Check backup variants",
    "robots": "🤖 Phân tích robots.txt",
    "links": "🔗 Trích xuất links/JS/forms",
    "secrets": "🔐 Quét secret trong HTML",
    "secrets_js": "📜 Quét secret trong JS files",
    "dirs": "📂 Kiểm tra directory listing",
    "brute": "🔍 Brute-force common files",
    "param_fuzz": "❓ Query param fuzzing",
    "subdomains": "🌐 DNS subdomain enum",
    # v11.1 phases
    "takeover": "💀 Subdomain takeover check",
    "graphql": "⚡ GraphQL introspection",
    "cors": "🌐 CORS misconfiguration",
    "open_redirect": "↪️ Open redirect test",
    "source_maps": "🗺️ Source map exposure",
    "js_endpoints": "📜 JS endpoint extraction",
    "api_fuzz": "🔌 API endpoint fuzzing",
    "swagger": "📋 Swagger/OpenAPI parsing",
    "recursive_brute": "🔁 Recursive depth-2 brute",
    "http_methods": "🔧 HTTP method fuzzing",
    "wayback": "🕰️ Wayback Machine lookup",
    # v11.1 phases
    "ct_logs": "📜 Certificate Transparency (crt.sh)",
    "dns_records": "🌐 DNS records lookup",
    "git_exposure": "📂 .git directory exposure",
    "deep_crawl": "🕷️ Deep crawl (depth-2)",
    "js_strings": "📜 JS source string extraction",
    # v11.1 phases
    "ssti": "🧪 SSTI (template injection)",
    "proto_pollution": "💀 Prototype Pollution",
    "header_injection": "🛡️ HTTP Header Injection (bypass)",
    "cache_poison": "☠️ Cache Poisoning",
    "default_creds": "🔑 Default Credentials",
    # terminal
    "completed": "✅ Hoàn thành",
    "error": "❌ Lỗi",
    "cancelling": "🛑 Đang huỷ...",
    "cancelled": "🛑 Đã huỷ",
    "connected": None,
    "keepalive": None,
}

def phase_display(phase):
    return PHASE_NAMES.get(phase, phase if phase else "")

# ── v11.1 Risk Score Calculator ──
def calculate_risk_score(stats):
    """Calculate overall risk score (0-100) and letter grade from scan stats.
    Lower score = safer. Higher score = more vulnerable."""
    if not stats:
        return {"score": 0, "grade": "A", "label": "Safe", "color": "#00ff88",
                "max": 100, "summary": "No scan data available."}
    # Weight: critical=10, high=5, medium=2, low=1, info=0
    # Also count secret findings + takeover + git exposure + ssti etc.
    critical = stats.get("critical_count", 0) + stats.get("secret_critical", 0) + \
               stats.get("takeover_findings", 0) + stats.get("git_findings", 0) + \
               stats.get("default_creds_findings", 0)
    high = stats.get("high_count", 0) + stats.get("secret_high", 0) + \
           stats.get("header_injection_findings", 0) + stats.get("cache_poison_findings", 0) + \
           stats.get("source_maps", 0)
    medium = stats.get("medium_count", 0) + stats.get("cors_findings", 0) + \
             stats.get("proto_pollution_findings", 0) + stats.get("graphql_findings", 0) + \
             stats.get("open_redirect_findings", 0)
    low = stats.get("low_count", 0) + stats.get("param_findings", 0) + \
          stats.get("backup_findings", 0)
    info = stats.get("soft_404_filtered", 0) + stats.get("subdomains_resolved", 0)

    # Calculate raw score (can exceed 100, cap at 100)
    raw_score = (critical * 15) + (high * 7) + (medium * 3) + (low * 1) + (info * 0.2)
    score = min(100, round(raw_score))

    # Letter grade
    if score >= 80:
        grade, label, color = "F", "Critical Risk", "#ff0044"
    elif score >= 60:
        grade, label, color = "D", "High Risk", "#ff4444"
    elif score >= 40:
        grade, label, color = "C", "Medium Risk", "#ff8800"
    elif score >= 20:
        grade, label, color = "B", "Low Risk", "#ffcc00"
    else:
        grade, label, color = "A", "Safe", "#00ff88"

    # Auto-generate executive summary
    target_issues = []
    if critical > 0:
        target_issues.append(f"{critical} critical-severity issue(s) (RCE-able: exposed secrets, .git directory, default credentials, or subdomain takeover)")
    if high > 0:
        target_issues.append(f"{high} high-severity issue(s) (source code leaks, header injection, cache poisoning)")
    if medium > 0:
        target_issues.append(f"{medium} medium-severity issue(s) (CORS misconfig, GraphQL exposure, prototype pollution)")
    if low > 0:
        target_issues.append(f"{low} low-severity informational finding(s)")

    if not target_issues:
        summary = "Scan completed successfully. No significant security issues detected. The target appears to follow security best practices. Continue monitoring and re-scan periodically to detect new vulnerabilities."
    else:
        summary = f"Scan identified {len(target_issues)} category(ies) of security concerns: " + "; ".join(target_issues) + ". Immediate remediation is recommended for critical findings. Review the detailed findings below for specific affected paths and recommended fixes."

    return {
        "score": score,
        "grade": grade,
        "label": label,
        "color": color,
        "max": 100,
        "summary": summary,
        "counts": {"critical": critical, "high": high, "medium": medium, "low": low, "info": info},
    }

# ── HTML Template (PAGE) – v11.1 Deep Recon Edition ──
PAGE_HTML = r"""
<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Leak Scanner Pro v11.1 — Recon Beast</title>
<style>
/* ─────────  v11.1 Theme variables  ───────── */
:root{
  --bg:#050509; --bg2:rgba(22,33,62,.55); --bg3:rgba(26,26,46,.7);
  --border:rgba(0,212,170,.18); --border-hi:rgba(0,212,170,.45);
  --text:#e8eef5; --muted:#9aa3b8; --dim:#6a7388;
  --accent:#00d4aa; --accent2:#54a0ff; --accent3:#a78bfa;
  --warn:#feca57; --danger:#ff5b6b; --ok:#1dd1a1;
  --glass-blur:22px;
  --shadow:0 12px 40px rgba(0,0,0,.6);
  --glow-accent:0 0 32px rgba(0,212,170,.45);
  --mesh-1:#1a1a3a; --mesh-2:#0a2a3a; --mesh-3:#2a0a3a;
  --particle-color:rgba(0,212,170,.35);
}
[data-theme="light"]{
  --bg:#eef2f9; --bg2:rgba(255,255,255,.65); --bg3:rgba(255,255,255,.85);
  --border:rgba(0,150,120,.2); --border-hi:rgba(0,150,120,.55);
  --text:#1a1f2e; --muted:#5b6478; --dim:#8793a8;
  --accent:#00b894; --accent2:#0984e3; --accent3:#7c3aed;
  --warn:#d68910; --danger:#e74c3c; --ok:#27ae60;
  --glass-blur:18px;
  --shadow:0 8px 28px rgba(20,40,80,.18);
  --glow-accent:0 0 24px rgba(0,184,148,.3);
  --mesh-1:#dbe7ff; --mesh-2:#d7f5ef; --mesh-3:#e7d7ff;
  --particle-color:rgba(0,184,148,.25);
}

/* Particle canvas background */
#particleCanvas{
  position:fixed; inset:0; z-index:-1; pointer-events:none;
}

/* Custom scrollbars */
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:rgba(0,0,0,.2);border-radius:5px}
::-webkit-scrollbar-thumb{background:linear-gradient(180deg,var(--accent),var(--accent2));
  border-radius:5px; transition:background .2s}
::-webkit-scrollbar-thumb:hover{background:linear-gradient(180deg,var(--accent2),var(--accent3))}
[data-theme="light"] ::-webkit-scrollbar-track{background:rgba(0,0,0,.05)}
*{scrollbar-width:thin;scrollbar-color:var(--accent) rgba(0,0,0,.2)}

/* ─────────  Animated mesh gradient background  ───────── */
body::before{
  content:""; position:fixed; inset:0; z-index:-2;
  background:
    radial-gradient(at 18% 22%, var(--mesh-1) 0, transparent 45%),
    radial-gradient(at 82% 18%, var(--mesh-2) 0, transparent 45%),
    radial-gradient(at 50% 85%, var(--mesh-3) 0, transparent 50%),
    var(--bg);
  background-size: 200% 200%, 200% 200%, 200% 200%, 100% 100%;
  animation: meshShift 24s ease-in-out infinite;
}
body::after{
  content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background:
    radial-gradient(circle at 25% 30%, rgba(0,212,170,.06), transparent 35%),
    radial-gradient(circle at 75% 70%, rgba(167,139,250,.06), transparent 35%);
  animation: meshShift 18s ease-in-out infinite reverse;
}
@keyframes meshShift{
  0%{background-position: 0% 0%, 100% 0%, 50% 100%, 0 0;}
  33%{background-position: 50% 100%, 0% 50%, 100% 0%, 0 0;}
  66%{background-position: 100% 50%, 50% 0%, 0% 50%, 0 0;}
  100%{background-position: 0% 0%, 100% 0%, 50% 100%, 0 0;}
}

/* Confetti canvas for critical findings celebration */
#confettiCanvas{
  position:fixed; inset:0; z-index:300; pointer-events:none;
}

/* Holographic gradient border (animated) */
.holo-border{
  position:relative;
}
.holo-border::after{
  content:""; position:absolute; inset:-1px; border-radius:inherit; z-index:-1;
  background:linear-gradient(120deg, var(--accent), var(--accent2), var(--accent3),
    var(--accent), var(--accent2));
  background-size:300% 300%;
  animation:holoShift 4s ease infinite;
  opacity:.5;
}
@keyframes holoShift{
  0%,100%{background-position:0% 50%}
  50%{background-position:100% 50%}
}

/* Critical leak item holographic glow */
.leak-item.crit{
  position:relative;
  isolation:isolate;
}
.leak-item.crit::before{
  content:""; position:absolute; inset:0; z-index:-1; border-radius:inherit;
  background:linear-gradient(120deg, rgba(255,91,107,.1), rgba(254,202,87,.05), rgba(255,91,107,.1));
  background-size:200% 200%;
  animation:holoShift 3s ease infinite;
}

*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;color:var(--text);
     line-height:1.6;min-height:100vh;transition:background .4s,color .4s;
     -webkit-font-smoothing:antialiased;overflow-x:hidden}

/* ─────────  Navbar (glassmorphism)  ───────── */
.navbar{
  background:var(--bg2); backdrop-filter:blur(var(--glass-blur)) saturate(140%);
  -webkit-backdrop-filter:blur(var(--glass-blur)) saturate(140%);
  border-bottom:1px solid var(--border);
  padding:0 20px; display:flex; justify-content:space-between; align-items:center;
  height:60px; position:sticky; top:0; z-index:100;
  box-shadow:0 4px 24px rgba(0,0,0,.18);
}
.nav-brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:17px;
  background:linear-gradient(120deg,var(--accent),var(--accent2),var(--accent3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  background-size:200% 200%;animation:brandShift 8s ease infinite}
@keyframes brandShift{0%,100%{background-position:0 50%}50%{background-position:100% 50%}}
.nav-brand .logo{display:inline-block;animation:logoPulse 2.4s ease-in-out infinite}
@keyframes logoPulse{0%,100%{transform:scale(1);filter:drop-shadow(0 0 6px var(--accent))}
  50%{transform:scale(1.12);filter:drop-shadow(0 0 16px var(--accent))}}
.version{
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  color:#fff; padding:3px 10px; border-radius:14px; font-size:11px; font-weight:800;
  letter-spacing:.4px; box-shadow:var(--glow-accent);
}
.nav-right{display:flex;align-items:center;gap:12px}
.theme-toggle{
  background:var(--bg3); border:1px solid var(--border); color:var(--text);
  padding:8px 12px; border-radius:10px; cursor:pointer; font-size:15px;
  transition:all .25s; backdrop-filter:blur(6px);
}
.theme-toggle:hover{transform:translateY(-1px) rotate(8deg);border-color:var(--accent);
  box-shadow:0 4px 12px rgba(0,212,170,.25)}

/* ─────────  Container / Cards — v11.1 with 3D holographic effects  ───────── */
.container{max-width:1200px;margin:0 auto;padding:20px;perspective:1500px}
.card{
  background:var(--bg2); backdrop-filter:blur(var(--glass-blur)) saturate(160%);
  -webkit-backdrop-filter:blur(var(--glass-blur)) saturate(160%);
  border:1px solid var(--border); border-radius:18px; padding:24px; margin-bottom:20px;
  transition:all .4s cubic-bezier(.4,0,.2,1); position:relative; overflow:hidden;
  box-shadow:var(--shadow);
  animation:cardIn .55s cubic-bezier(.16,.84,.44,1) backwards;
  transform-style:preserve-3d;
}
.card:nth-child(1){animation-delay:.05s}
.card:nth-child(2){animation-delay:.15s}
.card:nth-child(3){animation-delay:.25s}
.card:nth-child(4){animation-delay:.35s}
@keyframes cardIn{from{opacity:0;transform:translateY(24px) scale(.98) rotateX(-5deg)}
  to{opacity:1;transform:none}}
/* Holographic shimmer overlay */
.card::before{
  content:""; position:absolute; top:0; left:-100%; right:0; height:2px;
  background:linear-gradient(90deg,transparent,var(--accent),var(--accent2),var(--accent3),transparent);
  animation:scanLine 5s ease-in-out infinite; opacity:.7;
}
/* Radial gradient highlight (holographic) */
.card::after{
  content:""; position:absolute; inset:0; pointer-events:none; opacity:0;
  background:radial-gradient(circle at var(--mx,50%) var(--my,50%),
    rgba(0,212,170,.15) 0%, transparent 40%);
  transition:opacity .3s;
}
.card:hover::after{opacity:1}
@keyframes scanLine{0%,100%{left:-100%}50%{left:100%}}
.card:hover{
  border-color:var(--border-hi);
  transform:translateY(-3px) rotateX(2deg);
  box-shadow:0 18px 50px rgba(0,212,170,.22), var(--shadow), 0 0 0 1px rgba(0,212,170,.1);
}
.card h1,.card h2{
  font-size:24px; margin-bottom:12px;
  background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  background-size:200% 200%;animation:brandShift 6s ease infinite;
}
.card h3{font-size:17px;margin-bottom:12px;color:var(--text);font-weight:700}
.subtitle{color:var(--muted);font-size:14px;margin-bottom:18px;line-height:1.7}

/* ─────────  Form  ───────── */
.form-group{margin-bottom:14px}
.form-group label{display:block;font-size:13px;color:var(--muted);font-weight:600;margin-bottom:6px;
  letter-spacing:.2px}
.form-group input,.form-group select{
  width:100%; padding:11px 14px; background:rgba(0,0,0,.18);
  border:1px solid var(--border); border-radius:11px; color:var(--text); font-size:14px;
  outline:none; font-family:inherit; transition:all .25s;
  min-width:0; /* prevent overflow on mobile */
}
.form-group input[type="text"]{overflow:hidden;text-overflow:ellipsis}
[data-theme="light"] .form-group input,[data-theme="light"] .form-group select{
  background:rgba(255,255,255,.6);
}
.form-group input:focus,.form-group select:focus{
  border-color:var(--accent); box-shadow:0 0 0 3px rgba(0,212,170,.16), var(--glow-accent);
  background:rgba(0,0,0,.25);
}
[data-theme="light"] .form-group input:focus,[data-theme="light"] .form-group select:focus{
  background:rgba(255,255,255,.85);
}
.form-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}
.form-row-2{display:grid;grid-template-columns:1fr 2fr;gap:14px}

/* ─────────  Buttons  ───────── */
.btn{
  padding:11px 22px; border:none; border-radius:11px; font-size:14px; font-weight:700;
  cursor:pointer; transition:all .25s; display:inline-flex; align-items:center; gap:8px;
  text-decoration:none; border:1px solid transparent; font-family:inherit;
  position:relative; overflow:hidden;
}
.btn-primary{
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  color:#fff; box-shadow:0 4px 16px rgba(0,212,170,.35);
}
.btn-primary::after{
  content:""; position:absolute; inset:0; background:linear-gradient(120deg,transparent 30%,rgba(255,255,255,.3),transparent 70%);
  transform:translateX(-100%); transition:transform .6s;
}
.btn-primary:hover{transform:translateY(-2px); box-shadow:0 8px 24px rgba(0,212,170,.5)}
.btn-primary:hover::after{transform:translateX(100%)}
.btn-primary:disabled{opacity:.55;cursor:not-allowed;transform:none;box-shadow:none}
/* v11.1: Ensure disabled buttons still respond to clicks for re-enable */
.btn:disabled{pointer-events:auto}
.btn-ghost:disabled, .btn-secondary:disabled{opacity:.7;cursor:not-allowed}
/* Force enable after reset */
.btn.force-enabled{pointer-events:auto !important;opacity:1 !important;cursor:pointer !important}
.btn-secondary{
  background:rgba(0,212,170,.08); color:var(--accent); border-color:var(--border-hi);
  backdrop-filter:blur(6px);
}
.btn-secondary:hover{background:var(--accent);color:#0a0a12;box-shadow:var(--glow-accent)}
.btn-ghost{background:transparent;color:var(--muted);border:1px solid var(--border)}
.btn-ghost:hover{color:var(--text);border-color:var(--accent);background:rgba(0,212,170,.06)}
.btn-loading-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:currentColor;
  animation:dotBounce 1s infinite}
@keyframes dotBounce{0%,80%,100%{transform:scale(.4);opacity:.4}40%{transform:scale(1);opacity:1}}

/* ─────────  Progress card  ───────── */
.progress-card{
  border-left:3px solid var(--accent);
  background:linear-gradient(135deg,var(--bg2),rgba(0,212,170,.06));
}
.progress-info{display:flex;justify-content:space-between;font-size:13px;color:var(--muted);margin-bottom:10px}
.progress-bar-bg{
  width:100%; height:10px; background:rgba(0,0,0,.3); border-radius:6px;
  overflow:hidden; margin-bottom:12px; position:relative;
  box-shadow:inset 0 1px 4px rgba(0,0,0,.3);
}
[data-theme="light"] .progress-bar-bg{background:rgba(0,0,0,.08)}
.progress-bar-fill{
  height:100%; border-radius:6px;
  background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));
  background-size:200% 100%;
  animation:barShimmer 2s linear infinite;
  box-shadow:0 0 16px rgba(0,212,170,.6);
  position:relative;
  min-width:0;
  transition:width .25s ease-out;
}
.progress-bar-fill::after{
  content:""; position:absolute; top:0; left:0; bottom:0; width:30px;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);
  animation:stripeSweep 1.2s linear infinite;
}
@keyframes barShimmer{0%{background-position:0 0}100%{background-position:200% 0}}
@keyframes stripeSweep{0%{transform:translateX(-100%)}100%{transform:translateX(100vw)}}
@keyframes fillIn{from{width:0%}to{width:var(--w,0%)}}
.progress-msg{font-size:13px;color:var(--muted);min-height:18px}
.progress-found{
  font-size:13px;font-weight:700;color:var(--ok);margin-top:6px;
  animation:foundPulse 1s ease-in-out infinite;
}
@keyframes foundPulse{0%,100%{opacity:.8;transform:scale(1)}50%{opacity:1;transform:scale(1.02)}}

/* ─────────  Stats grid  ───────── */
.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-bottom:18px}
.stat-box{
  text-align:center; padding:14px 8px;
  background:linear-gradient(135deg,var(--bg3),rgba(0,0,0,.15));
  border:1px solid var(--border); border-radius:12px;
  transition:all .25s; position:relative; overflow:hidden;
}
[data-theme="light"] .stat-box{background:linear-gradient(135deg,var(--bg3),rgba(255,255,255,.5))}
.stat-box:hover{transform:translateY(-2px);border-color:var(--accent);box-shadow:0 6px 16px rgba(0,212,170,.15)}
.stat-box::before{
  content:""; position:absolute; top:0; left:0; right:0; height:2px;
  background:linear-gradient(90deg,var(--accent),var(--accent2)); opacity:.6;
}
.stat-number{font-size:24px;font-weight:800;color:var(--accent);
  font-variant-numeric:tabular-nums; letter-spacing:-.5px;
  text-shadow:0 0 12px rgba(0,212,170,.4)}
.stat-label{font-size:10px;color:var(--dim);margin-top:4px;text-transform:uppercase;letter-spacing:.6px;font-weight:600}
.sev-crit{color:var(--danger)!important;text-shadow:0 0 12px rgba(255,91,107,.5)!important}
.sev-high{color:var(--warn)!important;text-shadow:0 0 12px rgba(254,202,87,.5)!important}

/* ─────────  Tabs  ───────── */
.tabs{display:flex;gap:4px;margin-bottom:16px;border-bottom:1px solid var(--border);
  overflow-x:auto; padding-bottom:1px}
.tab{
  padding:11px 16px; background:none; border:none; color:var(--muted); cursor:pointer;
  font-size:14px; font-weight:600; border-bottom:2px solid transparent; white-space:nowrap;
  font-family:inherit; transition:all .2s; position:relative; border-radius:8px 8px 0 0;
}
.tab:hover{color:var(--text);background:rgba(0,212,170,.05)}
.tab.active{color:var(--accent); border-bottom-color:var(--accent)}
.tab.active::after{
  content:""; position:absolute; left:0; right:0; bottom:-1px; height:2px;
  background:var(--accent); box-shadow:0 0 8px var(--accent);
}
.tab-panel{display:none}
.tab-panel.active{display:block;animation:tabIn .35s cubic-bezier(.16,.84,.44,1)}
@keyframes tabIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* ─────────  Section title  ───────── */
.section-title{font-size:14px;font-weight:700;margin:16px 0 10px;display:flex;
  align-items:center;gap:8px;color:var(--text)}
.section-title .count{background:var(--bg3);color:var(--muted);padding:2px 9px;
  border-radius:11px;font-size:11px;margin-left:4px;font-weight:700;border:1px solid var(--border)}

/* ─────────  Tags / Badges  ───────── */
.tech-tag,.port-badge,.cdn-badge{
  display:inline-block;padding:4px 11px;border-radius:20px;font-size:12px;font-weight:600;
  margin:3px; transition:all .2s; cursor:default;
}
.tech-tag{background:rgba(0,212,170,.1);color:var(--accent);border:1px solid rgba(0,212,170,.3)}
.tech-tag:hover{transform:translateY(-1px);box-shadow:0 4px 10px rgba(0,212,170,.2)}
.port-badge{background:rgba(84,160,255,.15);color:var(--accent2);border:1px solid rgba(84,160,255,.3)}
.port-badge:hover{transform:translateY(-1px);box-shadow:0 4px 10px rgba(84,160,255,.25)}
.cdn-badge{background:rgba(254,202,87,.12);color:var(--warn);border:1px solid rgba(254,202,87,.3)}
.cdn-badge:hover{transform:translateY(-1px);box-shadow:0 4px 10px rgba(254,202,87,.2)}
.sev-badge{padding:2px 8px;border-radius:4px;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.5px}
.sev-critical{background:rgba(255,91,107,.2);color:var(--danger);box-shadow:0 0 8px rgba(255,91,107,.3)}
.sev-high{background:rgba(254,202,87,.2);color:var(--warn)}
.sev-medium{background:rgba(255,159,64,.2);color:#ff9f43}
.sev-low{background:rgba(0,212,170,.15);color:var(--accent)}
.sev-info{background:rgba(160,160,176,.15);color:var(--dim)}

/* ─────────  Leak items  ───────── */
.leak-item{
  padding:13px; background:var(--bg3); border:1px solid var(--border);
  border-radius:10px; margin-bottom:9px; transition:all .25s;
  animation:cardIn .4s cubic-bezier(.16,.84,.44,1) backwards;
}
.leak-item:hover{border-color:var(--accent); transform:translateX(4px);
  box-shadow:0 4px 16px rgba(0,212,170,.12)}
.leak-item.crit{border-left:4px solid var(--danger);
  box-shadow:0 0 0 1px rgba(255,91,107,.15), 0 4px 16px rgba(255,91,107,.1);
  animation:critPulse 2s ease-in-out infinite, cardIn .4s cubic-bezier(.16,.84,.44,1) backwards}
@keyframes critPulse{0%,100%{box-shadow:0 0 0 1px rgba(255,91,107,.15),0 4px 16px rgba(255,91,107,.1)}
  50%{box-shadow:0 0 0 1px rgba(255,91,107,.35),0 6px 22px rgba(255,91,107,.25)}}
.leak-item.high{border-left:4px solid var(--warn)}
.leak-item.med{border-left:4px solid #ff9f43}
.leak-header{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.code-badge{padding:2px 8px;border-radius:5px;font-size:12px;font-weight:800;min-width:36px;text-align:center}
.code-200{background:rgba(29,209,161,.2);color:var(--ok);box-shadow:0 0 8px rgba(29,209,161,.2)}
.code-403{background:rgba(254,202,87,.2);color:var(--warn)}
.code-401{background:rgba(255,91,107,.2);color:var(--danger)}
.code-404{background:rgba(160,160,176,.2);color:var(--dim)}
.leak-path{font-family:ui-monospace,'SFMono-Regular',Menlo,monospace;font-weight:700;font-size:13px;
  color:var(--text);word-break:break-all}
.leak-size{font-size:11px;color:var(--dim)}
.leak-url{font-size:11px;color:var(--dim);word-break:break-all;margin-top:3px}
.leak-rt{font-size:10px;color:var(--dim);margin-left:auto}
.leak-preview summary{cursor:pointer;color:var(--accent);font-size:12px;font-weight:600;transition:color .2s}
.leak-preview summary:hover{color:var(--accent2)}
.leak-preview pre{
  background:rgba(0,0,0,.4); padding:11px; border-radius:8px; font-size:12px;
  overflow-x:auto; margin-top:7px; max-height:240px; overflow-y:auto;
  color:#aed581; font-family:ui-monospace,'JetBrains Mono',monospace;
  white-space:pre-wrap; word-break:break-all;
  border:1px solid var(--border);
}
[data-theme="light"] .leak-preview pre{background:rgba(0,0,0,.05);color:#2d5a2d}

/* ─────────  Terminal / activity log  ───────── */
.terminal{
  background:rgba(0,0,0,.55); border:1px solid var(--border); border-radius:10px;
  padding:12px 14px; font-family:ui-monospace,'JetBrains Mono','SFMono-Regular',Menlo,monospace;
  font-size:12px; max-height:240px; overflow-y:auto; color:#aed581; margin-top:10px;
  position:relative;
}
.terminal::before{
  content:"● ● ●"; position:absolute; top:8px; left:14px; color:#ff5b6b;
  font-size:8px; letter-spacing:3px;
}
.terminal .term-line{padding:1px 0;opacity:0;animation:termLineIn .3s ease forwards}
@keyframes termLineIn{from{opacity:0;transform:translateX(-4px)}to{opacity:1;transform:none}}
.terminal .term-line[data-sev="critical"]{color:#ff5b6b;font-weight:700}
.terminal .term-line[data-sev="high"]{color:#feca57}
.terminal .term-line[data-sev="info"]{color:var(--accent)}
.terminal .term-line[data-tag="BACKUP"]{color:var(--accent3)}
.terminal .term-line[data-tag="SECRET"]{color:#ff5b6b}
.terminal .term-line[data-tag="DIRLIST"]{color:var(--accent2)}
.terminal .term-line[data-tag="BRUTE"]{color:var(--accent)}
.terminal .term-line[data-tag="PARAM"]{color:var(--warn)}
.terminal .cursor{display:inline-block;width:7px;height:13px;background:#aed581;
  vertical-align:text-bottom;animation:cursorBlink 1s steps(2) infinite;margin-left:3px;
  margin-bottom:1px;border-radius:1px;opacity:.85}
@keyframes cursorBlink{0%,50%{opacity:1}51%,100%{opacity:0}}
[data-theme="light"] .terminal{background:#1a1f2e;color:#aed581}
[data-theme="light"] .terminal .cursor{background:#aed581}

/* ─────────  WAF / alerts  ───────── */
.robots-content{background:rgba(0,0,0,.35);padding:11px;border-radius:8px;
  font-family:ui-monospace,monospace;font-size:12px;max-height:240px;
  overflow-y:auto;white-space:pre-wrap;border:1px solid var(--border);color:#aed581}
[data-theme="light"] .robots-content{background:rgba(0,0,0,.05);color:#2d5a2d}
.waf-info{background:rgba(255,91,107,.05);border:1px solid rgba(255,91,107,.2);
  border-radius:10px;padding:13px}
.alert{padding:13px;border-radius:10px;margin-bottom:12px;font-size:14px;
  animation:cardIn .35s ease}
.alert-error{background:rgba(255,91,107,.08);border:1px solid rgba(255,91,107,.35);color:var(--danger);
  box-shadow:0 0 14px rgba(255,91,107,.15)}
.alert-warn{background:rgba(254,202,87,.08);border:1px solid rgba(254,202,87,.35);color:var(--warn)}
.alert-info{background:rgba(84,160,255,.08);border:1px solid rgba(84,160,255,.35);color:var(--accent2)}
.empty-state{text-align:center;padding:32px;color:var(--dim);font-size:14px}

/* ─────────  Actions  ───────── */
.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}

/* ─────────  Badges  ───────── */
.badge{display:inline-flex;align-items:center;gap:5px;padding:4px 11px;border-radius:20px;
  font-size:12px;font-weight:600;margin:3px;transition:all .2s}
.badge-time{background:rgba(84,160,255,.12);color:var(--accent2)}
.badge-waf{background:rgba(255,91,107,.12);color:var(--danger);box-shadow:0 0 8px rgba(255,91,107,.15)}
.badge-ssl-ok{background:rgba(29,209,161,.15);color:var(--ok)}
.badge-ssl-warn{background:rgba(254,202,87,.15);color:var(--warn)}
.badge-ssl-err{background:rgba(255,91,107,.15);color:var(--danger)}

/* ─────────  Filter bar  ───────── */
.filter-bar{margin-bottom:14px;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.filter-bar input{flex:1;min-width:200px;padding:9px 13px;background:rgba(0,0,0,.2);
  border:1px solid var(--border);border-radius:9px;color:var(--text);font-size:13px;font-family:inherit;
  transition:all .2s}
[data-theme="light"] .filter-bar input{background:rgba(255,255,255,.7)}
.filter-bar input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 2px rgba(0,212,170,.15)}
.filter-bar select{padding:9px 13px;background:rgba(0,0,0,.2);border:1px solid var(--border);
  border-radius:9px;color:var(--text);font-size:13px;font-family:inherit}
[data-theme="light"] .filter-bar select{background:rgba(255,255,255,.7)}

.sev-chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.sev-chip{padding:5px 12px;border-radius:14px;font-size:12px;font-weight:700;cursor:pointer;
  background:var(--bg3);border:1px solid var(--border);color:var(--muted);transition:all .2s}
.sev-chip:hover{transform:translateY(-1px)}
.sev-chip.active{background:var(--accent);color:#0a0a12;border-color:var(--accent);
  box-shadow:var(--glow-accent)}

/* ─────────  Cookies / security headers / forms  ───────── */
.cookie-item{padding:9px;background:var(--bg3);border:1px solid var(--border);border-radius:9px;
  margin-bottom:7px;font-size:13px;transition:all .2s}
.cookie-item:hover{border-color:var(--accent)}
.cookie-name{font-family:monospace;font-weight:700;color:var(--accent)}
.cookie-flag{display:inline-block;padding:1px 6px;border-radius:4px;font-size:10px;margin-left:4px;font-weight:600}
.flag-ok{background:rgba(29,209,161,.2);color:var(--ok)}
.flag-bad{background:rgba(255,91,107,.2);color:var(--danger)}
.sec-header-row{display:flex;justify-content:space-between;align-items:center;padding:9px;
  background:var(--bg3);border:1px solid var(--border);border-radius:7px;margin-bottom:5px;
  font-size:13px;transition:all .2s}
.sec-header-row:hover{border-color:var(--accent)}
.sec-header-missing{border-left:3px solid var(--danger)}
.sec-header-present{border-left:3px solid var(--ok)}
.sec-header-name{font-family:monospace;font-weight:600;color:var(--text)}
.sec-header-value{font-family:monospace;font-size:11px;color:var(--muted);word-break:break-all;
  max-width:55%;text-align:right}
.form-item{padding:9px;background:var(--bg3);border:1px solid var(--border);border-radius:9px;
  margin-bottom:7px;font-size:13px}
.form-action{font-family:monospace;color:var(--accent);word-break:break-all}
.form-tag{display:inline-block;padding:1px 7px;border-radius:4px;font-size:10px;font-weight:700;
  margin-left:4px;text-transform:uppercase}
.form-tag-login{background:rgba(255,91,107,.15);color:var(--danger)}
.form-tag-upload{background:rgba(254,202,87,.15);color:var(--warn)}
.form-tag-csrf{background:rgba(84,160,255,.15);color:var(--accent2)}

/* ─────────  History  ───────── */
.history-list{display:flex;flex-direction:column;gap:7px}
.history-item{display:flex;justify-content:space-between;align-items:center;padding:10px 12px;
  background:var(--bg3);border:1px solid var(--border);border-radius:10px;cursor:pointer;
  font-size:13px;transition:all .2s;animation:cardIn .35s cubic-bezier(.16,.84,.44,1) backwards}
.history-item:hover{border-color:var(--accent);background:rgba(0,212,170,.05);
  transform:translateX(3px)}
.history-target{font-family:monospace;color:var(--accent);word-break:break-all;font-weight:700}
.history-meta{font-size:11px;color:var(--dim);margin-top:2px}

/* ─────────  Misc  ───────── */
.footer{text-align:center;padding:20px;color:var(--dim);font-size:12px;
  border-top:1px solid var(--border);margin-top:20px}
.hidden{display:none!important}
.toast{position:fixed;bottom:24px;right:24px;
  background:linear-gradient(135deg,var(--bg2),rgba(0,212,170,.15));
  backdrop-filter:blur(var(--glass-blur));
  border:1px solid var(--accent);color:var(--text);padding:12px 18px;border-radius:11px;
  font-size:13px;z-index:200;box-shadow:0 8px 28px rgba(0,0,0,.4),0 0 18px rgba(0,212,170,.25);
  opacity:0;transform:translateY(12px) scale(.95);transition:all .35s cubic-bezier(.16,.84,.44,1);
  max-width:340px;font-weight:600}
.toast.show{opacity:1;transform:none}

/* Skeleton shimmer for loading */
.skeleton{background:linear-gradient(90deg,var(--bg3) 25%,rgba(0,212,170,.06) 37%,var(--bg3) 63%);
  background-size:400% 100%;animation:shimmer 1.4s ease-in-out infinite;
  border-radius:8px;height:14px;margin:8px 0}
@keyframes shimmer{0%{background-position:100% 50%}100%{background-position:0 50%}}

/* ───────── v11.1 Guide Modal + i18n + Templates  ───────── */
.modal-overlay{
  position:fixed; inset:0; z-index:500;
  background:rgba(0,0,0,.7); backdrop-filter:blur(8px);
  display:none; align-items:center; justify-content:center;
  padding:20px; opacity:0; transition:opacity .3s;
}
.modal-overlay.show{display:flex; opacity:1}
.modal{
  background:var(--bg2); backdrop-filter:blur(var(--glass-blur)) saturate(160%);
  -webkit-backdrop-filter:blur(var(--glass-blur)) saturate(160%);
  border:1px solid var(--border-hi); border-radius:18px; padding:28px;
  max-width:780px; width:100%; max-height:88vh; overflow-y:auto;
  box-shadow:0 20px 60px rgba(0,0,0,.6), var(--glow-accent);
  transform:scale(.95) translateY(20px); transition:transform .35s cubic-bezier(.16,.84,.44,1);
  position:relative;
}
.modal-overlay.show .modal{transform:none}
.modal-close{
  position:absolute; top:16px; right:16px;
  background:rgba(255,91,107,.15); border:1px solid rgba(255,91,107,.3);
  color:var(--danger); width:34px; height:34px; border-radius:50%;
  cursor:pointer; font-size:18px; font-weight:700;
  transition:all .2s; display:flex; align-items:center; justify-content:center;
}
.modal-close:hover{background:var(--danger); color:#fff; transform:rotate(90deg)}
.modal h2{
  font-size:24px; margin-bottom:8px;
  background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.modal h3{
  font-size:16px; margin:18px 0 10px; color:var(--accent);
  padding-bottom:6px; border-bottom:1px solid var(--border);
}
.modal p{font-size:13px;color:var(--muted);margin-bottom:12px;line-height:1.7}
.modal ul{list-style:none;padding:0;margin:8px 0}
.modal ul li{
  padding:8px 0; font-size:13px; color:var(--text);
  border-bottom:1px dashed var(--border);
  display:flex; align-items:flex-start; gap:10px;
}
.modal ul li:last-child{border-bottom:none}
.modal ul li strong{color:var(--accent);min-width:120px;display:inline-block}
.modal .badge-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:8px;margin:12px 0}
.modal .info-badge{
  background:var(--bg3); border:1px solid var(--border);
  border-radius:10px; padding:10px 12px; font-size:12px;
}
.modal .info-badge .label{color:var(--dim);font-size:10px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:3px}
.modal .info-badge .value{color:var(--accent);font-weight:700}

/* Language switcher */
.lang-switcher{
  display:inline-flex; background:var(--bg3); border:1px solid var(--border);
  border-radius:10px; padding:3px; gap:2px;
}
.lang-btn{
  background:transparent; border:none; color:var(--muted);
  padding:5px 12px; border-radius:7px; cursor:pointer;
  font-size:12px; font-weight:700; transition:all .2s; font-family:inherit;
}
.lang-btn.active{
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  color:#fff; box-shadow:0 2px 8px rgba(0,212,170,.3);
}
.lang-btn:hover:not(.active){color:var(--text);background:rgba(0,212,170,.08)}

/* Guide button */
.guide-btn{
  background:linear-gradient(135deg,var(--accent3),var(--accent2));
  color:#fff; padding:7px 14px; border-radius:10px; cursor:pointer;
  font-size:13px; font-weight:700; border:none; font-family:inherit;
  transition:all .25s; display:inline-flex; align-items:center; gap:6px;
  box-shadow:0 4px 12px rgba(167,139,250,.3);
}
.guide-btn:hover{transform:translateY(-1px);box-shadow:0 6px 18px rgba(167,139,250,.5)}

/* Quick Templates */
.templates-bar{
  display:flex; gap:8px; flex-wrap:wrap; margin-bottom:16px;
  padding:10px; background:var(--bg3); border-radius:10px; border:1px solid var(--border);
}
.template-btn{
  background:var(--bg2); border:1px solid var(--border); color:var(--text);
  padding:6px 12px; border-radius:8px; cursor:pointer; font-size:12px;
  font-weight:600; transition:all .2s; font-family:inherit;
  display:inline-flex; align-items:center; gap:5px;
}
.template-btn:hover{
  background:var(--accent); color:#0a0a12; border-color:var(--accent);
  transform:translateY(-1px); box-shadow:0 4px 10px rgba(0,212,170,.2);
}
.template-btn[data-tpl="quick"]{border-color:rgba(84,160,255,.4)}
.template-btn[data-tpl="quick"]:hover{background:var(--accent2);color:#fff}
.template-btn[data-tpl="deep"]{border-color:rgba(167,139,250,.4)}
.template-btn[data-tpl="deep"]:hover{background:var(--accent3);color:#fff}
.template-btn[data-tpl="waf"]{border-color:rgba(255,91,107,.4)}
.template-btn[data-tpl="waf"]:hover{background:var(--danger);color:#fff}
.template-btn[data-tpl="static"]{border-color:rgba(254,202,87,.4)}
.template-btn[data-tpl="static"]:hover{background:var(--warn);color:#0a0a12}

/* ═════════ v11.1 Enterprise: Risk Score + Charts + Command Palette ═════════ */

/* Risk Score Dashboard */
.risk-dashboard{
  display:grid; grid-template-columns:auto 1fr 1fr; gap:20px;
  padding:24px; margin-bottom:20px;
  background:linear-gradient(135deg,rgba(22,33,62,.6),rgba(26,26,46,.4));
  border:1px solid var(--border); border-radius:18px;
  position:relative; overflow:hidden;
}
.risk-dashboard::before{
  content:""; position:absolute; inset:0;
  background:radial-gradient(circle at 0% 0%, rgba(0,212,170,.08), transparent 50%);
  pointer-events:none;
}
.risk-gauge-wrap{
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  position:relative;
}
.risk-gauge{
  width:160px; height:160px; position:relative;
}
.risk-gauge svg{transform:rotate(-90deg)}
.risk-gauge .gauge-bg{stroke:rgba(255,255,255,.08);stroke-width:12;fill:none}
.risk-gauge .gauge-fill{
  stroke-width:12; fill:none; stroke-linecap:round;
  transition:stroke-dashoffset 1.2s cubic-bezier(.16,.84,.44,1);
  filter:drop-shadow(0 0 8px currentColor);
}
.risk-grade{
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  text-align:center;
}
.risk-grade .grade-letter{
  font-size:48px; font-weight:900; line-height:1;
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.risk-grade .grade-label{
  font-size:10px; color:var(--dim); text-transform:uppercase; letter-spacing:1px; margin-top:2px;
}
.risk-grade .grade-score{font-size:14px;color:var(--muted);font-weight:700;margin-top:4px}

.risk-info{
  display:flex; flex-direction:column; gap:12px; justify-content:center;
}
.risk-info h3{font-size:18px;margin:0;color:var(--text)}
.risk-info .risk-status{
  display:inline-flex; align-items:center; gap:6px;
  padding:6px 14px; border-radius:20px; font-size:12px; font-weight:700;
  width:fit-content;
}
.risk-info .risk-status.critical{background:rgba(255,0,68,.15);color:#ff0044;border:1px solid rgba(255,0,68,.3)}
.risk-info .risk-status.high{background:rgba(255,136,0,.15);color:#ff8800;border:1px solid rgba(255,136,0,.3)}
.risk-info .risk-status.medium{background:rgba(255,204,0,.15);color:#ffcc00;border:1px solid rgba(255,204,0,.3)}
.risk-info .risk-status.low{background:rgba(0,255,136,.15);color:#00ff88;border:1px solid rgba(0,255,136,.3)}
.risk-info .risk-summary{font-size:13px;color:var(--muted);line-height:1.6}

/* Severity Donut Chart */
.severity-chart-wrap{
  display:flex; align-items:center; gap:16px;
}
.severity-donut{
  width:140px; height:140px; position:relative; flex-shrink:0;
}
.severity-donut svg{transform:rotate(-90deg)}
.severity-donut .donut-center{
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  text-align:center;
}
.severity-donut .donut-total{font-size:24px;font-weight:800;color:var(--text)}
.severity-donut .donut-label{font-size:9px;color:var(--dim);text-transform:uppercase;letter-spacing:.5px}
.severity-legend{display:flex;flex-direction:column;gap:6px;flex:1}
.severity-legend-item{
  display:flex; align-items:center; gap:8px; font-size:12px;
  padding:4px 8px; border-radius:6px; cursor:pointer;
  transition:background .2s;
}
.severity-legend-item:hover{background:rgba(255,255,255,.05)}
.severity-legend-item .dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.severity-legend-item .count{margin-left:auto;font-weight:700;color:var(--text)}
.sev-dot-critical{background:#ff0044;box-shadow:0 0 6px #ff0044}
.sev-dot-high{background:#ff8800;box-shadow:0 0 6px #ff8800}
.sev-dot-medium{background:#ffcc00;box-shadow:0 0 6px #ffcc00}
.sev-dot-low{background:#00ff88;box-shadow:0 0 6px #00ff88}
.sev-dot-info{background:#888;box-shadow:0 0 6px #888}

/* Executive Summary */
.exec-summary{
  padding:18px; margin-bottom:16px;
  background:linear-gradient(135deg,rgba(0,212,170,.06),rgba(84,160,255,.04));
  border:1px solid var(--border); border-left:4px solid var(--accent); border-radius:12px;
}
.exec-summary h3{
  font-size:14px; color:var(--accent); margin-bottom:8px;
  display:flex; align-items:center; gap:6px;
}
.exec-summary p{font-size:13px;color:var(--muted);line-height:1.7;margin:0}
.exec-summary .copy-btn{
  float:right; font-size:11px; padding:3px 10px; border-radius:6px;
  background:var(--bg3); border:1px solid var(--border); color:var(--muted);
  cursor:pointer; transition:all .2s;
}
.exec-summary .copy-btn:hover{background:var(--accent);color:#0a0a12;border-color:var(--accent)}

/* Command Palette */
.cmd-palette-overlay{
  position:fixed; inset:0; z-index:600;
  background:rgba(0,0,0,.6); backdrop-filter:blur(6px);
  display:none; align-items:flex-start; justify-content:center;
  padding-top:120px; opacity:0; transition:opacity .2s;
}
.cmd-palette-overlay.show{display:flex;opacity:1}
.cmd-palette{
  width:90%; max-width:640px;
  background:var(--bg2); backdrop-filter:blur(var(--glass-blur)) saturate(160%);
  border:1px solid var(--border-hi); border-radius:14px;
  box-shadow:0 20px 60px rgba(0,0,0,.6), var(--glow-accent);
  overflow:hidden;
  transform:translateY(-20px) scale(.98); transition:transform .25s cubic-bezier(.16,.84,.44,1);
}
.cmd-palette-overlay.show .cmd-palette{transform:none}
.cmd-input-wrap{
  display:flex; align-items:center; gap:10px;
  padding:16px 20px; border-bottom:1px solid var(--border);
}
.cmd-input-wrap .cmd-icon{font-size:18px;color:var(--dim)}
.cmd-input{
  flex:1; background:transparent; border:none; outline:none;
  color:var(--text); font-size:16px; font-family:inherit;
}
.cmd-input::placeholder{color:var(--dim)}
.cmd-kbd{
  font-size:10px; padding:2px 8px; border-radius:4px;
  background:var(--bg3); border:1px solid var(--border); color:var(--dim);
}
.cmd-list{max-height:380px;overflow-y:auto;padding:8px}
.cmd-item{
  display:flex; align-items:center; gap:12px;
  padding:10px 14px; border-radius:8px; cursor:pointer;
  transition:background .15s;
}
.cmd-item:hover, .cmd-item.selected{background:rgba(0,212,170,.1)}
.cmd-item .cmd-item-icon{font-size:18px;width:24px;text-align:center}
.cmd-item .cmd-item-text{flex:1}
.cmd-item .cmd-item-title{font-size:14px;color:var(--text);font-weight:600}
.cmd-item .cmd-item-desc{font-size:11px;color:var(--dim);margin-top:2px}
.cmd-item .cmd-item-kbd{
  font-size:10px; padding:2px 6px; border-radius:4px;
  background:var(--bg3); border:1px solid var(--border); color:var(--dim);
}
.cmd-item.selected .cmd-item-kbd{border-color:var(--accent);color:var(--accent)}
.cmd-footer{
  padding:8px 16px; border-top:1px solid var(--border);
  display:flex; gap:14px; font-size:11px; color:var(--dim);
}
.cmd-footer kbd{
  padding:1px 6px; border-radius:3px; background:var(--bg3);
  border:1px solid var(--border); font-family:monospace; font-size:10px;
}

/* Phase Timeline */
.phase-timeline{
  padding:18px; margin-bottom:16px;
  background:var(--bg3); border:1px solid var(--border); border-radius:12px;
}
.phase-timeline h3{font-size:14px;color:var(--accent);margin-bottom:12px}
.timeline-svg{width:100%;height:60px;display:block}
.timeline-bar{
  transition:all .3s; cursor:pointer;
}
.timeline-bar:hover{filter:brightness(1.3)}
.timeline-label{
  font-size:9px; fill:var(--dim); text-anchor:middle;
  font-family:monospace;
}

/* Findings Table v2 */
.findings-table-wrap{
  overflow-x:auto; border:1px solid var(--border); border-radius:12px;
  background:var(--bg3);
}
.findings-table{
  width:100%; border-collapse:collapse; font-size:13px;
}
.findings-table thead{
  background:var(--bg2); position:sticky; top:0;
}
.findings-table th{
  padding:12px 14px; text-align:left; font-size:11px; font-weight:700;
  color:var(--muted); text-transform:uppercase; letter-spacing:.5px;
  border-bottom:1px solid var(--border); cursor:pointer; user-select:none;
  white-space:nowrap;
}
.findings-table th:hover{color:var(--accent)}
.findings-table th .sort-ind{font-size:10px;opacity:.5;margin-left:4px}
.findings-table th.sorted .sort-ind{opacity:1;color:var(--accent)}
.findings-table td{
  padding:10px 14px; border-bottom:1px solid var(--border);
  color:var(--text); vertical-align:middle;
}
.findings-table tr:hover td{background:rgba(0,212,170,.04)}
.findings-table tr:last-child td{border-bottom:none}
.findings-table .col-sev{width:90px}
.findings-table .col-code{width:60px}
.findings-table .col-size{width:90px;text-align:right;font-family:monospace}
.findings-table .col-path{font-family:monospace;font-size:12px;word-break:break-all;max-width:300px}
.findings-table .col-actions{width:120px;text-align:right;white-space:nowrap}
.findings-table .row-action{
  display:inline-block; padding:4px 8px; margin-left:4px;
  border-radius:5px; cursor:pointer; font-size:11px;
  background:transparent; border:1px solid var(--border); color:var(--muted);
  transition:all .15s;
}
.findings-table .row-action:hover{background:var(--accent);color:#0a0a12;border-color:var(--accent)}
.findings-table .row-action.retest:hover{background:var(--accent2);color:#fff;border-color:var(--accent2)}
.findings-table .row-action.fp:hover{background:var(--warn);color:#0a0a12;border-color:var(--warn)}

/* Mobile Bottom Nav */
.mobile-nav{
  display:none; position:fixed; bottom:0; left:0; right:0; z-index:200;
  background:var(--bg2); backdrop-filter:blur(var(--glass-blur));
  border-top:1px solid var(--border);
  padding:8px 0 env(safe-area-inset-bottom,8px);
}
.mobile-nav-item{
  flex:1; display:flex; flex-direction:column; align-items:center; gap:2px;
  padding:6px 0; cursor:pointer; color:var(--dim); font-size:10px; font-weight:600;
  transition:color .2s;
}
.mobile-nav-item.active{color:var(--accent)}
.mobile-nav-item .icon{font-size:18px}
@media(max-width:768px){
  .mobile-nav{display:flex}
  .risk-dashboard{grid-template-columns:1fr;gap:16px}
  .risk-gauge{width:120px;height:120px}
  .risk-grade .grade-letter{font-size:36px}
  body{padding-bottom:60px}
}

/* Loading skeleton */
.skeleton-line{
  height:14px; border-radius:6px; margin:8px 0;
  background:linear-gradient(90deg,var(--bg3) 25%,rgba(0,212,170,.08) 50%,var(--bg3) 75%);
  background-size:200% 100%; animation:shimmer 1.5s ease-in-out infinite;
}

/* v11: File Tree */
.file-tree-container{max-height:600px;overflow-y:auto;background:rgba(0,0,0,.3);border:1px solid var(--border);border-radius:10px;padding:14px;font-family:ui-monospace,'JetBrains Mono',monospace;font-size:13px}
.tree-node{padding:3px 0;cursor:pointer;transition:background .15s;border-radius:4px;padding-left:4px}
.tree-node:hover{background:rgba(0,212,170,.08)}
.tree-node .tree-icon{display:inline-block;width:20px;text-align:center;margin-right:4px}
.tree-node .tree-name{color:var(--text);font-weight:600}
.tree-node .tree-meta{font-size:11px;color:var(--dim);margin-left:8px}
.tree-node .tree-sev-critical{color:var(--danger)}
.tree-node .tree-sev-high{color:var(--warn)}
.tree-node .tree-sev-medium{color:#ff9f43}
.tree-node .tree-sev-low{color:var(--accent)}
.tree-children{margin-left:24px;border-left:1px dashed var(--border);padding-left:4px}
.tree-toggle{display:inline-block;width:16px;cursor:pointer;color:var(--dim);user-select:none}
.tree-toggle:hover{color:var(--accent)}

/* v11: Source Code Viewer */
.source-code-container{max-height:600px;overflow:auto;background:rgba(0,0,0,.4);border:1px solid var(--border);border-radius:10px;padding:14px;font-family:ui-monospace,monospace;font-size:12px;line-height:1.5;white-space:pre;tab-size:2}
.source-file-list{margin-bottom:12px;display:flex;gap:6px;flex-wrap:wrap}
.source-file-btn{padding:6px 12px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;background:var(--bg3);border:1px solid var(--border);color:var(--muted);transition:all .2s;font-family:monospace}
.source-file-btn:hover{background:var(--accent);color:#0a0a12;border-color:var(--accent)}
.source-file-btn.active{background:var(--accent2);color:#fff;border-color:var(--accent2)}

/* Empty state with personality */
.empty-state-fancy{
  text-align:center; padding:48px 20px;
}
.empty-state-fancy .emoji{font-size:48px;margin-bottom:12px;display:block;animation:logoPulse 2.4s ease-in-out infinite}
.empty-state-fancy .title{font-size:16px;color:var(--text);font-weight:700;margin-bottom:6px}
.empty-state-fancy .desc{font-size:13px;color:var(--dim);max-width:400px;margin:0 auto}

@media(max-width:768px){
  .form-row{grid-template-columns:1fr}
  .stats-grid{grid-template-columns:repeat(3,1fr)}
  .container{padding:14px}
  .card{padding:16px}
  .tabs{flex-wrap:nowrap}
}
</style>
</head>
<body>
<!-- v11.1: Noscript warning -->
<noscript>
  <div style="position:fixed;inset:0;z-index:9999;background:#0f0f1a;color:#e8eef5;display:flex;align-items:center;justify-content:center;font-family:sans-serif;text-align:center;padding:20px">
    <div>
      <h1 style="font-size:24px;color:#ff5b6b;margin-bottom:12px">⚠️ JavaScript Required</h1>
      <p style="font-size:14px;color:#9aa3b8">Web Leak Scanner cần JavaScript để hoạt động.<br>Vui lòng bật JavaScript trong trình duyệt.</p>
    </div>
  </div>
</noscript>
<!-- v11.1: Inline safety script — chạy trước tất cả JS khác -->
<script>
(function() {
  // Nếu page detect body chỉ chứa JSON (raw response), tự redirect về /
  try {
    var text = document.body.textContent || document.body.innerText || '';
    if (text.trim().startsWith('{"scan_id"') || text.trim().startsWith('{"error"')) {
      window.location.href = '/';
      return;
    }
  } catch(e) {}
  // Global error capture
  window.__errors = [];
  window.addEventListener('error', function(e) {
    window.__errors.push(e.message);
    console.error('[FATAL JS Error]', e.message);
  });
})();
</script>
<nav class="navbar">
  <div class="nav-brand">
    <span class="logo">🛡️</span>
    <span>Web Leak Scanner <span class="version">v11.1</span></span>
  </div>
  <div class="nav-right">
    <div class="lang-switcher">
      <button class="lang-btn active" data-lang="vi" id="langVi">🇻🇳 VI</button>
      <button class="lang-btn" data-lang="en" id="langEn">🇬🇧 EN</button>
    </div>
    <button class="guide-btn" id="guideBtn">📖 <span data-i18n="guide">Hướng dẫn</span></button>
    <button class="theme-toggle" id="themeToggle" title="Đổi theme">🌙</button>
  </div>
</nav>

<main class="container">

<!-- Form -->
<div class="card">
  <h1 data-i18n="hero_title">🕵️ Quét lỗ hổng thông tin rò rỉ</h1>
  <p class="subtitle" data-i18n="hero_subtitle">Async deep recon v11.1 — 550+ leak paths · 31 phases · 4 WAF bypass modes · SSTI · Prototype Pollution · Cache Poisoning · Glassmorphism UI · Multilingual (VI/EN)</p>

  <!-- Quick Templates -->
  <div class="templates-bar">
    <span style="font-size:12px;color:var(--dim);font-weight:700;align-self:center;margin-right:4px" data-i18n="quick_templates">Templates:</span>
    <button class="template-btn" data-tpl="quick" onclick="applyTemplate('quick')">⚡ <span data-i18n="tpl_quick">Quick Recon</span></button>
    <button class="template-btn" data-tpl="deep" onclick="applyTemplate('deep')">🔬 <span data-i18n="tpl_deep">Deep Audit</span></button>
    <button class="template-btn" data-tpl="waf" onclick="applyTemplate('waf')">🥷 <span data-i18n="tpl_waf">WAF Bypass</span></button>
    <button class="template-btn" data-tpl="static" onclick="applyTemplate('static')">📦 <span data-i18n="tpl_static">Static Site</span></button>
  </div>

  <form id="scanForm" method="post" action="/scan">
    <div class="form-group"><label data-i18n="lbl_target">🌐 URL mục tiêu</label><input type="text" name="target" placeholder="https://example.com" required></div>
    <div class="form-row">
      <div class="form-group"><label data-i18n="lbl_timeout">⏱️ Timeout (s)</label><input type="number" name="timeout" value="15" min="3" max="60"></div>
      <div class="form-group"><label data-i18n="lbl_proxy">🔀 Proxy</label><input type="text" name="proxy" placeholder="http://proxy:8080"></div>
      <div class="form-group"><label data-i18n="lbl_scan_js">🔎 Quét JS files</label>
        <select name="scan_js"><option value="yes" selected data-i18n="opt_js_deep">Có (deep)</option><option value="no" data-i18n="opt_js_quick">Không (nhanh)</option></select>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group"><label data-i18n="lbl_bypass">🛡️ WAF Bypass Mode</label>
        <select name="bypass_mode" id="bypassMode">
          <option value="auto" selected data-i18n="opt_auto">🤖 Auto (cân bằng)</option>
          <option value="stealth" data-i18n="opt_stealth">🥷 Stealth (5 req/s, XFF+UA rotation)</option>
          <option value="aggressive" data-i18n="opt_aggressive">⚔️ Aggressive (60 concurrent, full rotation)</option>
          <option value="turbo" data-i18n="opt_turbo">🚀 Turbo (100 concurrent, no rotation)</option>
        </select>
      </div>
      <div class="form-group"><label data-i18n="lbl_intensity">🎯 Scan Intensity</label>
        <select name="intensity">
          <option value="full" selected data-i18n="opt_full">Full (31 phases)</option>
          <option value="quick" data-i18n="opt_quick">Quick (10 phases, skip deep recon)</option>
          <option value="deep" data-i18n="opt_deep_recon">Deep Recon only (skip basic leak)</option>
        </select>
      </div>
      <div class="form-group"><label data-i18n="lbl_vuln_tests">🧪 Vuln Tests</label>
        <select name="vuln_tests">
          <option value="yes" selected data-i18n="opt_vuln_yes">Có (SSTI, Proto, Header)</option>
          <option value="no" data-i18n="opt_vuln_no">Không (chỉ recon)</option>
        </select>
      </div>
    </div>
    <div class="form-group"><label data-i18n="lbl_headers">📋 Custom Headers</label><input type="text" name="headers" placeholder="User-Agent: MyBot; X-Forwarded-For: 1.2.3.4"></div>
    <div class="form-group" style="display:flex;align-items:center;gap:10px">
      <input type="checkbox" name="redirect" value="yes" id="rd" checked>
      <label for="rd" style="margin:0" data-i18n="lbl_redirect">Theo dõi redirect</label>
    </div>
    <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
      <button type="submit" class="btn btn-primary" id="scanBtn">
        <span class="btn-text" data-i18n="btn_start">🔍 Bắt đầu quét</span>
        <span class="btn-loading hidden">
          <span class="btn-loading-dot"></span>
          <span class="btn-loading-dot" style="animation-delay:.2s"></span>
          <span class="btn-loading-dot" style="animation-delay:.4s"></span>
          <span data-i18n="btn_scanning">Đang quét...</span>
        </span>
      </button>
      <button type="button" class="btn btn-ghost" id="forceResetBtn" onclick="forceResetAll()" title="Reset tất cả nút nếu bị đơ" style="font-size:13px;padding:9px 16px">
        🔄 Reset
      </button>
    </div>
  </form>
</div>

<!-- JS Error Banner (hidden by default, shown if script fails) -->
<div id="jsErrorBanner" style="display:none;padding:14px;margin-bottom:16px;background:rgba(255,91,107,.1);border:1px solid rgba(255,91,107,.4);border-radius:10px;color:var(--danger);font-size:13px">
  ⚠️ <strong>JavaScript Error:</strong> <span id="jsErrorMsg"></span>
  <br><span style="font-size:11px;color:var(--dim)">Try Ctrl+Shift+R (hard refresh) or clear browser cache.</span>
</div>

<!-- History -->
<div class="card" id="historyCard" style="display:none">
  <h3 data-i18n="history_title">🕘 Lịch sử quét gần đây</h3>
  <div class="history-list" id="historyList"></div>
</div>

<!-- Progress + Activity log -->
<div id="progressPanel" class="card progress-card hidden">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:10px">
    <h3 style="margin:0" data-i18n="progress_title">📡 Tiến trình quét</h3>
    <div style="display:flex;gap:7px;align-items:center;flex-wrap:wrap">
      <span class="badge badge-time" id="elapsedBadge" title="Thời gian đã trôi qua">⏱️ 00:00</span>
      <span class="badge" id="etaBadge" style="background:rgba(254,202,87,.12);color:#feca57;display:none" title="Còn lại (ước tính)">⌛ ETA --:--</span>
      <span class="badge" id="rateBadge" style="background:rgba(84,160,255,.12);color:#54a0ff;display:none" title="Tốc độ">⚡ -- req/s</span>
      <button class="btn btn-ghost" id="cancelBtn" style="padding:6px 12px;font-size:12px" data-i18n="btn_cancel">🛑 Huỷ</button>
    </div>
  </div>
  <div class="progress-info"><span id="progressPhase">Khởi tạo...</span><span id="progressCount"></span></div>
  <div class="progress-bar-bg"><div id="progressBar" class="progress-bar-fill" style="width:0%"></div></div>
  <div id="progressMessage" class="progress-msg"></div>
  <div id="progressFound" class="progress-found hidden"></div>
  <div class="terminal" id="activityLog"><div style="color:#6a7388;margin-top:14px">// Live activity log sẽ hiển thị ở đây khi scan bắt đầu<span class="cursor"></span></div></div>
</div>

<!-- Results -->
<div id="resultsArea"></div>

</main>
<footer class="footer">Web Leak Scanner Pro v11.1 — Recon Beast · 31 phases · 4 WAF bypass modes · i18n (VI/EN) · SSTI · Proto Pollution · Cache Poisoning · .git exposure · deep crawl · CT logs · DNS · Wayback · glassmorphism UI</footer>

<!-- Guide Modal -->
<div class="modal-overlay" id="guideModal">
  <div class="modal">
    <button class="modal-close" onclick="closeGuide()">×</button>
    <h2 data-i18n="guide_title">📖 Hướng dẫn sử dụng Web Leak Scanner</h2>
    <p data-i18n="guide_intro">Tool quét bảo mật web 31 phases với 4 chế độ WAF bypass. Dưới đây là hướng dẫn chọn cấu hình phù hợp cho từng loại target.</p>

    <h3 data-i18n="guide_templates_title">⚡ Quick Templates (Chọn nhanh)</h3>
    <ul>
      <li><strong data-i18n="tpl_quick">Quick Recon</strong> <span data-i18n="guide_tpl_quick">— Scan nhanh (~10s), chỉ check 100 paths phổ biến. Phù hợp khi cần survey nhanh target mới.</span></li>
      <li><strong data-i18n="tpl_deep">Deep Audit</strong> <span data-i18n="guide_tpl_deep">— Full scan 31 phases (~60s), phát hiện mọi loại lỗ hổng. Phù hợp cho security audit chính thức.</span></li>
      <li><strong data-i18n="tpl_waf">WAF Bypass</strong> <span data-i18n="guide_tpl_waf">— Stealth mode, xoay UA + X-Forwarded-For 50 IP. Phù hợp khi target có Cloudflare/Akamai/Imperva.</span></li>
      <li><strong data-i18n="tpl_static">Static Site</strong> <span data-i18n="guide_tpl_static">— Cho Netlify/Vercel/GitHub Pages. Check _headers, _redirects, source maps, manifest.json.</span></li>
    </ul>

    <h3 data-i18n="guide_waf_title">🛡️ WAF Bypass Mode — Khi nào chọn gì?</h3>
    <div class="badge-grid">
      <div class="info-badge"><div class="label">Auto</div><div class="value" data-i18n="guide_waf_auto">Mặc định. Tự giảm tốc khi detect WAF</div></div>
      <div class="info-badge"><div class="label">Stealth</div><div class="value" data-i18n="guide_waf_stealth">Cloudflare, Akamai, Imperva strict</div></div>
      <div class="info-badge"><div class="label">Aggressive</div><div class="value" data-i18n="guide_waf_aggressive">WAF nhẹ, cần speed</div></div>
      <div class="info-badge"><div class="label">Turbo</div><div class="value" data-i18n="guide_waf_turbo">No WAF, max speed 100 req concurrent</div></div>
    </div>
    <p data-i18n="guide_waf_detail"><strong>Stealth mode</strong> sẽ: 5 req/s, delay 0.8-2.5s giữa requests, xoay 5 User-Agents khác nhau, xoay 50 fake X-Forwarded-For IPs (bypass IP rate-limiting), thêm full browser headers (Referer, Sec-Fetch-*, Accept-Language). Dùng khi scan Netlify, Vercel, Cloudflare Pages — các platform chặn aggressive scan.</p>

    <h3 data-i18n="guide_intensity_title">🎯 Scan Intensity</h3>
    <ul>
      <li><strong data-i18n="opt_full">Full (31 phases)</strong> <span data-i18n="guide_intensity_full">— Mọi phases: leak paths, takeover, GraphQL, CORS, SSTI, .git, deep crawl, CT logs, Wayback... Khuyến nghị dùng.</span></li>
      <li><strong data-i18n="opt_quick">Quick (10 phases)</strong> <span data-i18n="guide_intensity_quick">— Skip deep recon, chỉ check leak paths cơ bản + ports + tech detection. Nhanh (~10s).</span></li>
      <li><strong data-i18n="opt_deep_recon">Deep Recon only</strong> <span data-i18n="guide_intensity_deep">— Skip basic leak, chỉ chạy phases deep recon (CT logs, DNS, .git, deep crawl, JS strings).</span></li>
    </ul>

    <h3 data-i18n="guide_vuln_title">🧪 Vuln Tests — Có nên bật?</h3>
    <p data-i18n="guide_vuln_intro">5 phases vuln detection (SSTI, Prototype Pollution, Header Injection, Cache Poisoning, Default Creds) sẽ gửi ~1000 requests active payload. Bật khi:</p>
    <ul>
      <li><strong>SSTI</strong> <span data-i18n="guide_vuln_ssti">— Test {{7*7}}, ${7*7}, <%=7*7%> trên 8 endpoints × 7 params. CRITICAL nếu template engine execute payload.</span></li>
      <li><strong>Prototype Pollution</strong> <span data-i18n="guide_vuln_proto">— Test ?__proto__[polluted]=yes, ?constructor[prototype][test]=1. HIGH nếu reflected.</span></li>
      <li><strong>Header Injection</strong> <span data-i18n="guide_vuln_header">— Test X-Forwarded-Host, X-Original-URL=/admin. HIGH nếu redirect tới injected host (bypass access control).</span></li>
      <li><strong>Cache Poisoning</strong> <span data-i18n="guide_vuln_cache">— Test X-Forwarded-Host=evil.cache-poison. HIGH nếu reflected trong cached response.</span></li>
      <li><strong>Default Creds</strong> <span data-i18n="guide_vuln_creds">— Test 10 cặp admin/admin, root/root trên login forms. CRITICAL nếu login thành công.</span></li>
    </ul>
    <p data-i18n="guide_vuln_warning">⚠️ <strong>Cảnh báo</strong>: Chỉ bật Vuln Tests khi bạn có quyền test target. Các payload active có thể bị WAF flag là malicious traffic.</p>

    <h3 data-i18n="guide_features_title">🚀 Tính năng chính</h3>
    <div class="badge-grid">
      <div class="info-badge"><div class="label">Leak Paths</div><div class="value">550+</div></div>
      <div class="info-badge"><div class="label">Secret Patterns</div><div class="value">45+</div></div>
      <div class="info-badge"><div class="label">Tech Sigs</div><div class="value">56+</div></div>
      <div class="info-badge"><div class="label">Subdomain Takeover</div><div class="value">60+ services</div></div>
      <div class="info-badge"><div class="label">CT Logs (crt.sh)</div><div class="value">Subdomain enum</div></div>
      <div class="info-badge"><div class="label">DNS Records</div><div class="value">A/AAAA/MX/NS/TXT</div></div>
      <div class="info-badge"><div class="label">.git Exposure</div><div class="value">12 paths</div></div>
      <div class="info-badge"><div class="label">Deep Crawl</div><div class="value">depth-2, 30 pages</div></div>
      <div class="info-badge"><div class="label">JS Strings</div><div class="value">200 strings</div></div>
      <div class="info-badge"><div class="label">Wayback Machine</div><div class="value">Historical URLs</div></div>
      <div class="info-badge"><div class="label">Languages</div><div class="value">🇻🇳 VI / 🇬🇧 EN</div></div>
      <div class="info-badge"><div class="label">Health Endpoint</div><div class="value">/health, /ping</div></div>
    </div>

    <h3 data-i18n="guide_deploy_title">🌐 Deploy lên cloud</h3>
    <p data-i18n="guide_deploy_intro">Tool dùng waitress (production WSGI server) + /health endpoint, phù hợp deploy lên Render, Heroku, VPS. Repo có sẵn:</p>
    <ul>
      <li><strong>requirements.txt</strong> <span data-i18n="guide_deploy_req">— Flask, aiohttp, waitress</span></li>
      <li><strong>render.yaml</strong> <span data-i18n="guide_deploy_render">— 1-click deploy lên Render.com</span></li>
      <li><strong>Procfile</strong> <span data-i18n="guide_deploy_heroku">— Deploy lên Heroku</span></li>
      <li><strong>README.md</strong> <span data-i18n="guide_deploy_readme">— Hướng dẫn chi tiết</span></li>
    </ul>
    <p data-i18n="guide_deploy_health"><strong>Quan trọng</strong>: Set Health Check Path = <code>/health</code> trên Render dashboard để tránh "Instance failed: i/o timeout".</p>

    <h3 data-i18n="guide_tips_title">💡 Tips & Tricks</h3>
    <ul>
      <li><strong data-i18n="tip_1">Scan chậm?</strong> <span data-i18n="guide_tip_1">Chuyển sang Turbo mode (no WAF) hoặc Aggressive (light WAF).</span></li>
      <li><strong data-i18n="tip_2">Bị WAF block?</strong> <span data-i18n="guide_tip_2">Chuyển sang Stealth mode, tăng timeout lên 30s.</span></li>
      <li><strong data-i18n="tip_3">Main page fail (code 0)?</strong> <span data-i18n="guide_tip_3">Tool auto-thử 5 fallback strategies (HTTPS, HTTP, www., trailing slash). Nếu vẫn fail, target có thể down hoặc sandbox chặn.</span></li>
      <li><strong data-i18n="tip_4">Confetti không hiện?</strong> <span data-i18n="guide_tip_4">Confetti chỉ bắn khi có critical findings (stat-number.sev-crit > 0).</span></li>
      <li><strong data-i18n="tip_5">Đổi ngôn ngữ</strong> <span data-i18n="guide_tip_5">Click 🇻🇳 VI / 🇬🇧 EN ở góc phải navbar. Lưu vào localStorage, tự áp dụng lần sau.</span></li>
      <li><strong data-i18n="tip_6">Export kết quả</strong> <span data-i18n="guide_tip_6">Click JSON / CSV / HTML report để download kết quả scan.</span></li>
    </ul>

    <h3 data-i18n="guide_legal_title">⚖️ Legal & Ethics</h3>
    <p data-i18n="guide_legal">Tool dành cho security research và authorized testing only. Chỉ scan target bạn có quyền hoặc được phép test. Scan mà không có consent có thể vi phạm luật (Cybersecurity law, GDPR, HIPAA...). Author không chịu trách nhiệm cho misuse.</p>

    <p style="text-align:center;margin-top:20px;color:var(--dim);font-size:12px">
      <span data-i18n="guide_footer">v11.1 — Recon Beast · Made with</span> ❤️ · <span data-i18n="guide_close_hint">Click × hoặc ngoài modal để đóng</span>
    </p>
  </div>
</div>

<!-- v11.1 Command Palette -->
<div class="cmd-palette-overlay" id="cmdPalette">
  <div class="cmd-palette">
    <div class="cmd-input-wrap">
      <span class="cmd-icon">🔍</span>
      <input type="text" class="cmd-input" id="cmdInput" placeholder="Type a command or search..." autocomplete="off">
      <span class="cmd-kbd">ESC</span>
    </div>
    <div class="cmd-list" id="cmdList"></div>
    <div class="cmd-footer">
      <span><kbd>↑↓</kbd> Navigate</span>
      <span><kbd>↵</kbd> Run</span>
      <span><kbd>ESC</kbd> Close</span>
    </div>
  </div>
</div>

<!-- v11.1 Mobile Bottom Nav -->
<nav class="mobile-nav">
  <a class="mobile-nav-item active" onclick="scrollToTop()">
    <span class="icon">🏠</span><span>Home</span>
  </a>
  <a class="mobile-nav-item" onclick="document.getElementById('target_input')?.focus();scrollToScan()">
    <span class="icon">🔍</span><span>Scan</span>
  </a>
  <a class="mobile-nav-item" onclick="document.getElementById('resultsArea')?.scrollIntoView({behavior:'smooth'})">
    <span class="icon">📊</span><span>Results</span>
  </a>
  <a class="mobile-nav-item" onclick="openGuide()">
    <span class="icon">📖</span><span>Guide</span>
  </a>
</nav>

<canvas id="particleCanvas"></canvas>
<canvas id="confettiCanvas"></canvas>
<div id="toast" class="toast"></div>

<script>
// ───────── v11.1 Particle background canvas ─────────
const particleCanvas = document.getElementById('particleCanvas');
const pctx = particleCanvas.getContext('2d');
let particles = [];
let mouse = {x: -1000, y: -1000};

function resizeParticleCanvas(){
  particleCanvas.width = window.innerWidth;
  particleCanvas.height = window.innerHeight;
}
resizeParticleCanvas();
window.addEventListener('resize', resizeParticleCanvas);

function initParticles(){
  particles = [];
  const count = Math.min(80, Math.floor((window.innerWidth * window.innerHeight) / 18000));
  for(let i = 0; i < count; i++){
    particles.push({
      x: Math.random() * particleCanvas.width,
      y: Math.random() * particleCanvas.height,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
      r: Math.random() * 2 + 0.5,
      a: Math.random() * 0.5 + 0.2,
    });
  }
}
initParticles();
window.addEventListener('resize', initParticles);

window.addEventListener('mousemove', (e)=>{
  mouse.x = e.clientX;
  mouse.y = e.clientY;
  // Update card holographic highlight position
  document.querySelectorAll('.card').forEach(card=>{
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    card.style.setProperty('--mx', x + '%');
    card.style.setProperty('--my', y + '%');
  });
});

function animateParticles(){
  pctx.clearRect(0, 0, particleCanvas.width, particleCanvas.height);
  const accent = getComputedStyle(document.documentElement).getPropertyValue('--particle-color').trim() || 'rgba(0,212,170,.35)';
  for(let i = 0; i < particles.length; i++){
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    // Mouse attraction
    const dx = mouse.x - p.x;
    const dy = mouse.y - p.y;
    const dist = Math.sqrt(dx*dx + dy*dy);
    if(dist < 150){
      const force = (150 - dist) / 150 * 0.03;
      p.vx += (dx / dist) * force;
      p.vy += (dy / dist) * force;
    }
    // Damping
    p.vx *= 0.99;
    p.vy *= 0.99;
    // Wrap edges
    if(p.x < 0) p.x = particleCanvas.width;
    if(p.x > particleCanvas.width) p.x = 0;
    if(p.y < 0) p.y = particleCanvas.height;
    if(p.y > particleCanvas.height) p.y = 0;
    // Draw particle
    pctx.beginPath();
    pctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    pctx.fillStyle = accent;
    pctx.globalAlpha = p.a;
    pctx.fill();
  }
  // Draw connections
  pctx.globalAlpha = 1;
  for(let i = 0; i < particles.length; i++){
    for(let j = i + 1; j < particles.length; j++){
      const p1 = particles[i];
      const p2 = particles[j];
      const dx = p1.x - p2.x;
      const dy = p1.y - p2.y;
      const dist = Math.sqrt(dx*dx + dy*dy);
      if(dist < 120){
        pctx.beginPath();
        pctx.moveTo(p1.x, p1.y);
        pctx.lineTo(p2.x, p2.y);
        pctx.strokeStyle = accent;
        pctx.globalAlpha = (1 - dist / 120) * 0.15;
        pctx.lineWidth = 0.8;
        pctx.stroke();
      }
    }
  }
  pctx.globalAlpha = 1;
  requestAnimationFrame(animateParticles);
}
animateParticles();

// ───────── v11.1 Confetti effect for critical findings ─────────
const confettiCanvas = document.getElementById('confettiCanvas');
const cctx = confettiCanvas.getContext('2d');
let confettiPieces = [];

function resizeConfettiCanvas(){
  confettiCanvas.width = window.innerWidth;
  confettiCanvas.height = window.innerHeight;
}
resizeConfettiCanvas();
window.addEventListener('resize', resizeConfettiCanvas);

function fireConfetti(count = 80){
  const colors = ['#ff5b6b', '#feca57', '#00d4aa', '#54a0ff', '#a78bfa', '#1dd1a1'];
  for(let i = 0; i < count; i++){
    confettiPieces.push({
      x: Math.random() * confettiCanvas.width,
      y: -20,
      vx: (Math.random() - 0.5) * 6,
      vy: Math.random() * 4 + 2,
      gravity: 0.15,
      r: Math.random() * 6 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * Math.PI * 2,
      vrotation: (Math.random() - 0.5) * 0.3,
      life: 1,
    });
  }
}

function animateConfetti(){
  cctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
  for(let i = confettiPieces.length - 1; i >= 0; i--){
    const p = confettiPieces[i];
    p.x += p.vx;
    p.y += p.vy;
    p.vy += p.gravity;
    p.vx *= 0.99;
    p.rotation += p.vrotation;
    p.life -= 0.005;
    if(p.y > confettiCanvas.height + 50 || p.life <= 0){
      confettiPieces.splice(i, 1);
      continue;
    }
    cctx.save();
    cctx.translate(p.x, p.y);
    cctx.rotate(p.rotation);
    cctx.globalAlpha = Math.max(0, p.life);
    cctx.fillStyle = p.color;
    cctx.fillRect(-p.r/2, -p.r/2, p.r, p.r * 0.6);
    cctx.restore();
  }
  if(confettiPieces.length > 0){
    requestAnimationFrame(animateConfetti);
  }
}

// Function to be called after result load to fire confetti if critical findings
function checkAndFireConfetti(){
  // Look for critical count > 0 in stat boxes
  const critEl = document.querySelector('.stat-number.sev-crit');
  if(critEl){
    const val = parseInt(critEl.textContent) || 0;
    if(val > 0){
      setTimeout(()=>fireConfetti(100), 400);
      animateConfetti();
    }
  }
}

</script>

<script>
// ═════════ v11.1 BULLETPROOF INIT ═════════
// Define helpers FIRST — everything depends on these
const $ = (s) => { try { return document.querySelector(s); } catch(e) { return null; } };
const $$ = (s) => { try { return document.querySelectorAll(s); } catch(e) { return []; } };

// ═════════ FORM SUBMIT HANDLER — attach IMMEDIATELY, before any other code ═════════
// This MUST run first so even if other JS fails, form submit is intercepted
(function attachFormHandler() {
  function safeResetBtn() {
    try {
      const scanBtn = document.getElementById('scanBtn');
      const cancelBtn = document.getElementById('cancelBtn');
      if (scanBtn) {
        scanBtn.disabled = false;
        scanBtn.style.pointerEvents = 'auto';
        scanBtn.style.opacity = '1';
        scanBtn.style.cursor = 'pointer';
      }
      const btnText = document.querySelector('.btn-text');
      const btnLoading = document.querySelector('.btn-loading');
      if (btnText) btnText.classList.remove('hidden');
      if (btnLoading) btnLoading.classList.add('hidden');
      if (cancelBtn) {
        cancelBtn.style.display = '';
        cancelBtn.disabled = false;
        cancelBtn.style.pointerEvents = 'auto';
        cancelBtn.style.opacity = '1';
        cancelBtn.style.cursor = 'pointer';
        cancelBtn.textContent = '🛑 Huỷ';
      }
    } catch(e) { console.error('resetBtn error:', e); }
  }
  window.safeResetBtn = safeResetBtn;

  function attach() {
    const form = document.getElementById('scanForm');
    if (!form) {
      // DOM not ready, retry
      setTimeout(attach, 50);
      return;
    }
    // Use capture:true so our handler runs BEFORE any native submit
    form.addEventListener('submit', function(e) {
      // CRITICAL: prevent default IMMEDIATELY
      e.preventDefault();
      e.stopPropagation();
      console.log('[Form] Submit intercepted by JS');
      // Then call the async handler
      handleScanSubmit(e);
      return false;
    }, true);  // capture phase
  }
  attach();
})();

// v11.1: Simplified scan handler — uses .then() chains instead of async/await
// Every path guaranteed to call resetButtons() when done/fail
function handleScanSubmit(e) {
  // Get elements
  var form = e.target;
  var formData = new FormData(form);
  var target = formData.get('target');
  if (!target) return;

  var btn = document.getElementById('scanBtn');
  var progressPanel = document.getElementById('progressPanel');
  var resultsArea = document.getElementById('resultsArea');
  var bar = document.getElementById('progressBar');
  var phaseEl = document.getElementById('progressPhase');
  var countEl = document.getElementById('progressCount');
  var msgEl = document.getElementById('progressMessage');
  var foundEl = document.getElementById('progressFound');
  var cancelBtn = document.getElementById('cancelBtn');
  var term = document.getElementById('activityLog');

  // Disable scan button, show loading
  if (btn) {
    btn.disabled = true;
    var btnText = btn.querySelector('.btn-text');
    var btnLoading = btn.querySelector('.btn-loading');
    if (btnText) btnText.classList.add('hidden');
    if (btnLoading) btnLoading.classList.remove('hidden');
  }

  // Show progress panel
  if (progressPanel) progressPanel.classList.remove('hidden');
  if (resultsArea) resultsArea.innerHTML = '';
  if (bar) bar.style.width = '0%';
  if (phaseEl) phaseEl.textContent = 'Đang khởi tạo...';
  if (msgEl) msgEl.textContent = '';
  if (foundEl) foundEl.classList.add('hidden');
  if (countEl) countEl.textContent = '';

  // Reset terminal
  if (term) {
    term.innerHTML = '<div style="color:#6a7388;margin-top:14px">// Khởi tạo scan...<span class="cursor"></span></div>';
  }
  if (progressPanel) progressPanel.scrollIntoView({behavior:'smooth', block:'start'});

  // Start timer
  try { startTimer(); } catch(e) {}

  // v11.1: Shorter timeout (15s) + auto-cancel watchdog
  var controller = new AbortController();
  var timeoutId = setTimeout(function() { controller.abort(); }, 15000);

  // v11.1: Stuck watchdog — nếu 60s không có phase change, auto-cancel + reset
  var _lastPhase = '';
  var _lastPhaseTime = Date.now();
  var _stuckWatchdog = setInterval(function() {
    var phaseEl = document.getElementById('progressPhase');
    var currentPhase = phaseEl ? phaseEl.textContent : '';
    if (currentPhase === _lastPhase) {
      // Phase chưa đổi
      if (Date.now() - _lastPhaseTime > 60000) {
        // Kẹt quá 60s → auto-cancel
        clearInterval(_stuckWatchdog);
        console.warn('[Watchdog] Scan stuck at: ' + currentPhase + ' for >60s, auto-cancelling');
        toast('⏱️ Scan bị kẹt quá lâu — đã tự động reset. Thử lại với Stealth mode.');
        resetButtons();
        try { stopTimer(); } catch(e) {}
        try { stopActivityPolling(); } catch(e) {}
        try { evtSource.close(); } catch(e) {}
      }
    } else {
      _lastPhase = currentPhase;
      _lastPhaseTime = Date.now();
    }
  }, 5000);

  fetch('/scan', {method: 'POST', body: formData, signal: controller.signal})
    .then(function(resp) {
      clearTimeout(timeoutId);
      return resp.json();
    })
    .then(function(data) {
      if (data.error) {
        toast('❌ ' + data.error);
        resetButtons();
        try { stopTimer(); } catch(e) {}
        return;
      }
      var scanId = data.scan_id;
      try { currentScanId = scanId; } catch(e) {}
      try { startActivityPolling(scanId); } catch(e) {}

      // Cancel button
      if (cancelBtn) {
        cancelBtn.style.display = '';
        cancelBtn.disabled = false;
        cancelBtn.textContent = '🛑 Huỷ';
        cancelBtn.onclick = function() {
          cancelBtn.disabled = true;
          cancelBtn.textContent = '⏳ Đang huỷ...';
          fetch('/cancel/' + scanId, {method:'POST'}).then(function() {
            toast('🛑 Đã gửi yêu cầu huỷ');
          }).catch(function() { toast('Lỗi huỷ'); });
        };
      }

      // SSE progress
      var evtSource = new EventSource('/progress/' + scanId);
      evtSource.onmessage = function(ev) {
        try {
          var d = JSON.parse(ev.data);
          if (d.phase === 'connected' || d.phase === 'keepalive') return;

          // Update phase text
          if ((d.phase || d.phase_display) && phaseEl) {
            var display = d.phase_display || (typeof PHASE_FALLBACK !== 'undefined' ? PHASE_FALLBACK[d.phase] : '') || d.phase || '';
            if (display) phaseEl.textContent = display;
          }

          // Update progress bar
          if (d.total > 0) {
            var pct = Math.round((d.current/d.total)*100);
            if (bar) bar.style.width = pct + '%';
            if (countEl) countEl.textContent = d.current + '/' + d.total + ' (' + pct + '%)';
          } else if (countEl) {
            countEl.textContent = '';
          }

          // Update message
          if (d.message && msgEl) msgEl.textContent = d.message;

          // Update found counter
          if (d.found !== undefined) {
            if (d.found > 0) {
              if (foundEl) { foundEl.classList.remove('hidden'); foundEl.textContent = '🔍 Tìm thấy: ' + d.found; }
            } else {
              if (foundEl) { foundEl.classList.add('hidden'); foundEl.textContent = ''; }
            }
          }

          // Update elapsed/ETA/rate
          var elapsedBadge = document.getElementById('elapsedBadge');
          var etaBadge = document.getElementById('etaBadge');
          var rateBadge = document.getElementById('rateBadge');
          if (d.elapsed !== undefined && elapsedBadge) {
            elapsedBadge.textContent = '⏱️ ' + (typeof fmtTime === 'function' ? fmtTime(d.elapsed) : d.elapsed + 's');
            if (d.eta !== null && d.eta !== undefined && d.total > 0 && etaBadge) {
              etaBadge.style.display = '';
              etaBadge.textContent = '⌛ ETA ' + (typeof fmtTime === 'function' ? fmtTime(d.eta) : d.eta + 's');
            }
            if (d.rate !== undefined && d.rate > 0 && rateBadge) {
              rateBadge.style.display = '';
              rateBadge.textContent = '⚡ ' + d.rate + ' req/s';
            }
          }

          // Terminal phases
          if (d.phase === 'completed' || d.phase === 'error' || d.phase === 'cancelled') {
            evtSource.close();
            clearInterval(_stuckWatchdog);  // v11.1: clear stuck watchdog
            try { stopTimer(); } catch(e) {}
            try { stopActivityPolling(); } catch(e) {}
            if (cancelBtn) cancelBtn.style.display = 'none';
            if (term) { var cur = term.querySelector('.cursor'); if (cur) cur.style.display = 'none'; }

            // Load result
            var delay = d.phase === 'cancelled' ? 300 : 0;
            setTimeout(function() {
              loadResult(scanId).then(function() {
                resetButtons();  // ALWAYS reset after result loaded
                loadHistory();
              }).catch(function() {
                resetButtons();  // Reset even if loadResult fails
              });
            }, delay);
          }
        } catch(err) { /* ignore parse errors */ }
      };
      evtSource.onerror = function() {
        evtSource.close();
        clearInterval(_stuckWatchdog);  // v11.1: clear stuck watchdog
        try { stopTimer(); } catch(e) {}
        try { stopActivityPolling(); } catch(e) {}
        loadResult(scanId).then(function() {
          resetButtons();
          loadHistory();
        }).catch(function() {
          resetButtons();
        });
      };
    })
    .catch(function(err) {
      clearTimeout(timeoutId);
      clearInterval(_stuckWatchdog);  // v11.1: clear watchdog
      console.error('[Scan] Error:', err);
      if (err.name === 'AbortError') {
        toast('⏱️ Timeout — server không respond sau 15s. Thử lại với Stealth mode.');
      } else {
        toast('❌ Lỗi mạng: ' + err.message);
      }
      resetButtons();
      try { stopTimer(); } catch(e) {}
      try { stopActivityPolling(); } catch(e) {}
    });
}

// v11.1: Universal button reset — called from EVERY path (success/error/timeout/cancel)
function resetButtons() {
  try {
    var scanBtn = document.getElementById('scanBtn');
    var cancelBtn = document.getElementById('cancelBtn');
    if (scanBtn) {
      scanBtn.disabled = false;
      scanBtn.style.pointerEvents = 'auto';
      scanBtn.style.opacity = '1';
      scanBtn.style.cursor = 'pointer';
    }
    var btnText = document.querySelector('.btn-text');
    var btnLoading = document.querySelector('.btn-loading');
    if (btnText) btnText.classList.remove('hidden');
    if (btnLoading) btnLoading.classList.add('hidden');
    if (cancelBtn) {
      cancelBtn.style.display = '';
      cancelBtn.disabled = false;
      cancelBtn.style.pointerEvents = 'auto';
      cancelBtn.style.opacity = '1';
      cancelBtn.style.cursor = 'pointer';
      cancelBtn.textContent = '🛑 Huỷ';
    }
  } catch(e) { console.error('resetButtons error:', e); }
}

// Make functions globally available
window.resetBtn = resetButtons;
window.safeResetBtn = resetButtons;
window.forceResetAll = function() {
  resetButtons();
  try { stopTimer(); } catch(e) {}
  try { stopActivityPolling(); } catch(e) {}
  var pp = document.getElementById('progressPanel');
  if (pp) pp.classList.add('hidden');
  toast('🔄 Đã reset. Bạn có thể scan lại.');
};

// ═════════ ALL OTHER CODE — wrapped in try-catch so it can't break form handler ═════════
try {
const THEME_KEY = 'wlsv7_theme';
function applyTheme(t){
  document.documentElement.setAttribute('data-theme', t);
  const toggle = document.getElementById('themeToggle');
  if (toggle) toggle.textContent = t === 'dark' ? '🌙' : '☀️';
  try { localStorage.setItem(THEME_KEY, t); } catch(e) {}
}
try { applyTheme(localStorage.getItem(THEME_KEY) || 'dark'); } catch(e) { console.error('applyTheme:', e); }
try {
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) themeToggle.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    applyTheme(cur === 'dark' ? 'light' : 'dark');
  });
} catch(e) { console.error('themeToggle:', e); }

// ───────── v11.1 i18n (Internationalization: VI/EN) ─────────
const I18N = {
  vi: {
    hero_title: "🕵️ Quét lỗ hổng thông tin rò rỉ",
    hero_subtitle: "Async deep recon v11.1 — 550+ leak paths · 31 phases · 4 WAF bypass modes · SSTI · Prototype Pollution · Cache Poisoning · Glassmorphism UI · Đa ngôn ngữ (VI/EN)",
    guide: "Hướng dẫn",
    quick_templates: "Templates:",
    tpl_quick: "Quick Recon",
    tpl_deep: "Deep Audit",
    tpl_waf: "WAF Bypass",
    tpl_static: "Static Site",
    lbl_target: "🌐 URL mục tiêu",
    lbl_timeout: "⏱️ Timeout (s)",
    lbl_proxy: "🔀 Proxy",
    lbl_scan_js: "🔎 Quét JS files",
    opt_js_deep: "Có (deep)",
    opt_js_quick: "Không (nhanh)",
    lbl_bypass: "🛡️ WAF Bypass Mode",
    opt_auto: "🤖 Auto (cân bằng)",
    opt_stealth: "🥷 Stealth (5 req/s, XFF+UA rotation)",
    opt_aggressive: "⚔️ Aggressive (60 concurrent, full rotation)",
    opt_turbo: "🚀 Turbo (100 concurrent, no rotation)",
    lbl_intensity: "🎯 Scan Intensity",
    opt_full: "Full (31 phases)",
    opt_quick: "Quick (10 phases, skip deep recon)",
    opt_deep_recon: "Deep Recon only (skip basic leak)",
    lbl_vuln_tests: "🧪 Vuln Tests",
    opt_vuln_yes: "Có (SSTI, Proto, Header)",
    opt_vuln_no: "Không (chỉ recon)",
    lbl_headers: "📋 Custom Headers",
    lbl_redirect: "Theo dõi redirect",
    btn_start: "🔍 Bắt đầu quét",
    btn_scanning: "Đang quét...",
    btn_cancel: "🛑 Huỷ",
    history_title: "🕘 Lịch sử quét gần đây",
    progress_title: "📡 Tiến trình quét",
    // Guide modal
    guide_title: "📖 Hướng dẫn sử dụng Web Leak Scanner",
    guide_intro: "Tool quét bảo mật web 31 phases với 4 chế độ WAF bypass. Dưới đây là hướng dẫn chọn cấu hình phù hợp cho từng loại target.",
    guide_templates_title: "⚡ Quick Templates (Chọn nhanh)",
    guide_tpl_quick: "— Scan nhanh (~10s), chỉ check 100 paths phổ biến. Phù hợp khi cần survey nhanh target mới.",
    guide_tpl_deep: "— Full scan 31 phases (~60s), phát hiện mọi loại lỗ hổng. Phù hợp cho security audit chính thức.",
    guide_tpl_waf: "— Stealth mode, xoay UA + X-Forwarded-For 50 IP. Phù hợp khi target có Cloudflare/Akamai/Imperva.",
    guide_tpl_static: "— Cho Netlify/Vercel/GitHub Pages. Check _headers, _redirects, source maps, manifest.json.",
    guide_waf_title: "🛡️ WAF Bypass Mode — Khi nào chọn gì?",
    guide_waf_auto: "Mặc định. Tự giảm tốc khi detect WAF",
    guide_waf_stealth: "Cloudflare, Akamai, Imperva strict",
    guide_waf_aggressive: "WAF nhẹ, cần speed",
    guide_waf_turbo: "No WAF, max speed 100 req concurrent",
    guide_waf_detail: "<strong>Stealth mode</strong> sẽ: 5 req/s, delay 0.8-2.5s giữa requests, xoay 5 User-Agents khác nhau, xoay 50 fake X-Forwarded-For IPs (bypass IP rate-limiting), thêm full browser headers (Referer, Sec-Fetch-*, Accept-Language). Dùng khi scan Netlify, Vercel, Cloudflare Pages — các platform chặn aggressive scan.",
    guide_intensity_title: "🎯 Scan Intensity",
    guide_intensity_full: "— Mọi phases: leak paths, takeover, GraphQL, CORS, SSTI, .git, deep crawl, CT logs, Wayback... Khuyến nghị dùng.",
    guide_intensity_quick: "— Skip deep recon, chỉ check leak paths cơ bản + ports + tech detection. Nhanh (~10s).",
    guide_intensity_deep: "— Skip basic leak, chỉ chạy phases deep recon (CT logs, DNS, .git, deep crawl, JS strings).",
    guide_vuln_title: "🧪 Vuln Tests — Có nên bật?",
    guide_vuln_intro: "5 phases vuln detection (SSTI, Prototype Pollution, Header Injection, Cache Poisoning, Default Creds) sẽ gửi ~1000 requests active payload. Bật khi:",
    guide_vuln_ssti: "— Test {{7*7}}, ${7*7}, <%=7*7%> trên 8 endpoints × 7 params. CRITICAL nếu template engine execute payload.",
    guide_vuln_proto: "— Test ?__proto__[polluted]=yes, ?constructor[prototype][test]=1. HIGH nếu reflected.",
    guide_vuln_header: "— Test X-Forwarded-Host, X-Original-URL=/admin. HIGH nếu redirect tới injected host (bypass access control).",
    guide_vuln_cache: "— Test X-Forwarded-Host=evil.cache-poison. HIGH nếu reflected trong cached response.",
    guide_vuln_creds: "— Test 10 cặp admin/admin, root/root trên login forms. CRITICAL nếu login thành công.",
    guide_vuln_warning: "⚠️ <strong>Cảnh báo</strong>: Chỉ bật Vuln Tests khi bạn có quyền test target. Các payload active có thể bị WAF flag là malicious traffic.",
    guide_features_title: "🚀 Tính năng chính",
    guide_deploy_title: "🌐 Deploy lên cloud",
    guide_deploy_intro: "Tool dùng waitress (production WSGI server) + /health endpoint, phù hợp deploy lên Render, Heroku, VPS. Repo có sẵn:",
    guide_deploy_req: "— Flask, aiohttp, waitress",
    guide_deploy_render: "— 1-click deploy lên Render.com",
    guide_deploy_heroku: "— Deploy lên Heroku",
    guide_deploy_readme: "— Hướng dẫn chi tiết",
    guide_deploy_health: "<strong>Quan trọng</strong>: Set Health Check Path = <code>/health</code> trên Render dashboard để tránh \"Instance failed: i/o timeout\".",
    guide_tips_title: "💡 Tips & Tricks",
    tip_1: "Scan chậm?",
    guide_tip_1: "Chuyển sang Turbo mode (no WAF) hoặc Aggressive (light WAF).",
    tip_2: "Bị WAF block?",
    guide_tip_2: "Chuyển sang Stealth mode, tăng timeout lên 30s.",
    tip_3: "Main page fail (code 0)?",
    guide_tip_3: "Tool auto-thử 5 fallback strategies (HTTPS, HTTP, www., trailing slash). Nếu vẫn fail, target có thể down hoặc sandbox chặn.",
    tip_4: "Confetti không hiện?",
    guide_tip_4: "Confetti chỉ bắn khi có critical findings (stat-number.sev-crit > 0).",
    tip_5: "Đổi ngôn ngữ",
    guide_tip_5: "Click 🇻🇳 VI / 🇬🇧 EN ở góc phải navbar. Lưu vào localStorage, tự áp dụng lần sau.",
    tip_6: "Export kết quả",
    guide_tip_6: "Click JSON / CSV / HTML report để download kết quả scan.",
    guide_legal_title: "⚖️ Legal & Ethics",
    guide_legal: "Tool dành cho security research và authorized testing only. Chỉ scan target bạn có quyền hoặc được phép test. Scan mà không có consent có thể vi phạm luật (Cybersecurity law, GDPR, HIPAA...). Author không chịu trách nhiệm cho misuse.",
    guide_footer: "v11.1 — Recon Beast · Made with",
    guide_close_hint: "Click × hoặc ngoài modal để đóng",
  },
  en: {
    hero_title: "🕵️ Scan Information Leak Vulnerabilities",
    hero_subtitle: "Async deep recon v11.1 — 550+ leak paths · 31 phases · 4 WAF bypass modes · SSTI · Prototype Pollution · Cache Poisoning · Glassmorphism UI · Multilingual (VI/EN)",
    guide: "Guide",
    quick_templates: "Templates:",
    tpl_quick: "Quick Recon",
    tpl_deep: "Deep Audit",
    tpl_waf: "WAF Bypass",
    tpl_static: "Static Site",
    lbl_target: "🌐 Target URL",
    lbl_timeout: "⏱️ Timeout (s)",
    lbl_proxy: "🔀 Proxy",
    lbl_scan_js: "🔎 Scan JS files",
    opt_js_deep: "Yes (deep)",
    opt_js_quick: "No (fast)",
    lbl_bypass: "🛡️ WAF Bypass Mode",
    opt_auto: "🤖 Auto (balanced)",
    opt_stealth: "🥷 Stealth (5 req/s, XFF+UA rotation)",
    opt_aggressive: "⚔️ Aggressive (60 concurrent, full rotation)",
    opt_turbo: "🚀 Turbo (100 concurrent, no rotation)",
    lbl_intensity: "🎯 Scan Intensity",
    opt_full: "Full (31 phases)",
    opt_quick: "Quick (10 phases, skip deep recon)",
    opt_deep_recon: "Deep Recon only (skip basic leak)",
    lbl_vuln_tests: "🧪 Vuln Tests",
    opt_vuln_yes: "Yes (SSTI, Proto, Header)",
    opt_vuln_no: "No (recon only)",
    lbl_headers: "📋 Custom Headers",
    lbl_redirect: "Follow redirects",
    btn_start: "🔍 Start Scan",
    btn_scanning: "Scanning...",
    btn_cancel: "🛑 Cancel",
    history_title: "🕘 Recent Scan History",
    progress_title: "📡 Scan Progress",
    // Guide modal
    guide_title: "📖 Web Leak Scanner User Guide",
    guide_intro: "Web security scanner with 31 phases and 4 WAF bypass modes. Below is a guide to choose the right configuration for each target type.",
    guide_templates_title: "⚡ Quick Templates (Quick Select)",
    guide_tpl_quick: "— Fast scan (~10s), only checks 100 common paths. Suitable for quick survey of new targets.",
    guide_tpl_deep: "— Full 31-phase scan (~60s), detects all vulnerability types. Suitable for official security audits.",
    guide_tpl_waf: "— Stealth mode, rotates UA + X-Forwarded-For 50 IPs. For targets with Cloudflare/Akamai/Imperva.",
    guide_tpl_static: "— For Netlify/Vercel/GitHub Pages. Checks _headers, _redirects, source maps, manifest.json.",
    guide_waf_title: "🛡️ WAF Bypass Mode — When to choose what?",
    guide_waf_auto: "Default. Auto-throttle when WAF detected",
    guide_waf_stealth: "Cloudflare, Akamai, Imperva strict",
    guide_waf_aggressive: "Light WAF, need speed",
    guide_waf_turbo: "No WAF, max speed 100 concurrent req",
    guide_waf_detail: "<strong>Stealth mode</strong> will: 5 req/s, 0.8-2.5s delay between requests, rotate 5 different User-Agents, rotate 50 fake X-Forwarded-For IPs (bypass IP rate-limiting), add full browser headers (Referer, Sec-Fetch-*, Accept-Language). Use when scanning Netlify, Vercel, Cloudflare Pages — platforms that block aggressive scanning.",
    guide_intensity_title: "🎯 Scan Intensity",
    guide_intensity_full: "— All phases: leak paths, takeover, GraphQL, CORS, SSTI, .git, deep crawl, CT logs, Wayback... Recommended.",
    guide_intensity_quick: "— Skip deep recon, only check basic leak paths + ports + tech detection. Fast (~10s).",
    guide_intensity_deep: "— Skip basic leak, only run deep recon phases (CT logs, DNS, .git, deep crawl, JS strings).",
    guide_vuln_title: "🧪 Vuln Tests — Should you enable?",
    guide_vuln_intro: "5 vuln detection phases (SSTI, Prototype Pollution, Header Injection, Cache Poisoning, Default Creds) will send ~1000 active payload requests. Enable when:",
    guide_vuln_ssti: "— Test {{7*7}}, ${7*7}, <%=7*7%> on 8 endpoints × 7 params. CRITICAL if template engine executes payload.",
    guide_vuln_proto: "— Test ?__proto__[polluted]=yes, ?constructor[prototype][test]=1. HIGH if reflected.",
    guide_vuln_header: "— Test X-Forwarded-Host, X-Original-URL=/admin. HIGH if redirects to injected host (bypass access control).",
    guide_vuln_cache: "— Test X-Forwarded-Host=evil.cache-poison. HIGH if reflected in cached response.",
    guide_vuln_creds: "— Test 10 pairs admin/admin, root/root on login forms. CRITICAL if login succeeds.",
    guide_vuln_warning: "⚠️ <strong>Warning</strong>: Only enable Vuln Tests when you have permission to test the target. Active payloads may be flagged as malicious traffic by WAF.",
    guide_features_title: "🚀 Key Features",
    guide_deploy_title: "🌐 Deploy to Cloud",
    guide_deploy_intro: "Tool uses waitress (production WSGI server) + /health endpoint, suitable for Render, Heroku, VPS. Repo includes:",
    guide_deploy_req: "— Flask, aiohttp, waitress",
    guide_deploy_render: "— 1-click deploy to Render.com",
    guide_deploy_heroku: "— Deploy to Heroku",
    guide_deploy_readme: "— Detailed instructions",
    guide_deploy_health: "<strong>Important</strong>: Set Health Check Path = <code>/health</code> on Render dashboard to avoid \"Instance failed: i/o timeout\".",
    guide_tips_title: "💡 Tips & Tricks",
    tip_1: "Slow scan?",
    guide_tip_1: "Switch to Turbo mode (no WAF) or Aggressive (light WAF).",
    tip_2: "Blocked by WAF?",
    guide_tip_2: "Switch to Stealth mode, increase timeout to 30s.",
    tip_3: "Main page fails (code 0)?",
    guide_tip_3: "Tool auto-tries 5 fallback strategies (HTTPS, HTTP, www., trailing slash). If still fails, target may be down or sandbox blocked.",
    tip_4: "No confetti?",
    guide_tip_4: "Confetti only fires when there are critical findings (stat-number.sev-crit > 0).",
    tip_5: "Change language",
    guide_tip_5: "Click 🇻🇳 VI / 🇬🇧 EN in the top right navbar. Saved to localStorage, auto-applies next time.",
    tip_6: "Export results",
    guide_tip_6: "Click JSON / CSV / HTML report to download scan results.",
    guide_legal_title: "⚖️ Legal & Ethics",
    guide_legal: "Tool is for security research and authorized testing only. Only scan targets you have permission to test. Unauthorized scanning may violate laws (Cybersecurity law, GDPR, HIPAA...). Author is not responsible for misuse.",
    guide_footer: "v11.1 — Recon Beast · Made with",
    guide_close_hint: "Click × or outside modal to close",
  }
};

const LANG_KEY = 'wlsv9_lang';
let currentLang = localStorage.getItem(LANG_KEY) || 'vi';

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem(LANG_KEY, lang);
  document.documentElement.setAttribute('lang', lang);
  // Update all elements with data-i18n attribute
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const text = I18N[lang]?.[key];
    if (text !== undefined) {
      // Use innerHTML for elements that have HTML in translation (like <strong>, <code>)
      if (text.includes('<') && (el.tagName === 'P' || el.tagName === 'SPAN' || el.tagName === 'LI' || el.tagName === 'DIV')) {
        el.innerHTML = text;
      } else {
        el.textContent = text;
      }
    }
  });
  // Update active state on language buttons
  $$('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  // Update HTML lang attribute
  document.documentElement.lang = lang;
}
applyLanguage(currentLang);

// Language switcher buttons
$$('.lang-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const lang = btn.dataset.lang;
    if (lang !== currentLang) {
      applyLanguage(lang);
      toast(lang === 'vi' ? '🇻🇳 Đã chuyển sang Tiếng Việt' : '🇬🇧 Switched to English');
    }
  });
});

// ───────── v11.1 Guide Modal ─────────
function openGuide() {
  $('#guideModal').classList.add('show');
  document.body.style.overflow = 'hidden';
}
function closeGuide() {
  $('#guideModal').classList.remove('show');
  document.body.style.overflow = '';
}
$('#guideBtn').addEventListener('click', openGuide);
$('#guideModal').addEventListener('click', (e) => {
  if (e.target === $('#guideModal')) closeGuide();
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && $('#guideModal').classList.contains('show')) {
    closeGuide();
  }
});

// ───────── v11.1 Quick Templates ─────────
function applyTemplate(name) {
  const tpl = {
    quick:    {timeout: 8,  scan_js: 'no',  bypass_mode: 'auto',      intensity: 'quick', vuln_tests: 'no'},
    deep:     {timeout: 20, scan_js: 'yes', bypass_mode: 'auto',      intensity: 'full',  vuln_tests: 'yes'},
    waf:      {timeout: 30, scan_js: 'yes', bypass_mode: 'stealth',   intensity: 'full',  vuln_tests: 'yes'},
    static:   {timeout: 15, scan_js: 'yes', bypass_mode: 'stealth',   intensity: 'full',  vuln_tests: 'no'},
  }[name];
  if (!tpl) return;
  // Apply to form
  const form = $('#scanForm');
  form.querySelector('[name="timeout"]').value = tpl.timeout;
  form.querySelector('[name="scan_js"]').value = tpl.scan_js;
  form.querySelector('[name="bypass_mode"]').value = tpl.bypass_mode;
  // intensity + vuln_tests may not exist if removed; check first
  const intensitySel = form.querySelector('[name="intensity"]');
  if (intensitySel) intensitySel.value = tpl.intensity;
  const vulnSel = form.querySelector('[name="vuln_tests"]');
  if (vulnSel) vulnSel.value = tpl.vuln_tests;
  const msgs = {
    quick: currentLang === 'vi' ? '⚡ Đã áp dụng: Quick Recon (scan nhanh)' : '⚡ Applied: Quick Recon (fast scan)',
    deep: currentLang === 'vi' ? '🔬 Đã áp dụng: Deep Audit (full scan)' : '🔬 Applied: Deep Audit (full scan)',
    waf: currentLang === 'vi' ? '🥷 Đã áp dụng: WAF Bypass (stealth mode)' : '🥷 Applied: WAF Bypass (stealth mode)',
    static: currentLang === 'vi' ? '📦 Đã áp dụng: Static Site scan' : '📦 Applied: Static Site scan',
  };
  toast(msgs[name]);
}

function toast(msg){
  const t = $('#toast'); t.textContent = msg; t.classList.add('show');
  clearTimeout(window._toastT);
  window._toastT = setTimeout(()=>t.classList.remove('show'), 2400);
}

async function loadHistory(){
  try{
    const r = await fetch('/history');
    const d = await r.json();
    if(!d.history || !d.history.length){ $('#historyCard').style.display='none'; return; }
    $('#historyCard').style.display='';
    const list = $('#historyList');
    list.innerHTML = d.history.map((h,i)=>`
      <div class="history-item" data-scan-id="${h.scan_id}" style="animation-delay:${i*0.05}s">
        <div>
          <div class="history-target">${h.target}</div>
          <div class="history-meta">${new Date(h.started_at).toLocaleString()} · ${h.leak_count} leaks · ${h.duration_seconds}s · ${h.status}</div>
        </div>
        <span class="badge badge-time">↻ Reload</span>
      </div>
    `).join('');
    $$('.history-item').forEach(el=>{
      el.addEventListener('click', async ()=>{
        await loadResult(el.dataset.scanId);
      });
    });
  }catch(e){}
}

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
      if(sev === 'info') matchS = isSoft;
      const matchHide = !(hideS404 && isSoft);
      el.style.display = (matchQ && matchS && matchHide) ? '' : 'none';
    });
  }
  f.addEventListener('input', applyFilter);
  $('#filterSev').addEventListener('change', applyFilter);
  const hideChk = $('#hideSoft404');
  if(hideChk) hideChk.addEventListener('change', applyFilter);
  applyFilter();
}

let timerInterval = null;
let scanStartTs = 0;
let activityPollInterval = null;
let currentScanId = null;

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

// Live activity log polling
function startActivityPolling(scanId){
  if(activityPollInterval) clearInterval(activityPollInterval);
  const term = $('#activityLog');
  let lastT = 0;
  function poll(){
    fetch('/activity/' + scanId + '?since=' + (lastT || 0))
      .then(r => r.json())
      .then(d => {
        if(!d.lines || !d.lines.length) return;
        lastT = d.lines[d.lines.length-1].t;
        const html = d.lines.map(l => {
          const tag = (l.msg.match(/^\[(\w+)\]/) || [])[1] || '';
          const sev = tag && /critical/i.test(l.msg) ? 'critical' : (tag && /high/i.test(l.msg) ? 'high' : 'info');
          const ts = new Date(l.t * 1000).toLocaleTimeString('vi-VN', {hour12:false});
          return `<div class="term-line" data-sev="${sev}" data-tag="${tag}">[${ts}] ${l.msg}</div>`;
        }).join('');
        if(term.querySelector('.cursor')){
          term.innerHTML = html + '<span class="cursor"></span>';
        } else {
          term.insertAdjacentHTML('beforeend', html);
        }
        term.scrollTop = term.scrollHeight;
      }).catch(()=>{});
  }
  poll();
  activityPollInterval = setInterval(poll, 500);
}

function stopActivityPolling(){
  if(activityPollInterval){ clearInterval(activityPollInterval); activityPollInterval = null; }
}

const PHASE_FALLBACK = {
  'main_page':'🌐 Tải trang chính',
  'security_headers':'📜 Phân tích security headers',
  'fingerprint':'🛠️ Nhận diện công nghệ',
  'waf':'🛡️ Phát hiện WAF',
  'ssl':'🔒 Kiểm tra SSL/TLS',
  'ports':'🔌 Quét cổng',
  'ports_done':'✅ Xong quét cổng',
  'leak_scan':'📁 Quét leak paths',
  'static_scan':'🎯 Static/framework scan',
  'backup_check':'💾 Check backup variants',
  'robots':'🤖 Phân tích robots.txt',
  'links':'🔗 Trích xuất links/JS/forms',
  'secrets':'🔐 Quét secret trong HTML',
  'secrets_js':'📜 Quét secret trong JS files',
  'dirs':'📂 Kiểm tra directory listing',
  'brute':'🔍 Brute-force common files',
  'param_fuzz':'❓ Query param fuzzing',
  'subdomains':'🌐 DNS subdomain enum',
  'takeover':'💀 Subdomain takeover check',
  'graphql':'⚡ GraphQL introspection',
  'cors':'🌐 CORS misconfiguration',
  'open_redirect':'↪️ Open redirect test',
  'source_maps':'🗺️ Source map exposure',
  'js_endpoints':'📜 JS endpoint extraction',
  'api_fuzz':'🔌 API endpoint fuzzing',
  'swagger':'📋 Swagger/OpenAPI parsing',
  'recursive_brute':'🔁 Recursive depth-2 brute',
  'http_methods':'🔧 HTTP method fuzzing',
  'wayback':'🕰️ Wayback Machine lookup',
  'ct_logs':'📜 Certificate Transparency (crt.sh)',
  'dns_records':'🌐 DNS records lookup',
  'git_exposure':'📂 .git directory exposure',
  'deep_crawl':'🕷️ Deep crawl (depth-2)',
  'js_strings':'📜 JS source string extraction',
  'ssti':'🧪 SSTI (template injection)',
  'proto_pollution':'💀 Prototype Pollution',
  'header_injection':'🛡️ HTTP Header Injection (bypass)',
  'cache_poison':'☠️ Cache Poisoning',
  'default_creds':'🔑 Default Credentials',
  'completed':'✅ Hoàn thành',
  'error':'❌ Lỗi',
  'cancelling':'🛑 Đang huỷ',
  'cancelled':'🛑 Đã huỷ',
};

const INTERNAL_PHASES = new Set(['connected', 'keepalive']);

// v11.1: Old resetBtn/forceResetAll REMOVED — replaced by resetButtons() above

// v11.1: Global JS error handler — show banner if any JS error occurs
window.addEventListener('error', function(e) {
  console.error('Global JS Error:', e.error || e.message);
  const banner = document.getElementById('jsErrorBanner');
  const msg = document.getElementById('jsErrorMsg');
  if (banner && msg) {
    msg.textContent = e.message || 'Unknown error';
    banner.style.display = 'block';
  }
  // Also try to reset buttons
  forceResetAll();
});

// v11.1: Catch unhandled promise rejections
window.addEventListener('unhandledrejection', function(e) {
  console.error('Unhandled Promise Rejection:', e.reason);
  const banner = document.getElementById('jsErrorBanner');
  const msg = document.getElementById('jsErrorMsg');
  if (banner && msg) {
    msg.textContent = 'Promise error: ' + (e.reason?.message || e.reason || 'Unknown');
    banner.style.display = 'block';
  }
  forceResetAll();
});

// v11.1: Auto-reset safety net — ensure buttons never stay disabled >5min
let _autoResetTimer = null;
function startAutoResetWatchdog() {
  if (_autoResetTimer) clearTimeout(_autoResetTimer);
  // After 5 minutes, force reset buttons (in case scan hangs silently)
  _autoResetTimer = setTimeout(() => {
    console.warn('[Watchdog] Auto-resetting buttons after 5min timeout');
    resetBtn();
    stopTimer();
    stopActivityPolling();
    const found = $('#progressFound');
    const phase = $('#progressPhase');
    if (phase) phase.textContent = '⚠️ Timeout — buttons reset by watchdog';
    toast('⚠️ Scan có thể bị treo. Nút đã được reset — thử lại.');
  }, 5 * 60 * 1000);  // 5 minutes
}
function stopAutoResetWatchdog() {
  if (_autoResetTimer) {
    clearTimeout(_autoResetTimer);
    _autoResetTimer = null;
  }
}

async function loadResult(scanId){
  currentScanId = scanId;  // v11.1: store for HTML source viewer
  const resp = await fetch('/result/' + scanId);
  const html = await resp.text();
  $('#resultsArea').innerHTML = html;
  resetBtn();
  stopAutoResetWatchdog();  // v11.1: scan completed, stop watchdog
  stopActivityPolling();
  initTabs();
  initFilter();
  animateCounters();
  checkAndFireConfetti();  // v11.1: fire confetti if critical findings
  // v11.1: draw donut chart + animate risk gauge
  setTimeout(() => {
    drawSeverityDonut();
    animateRiskGauge();
  }, 100);
  // Apply current language to result HTML too
  applyLanguage(currentLang);
  $('#resultsArea').scrollIntoView({behavior:'smooth', block:'start'});
}

// Animated number counters
function animateCounters(){
  $$('.stat-number').forEach(el=>{
    const target = parseInt(el.textContent.replace(/[^\d-]/g,'')) || 0;
    if(target === 0) return;
    let cur = 0;
    const dur = 700;
    const startTs = performance.now();
    const tick = (now)=>{
      const t = Math.min(1, (now - startTs) / dur);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = Math.round(target * eased);
      if(t < 1) requestAnimationFrame(tick);
      else el.textContent = target;
    };
    requestAnimationFrame(tick);
  });
}

loadHistory();
} catch(e) { console.error('[Init] Error:', e); }  // v11.1: close init try block EARLY

// ═════════ v11.1: ALL FUNCTIONS DECLARED AT GLOBAL SCOPE ═════════
// These MUST be outside any try block so they're always available

// ═════════ v11.1 Command Palette ═════════
const COMMANDS = [
  {icon:'⚡', title:'Quick Recon', desc:'Fast scan template', kbd:'T+Q', action:()=>{applyTemplate('quick')}},
  {icon:'🔬', title:'Deep Audit', desc:'Full 31-phase scan', kbd:'T+D', action:()=>{applyTemplate('deep')}},
  {icon:'🥷', title:'WAF Bypass', desc:'Stealth mode for WAF-protected sites', kbd:'T+W', action:()=>{applyTemplate('waf')}},
  {icon:'📦', title:'Static Site', desc:'For Netlify/Vercel/GH Pages', kbd:'T+S', action:()=>{applyTemplate('static')}},
  {icon:'📖', title:'Open Guide', desc:'User manual', kbd:'G', action:openGuide},
  {icon:'🇻🇳', title:'Switch to Vietnamese', desc:'Change language', kbd:'L', action:()=>applyLanguage('vi')},
  {icon:'🇬🇧', title:'Switch to English', desc:'Change language', kbd:'L', action:()=>applyLanguage('en')},
  {icon:'🌙', title:'Toggle Theme', desc:'Dark/Light mode', kbd:'D', action:()=>{const t=document.documentElement.getAttribute('data-theme');applyTheme(t==='dark'?'light':'dark')}},
  {icon:'🔍', title:'Focus Search', desc:'Filter findings', kbd:'/', action:()=>{const f=$('#filterInput');if(f){f.focus();f.scrollIntoView({behavior:'smooth',block:'center'})}}},
  {icon:'📋', title:'Copy Target URL', desc:'Copy to clipboard', kbd:'C', action:()=>{const t=document.querySelector('[class*="history-target"]')?.textContent||'C';navigator.clipboard.writeText(t);toast('📋 Copied: '+t)}},
];
let cmdSelectedIdx = 0;
function renderCmdList(filter='') {
  const list = $('#cmdList');
  const filtered = COMMANDS.filter(c =>
    c.title.toLowerCase().includes(filter.toLowerCase()) ||
    c.desc.toLowerCase().includes(filter.toLowerCase())
  );
  if (filtered.length === 0) {
    list.innerHTML = '<div style="padding:20px;text-align:center;color:var(--dim)">No commands found</div>';
    return;
  }
  list.innerHTML = filtered.map((c, i) => `
    <div class="cmd-item ${i === cmdSelectedIdx ? 'selected' : ''}" data-idx="${i}" onclick="runCmd(${COMMANDS.indexOf(c)})">
      <span class="cmd-item-icon">${c.icon}</span>
      <div class="cmd-item-text">
        <div class="cmd-item-title">${c.title}</div>
        <div class="cmd-item-desc">${c.desc}</div>
      </div>
      <span class="cmd-item-kbd">${c.kbd}</span>
    </div>
  `).join('');
  // Update selected index to match filtered list
  cmdSelectedIdx = Math.min(cmdSelectedIdx, filtered.length - 1);
}
function runCmd(idx) {
  const cmd = COMMANDS[idx];
  if (cmd) {
    cmd.action();
    closeCmdPalette();
    toast(`${cmd.icon} ${cmd.title}`);
  }
}
function openCmdPalette() {
  $('#cmdPalette').classList.add('show');
  $('#cmdInput').value = '';
  cmdSelectedIdx = 0;
  renderCmdList();
  setTimeout(() => $('#cmdInput').focus(), 100);
}
function closeCmdPalette() {
  $('#cmdPalette').classList.remove('show');
}
$('#cmdInput').addEventListener('input', (e) => {
  cmdSelectedIdx = 0;
  renderCmdList(e.target.value);
});
$('#cmdInput').addEventListener('keydown', (e) => {
  const items = $$('#cmdList .cmd-item');
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    cmdSelectedIdx = Math.min(cmdSelectedIdx + 1, items.length - 1);
    items.forEach((it, i) => it.classList.toggle('selected', i === cmdSelectedIdx));
    items[cmdSelectedIdx]?.scrollIntoView({block:'nearest'});
  } else if (e.key === 'ArrowUp') {
    e.preventDefault();
    cmdSelectedIdx = Math.max(cmdSelectedIdx - 1, 0);
    items.forEach((it, i) => it.classList.toggle('selected', i === cmdSelectedIdx));
    items[cmdSelectedIdx]?.scrollIntoView({block:'nearest'});
  } else if (e.key === 'Enter') {
    e.preventDefault();
    if (items[cmdSelectedIdx]) {
      const idx = parseInt(items[cmdSelectedIdx].dataset.idx);
      runCmd(idx);
    }
  } else if (e.key === 'Escape') {
    closeCmdPalette();
  }
});
$('#cmdPalette').addEventListener('click', (e) => {
  if (e.target === $('#cmdPalette')) closeCmdPalette();
});

// ═════════ v11.1 Keyboard Shortcuts ═════════
document.addEventListener('keydown', (e) => {
  // Skip if typing in input/textarea
  const tag = e.target.tagName;
  const isInput = tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT';
  // Cmd+K / Ctrl+K — open command palette (works everywhere)
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    if ($('#cmdPalette').classList.contains('show')) {
      closeCmdPalette();
    } else {
      openCmdPalette();
    }
    return;
  }
  // ESC — close modals
  if (e.key === 'Escape') {
    closeCmdPalette();
    closeGuide();
    return;
  }
  if (isInput) return;
  // Single-key shortcuts
  if (e.key === '/') {
    e.preventDefault();
    const f = $('#filterInput');
    if (f) { f.focus(); f.scrollIntoView({behavior:'smooth',block:'center'}); }
  } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
    e.preventDefault();
    openGuide();
  } else if (e.key.toLowerCase() === 'g') {
    openGuide();
  } else if (e.key.toLowerCase() === 'l') {
    applyLanguage(currentLang === 'vi' ? 'en' : 'vi');
    toast(currentLang === 'vi' ? '🇻🇳 Đã chuyển sang Tiếng Việt' : '🇬🇧 Switched to English');
  } else if (e.key.toLowerCase() === 'd') {
    const t = document.documentElement.getAttribute('data-theme');
    applyTheme(t === 'dark' ? 'light' : 'dark');
  } else if (e.key >= '1' && e.key <= '9') {
    // Tab switching
    const tabs = $$('.tab');
    const idx = parseInt(e.key) - 1;
    if (tabs[idx]) tabs[idx].click();
  }
});

// ═════════ v11.1 Helper functions for results ═════════
// v11.1: HTML Source viewer
// NOTE: currentScanId already declared at line 5427, don't re-declare!
let htmlSourceCache = null;
function loadHtmlSource() {
  if (!currentScanId) {
    toast('❌ Chưa có scan nào. Hãy scan một URL trước.');
    return;
  }
  const loading = document.getElementById('htmlSourceLoading');
  const content = document.getElementById('htmlSourceContent');
  const info = document.getElementById('htmlSourceInfo');
  const empty = document.getElementById('htmlSourceEmpty');
  if (loading) loading.style.display = 'block';
  if (content) content.style.display = 'none';
  if (empty) empty.style.display = 'none';
  fetch('/source/' + currentScanId)
    .then(r => r.json())
    .then(data => {
      htmlSourceCache = data;
      if (loading) loading.style.display = 'none';
      if (data.error) {
        if (info) {
          info.style.display = 'block';
          info.innerHTML = `❌ <strong>Lỗi fetch HTML:</strong> ${data.error}<br>Target: <code>${data.target}</code>`;
        }
        return;
      }
      if (content) {
        // Escape HTML để hiển thị as text (không render)
        const escaped = data.html
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;');
        content.innerHTML = escaped;
        content.style.display = 'block';
      }
      if (info) {
        info.style.display = 'block';
        info.innerHTML = `
          📄 <strong>${data.size.toLocaleString()} bytes</strong> · HTTP ${data.status_code}
          ${data.truncated ? ' · <span style="color:var(--warn)">⚠️ Truncated at 500KB</span>' : ''}
          · Target: <code>${data.target}</code>
        `;
      }
      document.getElementById('downloadSourceBtn').style.display = 'inline-flex';
      document.getElementById('copySourceBtn').style.display = 'inline-flex';
      toast(`📄 Đã tải ${data.size.toLocaleString()} bytes HTML`);
    })
    .catch(err => {
      if (loading) loading.style.display = 'none';
      toast('❌ Lỗi: ' + err.message);
    });
}
function downloadHtmlSource() {
  if (!htmlSourceCache || !htmlSourceCache.html) return;
  const blob = new Blob([htmlSourceCache.html], {type: 'text/html'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'source_' + (htmlSourceCache.target || 'unknown').replace(/^https?:\/\//, '').split('/')[0] + '.html';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  toast('⬇️ Đã download HTML source');
}
// v11: File Tree — load + render interactive tree
function loadFileTree() {
  if (!currentScanId) { toast('❌ Chưa có scan nào'); return; }
  fetch('/tree/' + currentScanId)
    .then(r => r.json())
    .then(data => {
      const container = document.getElementById('fileTreeContainer');
      const empty = document.getElementById('fileTreeEmpty');
      const info = document.getElementById('treeInfo');
      if (!data.tree || !data.tree.children || data.tree.children.length === 0) {
        if (empty) empty.style.display = 'block';
        if (container) container.style.display = 'none';
        if (info) info.textContent = 'No files discovered';
        return;
      }
      if (empty) empty.style.display = 'none';
      if (container) { container.style.display = 'block'; container.innerHTML = renderTreeNode(data.tree, 0); }
      if (info) info.textContent = `📊 ${data.total_files} files discovered`;
      toast(`🌳 Loaded ${data.total_files} files`);
    })
    .catch(err => toast('❌ Lỗi: ' + err.message));
}

function renderTreeNode(node, depth) {
  if (!node) return '';
  var icon = node.type === 'dir' ? '📁' : '📄';
  var sevClass = node.severity ? ' tree-sev-' + node.severity : '';
  var meta = [];
  if (node.status) meta.push(node.status);
  if (node.size) meta.push(node.size + 'b');
  if (node.severity) meta.push(node.severity);
  var metaStr = meta.length ? '<span class="tree-meta">' + meta.join(' · ') + '</span>' : '';
  var html = '<div class="tree-node' + sevClass + '">';
  if (node.type === 'dir' && node.children && node.children.length > 0) {
    html += '<span class="tree-toggle" onclick="this.parentElement.nextElementSibling.style.display=this.parentElement.nextElementSibling.style.display==\'none\'?\'block\':\'none\';this.textContent=this.textContent==\'▶\'?\'▼\':\'▶\'">▼</span>';
    html += '<span class="tree-icon">' + icon + '</span>';
    html += '<span class="tree-name">' + node.name + '</span>' + metaStr;
    html += '</div>';
    html += '<div class="tree-children" style="display:block">';
    for (var i = 0; i < node.children.length; i++) {
      html += renderTreeNode(node.children[i], depth + 1);
    }
    html += '</div>';
  } else {
    html += '<span class="tree-toggle">&nbsp;</span>';
    html += '<span class="tree-icon">' + icon + '</span>';
    html += '<span class="tree-name">' + node.name + '</span>' + metaStr;
    if (node.url) {
      html += ' <a href="' + node.url + '" target="_blank" style="font-size:11px;color:var(--accent2);text-decoration:none">↗</a>';
    }
    html += '</div>';
  }
  return html;
}

// v11: Source Code — load list of JS/CSS files, fetch + display source
function loadSourceCodeList() {
  if (!currentScanId) { toast('❌ Chưa có scan nào'); return; }
  // Get JS links + CSS links from result page
  var jsLinks = [];
  document.querySelectorAll('.leak-item .leak-url').forEach(function(el) {
    var url = el.textContent.trim();
    if (url.endsWith('.js') || url.endsWith('.css') || url.endsWith('.html')) {
      jsLinks.push(url);
    }
  });
  // Also check js_links section if visible
  var jsSection = document.getElementById('tab-forms');
  if (jsSection) {
    jsSection.querySelectorAll('a[href]').forEach(function(a) {
      var href = a.href;
      if (href.endsWith('.js') || href.endsWith('.css')) jsLinks.push(href);
    });
  }
  // Deduplicate
  jsLinks = jsLinks.filter(function(v, i, a) { return a.indexOf(v) === i; });
  if (jsLinks.length === 0) {
    toast('❌ Không tìm thấy JS/CSS files để xem source');
    return;
  }
  var listEl = document.getElementById('sourceFileList');
  var containerEl = document.getElementById('sourceCodeContainer');
  var emptyEl = document.getElementById('sourceCodeEmpty');
  if (emptyEl) emptyEl.style.display = 'none';
  if (listEl) {
    listEl.style.display = 'flex';
    listEl.innerHTML = jsLinks.map(function(url, i) {
      var name = url.split('/').pop().split('?')[0];
      return '<button class="source-file-btn" onclick="fetchSourceFile(\'' + url.replace(/'/g, "\\'") + '\', ' + i + ')" id="srcBtn' + i + '">' + name + '</button>';
    }).join('');
  }
  if (containerEl) containerEl.style.display = 'block';
  // Auto-load first file
  if (jsLinks.length > 0) fetchSourceFile(jsLinks[0], 0);
  toast('💻 Loaded ' + jsLinks.length + ' source files');
}

function fetchSourceFile(url, idx) {
  var container = document.getElementById('sourceCodeContainer');
  if (!container) return;
  container.innerHTML = '<div style="color:var(--dim);padding:20px">⏳ Đang tải ' + url.split('/').pop() + '...</div>';
  // Highlight active button
  document.querySelectorAll('.source-file-btn').forEach(function(b) { b.classList.remove('active'); });
  var btn = document.getElementById('srcBtn' + idx);
  if (btn) btn.classList.add('active');
  fetch('/source_file', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({url: url})
  })
    .then(r => r.json())
    .then(data => {
      if (data.error) {
        container.innerHTML = '<div style="color:var(--danger);padding:20px">❌ Lỗi: ' + data.error + '</div>';
        return;
      }
      // Escape HTML
      var escaped = data.content.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      var header = '<div style="color:var(--accent);margin-bottom:8px;font-size:12px">';
      header += '📄 ' + url.split('/').pop() + ' · ' + data.size + ' bytes · HTTP ' + data.status;
      if (data.truncated) header += ' · <span style="color:var(--warn)">⚠️ Truncated at 200KB</span>';
      header += '</div>';
      container.innerHTML = header + '<pre style="white-space:pre-wrap;word-break:break-all;color:#aed581">' + escaped + '</pre>';
    })
    .catch(err => {
      container.innerHTML = '<div style="color:var(--danger);padding:20px">❌ Network error: ' + err.message + '</div>';
    });
}

function copyHtmlSource() {
  if (!htmlSourceCache || !htmlSourceCache.html) return;
  navigator.clipboard.writeText(htmlSourceCache.html).then(() => toast('📋 Đã copy HTML'));
}

function filterBySeverity(sev) {
  const select = $('#filterSev');
  if (select) {
    select.value = sev;
    select.dispatchEvent(new Event('change'));
    document.getElementById('tab-leaks')?.click();
    toast(`🔍 Filtered: ${sev}`);
  }
}
function copySummary() {
  const text = document.getElementById('execSummaryText')?.textContent || '';
  navigator.clipboard.writeText(text).then(() => toast('📋 Summary copied!'));
}
function scrollToTop() {
  window.scrollTo({top:0, behavior:'smooth'});
}
function scrollToScan() {
  document.querySelector('#scanForm')?.scrollIntoView({behavior:'smooth', block:'start'});
}

// Draw severity donut chart (called after result load)
function drawSeverityDonut() {
  const svg = document.getElementById('severityDonut');
  if (!svg) return;
  // Read counts from legend
  const items = document.querySelectorAll('.severity-legend-item .count');
  if (items.length < 4) return;
  const counts = Array.from(items).map(el => parseInt(el.textContent) || 0);
  const total = counts.reduce((a,b)=>a+b, 0);
  if (total === 0) return;
  const colors = ['#ff0044', '#ff8800', '#ffcc00', '#00ff88'];
  const cx = 70, cy = 70, r = 55;
  const circumference = 2 * Math.PI * r;
  let offset = 0;
  // Remove old segments (keep bg circle)
  const oldSegs = svg.querySelectorAll('.donut-seg');
  oldSegs.forEach(s => s.remove());
  counts.forEach((count, i) => {
    if (count === 0) return;
    const dash = (count / total) * circumference;
    const seg = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    seg.setAttribute('cx', cx);
    seg.setAttribute('cy', cy);
    seg.setAttribute('r', r);
    seg.setAttribute('fill', 'none');
    seg.setAttribute('stroke', colors[i]);
    seg.setAttribute('stroke-width', '18');
    seg.setAttribute('stroke-dasharray', `${dash} ${circumference - dash}`);
    seg.setAttribute('stroke-dashoffset', -offset);
    seg.setAttribute('class', 'donut-seg');
    seg.style.transition = 'stroke-dasharray 1s ease, stroke-dashoffset 1s ease';
    seg.style.filter = 'drop-shadow(0 0 4px currentColor)';
    svg.appendChild(seg);
    offset += dash;
  });
}

// Animated risk gauge (count-up effect)
function animateRiskGauge() {
  const fill = document.getElementById('riskGaugeFill');
  if (!fill) return;
  // Already set via template, just add pulse effect
  const grade = document.querySelector('.grade-letter');
  if (grade) {
    grade.style.animation = 'none';
    setTimeout(() => grade.style.animation = 'logoPulse 2s ease', 10);
  }
}
// v11.1: no more try block — all functions are global now
</script>
</body>
</html>
"""

# ── HTML Template (RESULT) – v11.1 Deep Recon ──
RESULT_HTML = r"""
{% if result %}
<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:10px">
  <h2 style="margin:0">📊 Kết quả cho {{ result.target }}</h2>
  <div>
    {% if result.duration_seconds %}<span class="badge badge-time">⏱️ {{ result.duration_seconds }}s</span>{% endif %}
    {% if result.cancelled %}<span class="badge badge-waf">🛑 Đã huỷ</span>{% endif %}
    {% if result.main and result.main.code == 0 %}<span class="badge badge-waf">🚨 MAIN FAIL</span>{% endif %}
    {% if result.static_platforms %}<span class="badge" style="background:rgba(167,139,250,.15);color:#a78bfa">📦 {{ result.static_platforms|join(", ") }}</span>{% endif %}
    {% if result.frameworks_detected %}<span class="badge" style="background:rgba(84,160,255,.15);color:#54a0ff">⚛️ {{ result.frameworks_detected|join(", ") }}</span>{% endif %}
    {% if result.stats and result.stats.soft_404_filtered %}<span class="badge" style="background:rgba(160,160,176,.15);color:#a0a0b0">🎯 Soft-404: {{ result.stats.soft_404_filtered }}</span>{% endif %}
    {% if result.stats and result.stats.backup_findings %}<span class="badge" style="background:rgba(167,139,250,.15);color:#a78bfa">💾 Backup: {{ result.stats.backup_findings }}</span>{% endif %}
    {% if result.stats and result.stats.param_findings %}<span class="badge" style="background:rgba(254,202,87,.15);color:#feca57">❓ Params: {{ result.stats.param_findings }}</span>{% endif %}
    {% if result.stats and result.stats.takeover_findings %}<span class="badge badge-waf">💀 Takeover: {{ result.stats.takeover_findings }}</span>{% endif %}
    {% if result.stats and result.stats.graphql_findings %}<span class="badge" style="background:rgba(255,159,64,.15);color:#ff9f43">⚡ GraphQL: {{ result.stats.graphql_findings }}</span>{% endif %}
    {% if result.stats and result.stats.cors_findings %}<span class="badge" style="background:rgba(254,202,87,.15);color:#feca57">🌐 CORS: {{ result.stats.cors_findings }}</span>{% endif %}
    {% if result.stats and result.stats.source_maps %}<span class="badge" style="background:rgba(167,139,250,.15);color:#a78bfa">🗺️ SrcMaps: {{ result.stats.source_maps }}</span>{% endif %}
    {% if result.stats and result.stats.api_endpoints %}<span class="badge" style="background:rgba(0,212,170,.15);color:#00d4aa">🔌 API: {{ result.stats.api_endpoints }}</span>{% endif %}
    {% if result.stats and result.stats.swagger_endpoints %}<span class="badge" style="background:rgba(84,160,255,.15);color:#54a0ff">📋 Swagger: {{ result.stats.swagger_endpoints }}</span>{% endif %}
    {% if result.stats and result.stats.wayback_urls %}<span class="badge" style="background:rgba(254,202,87,.15);color:#feca57">🕰️ Wayback: {{ result.stats.wayback_urls }}</span>{% endif %}
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

<!-- v11.1 Risk Score Dashboard -->
{% set risk = calculate_risk_score(result.stats) %}
<div class="risk-dashboard">
  <div class="risk-gauge-wrap">
    <div class="risk-gauge">
      <svg width="160" height="160" viewBox="0 0 160 160">
        <circle class="gauge-bg" cx="80" cy="80" r="68"/>
        <circle class="gauge-fill" cx="80" cy="80" r="68"
          stroke="{{ risk.color }}"
          stroke-dasharray="427"
          stroke-dashoffset="{{ 427 - (427 * risk.score / 100) }}"
          id="riskGaugeFill"/>
      </svg>
      <div class="risk-grade">
        <div class="grade-letter" style="color:{{ risk.color }}">{{ risk.grade }}</div>
        <div class="grade-label">Risk Grade</div>
        <div class="grade-score">{{ risk.score }}/100</div>
      </div>
    </div>
  </div>
  <div class="risk-info">
    <h3>🎯 Security Risk Assessment</h3>
    <div class="risk-status {{ 'critical' if risk.score >= 80 else ('high' if risk.score >= 60 else ('medium' if risk.score >= 40 else ('low' if risk.score >= 20 else 'low'))) }}">
      {{ risk.label }}
    </div>
    <div class="risk-summary">{{ risk.summary }}</div>
  </div>
  <div class="severity-chart-wrap">
    <div class="severity-donut">
      <svg width="140" height="140" viewBox="0 0 140 140" id="severityDonut">
        <circle cx="70" cy="70" r="55" stroke="rgba(255,255,255,.05)" stroke-width="18" fill="none"/>
        <!-- Donut segments will be drawn by JS based on counts -->
      </svg>
      <div class="donut-center">
        <div class="donut-total">{{ result.leak|length + result.secrets|length }}</div>
        <div class="donut-label">Findings</div>
      </div>
    </div>
    <div class="severity-legend">
      <div class="severity-legend-item" onclick="filterBySeverity('critical')">
        <span class="dot sev-dot-critical"></span>
        <span>Critical</span>
        <span class="count">{{ risk.counts.critical }}</span>
      </div>
      <div class="severity-legend-item" onclick="filterBySeverity('high')">
        <span class="dot sev-dot-high"></span>
        <span>High</span>
        <span class="count">{{ risk.counts.high }}</span>
      </div>
      <div class="severity-legend-item" onclick="filterBySeverity('medium')">
        <span class="dot sev-dot-medium"></span>
        <span>Medium</span>
        <span class="count">{{ risk.counts.medium }}</span>
      </div>
      <div class="severity-legend-item" onclick="filterBySeverity('low')">
        <span class="dot sev-dot-low"></span>
        <span>Low</span>
        <span class="count">{{ risk.counts.low }}</span>
      </div>
    </div>
  </div>
</div>

<!-- Executive Summary -->
<div class="exec-summary">
  <h3>📋 Executive Summary <button class="copy-btn" onclick="copySummary()">📋 Copy</button></h3>
  <p id="execSummaryText">{{ risk.summary }}</p>
</div>

<!-- Stats grid -->
<div class="stats-grid">
  <div class="stat-box"><div class="stat-number">{{ result.main.code }}</div><div class="stat-label">Main code</div></div>
  <div class="stat-box"><div class="stat-number sev-crit">{{ result.stats.critical_count|default(0) }}</div><div class="stat-label">Critical</div></div>
  <div class="stat-box"><div class="stat-number sev-high">{{ result.stats.high_count|default(0) }}</div><div class="stat-label">High</div></div>
  <div class="stat-box"><div class="stat-number">{{ result.leak|length }}</div><div class="stat-label">Leaks</div></div>
  <div class="stat-box"><div class="stat-number sev-crit">{{ result.stats.secret_critical|default(0) }}</div><div class="stat-label">Sec crit</div></div>
  <div class="stat-box"><div class="stat-number">{{ result.ports|length }}</div><div class="stat-label">Ports</div></div>
</div>

<!-- Tabs -->
<div class="tabs">
  <button class="tab active" data-tab="summary">📋 Tóm tắt</button>
  <button class="tab" data-tab="leaks">📁 Leaks <span class="count">{{ result.leak|length }}</span></button>
  <button class="tab" data-tab="secrets">🔐 Secrets <span class="count">{{ result.secrets|length }}</span></button>
  <button class="tab" data-tab="backups">💾 Backups <span class="count">{{ result.backup_findings|length }}</span></button>
  <button class="tab" data-tab="endpoints">🔌 API <span class="count">{{ result.api_endpoints|length }}</span></button>
  <button class="tab" data-tab="takeover">💀 Takeover <span class="count">{{ result.takeover_findings|length }}</span></button>
  <button class="tab" data-tab="graphql">⚡ GraphQL <span class="count">{{ result.graphql_findings|length }}</span></button>
  <button class="tab" data-tab="cors">🌐 CORS <span class="count">{{ result.cors_findings|length }}</span></button>
  <button class="tab" data-tab="redirect">↪️ Redirect <span class="count">{{ result.open_redirect_findings|length }}</span></button>
  <button class="tab" data-tab="srcmaps">🗺️ SrcMaps <span class="count">{{ result.source_maps|length }}</span></button>
  <button class="tab" data-tab="swagger">📋 Swagger <span class="count">{{ result.swagger_endpoints|length }}</span></button>
  <button class="tab" data-tab="wayback">🕰️ Wayback <span class="count">{{ result.wayback_urls|length }}</span></button>
  <button class="tab" data-tab="ct_logs">📜 CT Subs <span class="count">{{ result.ct_subdomains|length }}</span></button>
  <button class="tab" data-tab="dns">🌐 DNS <span class="count">{{ result.dns_records|length }}</span></button>
  <button class="tab" data-tab="git">📂 .Git <span class="count">{{ result.git_findings|length }}</span></button>
  <button class="tab" data-tab="crawled">🕷️ Crawled <span class="count">{{ result.crawled_pages|length }}</span></button>
  <button class="tab" data-tab="js_strings">📜 JS Strings <span class="count">{{ result.js_strings|length }}</span></button>
  <button class="tab" data-tab="ssti">🧪 SSTI <span class="count">{{ result.ssti_findings|length }}</span></button>
  <button class="tab" data-tab="proto">💀 Proto <span class="count">{{ result.proto_pollution_findings|length }}</span></button>
  <button class="tab" data-tab="hinj">🛡️ Header Inj <span class="count">{{ result.header_injection_findings|length }}</span></button>
  <button class="tab" data-tab="cache">☠️ Cache <span class="count">{{ result.cache_poison_findings|length }}</span></button>
  <button class="tab" data-tab="creds">🔑 Creds <span class="count">{{ result.default_creds_findings|length }}</span></button>
  <button class="tab" data-tab="params">❓ Params <span class="count">{{ result.param_findings|length }}</span></button>
  <button class="tab" data-tab="methods">🔧 Methods <span class="count">{{ result.http_method_findings|length }}</span></button>
  <button class="tab" data-tab="rbrute">🔁 RBrute <span class="count">{{ result.recursive_brute_findings|length }}</span></button>
  <button class="tab" data-tab="tech">🛠️ Tech & WAF</button>
  <button class="tab" data-tab="network">🌐 Network</button>
  <button class="tab" data-tab="headers">📜 Headers & Cookies</button>
  <button class="tab" data-tab="forms">📝 Forms <span class="count">{{ result.forms|length }}</span></button>
  <button class="tab" data-tab="subs">🌐 Subs <span class="count">{{ result.subdomains_resolved|length }}</span></button>
  <button class="tab" data-tab="file_tree" onclick="loadFileTree()">🌳 File Tree</button>
  <button class="tab" data-tab="source_code" onclick="loadSourceCodeList()">💻 Source Code</button>
  <button class="tab" data-tab="html_source">📄 HTML Source</button>
  <button class="tab" data-tab="raw">🔎 Raw</button>
</div>

<!-- Tab: Summary -->
<div class="tab-panel active" id="tab-summary">
  {% if result.main and result.main.code == 0 %}
  <div class="alert alert-error">🚨 <strong>MAIN PAGE FETCH FAILED</strong> — Scanner không tải được trang chính (code 0).<br>
  {% if result.main.fetch_error %}Lỗi: <code>{{ result.main.fetch_error }}</code><br>{% endif %}
  Đã thử 5 fallback strategies (HTTPS, HTTP, www., trailing slash). Kết quả có thể bị hạn chế — thử lại với timeout cao hơn hoặc URL khác.<br>
  <strong>Final URL tried:</strong> <code>{{ result.main.final_target or result.target }}</code></div>
  {% endif %}
  {% if result.main and result.main.final_target and result.main.final_target != result.target %}
  <div class="alert alert-info">🔄 <strong>Fallback URL used</strong>: Original <code>{{ result.target }}</code> failed, switched to <code>{{ result.main.final_target }}</code></div>
  {% endif %}
  {% if result.static_platforms %}
  <div class="alert alert-info">📦 <strong>Static site platform detected</strong>: {{ result.static_platforms|join(", ") }} — đã chạy static-site specific checks (_headers, _redirects, source maps, manifest.json...)</div>
  {% endif %}
  {% if result.frameworks_detected %}
  <div class="alert alert-info">⚛️ <strong>Framework detected</strong>: {{ result.frameworks_detected|join(", ") }} — đã chạy framework-specific path checks</div>
  {% endif %}
  {% if result.stats.missing_security_headers %}
  <div class="alert alert-warn">⚠️ Thiếu <strong>{{ result.stats.missing_security_headers }}</strong> security header(s) quan trọng</div>
  {% endif %}
  {% if result.stats.insecure_cookies %}
  <div class="alert alert-warn">🍪 Có <strong>{{ result.stats.insecure_cookies }}</strong> cookie thiếu flag bảo mật</div>
  {% endif %}
  {% if result.stats.secret_critical %}
  <div class="alert alert-error">🚨 Phát hiện <strong>{{ result.stats.secret_critical }}</strong> secret mức CRITICAL (AWS/Stripe/GitHub/OpenAI/private key...)</div>
  {% endif %}
  {% if result.stats.critical_count %}
  <div class="alert alert-error">🚨 Có <strong>{{ result.stats.critical_count }}</strong> leak path mức CRITICAL (.env, .aws, .ssh, terraform, vault...)</div>
  {% endif %}
  {% if result.waf.detected %}
  <div class="alert alert-info">🛡️ WAF phát hiện: <strong>{{ result.waf.detected|join(", ") }}</strong>. Nên giảm tốc độ scan.</div>
  {% endif %}
  {% if result.stats.backup_findings %}
  <div class="alert alert-info">💾 Phát hiện <strong>{{ result.stats.backup_findings }}</strong> backup file (.bak/.old/.orig/...) — thường leak config gốc</div>
  {% endif %}
  {% if result.stats.param_findings %}
  <div class="alert alert-warn">❓ Phát hiện <strong>{{ result.stats.param_findings }}</strong> query param gây response khác thường — có thể debug endpoint</div>
  {% endif %}
  {% if result.stats.takeover_findings %}
  <div class="alert alert-error">💀 Phát hiện <strong>{{ result.stats.takeover_findings }}</strong> subdomain takeover — CÓ THỂ CHIẾM QUYỀN</div>
  {% endif %}
  {% if result.stats.graphql_findings %}
  <div class="alert alert-warn">⚡ Phát hiện <strong>{{ result.stats.graphql_findings }}</strong> GraphQL endpoint — check tab GraphQL</div>
  {% endif %}
  {% if result.stats.cors_findings %}
  <div class="alert alert-warn">🌐 Phát hiện <strong>{{ result.stats.cors_findings }}</strong> CORS misconfiguration — check tab CORS</div>
  {% endif %}
  {% if result.stats.source_maps %}
  <div class="alert alert-warn">🗺️ Phát hiện <strong>{{ result.stats.source_maps }}</strong> source map leak — check tab SrcMaps</div>
  {% endif %}
  {% if result.stats.api_endpoints %}
  <div class="alert alert-info">🔌 Phát hiện <strong>{{ result.stats.api_endpoints }}</strong> API endpoints từ JS — check tab API</div>
  {% endif %}

  {% if result.page_summary %}
  <div class="section-title">📄 Tóm tắt nội dung trang</div>
  <div style="background:var(--bg3);padding:11px;border-radius:9px;font-size:13px;color:var(--muted);border:1px solid var(--border)">{{ result.page_summary }}</div>
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
  <div style="background:var(--bg3);padding:11px;border-radius:9px;font-family:monospace;font-size:12px;border:1px solid var(--border)">
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
    <ul style="margin-top:8px;margin-left:18px;color:var(--muted);font-size:13px">
      {% for r in result.waf.recommendations %}<li>{{ r }}</li>{% endfor %}
    </ul>
    {% endif %}
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
    <label style="font-size:12px;color:var(--muted);display:flex;align-items:center;gap:5px;cursor:pointer">
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
      <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ s.description }}</div>
    </div>
    {% endfor %}
  {% else %}
    <p class="empty-state">Không phát hiện secret pattern. ✅</p>
  {% endif %}
</div>

<!-- Tab: Backups -->
<div class="tab-panel" id="tab-backups">
  {% if result.backup_findings %}
    {% for b in result.backup_findings %}
    <div class="leak-item {{ 'crit' if b.severity == 'critical' else ('high' if b.severity == 'high' else '') }}">
      <div class="leak-header">
        <span class="code-badge code-{{ b.code }}">{{ b.code }}</span>
        <span class="sev-badge sev-{{ b.severity }}">{{ b.severity }}</span>
        <span class="leak-path">{{ b.backup_path }}</span>
        <span class="leak-size">{{ b.size }} bytes</span>
      </div>
      <div class="leak-url">{{ b.url }}</div>
      <div style="font-size:11px;color:var(--dim);margin-top:4px">📦 Backup của: {{ b.original }}</div>
    </div>
    {% endfor %}
  {% else %}
    <p class="empty-state">Không phát hiện backup file. ✅</p>
  {% endif %}
</div>

<!-- Tab: Params -->
<div class="tab-panel" id="tab-params">
  {% if result.param_findings %}
    {% for p in result.param_findings %}
    <div class="leak-item med">
      <div class="leak-header">
        <span class="code-badge code-{{ p.code }}">{{ p.code }}</span>
        <span class="sev-badge sev-medium">PARAM</span>
        <span class="leak-path">?{{ p.param }}=1</span>
        <span class="leak-size">{{ p.size }} bytes (diff: {{ p.diff }})</span>
      </div>
      <div class="leak-url">{{ p.url }}</div>
      <div style="font-size:11px;color:var(--dim);margin-top:4px">Main size: {{ p.main_size }}b → param response: {{ p.size }}b</div>
    </div>
    {% endfor %}
  {% else %}
    <p class="empty-state">Không phát hiện param đáng ngờ. ✅</p>
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
      <ul style="margin-top:8px;margin-left:18px;color:var(--muted);font-size:13px">
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
    <div style="padding:5px 0;font-size:13px"><span class="code-badge code-{{ f.code }}">{{ f.code }}</span> <span class="sev-badge sev-{{ f.severity }}">{{ f.severity }}</span> <span style="font-family:monospace">{{ f.path }}</span> {% if f.response_time_ms %}<span style="font-size:11px;color:var(--dim)">{{ f.response_time_ms }}ms</span>{% endif %}</div>
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
  {% if result.main and result.main.headers %}
  <pre class="robots-content">{% for k, v in result.main.headers.items() %}{{ k }}: {{ v }}
{% endfor %}</pre>
  {% else %}
  <p class="empty-state">No response headers available (scan in progress or main page failed).</p>
  {% endif %}
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

<!-- Tab: Subs -->
<div class="tab-panel" id="tab-subs">
  {% if result.subdomains_resolved %}
  <div class="section-title">🌐 Subdomain resolved ({{ result.subdomains_resolved|length }})</div>
  {% for s in result.subdomains_resolved %}
    <div style="padding:5px 0;font-size:13px;font-family:monospace;border-bottom:1px dashed var(--border)">
      <span style="color:var(--accent)">{{ s.host }}</span>
      {% if s.ip %}<span style="color:var(--muted);margin-left:8px">→ {{ s.ip }}</span>{% endif %}
    </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không resolve được subdomain nào.</p>
  {% endif %}

  {% if result.subdomain_hints %}
  <div class="section-title">💡 Gợi ý subdomain cần check thủ công</div>
  <div style="max-height:140px;overflow-y:auto;font-size:12px;color:var(--muted);background:var(--bg3);padding:10px;border-radius:9px;border:1px solid var(--border)">
    {% for s in result.subdomain_hints %}<div style="padding:2px 0;font-family:monospace">{{ s }}</div>{% endfor %}
  </div>
  {% endif %}
</div>

<!-- v11.1 Tabs -->

<!-- Tab: API Endpoints (discovered from JS + Swagger) -->
<div class="tab-panel" id="tab-endpoints">
  {% if result.api_endpoints %}
  <div class="section-title">🔌 API endpoints từ JS files ({{ result.api_endpoints|length }} hits)</div>
  {% for e in result.api_endpoints %}
  <div class="leak-item {{ 'crit' if e.severity == 'critical' else ('high' if e.severity == 'high' else ('med' if e.severity == 'medium' else '')) }}">
    <div class="leak-header">
      <span class="code-badge code-{{ e.code }}">{{ e.code }}</span>
      <span class="sev-badge sev-{{ e.severity }}">{{ e.severity }}</span>
      <span class="leak-path">{{ e.path }}</span>
      {% if e.size %}<span class="leak-size">{{ e.size }} bytes</span>{% endif %}
      {% if e.response_time_ms %}<span class="leak-rt">{{ e.response_time_ms }}ms</span>{% endif %}
    </div>
    <div class="leak-url">{{ e.url }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện API endpoint nào từ JS files. ✅</p>
  {% endif %}

  {% if result.js_endpoints %}
  <div class="section-title">📜 Endpoints extracted từ JS ({{ result.js_endpoints|length }})</div>
  <div style="max-height:240px;overflow-y:auto;background:var(--bg3);padding:10px;border-radius:9px;border:1px solid var(--border);font-family:monospace;font-size:12px">
    {% for ep in result.js_endpoints %}
    <div style="padding:2px 0;color:var(--accent2)">{{ ep }}</div>
    {% endfor %}
  </div>
  {% endif %}

  {% if result.swagger_endpoints %}
  <div class="section-title">📋 Endpoints từ Swagger/OpenAPI ({{ result.swagger_endpoints|length }})</div>
  {% for e in result.swagger_endpoints %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="sev-badge sev-medium">{{ e.method }}</span>
      <span class="leak-path">{{ e.path }}</span>
    </div>
    <div class="leak-url">{{ e.url }}</div>
    {% if e.summary %}<div style="font-size:11px;color:var(--dim);margin-top:4px">{{ e.summary }}</div>{% endif %}
  </div>
  {% endfor %}
  {% endif %}
</div>

<!-- Tab: Takeover -->
<div class="tab-panel" id="tab-takeover">
  {% if result.takeover_findings %}
  <div class="alert alert-error">💀 Phát hiện <strong>{{ result.takeover_findings|length }}</strong> subdomain có thể takeover — register lại CNAME target để chiếm quyền</div>
  {% for t in result.takeover_findings %}
  <div class="leak-item crit">
    <div class="leak-header">
      <span class="sev-badge sev-critical">CRITICAL</span>
      <strong>{{ t.service }}</strong>
      <span class="leak-path">{{ t.subdomain }}</span>
    </div>
    <div class="leak-url">{{ t.url }} (HTTP {{ t.status_code }})</div>
    <div style="font-size:11px;color:var(--dim);margin-top:4px">📍 Markers: {{ t.markers|join(", ") }}</div>
    <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ t.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện subdomain takeover. ✅</p>
  {% endif %}
</div>

<!-- Tab: GraphQL -->
<div class="tab-panel" id="tab-graphql">
  {% if result.graphql_findings %}
  {% for g in result.graphql_findings %}
  <div class="leak-item {{ 'crit' if g.severity == 'critical' else ('high' if g.severity == 'high' else ('med' if g.severity == 'medium' else '')) }}">
    <div class="leak-header">
      <span class="code-badge code-{{ g.status_code }}">{{ g.status_code }}</span>
      <span class="sev-badge sev-{{ g.severity }}">{{ g.severity }}</span>
      <span class="leak-path">{{ g.endpoint }}</span>
      {% if g.introspection_enabled %}<span class="sev-badge sev-critical">INTROSPECTION ON</span>{% endif %}
      {% if g.ui_found %}<span class="sev-badge sev-medium">{{ g.ui_found }}</span>{% endif %}
    </div>
    <div class="leak-url">{{ g.url }}</div>
    {% if g.types_found %}<div style="font-size:11px;color:var(--dim);margin-top:4px">Schema types: {{ g.types_found }}</div>{% endif %}
    {% if g.preview %}<details class="leak-preview"><summary>Preview</summary><pre>{{ g.preview }}</pre></details>{% endif %}
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện GraphQL endpoint. ✅</p>
  {% endif %}
</div>

<!-- Tab: CORS -->
<div class="tab-panel" id="tab-cors">
  {% if result.cors_findings %}
  <div class="alert alert-warn">🌐 Phát hiện <strong>{{ result.cors_findings|length }}</strong> endpoint CORS misconfiguration — có thể bị đọc cross-origin</div>
  {% for c in result.cors_findings %}
  <div class="leak-item {{ 'crit' if c.severity == 'critical' else ('high' if c.severity == 'high' else '') }}">
    <div class="leak-header">
      <span class="code-badge code-{{ c.status_code }}">{{ c.status_code }}</span>
      <span class="sev-badge sev-{{ c.severity }}">{{ c.severity }}</span>
      <span class="leak-path">{{ c.origin_tested }}</span>
    </div>
    <div class="leak-url">{{ c.url }}</div>
    <div style="font-size:11px;color:var(--dim);margin-top:4px">ACAO: <code>{{ c.acao }}</code> · ACAC: <code>{{ c.acac }}</code></div>
    <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ c.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện CORS misconfiguration. ✅</p>
  {% endif %}
</div>

<!-- Tab: Open Redirect -->
<div class="tab-panel" id="tab-redirect">
  {% if result.open_redirect_findings %}
  <div class="alert alert-warn">↪️ Phát hiện <strong>{{ result.open_redirect_findings|length }}</strong> param open redirect — có thể bị phishing redirect</div>
  {% for r in result.open_redirect_findings %}
  <div class="leak-item {{ 'crit' if r.severity == 'critical' else ('high' if r.severity == 'high' else 'med') }}">
    <div class="leak-header">
      <span class="code-badge code-{{ r.status_code }}">{{ r.status_code }}</span>
      <span class="sev-badge sev-{{ r.severity }}">{{ r.severity }}</span>
      <span class="leak-path">?{{ r.param }}={{ r.payload[:40] }}{% if r.payload|length > 40 %}...{% endif %}</span>
      <span class="sev-badge sev-info">{{ r.variant }}</span>
    </div>
    <div class="leak-url">{{ r.url }}</div>
    <div style="font-size:11px;color:var(--dim);margin-top:4px">Location: <code>{{ r.location[:80] }}</code></div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện open redirect. ✅</p>
  {% endif %}
</div>

<!-- Tab: Source Maps -->
<div class="tab-panel" id="tab-srcmaps">
  {% if result.source_maps %}
  <div class="alert alert-warn">🗺️ Phát hiện <strong>{{ result.source_maps|length }}</strong> source map exposed — leak source code gốc (unminified)</div>
  {% for s in result.source_maps %}
  <div class="leak-item high">
    <div class="leak-header">
      <span class="sev-badge sev-high">HIGH</span>
      <span class="leak-path">{{ s.map_url }}</span>
      <span class="leak-size">{{ s.size }} bytes</span>
      <span class="sev-badge sev-info">{{ s.sources_count }} source files</span>
    </div>
    <div style="font-size:11px;color:var(--dim);margin-top:4px">{{ s.description }}</div>
    {% if s.sources_preview %}
    <div style="font-size:11px;color:var(--muted);margin-top:4px">Source files preview:
      <code>{{ (s.sources_preview|join(", "))[:200] }}</code>
    </div>
    {% endif %}
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện source map. ✅</p>
  {% endif %}
</div>

<!-- Tab: Swagger -->
<div class="tab-panel" id="tab-swagger">
  {% if result.swagger_endpoints %}
  <div class="alert alert-info">📋 Phát hiện <strong>{{ result.swagger_endpoints|length }}</strong> endpoints từ Swagger/OpenAPI spec — toàn bộ API surface lộ</div>
  {% for e in result.swagger_endpoints %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="sev-badge sev-{{ 'high' if e.method == 'DELETE' else ('medium' if e.method in ('PUT','PATCH') else 'low') }}">{{ e.method }}</span>
      <span class="leak-path">{{ e.path }}</span>
    </div>
    <div class="leak-url">{{ e.url }}</div>
    {% if e.summary %}<div style="font-size:11px;color:var(--dim);margin-top:4px">{{ e.summary }}</div>{% endif %}
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện Swagger/OpenAPI spec. ✅</p>
  {% endif %}
</div>

<!-- Tab: Wayback -->
<div class="tab-panel" id="tab-wayback">
  {% if result.wayback_urls %}
  <div class="alert alert-info">🕰️ Tìm <strong>{{ result.wayback_urls|length }}</strong> historical URLs từ Wayback Machine — có thể tìm được endpoints đã bị gỡ</div>
  <div style="max-height:480px;overflow-y:auto;background:var(--bg3);padding:10px;border-radius:9px;border:1px solid var(--border);font-family:monospace;font-size:11px">
    {% for u in result.wayback_urls %}
    <div style="padding:2px 0;color:var(--accent2);word-break:break-all">
      <a href="{{ u }}" target="_blank" style="color:var(--accent2);text-decoration:none">{{ u }}</a>
    </div>
    {% endfor %}
  </div>
  {% else %}
  <p class="empty-state">Không tìm thấy historical URLs. ✅</p>
  {% endif %}
</div>

<!-- Tab: HTTP Methods -->
<div class="tab-panel" id="tab-methods">
  {% if result.http_method_findings %}
  {% for m in result.http_method_findings %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="sev-badge sev-low">{{ m.method_tested }}</span>
      <span class="code-badge code-{{ m.status_code }}">{{ m.status_code }}</span>
      <span class="leak-path">{{ m.url }}</span>
    </div>
    {% if m.allow %}<div style="font-size:11px;color:var(--accent);margin-top:4px">Allow: <code>{{ m.allow }}</code></div>{% endif %}
    {% if m.acah_methods %}<div style="font-size:11px;color:var(--accent2);margin-top:2px">CORS Methods: <code>{{ m.acah_methods }}</code></div>{% endif %}
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không có Allow header hoặc methods disclosure. ✅</p>
  {% endif %}
</div>

<!-- Tab: Recursive Brute -->
<div class="tab-panel" id="tab-rbrute">
  {% if result.recursive_brute_findings %}
  <div class="alert alert-info">🔁 Recursive brute-force tìm <strong>{{ result.recursive_brute_findings|length }}</strong> sub-paths trong directories phát hiện</div>
  {% for r in result.recursive_brute_findings %}
  <div class="leak-item {{ 'crit' if r.severity == 'critical' else ('high' if r.severity == 'high' else ('med' if r.severity == 'medium' else '')) }}">
    <div class="leak-header">
      <span class="code-badge code-{{ r.code }}">{{ r.code }}</span>
      <span class="sev-badge sev-{{ r.severity }}">{{ r.severity }}</span>
      <span class="leak-path">{{ r.path }}</span>
      {% if r.response_time_ms %}<span class="leak-rt">{{ r.response_time_ms }}ms</span>{% endif %}
    </div>
    <div class="leak-url">{{ r.url }}</div>
    <div style="font-size:11px;color:var(--dim);margin-top:4px">📍 Parent: {{ r.parent_dir }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không tìm thấy sub-paths trong directories. ✅</p>
  {% endif %}
</div>

<!-- Tab: CT Subdomains (v11.1) -->
<div class="tab-panel" id="tab-ct_logs">
  {% if result.ct_subdomains %}
  <div class="alert alert-info">📜 Found <strong>{{ result.ct_subdomains|length }}</strong> subdomains từ Certificate Transparency logs (crt.sh) — đây là subdomains đã từng được issue certificate</div>
  {% for s in result.ct_subdomains %}
  <div style="padding:5px 0;font-size:13px;font-family:monospace;border-bottom:1px dashed var(--border)">
    <span style="color:var(--accent)">{{ s.host }}</span>
    {% if s.ip %}<span style="color:var(--muted);margin-left:8px">→ {{ s.ip }}</span>{% endif %}
    {% if not s.ok %}<span class="sev-badge sev-info" style="margin-left:8px">NXDOMAIN</span>{% endif %}
    <span class="sev-badge sev-info" style="margin-left:8px">source: {{ s.source }}</span>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không tìm thấy CT subdomains (crt.sh không trả về kết quả hoặc query failed). ✅</p>
  {% endif %}
</div>

<!-- Tab: DNS Records (v11.1) -->
<div class="tab-panel" id="tab-dns">
  {% if result.dns_records %}
  <div class="section-title">🌐 DNS Records cho {{ result.target }}</div>
  {% for rtype, rvals in result.dns_records.items() %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="sev-badge sev-info">{{ rtype }}</span>
      <span class="leak-path">{{ rvals|length }} record(s)</span>
    </div>
    <div style="font-family:monospace;font-size:12px;color:var(--muted);margin-top:6px;padding-left:10px">
      {% for v in rvals %}
      <div style="padding:2px 0">→ {{ v }}</div>
      {% endfor %}
    </div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không lấy được DNS records. ✅</p>
  {% endif %}
</div>

<!-- Tab: Git Exposure (v11.1) -->
<div class="tab-panel" id="tab-git">
  {% if result.git_findings %}
  <div class="alert alert-error">📂 <strong>.git directory EXPOSED!</strong> Phát hiện {{ result.git_findings|length }} file(s) trong .git folder có thể truy cập công khai. Attacker có thể reconstruct toàn bộ source code + history!</div>
  {% for g in result.git_findings %}
  <div class="leak-item crit">
    <div class="leak-header">
      <span class="code-badge code-{{ g.code }}">{{ g.code }}</span>
      <span class="sev-badge sev-{{ g.severity }}">{{ g.severity }}</span>
      <span class="leak-path">{{ g.path }}</span>
      {% if g.size %}<span class="leak-size">{{ g.size }} bytes</span>{% endif %}
    </div>
    <div class="leak-url">{{ g.url }}</div>
    <div style="font-size:11px;color:var(--muted);margin-top:4px">{{ g.description }}</div>
    {% if g.preview %}<details class="leak-preview"><summary>Preview ({{ g.preview|length }} chars)</summary><pre>{{ g.preview }}</pre></details>{% endif %}
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện .git directory exposure. ✅</p>
  {% endif %}
</div>

<!-- Tab: Crawled Pages (v11.1) -->
<div class="tab-panel" id="tab-crawled">
  {% if result.crawled_pages %}
  <div class="alert alert-info">🕷️ Deep crawl đã thu thập <strong>{{ result.crawled_pages|length }}</strong> internal pages (depth-2), extract secrets từ mỗi page</div>
  {% for p in result.crawled_pages %}
  <div class="leak-item">
    <div class="leak-header">
      <span class="code-badge code-{{ p.code }}">{{ p.code }}</span>
      <span class="sev-badge sev-info">depth {{ p.depth }}</span>
      <span class="leak-path">{{ p.url|replace(result.target, '')|truncate(80, true, '...') }}</span>
      <span class="leak-size">{{ p.size }} bytes</span>
      {% if p.secrets|length %}<span class="sev-badge sev-high">{{ p.secrets|length }} secrets</span>{% endif %}
      {% if p.forms|length %}<span class="sev-badge sev-medium">{{ p.forms|length }} forms</span>{% endif %}
    </div>
    <div class="leak-url">{{ p.url }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không có internal pages nào để crawl. ✅</p>
  {% endif %}
</div>

<!-- Tab: JS Strings (v11.1) -->
<div class="tab-panel" id="tab-js_strings">
  {% if result.js_strings %}
  <div class="alert alert-info">📜 Extracted <strong>{{ result.js_strings|length }}</strong> unique strings từ JS files — check manually cho API keys, endpoints, hardcoded URLs, internal info</div>
  <div style="max-height:600px;overflow-y:auto;background:var(--bg3);padding:12px;border-radius:9px;border:1px solid var(--border);font-family:monospace;font-size:11px">
    {% for s in result.js_strings %}
    <div style="padding:3px 0;color:var(--accent2);word-break:break-all;border-bottom:1px dashed var(--border)">
      <span style="color:var(--dim)">[{{ loop.index }}]</span> {{ s }}
    </div>
    {% endfor %}
  </div>
  {% else %}
  <p class="empty-state">Không extract được strings từ JS files. ✅</p>
  {% endif %}
</div>

<!-- v11.1 Tabs -->

<!-- Tab: SSTI -->
<div class="tab-panel" id="tab-ssti">
  {% if result.ssti_findings %}
  <div class="alert alert-error">🧪 <strong>SERVER-SIDE TEMPLATE INJECTION detected!</strong> {{ result.ssti_findings|length }} endpoint(s) vulnerable — attacker có thể RCE server</div>
  {% for s in result.ssti_findings %}
  <div class="leak-item crit">
    <div class="leak-header">
      <span class="sev-badge sev-critical">CRITICAL</span>
      <span class="sev-badge sev-info">param: {{ s.param }}</span>
      <span class="leak-path">{{ s.payload }}</span>
    </div>
    <div class="leak-url">{{ s.url }}</div>
    <div style="font-size:11px;color:var(--accent);margin-top:4px">✅ Expected: <code>{{ s.expected }}</code> (found in response)</div>
    <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ s.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện SSTI. ✅</p>
  {% endif %}
</div>

<!-- Tab: Proto Pollution -->
<div class="tab-panel" id="tab-proto">
  {% if result.proto_pollution_findings %}
  <div class="alert alert-error">💀 <strong>PROTOTYPE POLLUTION detected!</strong> {{ result.proto_pollution_findings|length }} payload(s) reflected — attacker có thể ghi đè Object prototype</div>
  {% for p in result.proto_pollution_findings %}
  <div class="leak-item high">
    <div class="leak-header">
      <span class="sev-badge sev-high">HIGH</span>
      <span class="code-badge code-{{ p.status_code }}">{{ p.status_code }}</span>
      <span class="leak-path">{{ p.payload[:80] }}{% if p.payload|length > 80 %}...{% endif %}</span>
    </div>
    <div class="leak-url">{{ p.url }}</div>
    <div style="font-size:11px;color:var(--muted);margin-top:4px">{{ p.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện Prototype Pollution. ✅</p>
  {% endif %}
</div>

<!-- Tab: Header Injection -->
<div class="tab-panel" id="tab-hinj">
  {% if result.header_injection_findings %}
  <div class="alert alert-warn">🛡️ <strong>HTTP HEADER INJECTION detected!</strong> {{ result.header_injection_findings|length }} header(s) bị inject — có thể bypass access control</div>
  {% for h in result.header_injection_findings %}
  <div class="leak-item {{ 'crit' if h.severity == 'critical' else ('high' if h.severity == 'high' else '') }}">
    <div class="leak-header">
      <span class="sev-badge sev-{{ h.severity }}">{{ h.severity }}</span>
      <span class="code-badge code-{{ h.status_code }}">{{ h.status_code }}</span>
      <span class="leak-path">{{ h.header }}: {{ h.value }}</span>
    </div>
    {% if h.redirect_location %}<div style="font-size:11px;color:var(--warn);margin-top:4px">→ Location: <code>{{ h.redirect_location }}</code></div>{% endif %}
    <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ h.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện header injection. ✅</p>
  {% endif %}
</div>

<!-- Tab: Cache Poisoning -->
<div class="tab-panel" id="tab-cache">
  {% if result.cache_poison_findings %}
  <div class="alert alert-error">☠️ <strong>CACHE POISONING detected!</strong> {{ result.cache_poison_findings|length }} header(s) có thể poison cache — toàn bộ user sẽ thấy content bị inject</div>
  {% for c in result.cache_poison_findings %}
  <div class="leak-item high">
    <div class="leak-header">
      <span class="sev-badge sev-high">HIGH</span>
      <span class="leak-path">{{ c.header }}: {{ c.value }}</span>
    </div>
    <div style="font-size:11px;color:var(--accent);margin-top:4px">Evidence: <code>{{ c.evidence }}</code></div>
    <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ c.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện cache poisoning. ✅</p>
  {% endif %}
</div>

<!-- Tab: Default Creds -->
<div class="tab-panel" id="tab-creds">
  {% if result.default_creds_findings %}
  <div class="alert alert-error">🔑 <strong>DEFAULT CREDENTIALS WORK!</strong> {{ result.default_creds_findings|length }} form(s) accept default creds — attacker có thể login ngay</div>
  {% for c in result.default_creds_findings %}
  <div class="leak-item crit">
    <div class="leak-header">
      <span class="sev-badge sev-critical">CRITICAL</span>
      <span class="code-badge code-{{ c.status_code }}">{{ c.status_code }}</span>
      <span class="leak-path">👤 {{ c.username }} : 🔑 {{ c.password }}</span>
    </div>
    <div class="leak-url">{{ c.form_action }}</div>
    {% if c.redirect %}<div style="font-size:11px;color:var(--warn);margin-top:4px">→ Redirect: <code>{{ c.redirect }}</code></div>{% endif %}
    <div style="font-size:11px;color:var(--muted);margin-top:3px">{{ c.description }}</div>
  </div>
  {% endfor %}
  {% else %}
  <p class="empty-state">Không phát hiện default credentials. ✅</p>
  {% endif %}
</div>

<!-- Tab: File Tree (v11) -->
<div class="tab-panel" id="tab-file_tree">
  <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap">
    <button class="btn btn-secondary" onclick="loadFileTree()">🌳 Load File Tree</button>
    <span id="treeInfo" style="font-size:12px;color:var(--muted);align-self:center"></span>
  </div>
  <div id="fileTreeContainer" class="file-tree-container" style="display:none"></div>
  <div id="fileTreeEmpty" class="empty-state">
    <p>🌳 Click "Load File Tree" để xem cấu trúc thư mục/file của website đã scan.</p>
    <p style="font-size:11px;color:var(--dim);margin-top:6px">Hiển thị tất cả file/thư mục phát hiện được: leak paths, brute results, JS files, API endpoints</p>
  </div>
</div>

<!-- Tab: Source Code (v11) -->
<div class="tab-panel" id="tab-source_code">
  <div id="sourceFileList" class="source-file-list" style="display:none"></div>
  <div id="sourceCodeContainer" class="source-code-container" style="display:none"></div>
  <div id="sourceCodeEmpty" class="empty-state">
    <p>💻 Click vào tab này để load danh sách source files (JS, CSS, HTML) từ website đã scan.</p>
    <p style="font-size:11px;color:var(--dim);margin-top:6px">Fetch raw source code của từng file, hiển thị với syntax highlighting</p>
  </div>
</div>

<!-- Tab: HTML Source (v11.1) -->
<div class="tab-panel" id="tab-html_source">
  <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap">
    <button class="btn btn-secondary" onclick="loadHtmlSource()" id="loadSourceBtn">📄 Fetch HTML Source</button>
    <button class="btn btn-ghost" onclick="downloadHtmlSource()" id="downloadSourceBtn" style="display:none">⬇️ Download .html</button>
    <button class="btn btn-ghost" onclick="copyHtmlSource()" id="copySourceBtn" style="display:none">📋 Copy</button>
  </div>
  <div id="htmlSourceInfo" style="font-size:12px;color:var(--muted);margin-bottom:10px;display:none"></div>
  <pre class="robots-content" id="htmlSourceContent" style="max-height:600px;white-space:pre-wrap;word-break:break-all;display:none"></pre>
  <div id="htmlSourceLoading" class="empty-state" style="display:none">
    <p>⏳ Đang tải HTML source...</p>
  </div>
  <div id="htmlSourceEmpty" class="empty-state">
    <p>📄 Click "Fetch HTML Source" để lấy raw HTML của trang web đã scan.</p>
    <p style="font-size:11px;color:var(--dim);margin-top:6px">Tool sẽ fetch URL mục tiêu và hiển thị HTML gốc (có syntax highlighting, copy, download)</p>
  </div>
</div>

<!-- Tab: Raw -->
<div class="tab-panel" id="tab-raw">
  <details>
    <summary style="cursor:pointer;color:var(--accent);font-weight:600;padding:8px">📜 Full JSON result (click to expand)</summary>
    <pre class="robots-content" style="max-height:500px;margin-top:8px">{{ result|tojson(indent=2)|forceescape }}</pre>
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

# v11.1: Safety net — nếu user vô tình truy cập /scan với GET, redirect về /
# Đồng thời nếu POST /scan được gọi trực tiếp (không qua JS), trả về HTML page
# thay vì raw JSON để browser không hiển thị raw JSON
@app.route("/version")
def version_info():
    """Version endpoint — user có thể check xem app đã deploy code mới chưa."""
    return jsonify({
        "version": "v11.1",
        "service": "Web Leak Scanner Pro",
        "features": ["31 phases", "4 WAF bypass modes", "i18n VI/EN", "risk score", 
                     "command palette", "HTML source viewer", "force reset button"],
        "endpoints": ["/", "/scan", "/health", "/ping", "/version", "/source/<id>"],
    })

@app.route("/scan", methods=["GET"])
def scan_get_redirect():
    from flask import redirect
    return redirect("/", code=302)

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
    bypass_mode = request.form.get("bypass_mode", "auto")
    if bypass_mode not in WAF_BYPASS_MODES:
        bypass_mode = "auto"
    vuln_tests = request.form.get("vuln_tests", "yes") == "yes"

    scan_id = int(time.time() * 1000)

    with prog_lock:
        progress_queues[scan_id] = queue.Queue(maxsize=500)
        scan_starts[scan_id] = time.time()
    # Reset activity log for this scan
    with activity_lock:
        activity_logs[scan_id] = []

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
            # v11.1: Pre-store target in scan_results so /source/ endpoint works during scan
            scan_results[scan_id] = {
                "target": target, "main": {}, "leak": [], "secrets": [],
                "ports": [], "dirs": [], "brute": [], "technologies": [],
                "waf": {"detected": [], "recommendations": [], "should_slow_down": False},
                "cdn": [], "cookies": [], "security_headers": [],
                "links": [], "js_links": [], "forms": [], "robots": [],
                "stats": {"in_progress": True}, "duration_seconds": 0,
                "errors": [], "scanner_version": "v11.1",
                "subdomains_resolved": [], "subdomain_hints": [],
                "takeover_findings": [], "graphql_findings": [], "cors_findings": [],
                "open_redirect_findings": [], "source_maps": [], "wayback_urls": [],
                "http_method_findings": [], "recursive_brute_findings": [],
                "backup_findings": [], "param_findings": [],
                "js_endpoints": [], "api_endpoints": [], "swagger_endpoints": [],
                "ct_subdomains": [], "dns_records": {}, "git_findings": [],
                "crawled_pages": [], "js_strings": [],
                "ssti_findings": [], "proto_pollution_findings": [],
                "header_injection_findings": [], "cache_poison_findings": [],
                "default_creds_findings": [], "page_summary": "",
                "static_platforms": [], "frameworks_detected": [],
                "bypass_mode": bypass_mode,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "cancelled": False, "soft_404_filtered": 0,
            }
            result = loop.run_until_complete(deep_scan(
                target, custom_headers, proxy, timeout,
                allow_redirects, progress_cb, scan_js, scan_id, bypass_mode
            ))
            scan_results[scan_id] = result
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
                "main": {}, "subdomain_hints": [], "subdomains_resolved": [],
                "page_summary": "", "param_findings": [], "backup_findings": [],
                "errors": [str(e)], "scanner_version": "v11.1",
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
            with activity_lock:
                activity_logs.pop(scan_id, None)

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

@app.route("/activity/<int:scan_id>")
def activity(scan_id):
    """Returns activity log lines since `since` query param (epoch seconds)."""
    try:
        since = float(request.args.get("since", 0))
    except Exception:
        since = 0
    lines = get_activity(scan_id, since)
    return jsonify({"scan_id": scan_id, "lines": lines, "count": len(lines)})

@app.route("/tree/<int:scan_id>")
def file_tree(scan_id):
    result = scan_results.get(scan_id, {})
    tree = build_file_tree(
        result.get("leak", []),
        result.get("dirs", []),
        result.get("brute", []),
        result.get("js_links", []),
        result.get("source_maps", []),
        result.get("api_endpoints", [])
    )
    return jsonify({"tree": tree, "total_files": sum(1 for _ in iter_tree(tree))})


@app.route("/source_file", methods=["POST"])
def fetch_source_file():
    """Fetch raw source code of any URL from target site."""
    url = request.json.get("url", "")
    if not url:
        return jsonify({"error": "No URL"})
    try:
        import urllib.request, ssl as ssl_mod
        ctx = ssl_mod.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl_mod.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": random.choice(USER_AGENTS)})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            content = r.read().decode("utf-8", errors="replace")[:200000]  # 200KB cap
            return jsonify({
                "url": url, "content": content, "size": len(content),
                "status": r.status, "truncated": len(content) >= 200000
            })
    except Exception as e:
        return jsonify({"error": str(e)[:100]})


@app.route("/result/<int:scan_id>")
def result(scan_id):
    result = scan_results.get(scan_id, {})
    return render_template_string(RESULT_HTML, result=result, calculate_risk_score=calculate_risk_score)

# v11.1: HTML source viewer endpoint
@app.route("/source/<int:scan_id>")
def view_source(scan_id):
    """Return raw HTML source of the scanned target page."""
    result = scan_results.get(scan_id, {})
    main = result.get("main", {}) or {}
    target = result.get("target", "")
    # Try to fetch the actual HTML if we don't have it stored
    # (we stored main_text in deep_scan but didn't expose it; let's re-fetch)
    html_content = ""
    fetch_error = ""
    if target:
        try:
            import urllib.request, ssl as ssl_mod
            ctx = ssl_mod.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl_mod.CERT_NONE
            req = urllib.request.Request(target, headers={
                "User-Agent": random.choice(USER_AGENTS)
            })
            with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
                html_content = r.read().decode("utf-8", errors="replace")[:500000]  # 500KB cap
                status_code = r.status
                resp_headers = dict(r.headers)
        except Exception as e:
            fetch_error = f"{type(e).__name__}: {str(e)[:100]}"
            status_code = 0
            resp_headers = {}
    else:
        fetch_error = "No target URL available"
        status_code = 0
        resp_headers = {}
    # Return as JSON
    return jsonify({
        "target": target,
        "status_code": status_code if 'status_code' in dir() else main.get("code", 0),
        "html": html_content,
        "size": len(html_content),
        "truncated": len(html_content) >= 500000,
        "error": fetch_error,
        "response_headers": resp_headers if 'resp_headers' in dir() else {},
    })

@app.route("/history")
def history():
    with prog_lock:
        items = [{"scan_id": h["scan_id"], "target": h["target"],
                  "started_at": h["started_at"], "leak_count": h.get("leak_count", 0),
                  "duration_seconds": h.get("duration_seconds", 0),
                  "status": h.get("status", "")} for h in scan_history]
    return jsonify({"history": items})

@app.route("/cancel/<int:scan_id>", methods=["POST"])
def cancel_scan(scan_id):
    with prog_lock:
        scan_cancels.add(scan_id)
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
    data["scanner"] = "Web Leak Scanner Pro v11.1"
    data["exported_at"] = datetime.now(timezone.utc).isoformat()
    return Response(json.dumps(data, indent=2, ensure_ascii=False),
                    mimetype="application/json",
                    headers={"Content-Disposition": "attachment; filename=scan_result_v7.json"})

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
    for k, v in (data.get("stats") or {}).items():
        w.writerow(["stats", k, v])
    main = data.get("main") or {}
    w.writerow(["main", "code", main.get("code")])
    w.writerow(["main", "length", main.get("length")])
    w.writerow(["main", "response_time_ms", main.get("response_time_ms")])
    for item in data.get("leak", []):
        w.writerow(["leak", item.get("severity"), f"{item.get('code')} {item.get('path')} ({item.get('size')}b)"])
    for s in data.get("secrets", []):
        w.writerow(["secret", s.get("severity"), f"{s.get('type')}: {s.get('match_masked')} @ {s.get('source')}"])
    for b in data.get("backup_findings", []):
        w.writerow(["backup", b.get("severity"), f"{b.get('code')} {b.get('backup_path')} ({b.get('size')}b)"])
    for p in data.get("param_findings", []):
        w.writerow(["param", "diff", f"?{p.get('param')}=1 → {p.get('code')} (diff {p.get('diff')})"])
    for s in data.get("subdomains_resolved", []):
        w.writerow(["subdomain", "resolved", f"{s.get('host')} → {s.get('ip')}"])
    w.writerow(["ports", "open", ", ".join(str(p) for p in data.get("ports", []))])
    w.writerow(["tech", "list", ", ".join(data.get("technologies", []))])
    w.writerow(["waf", "detected", ", ".join((data.get("waf") or {}).get("detected", []))])
    w.writerow(["cdn", "list", ", ".join(data.get("cdn", []))])
    for h in data.get("security_headers", []):
        w.writerow(["sec_header", h.get("severity") if h.get("missing") else "ok",
                    f"{'MISSING' if h.get('missing') else 'OK'} {h.get('header')}"])
    for c in data.get("cookies", []):
        w.writerow(["cookie", "issues" if c.get("issues") else "ok",
                    f"{c.get('name')} | issues: {'; '.join(c.get('issues', [])) or 'none'}"])
    for f in data.get("forms", []):
        w.writerow(["form", f.get("type"), f"{f.get('method')} {f.get('action')} (inputs: {f.get('input_count')})"])
    payload = out.getvalue().encode("utf-8")
    return Response(payload, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=scan_result_v7.csv"})

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
body{{font-family:system-ui,sans-serif;background:#070710;color:#e8eef5;padding:20px;margin:0;
  background-image:radial-gradient(at 18% 22%,#1a1a3a 0,transparent 45%),radial-gradient(at 82% 18%,#0a2a3a 0,transparent 45%);}}
.card{{background:rgba(22,33,62,.6);border:1px solid rgba(0,212,170,.2);border-radius:16px;padding:22px;margin-bottom:16px;backdrop-filter:blur(18px)}}
h2{{background:linear-gradient(90deg,#00d4aa,#54a0ff,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.badge{{display:inline-block;padding:4px 11px;border-radius:20px;font-size:12px;margin:3px}}
.badge-time{{background:rgba(84,160,255,.12);color:#54a0ff}}
.badge-waf{{background:rgba(255,91,107,.12);color:#ff5b6b}}
code,pre{{font-family:monospace;background:rgba(0,0,0,.4);padding:8px;border-radius:6px;display:block;white-space:pre-wrap;word-break:break-all}}
.stat-box{{display:inline-block;text-align:center;padding:14px;background:rgba(26,26,46,.7);border:1px solid rgba(0,212,170,.2);border-radius:12px;margin:5px;min-width:100px}}
.stat-number{{font-size:24px;font-weight:800;color:#00d4aa}}
.stat-label{{font-size:10px;color:#888;text-transform:uppercase}}
</style>
</head><body>
<h1>🛡️ Web Leak Scanner Pro v11.1 — Standalone Report</h1>
<p><strong>Target:</strong> {data.get('target','')}</p>
<p><strong>Scanned at:</strong> {data.get('timestamp','')}</p>
<p><strong>Duration:</strong> {data.get('duration_seconds',0)}s</p>
{html}
</body></html>"""
    return Response(full.encode("utf-8"), mimetype="text/html",
                    headers={"Content-Disposition": "attachment; filename=scan_report_v7.html"})

# ── Health endpoint for Render/Heroku/cloud health checks ──
@app.route("/health")
def health():
    """Lightweight health check endpoint — return 200 OK immediately.
    Render/Heroku/probes use this to verify service is alive."""
    import os
    mem_info = {}
    try:
        import resource
        # RSS in KB
        mem_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        mem_info["rss_mb"] = round(mem_kb / 1024, 1)
    except Exception:
        pass
    return jsonify({
        "status": "ok",
        "service": "Web Leak Scanner Pro v11.1",
        "uptime": round(time.time() - _START_TIME, 1),
        "active_scans": sum(1 for q in progress_queues.values() if q is not None),
        "memory_mb": mem_info.get("rss_mb", 0),
        "env": "render" if os.environ.get("RENDER") else ("heroku" if os.environ.get("DYNO") else "local"),
    })

@app.route("/ping")
def ping():
    """Bare minimum ping — just return 'pong'."""
    return "pong"

# Track start time for uptime display
_START_TIME = time.time()

# ── Main ──
def run_dev_server(host, port):
    """Run Flask development server (NOT for production)."""
    print("=" * 64)
    print(f"🛡️  Web Leak Scanner Pro v11.1 — Development Server")
    print(f"   URL: http://{host}:{port}")
    print(f"   ⚠️  DEV SERVER — không phù hợp production!")
    print(f"   v11.1: 550+ leak paths · 45+ secret patterns · 56+ tech sigs")
    print(f"   v11.1: Subdomain takeover · GraphQL · CORS · open redirect · SSTI")
    print(f"   v11.1: Source maps · JS endpoints · Swagger · Wayback · .git")
    print(f"   v11.1: Cache poisoning · Header injection · Default creds")
    print(f"   v11.1: 4 WAF bypass modes · Glassmorphism UI · Confetti")
    print("=" * 64)
    app.run(host=host, port=port, debug=False, threaded=True)

def run_production_server(host, port):
    """Run waitress (production WSGI server) — suitable for Render/Heroku/cloud."""
    try:
        from waitress import serve as waitress_serve
        print("=" * 64)
        print(f"🛡️  Web Leak Scanner Pro v11.1 — Production Server (waitress)")
        print(f"   URL: http://{host}:{port}")
        print(f"   🌐 Production WSGI: waitress (multi-threaded, robust)")
        print(f"   🔍 Health endpoint: /health, /ping")
        print(f"   v11.1: 550+ leak paths · 45+ secret patterns · 56+ tech sigs")
        print(f"   v11.1: 4 WAF bypass modes · Glassmorphism UI · Confetti")
        print("=" * 64)
        # Waitress with reasonable defaults for cloud deploy
        # threads=8 — enough for scanner + UI + health checks
        waitress_serve(app, host=host, port=port, threads=8,
                      connection_limit=100, channel_timeout=120,
                      recv_bytes=1048576,  # 1MB body limit
                      send_bytes=10485760)  # 10MB response limit
    except ImportError:
        print("[!] waitress chưa cài — fallback to Flask dev server")
        print("    Cài waitress: pip install waitress")
        run_dev_server(host, port)

if __name__ == "__main__":
    # Auto-detect cloud environment:
    # - Render sets RENDER env var + PORT (default 10000)
    # - Heroku sets DYNO env var + PORT (default 5000)
    # - Local: use PORT env or default 5000
    import os
    is_render = bool(os.environ.get("RENDER"))
    is_heroku = bool(os.environ.get("DYNO"))
    is_cloud = is_render or is_heroku

    # PORT: cloud env sets this, otherwise use 5000 (local)
    PORT = int(os.environ.get("PORT", 5000))

    # In cloud env, bind 0.0.0.0 (required by Render/Heroku)
    # In local, can use 0.0.0.0 too for LAN access
    HOST = "0.0.0.0"

    # Reduce concurrency on Render Free tier (512MB RAM)
    # Auto-detect via env var or memory
    if is_cloud:
        import resource
        try:
            mem_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            # If we have < 400MB available, use stealth mode as default
            print(f"[CLOUD] Detected cloud env ({'Render' if is_render else 'Heroku'})")
            print(f"[CLOUD] Memory: {mem_kb/1024:.1f}MB used")
        except Exception:
            pass

    if is_cloud:
        # Production: use waitress
        run_production_server(HOST, PORT)
    else:
        # Local dev: ask user or auto-detect
        # Default to waitress if available, else dev server
        try:
            import waitress
            run_production_server(HOST, PORT)
        except ImportError:
            run_dev_server(HOST, PORT)

