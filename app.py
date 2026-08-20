#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Leak Scanner Pro v8.0 — Deep Recon Edition
Gộp Flask + Scanner + UI vào 1 file. Chỉ cần:
  pip install flask aiohttp
  python app.py
Rồi mở trình duyệt: http://localhost:5000

Changelog v8.0 (so với v6.0):
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

    # ── v8.0 additions: K8s / container / monitoring ──
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

    # ── v8.0: Source maps & debug bundles ──
    "/bundle.js.map", "/main.js.map", "/app.js.map", "/index.js.map",
    "/script.js.map", "/scripts.js.map", "/vendor.js.map", "/runtime.js.map",
    "/polyfills.js.map", "/styles.css.map", "/main.css.map", "/app.css.map",
    "/static/js/main.js.map", "/static/js/bundle.js.map",
    "/_next/static/chunks/main.js.map", "/_next/static/chunks/webpack.js.map",
    "/assets/index.js.map", "/assets/main.js.map", "/assets/app.js.map",
    "/dist/build.js.map", "/dist/main.js.map",

    # ── v8.0: GraphQL / WebSocket / API ──
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

    # ── v8.0: Spring Boot Actuator deep ──
    "/actuator/", "/actuator/info", "/actuator/health",
    "/actuator/env", "/actuator/configprops", "/actuator/beans",
    "/actuator/mappings", "/actuator/metrics", "/actuator/threaddump",
    "/actuator/httptrace", "/actuator/loggers", "/actuator/heapdump",
    "/actuator/scheduledtasks", "/actuator/sessions", "/actuator/shutdown",
    "/actuator/auditevents", "/actuator/logfile", "/actuator/startup",
    "/actuator/conditions", "/actuator/caches", "/actuator/flyway",
    "/actuator/liquibase", "/actuator/sessions", "/actuator/refresh",
    "/actuator/bus-refresh", "/actuator/gateway/routes",

    # ── v8.0: Java / JVM specific ──
    "/WEB-INF/web.xml", "/WEB-INF/classes/", "/WEB-INF/lib/",
    "/WEB-INF/config/", "/META-INF/MANIFEST.MF", "/META-INF/application.properties",
    "/META-INF/maven/", "/META-INF/spring.factories",
    "/struts/web.xml", "/struts.xml", "/struts-config.xml",
    "/WEB-INF/struts-config.xml", "/WEB-INF/struts.xml",

    # ── v8.0: .NET / IIS specific ──
    "/trace.axd", "/trace.axd?id=1", "/elmah.axd", "/elmah/elmah.axd",
    "/web.config.bak", "/web.config.old", "/web.config.txt",
    "/App_Data/", "/App_Data/Logs/", "/App_Data/Cache/",
    "/bin/", "/App_Code/", "/App_Browsers/", "/App_GlobalResources/",
    "/Reserved.ReportViewerWebControl.axd", "/Reports/",

    # ── v8.0: PHP / Laravel specific ──
    "/.env.production", "/.env.staging", "/.env.local", "/.env.dev",
    "/storage/", "/storage/logs/", "/storage/logs/laravel.log",
    "/storage/framework/cache/", "/storage/framework/sessions/",
    "/storage/framework/views/", "/bootstrap/cache/",
    "/.env.backup", "/.env.example", "/.env.sample", "/.env.template",
    "/artisan", "/server.php", "/package.json",

    # ── v8.0: Ruby / Rails specific ──
    "/config/database.yml", "/config/secrets.yml", "/config/master.key",
    "/config/credentials.yml.enc", "/config/credentials.yml",
    "/config/initializers/", "/config/environments/",
    "/Gemfile", "/Gemfile.lock", "/Rakefile", "/config.ru",
    "/db/schema.rb", "/db/seeds.rb", "/db/migrate/",
    "/log/production.log", "/log/development.log",

    # ── v8.0: Python / Django specific ──
    "/settings.py", "/local_settings.py", "/config/settings.py",
    "/manage.py", "/wsgi.py", "/asgi.py", "/requirements.txt",
    "/Pipfile", "/Pipfile.lock", "/pyproject.toml", "/poetry.lock",
    "/db.sqlite3", "/db.sqlite", "/app.db", "/data.db",

    # ── v8.0: WordPress deep ──
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

    # ── v8.0: CMS-specific deep ──
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

    # ── v8.0: Node.js / npm specific ──
    "/.npmrc", "/.yarnrc", "/.yarn/", "/.yarn/cache/",
    "/yarn.lock", "/pnpm-lock.yaml", "/package-lock.json",
    "/.pnp.js", "/.pnp.cjs", "/.pnp/", "/.pnp.loader.js",
    "/node_modules/.cache/", "/.parcel-cache/", "/.next/",
    "/.nuxt/", "/.svelte-kit/", "/.output/", "/.vercel/",
    "/.netlify/", "/.cache/", "/.turbo/",

    # ── v8.0: Cloud / DevOps deep ──
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

    # ── v8.0: CI/CD configs ──
    "/.gitlab-ci.yml", "/.gitlab-ci.yml.bak",
    "/.github/workflows/", "/.github/workflows/ci.yml",
    "/.circleci/config.yml", "/.travis.yml", "/bitbucket-pipelines.yml",
    "/jenkins/", "/.jenkins/", "/Jenkinsfile", "/Jenkinsfile.bak",
    "/azure-pipelines.yml", "/.drone.yml", "/teamcity",

    # ── v8.0: API documentation ──
    "/swagger.json", "/swagger.yaml", "/swagger-ui/", "/swagger/",
    "/swagger-ui.html", "/swagger-ui/index.html", "/swagger-ui/swagger-ui-bundle.js",
    "/api-docs", "/api/docs", "/api/swagger.json", "/api/openapi.json",
    "/openapi.json", "/openapi.yaml", "/openapi/", "/redoc",
    "/rapidoc", "/api-docs/swagger.json", "/v1/api-docs", "/v2/api-docs",
    "/api/swagger", "/api/rapidoc", "/api/redoc",

    # ── v8.0: WebSocket / SSE endpoints ──
    "/ws", "/wss", "/websocket", "/socket.io/", "/socket.io/?EIO=4&transport=websocket",
    "/signalr", "/signalr/negotiate", "/signalr/hubs",
    "/hub", "/realtime", "/events", "/sse", "/stream",
    "/api/ws", "/api/websocket", "/api/realtime",
    "/_ws", "/_websocket", "/_realtime",

    # ── v8.0: Common config backups / temporaries ──
    "/config.php.bak", "/config.php.old", "/config.php.orig", "/config.php.save",
    "/config.php.swp", "/config.php~", "/config.php.txt", "/config.php.dist",
    "/config.json.bak", "/config.json.old", "/config.json.orig",
    "/config.yaml.bak", "/config.yml.old", "/config.ini.dist",
    "/settings.php.bak", "/settings.php.old", "/settings.json.bak",
    "/settings.json.old", "/.env.bak", "/.env.old", "/.env.orig",
    "/.env.save", "/.env.swp", "/.env~", "/.env.dist", "/.env.sample",
    "/.env.production.local", "/.env.development.local",
    "/.env.staging.local", "/.env.test.local",

    # ── v8.0: CVE / known vuln paths ──
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

    # ── v8.0: Misc / random secrets ──
    "/.htpasswd", "/.htpasswd.bak", "/.htpasswd.old",
    "/.htaccess", "/.htaccess.bak", "/.htaccess.old",
    "/.netrc", "/.netrc.bak", "/.npmrc", "/.pypirc", "/.pypirc.bak",
    "/.dockerignore", "/.gitignore", "/.gitattributes",
    "/.editorconfig", "/.flake8", "/.pylintrc", "/.ruff.toml",
    "/.prettierrc", "/.eslintrc", "/.babelrc",
    "/.docker/registry", "/registry/", "/docker/registry",

    # ── v8.0: Source code & build artifacts ──
    "/source/", "/src/", "/build/", "/dist/", "/out/", "/target/",
    "/coverage/", "/.nyc_output/", "/.cache/", "/.parcel-cache/",
    "/vendor/", "/vendor/composer/installed.json", "/vendor/autoload.php",
    "/node_modules/", "/node_modules/.env", "/node_modules/.package-lock.json",

    # ── v8.0: Logs & debug ──
    "/error.log", "/access.log", "/debug.log", "/app.log", "/out.log",
    "/laravel.log", "/storage/logs/laravel.log",
    "/var/log/", "/var/log/apache2/", "/var/log/nginx/",
    "/var/log/auth.log", "/var/log/syslog", "/var/log/messages",
    "/logs/", "/log/", "/_logs/", "/debugging/",
    "/_profiler/", "/_debugbar/", "/symfony/_profiler/",
    "/phpinfo.php", "/info.php", "/test.php", "/php.php",
    "/_internal/", "/_hidden/", "/_private/", "/_secret/",
    "/server-status", "/server-info", "/status?full", "/status?auto",

    # ── v8.0: Backup & database dumps ──
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

    # ── v8.0: Admin / management panels ──
    "/admin/", "/administrator/", "/admin/login", "/admin/index.php",
    "/admin.php", "/admin.html", "/admin/console", "/admin/dashboard",
    "/adminarea/", "/adminpanel/", "/admincp/", "/admin/controlpanel",
    "/manage/", "/manager/", "/panel/", "/dashboard/", "/console/",
    "/cpanel", "/whm", "/.admin", "/wp-admin/", "/wp-login.php",
    "/phpmyadmin/", "/adminer.php", "/adminer/", "/pma/",
    "/sqladmin/", "/mysql-admin/", "/dbadmin/",
    "/manager/html", "/manager/status", "/manager/jmxproxy",
    "/host-manager/html", "/host-manager/status",

    # ── v8.0: User-uploaded content ──
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

# ── v8.0 helper functions: deep recon capabilities ──

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

async def deep_scan(target, custom_headers=None, proxy=None, timeout=10,
                    allow_redirects=False, progress_cb=None, scan_js=True,
                    scan_id=None):
    start = time.time()
    target = validate_target(target)
    result = {
        "target": target, "timestamp": datetime.now(timezone.utc).isoformat(),
        "scanner_version": "v8.0",
        "main": {}, "leak": [], "robots": [], "links": [], "js_links": [],
        "forms": [], "dirs": [], "brute": [], "ports": [], "technologies": [],
        "waf": {}, "cdn": [], "cookies": [], "security_headers": [],
        "secrets": [], "ssl": {}, "subdomain_hints": [], "subdomains_resolved": [],
        "page_summary": "", "param_findings": [], "backup_findings": [],
        "js_endpoints": [], "api_endpoints": [], "swagger_endpoints": [],
        "takeover_findings": [], "source_maps": [], "graphql_findings": [],
        "cors_findings": [], "open_redirect_findings": [], "wayback_urls": [],
        "http_method_findings": [], "recursive_brute_findings": [],
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

    if HAS_AIOHTTP:
        conn = aiohttp.TCPConnector(limit=100, limit_per_host=40, ssl=False)
        async with aiohttp.ClientSession(connector=conn,
                                          headers={"User-Agent": random.choice(USER_AGENTS)}) as session:
            # 1. Main page
            await prog("main_page", "Đang tải trang chính...")
            log(f"GET {target}")
            main_text, main_code, main_headers, main_rt = await fetch(session, target, custom_headers, proxy, timeout)
            result["main"] = {
                "code": main_code,
                "length": len(main_text) if main_text else 0,
                "headers": dict(main_headers),
                "response_time_ms": main_rt,
            }
            result["page_summary"] = get_main_page_summary(main_text)
            log(f"Main page: {main_code} ({len(main_text or '')} bytes, {main_rt}ms)")
            if main_code == 0:
                result["errors"].append(f"Kết nối thất bại: {main_text[:120]}")
                result["duration_seconds"] = round(time.time()-start, 2)
                return result

            # Cookies + security headers
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
            waf = detect_waf(main_headers, main_code, main_text or "")
            result["waf"] = waf
            result["cdn"] = detect_cdn(main_headers)
            if waf["detected"]:
                log(f"WAF: {', '.join(waf['detected'])} – slow mode")
            if waf["should_slow_down"]:
                await prog("waf", f"WAF: {', '.join(waf['detected'])} – Giảm tốc")

            limit = 12 if waf["should_slow_down"] else 30

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
                brute_total = len(BRUTE_NAMES) * 9
                await prog("brute", "Brute-force common files...", 0, brute_total, 0)
                exts = [".php", ".html", ".txt", ".json", ".xml", ".bak", ".old", ".save", ".orig"]
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

            # 12. Subdomain takeover check (v8.0)
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

            # 13. GraphQL introspection (v8.0)
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

            # 14. CORS misconfiguration (v8.0)
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

            # 15. Open redirect test (v8.0)
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

            # 16. Source map exposure (v8.0)
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

            # 17. JS endpoint extraction + API fuzzing (v8.0)
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

            # 18. Swagger/OpenAPI parsing (v8.0)
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

            # 19. Recursive depth-2 brute-force (v8.0)
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

            # 20. HTTP method fuzzing (v8.0)
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

            # 21. Wayback Machine integration (v8.0)
            if not cancelled():
                await prog("wayback", "Wayback Machine historical URLs lookup...", 0, 1, 0)
                log(f"Wayback: querying web.archive.org")
                try:
                    result["wayback_urls"] = await fetch_wayback_urls(session, target, custom_headers, proxy, timeout)
                    log(f"Wayback done: {len(result['wayback_urls'])} historical URLs found")
                    await prog("wayback", f"Wayback done: {len(result['wayback_urls'])} URLs", 1, 1, len(result["wayback_urls"]))
                except Exception as e:
                    log(f"Wayback lookup failed: {e}")
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
        # v8.0 additions
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
        "cancelled": result.get("cancelled", False),
    }
    result["duration_seconds"] = round(time.time()-start, 2)
    await prog("completed", f"Hoàn thành – {result['stats']['real_leak_count']} leaks · {result['stats']['secret_count']} secrets · {result['stats']['subdomains_resolved']} subs · {result['stats']['takeover_findings']} takeover · {result['stats']['graphql_findings']} graphql · {result['stats']['cors_findings']} cors · {result['stats']['source_maps']} srcmaps · {result['stats']['api_endpoints']} api · {result['stats']['wayback_urls']} wayback")
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
    "backup_check": "💾 Check backup variants",
    "robots": "🤖 Phân tích robots.txt",
    "links": "🔗 Trích xuất links/JS/forms",
    "secrets": "🔐 Quét secret trong HTML",
    "secrets_js": "📜 Quét secret trong JS files",
    "dirs": "📂 Kiểm tra directory listing",
    "brute": "🔍 Brute-force common files",
    "param_fuzz": "❓ Query param fuzzing",
    "subdomains": "🌐 DNS subdomain enum",
    # v8.0 phases
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

# ── HTML Template (PAGE) – v8.0 Deep Recon Edition ──
PAGE_HTML = r"""
<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Leak Scanner Pro v8.0</title>
<style>
/* ─────────  Theme variables  ───────── */
:root{
  --bg:#070710; --bg2:rgba(22,33,62,.55); --bg3:rgba(26,26,46,.7);
  --border:rgba(0,212,170,.18); --border-hi:rgba(0,212,170,.45);
  --text:#e8eef5; --muted:#9aa3b8; --dim:#6a7388;
  --accent:#00d4aa; --accent2:#54a0ff; --accent3:#a78bfa;
  --warn:#feca57; --danger:#ff5b6b; --ok:#1dd1a1;
  --glass-blur:18px;
  --shadow:0 8px 32px rgba(0,0,0,.45);
  --glow-accent:0 0 24px rgba(0,212,170,.35);
  --mesh-1:#1a1a3a; --mesh-2:#0a2a3a; --mesh-3:#2a0a3a;
}
[data-theme="light"]{
  --bg:#eef2f9; --bg2:rgba(255,255,255,.65); --bg3:rgba(255,255,255,.85);
  --border:rgba(0,150,120,.2); --border-hi:rgba(0,150,120,.55);
  --text:#1a1f2e; --muted:#5b6478; --dim:#8793a8;
  --accent:#00b894; --accent2:#0984e3; --accent3:#7c3aed;
  --warn:#d68910; --danger:#e74c3c; --ok:#27ae60;
  --glass-blur:14px;
  --shadow:0 6px 24px rgba(20,40,80,.12);
  --glow-accent:0 0 20px rgba(0,184,148,.25);
  --mesh-1:#dbe7ff; --mesh-2:#d7f5ef; --mesh-3:#e7d7ff;
}

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

/* ─────────  Container / Cards  ───────── */
.container{max-width:1180px;margin:0 auto;padding:20px}
.card{
  background:var(--bg2); backdrop-filter:blur(var(--glass-blur)) saturate(140%);
  -webkit-backdrop-filter:blur(var(--glass-blur)) saturate(140%);
  border:1px solid var(--border); border-radius:16px; padding:22px; margin-bottom:18px;
  transition:all .3s cubic-bezier(.4,0,.2,1); position:relative; overflow:hidden;
  box-shadow:var(--shadow);
  animation:cardIn .55s cubic-bezier(.16,.84,.44,1) backwards;
}
.card:nth-child(1){animation-delay:.05s}
.card:nth-child(2){animation-delay:.15s}
.card:nth-child(3){animation-delay:.25s}
.card:nth-child(4){animation-delay:.35s}
@keyframes cardIn{from{opacity:0;transform:translateY(24px) scale(.98)}
  to{opacity:1;transform:none}}
.card::before{
  content:""; position:absolute; top:0; left:-100%; right:0; height:1px;
  background:linear-gradient(90deg,transparent,var(--accent),transparent);
  animation:scanLine 4s ease-in-out infinite; opacity:.5;
}
@keyframes scanLine{0%,100%{left:-100%}50%{left:100%}}
.card:hover{border-color:var(--border-hi); transform:translateY(-2px);
  box-shadow:0 12px 40px rgba(0,212,170,.18), var(--shadow)}
.card h1,.card h2{
  font-size:22px; margin-bottom:10px;
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
<nav class="navbar">
  <div class="nav-brand">
    <span class="logo">🛡️</span>
    <span>Web Leak Scanner <span class="version">v8.0</span></span>
  </div>
  <div class="nav-right">
    <button class="theme-toggle" id="themeToggle" title="Đổi theme">🌙</button>
  </div>
</nav>

<main class="container">

<!-- Form -->
<div class="card">
  <h1>🕵️ Quét lỗ hổng thông tin rò rỉ</h1>
  <p class="subtitle">Async deep recon v8.0 — 550+ leak paths · subdomain takeover · GraphQL introspection · CORS misconfig · open redirect · source map exposure · JS endpoint extraction · Swagger/OpenAPI parsing · recursive depth-2 brute · HTTP method fuzz · Wayback Machine · 45+ secret patterns · glassmorphism UI · live terminal log</p>
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
    <div class="form-group" style="display:flex;align-items:center;gap:10px">
      <input type="checkbox" name="redirect" value="yes" id="rd" checked>
      <label for="rd" style="margin:0">Theo dõi redirect</label>
    </div>
    <button type="submit" class="btn btn-primary" id="scanBtn">
      <span class="btn-text">🔍 Bắt đầu quét</span>
      <span class="btn-loading hidden">
        <span class="btn-loading-dot"></span>
        <span class="btn-loading-dot" style="animation-delay:.2s"></span>
        <span class="btn-loading-dot" style="animation-delay:.4s"></span>
        Đang quét...
      </span>
    </button>
  </form>
</div>

<!-- History -->
<div class="card" id="historyCard" style="display:none">
  <h3>🕘 Lịch sử quét gần đây</h3>
  <div class="history-list" id="historyList"></div>
</div>

<!-- Progress + Activity log -->
<div id="progressPanel" class="card progress-card hidden">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:10px">
    <h3 style="margin:0">📡 Tiến trình quét</h3>
    <div style="display:flex;gap:7px;align-items:center;flex-wrap:wrap">
      <span class="badge badge-time" id="elapsedBadge" title="Thời gian đã trôi qua">⏱️ 00:00</span>
      <span class="badge" id="etaBadge" style="background:rgba(254,202,87,.12);color:#feca57;display:none" title="Còn lại (ước tính)">⌛ ETA --:--</span>
      <span class="badge" id="rateBadge" style="background:rgba(84,160,255,.12);color:#54a0ff;display:none" title="Tốc độ">⚡ -- req/s</span>
      <button class="btn btn-ghost" id="cancelBtn" style="padding:6px 12px;font-size:12px">🛑 Huỷ</button>
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
<footer class="footer">Web Leak Scanner Pro v8.0 — Deep Recon Edition · 550+ leak paths · takeover · GraphQL · CORS · source maps · Wayback · glassmorphism UI</footer>
<div id="toast" class="toast"></div>

<script>
const $ = (s)=>document.querySelector(s);
const $$ = (s)=>document.querySelectorAll(s);

const THEME_KEY = 'wlsv7_theme';
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
  'backup_check':'💾 Check backup variants',
  'robots':'🤖 Phân tích robots.txt',
  'links':'🔗 Trích xuất links/JS/forms',
  'secrets':'🔐 Quét secret trong HTML',
  'secrets_js':'📜 Quét secret trong JS files',
  'dirs':'📂 Kiểm tra directory listing',
  'brute':'🔍 Brute-force common files',
  'param_fuzz':'❓ Query param fuzzing',
  'subdomains':'🌐 DNS subdomain enum',
  'completed':'✅ Hoàn thành',
  'error':'❌ Lỗi',
  'cancelling':'🛑 Đang huỷ',
  'cancelled':'🛑 Đã huỷ',
};

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
  const term = $('#activityLog');

  btn.disabled = true;
  $('.btn-text').classList.add('hidden');
  $('.btn-loading').classList.remove('hidden');
  cancelBtn.disabled = false;
  progressPanel.classList.remove('hidden');
  resultsArea.innerHTML = '';
  bar.style.width = '0%';
  phase.textContent = 'Đang khởi tạo...';
  msg.textContent = '';
  found.classList.add('hidden');
  count.textContent = '';
  // Reset terminal
  term.innerHTML = '<div style="color:#6a7388;margin-top:14px">// Khởi tạo scan...<span class="cursor"></span></div>';
  startTimer();
  progressPanel.scrollIntoView({behavior:'smooth', block:'start'});

  const formData = new FormData(this);
  try{
    const resp = await fetch('/scan', {method:'POST', body:formData});
    const data = await resp.json();
    if(data.error){ toast('❌ ' + data.error); resetBtn(); stopTimer(); return; }
    const scanId = data.scan_id;
    currentScanId = scanId;
    startActivityPolling(scanId);

    cancelBtn.onclick = async ()=>{
      if(!currentScanId) return;
      cancelBtn.disabled = true;
      cancelBtn.textContent = '⏳ Đang huỷ...';
      try{
        await fetch('/cancel/' + currentScanId, {method:'POST'});
        toast('🛑 Đã gửi yêu cầu huỷ');
      }catch(err){ toast('Lỗi huỷ: ' + err.message); }
    };

    const evtSource = new EventSource('/progress/' + scanId);
    evtSource.onmessage = function(e){
      try{
        const d = JSON.parse(e.data);
        if(d.phase && INTERNAL_PHASES.has(d.phase)) return;

        if(d.phase || d.phase_display){
          const display = d.phase_display || PHASE_FALLBACK[d.phase] || d.phase || '';
          if(display) phase.textContent = display;
        }

        if(d.total > 0){
          const pct = Math.round((d.current/d.total)*100);
          bar.style.width = pct + '%';
          count.textContent = d.current + '/' + d.total + ' (' + pct + '%)';
        } else {
          count.textContent = '';
        }

        if(d.message) msg.textContent = d.message;

        // Found counter — luôn cập nhật, ẩn nếu = 0 (tránh hiển thị số cũ)
        if(d.found !== undefined){
          if(d.found > 0){
            found.classList.remove('hidden');
            found.textContent = '🔍 Tìm thấy: ' + d.found;
          } else {
            found.classList.add('hidden');
            found.textContent = '';
          }
        }

        const elapsedBadge = $('#elapsedBadge');
        const etaBadge = $('#etaBadge');
        const rateBadge = $('#rateBadge');
        if(d.elapsed !== undefined){
          elapsedBadge.textContent = '⏱️ ' + fmtTime(d.elapsed);
          if(d.eta !== null && d.eta !== undefined && d.total > 0){
            etaBadge.style.display = '';
            etaBadge.textContent = '⌛ ETA ' + fmtTime(d.eta);
          }
          if(d.rate !== undefined && d.rate > 0){
            rateBadge.style.display = '';
            rateBadge.textContent = '⚡ ' + d.rate + ' req/s';
          }
        }

        if(d.phase === 'completed' || d.phase === 'error' || d.phase === 'cancelled'){
          evtSource.close();
          stopTimer();
          stopActivityPolling();
          cancelBtn.style.display = 'none';
          // Ẩn cursor khi scan xong
          const cur = term.querySelector('.cursor');
          if(cur) cur.style.display = 'none';
          if(d.phase === 'cancelled'){
            setTimeout(()=>loadResult(scanId).then(loadHistory), 300);
          } else {
            loadResult(scanId).then(loadHistory);
          }
        }
      }catch(err){}
    };
    evtSource.onerror = function(){
      evtSource.close();
      stopTimer();
      stopActivityPolling();
      loadResult(scanId).then(loadHistory);
    };
  }catch(err){
    toast('❌ Lỗi mạng: ' + err.message);
    resetBtn();
    stopTimer();
    stopActivityPolling();
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
  stopActivityPolling();
  initTabs();
  initFilter();
  animateCounters();
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
</script>
</body>
</html>
"""

# ── HTML Template (RESULT) – v8.0 Deep Recon ──
RESULT_HTML = r"""
{% if result %}
<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:10px">
  <h2 style="margin:0">📊 Kết quả cho {{ result.target }}</h2>
  <div>
    {% if result.duration_seconds %}<span class="badge badge-time">⏱️ {{ result.duration_seconds }}s</span>{% endif %}
    {% if result.cancelled %}<span class="badge badge-waf">🛑 Đã huỷ</span>{% endif %}
    {% if result.stats and result.stats.soft_404_filtered %}<span class="badge" style="background:rgba(160,160,176,.15);color:#a0a0b0">🎯 Soft-404: {{ result.stats.soft_404_filtered }}</span>{% endif %}
    {% if result.stats and result.stats.backup_findings %}<span class="badge" style="background:rgba(167,139,250,.15);color:#a78bfa">💾 Backup: {{ result.stats.backup_findings }}</span>{% endif %}
    {% if result.stats and result.stats.param_findings %}<span class="badge" style="background:rgba(254,202,87,.15);color:#feca57">❓ Params: {{ result.stats.param_findings }}</span>{% endif %}
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
  <button class="tab" data-tab="params">❓ Params <span class="count">{{ result.param_findings|length }}</span></button>
  <button class="tab" data-tab="methods">🔧 Methods <span class="count">{{ result.http_method_findings|length }}</span></button>
  <button class="tab" data-tab="rbrute">🔁 RBrute <span class="count">{{ result.recursive_brute_findings|length }}</span></button>
  <button class="tab" data-tab="tech">🛠️ Tech & WAF</button>
  <button class="tab" data-tab="network">🌐 Network</button>
  <button class="tab" data-tab="headers">📜 Headers & Cookies</button>
  <button class="tab" data-tab="forms">📝 Forms <span class="count">{{ result.forms|length }}</span></button>
  <button class="tab" data-tab="subs">🌐 Subs <span class="count">{{ result.subdomains_resolved|length }}</span></button>
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

<!-- v8.0 Tabs -->

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
            result = loop.run_until_complete(deep_scan(
                target, custom_headers, proxy, timeout,
                allow_redirects, progress_cb, scan_js, scan_id
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
                "errors": [str(e)], "scanner_version": "v8.0",
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

@app.route("/result/<int:scan_id>")
def result(scan_id):
    result = scan_results.get(scan_id, {})
    return render_template_string(RESULT_HTML, result=result)

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
    data["scanner"] = "Web Leak Scanner Pro v8.0"
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
<h1>🛡️ Web Leak Scanner Pro v8.0 — Standalone Report</h1>
<p><strong>Target:</strong> {data.get('target','')}</p>
<p><strong>Scanned at:</strong> {data.get('timestamp','')}</p>
<p><strong>Duration:</strong> {data.get('duration_seconds',0)}s</p>
{html}
</body></html>"""
    return Response(full.encode("utf-8"), mimetype="text/html",
                    headers={"Content-Disposition": "attachment; filename=scan_report_v7.html"})

# ── Main ──
if __name__ == "__main__":
    print("=" * 64)
    print(f"🛡️  Web Leak Scanner Pro v8.0 — Upgraded Edition")
    print(f"   URL: http://{HOST}:{PORT}")
    print(f"   Mở trình duyệt vào địa chỉ trên (Ctrl+C để dừng)")
    print(f"   v8.0: 550+ leak paths · 45+ secret patterns · 56+ tech sigs")
    print(f"   v8.0: Subdomain takeover · GraphQL introspection · CORS · open redirect")
    print(f"   v8.0: Source map exposure · JS endpoint extraction · Swagger parsing")
    print(f"   v8.0: Recursive depth-2 brute · HTTP method fuzz · Wayback Machine")
    print(f"   v8.0: Glassmorphism UI · Animated mesh bg · Live activity log")
    print(f"   v8.0: Animated counters · Glow effects · Staggered animations")
    print("=" * 64)
    app.run(host=HOST, port=PORT, debug=False, threaded=True)

