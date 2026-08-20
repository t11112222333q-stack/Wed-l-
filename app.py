#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Leak Scanner Pro v4.0 – Web Single-File Edition
Gộp Flask + Scanner + UI vào 1 file. Chỉ cần:
  pip install flask aiohttp
  python web_leak_web.py
Rồi mở trình duyệt: http://localhost:5000
"""
import os, sys, re, json, time, random, asyncio, threading, queue
from datetime import datetime, timezone
from urllib.parse import urlparse, urljoin
from functools import wraps

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
]
COMMON_PORTS = [80, 443, 8080, 8443, 3000, 5000, 8000, 8888, 9000, 9200]
BLOCKED_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "::1", "169.254.169.254", "metadata.google.internal"}

LEAK_PATHS = [
    "/robots.txt", "/sitemap.xml", "/.env", "/.env.local", "/.env.production",
    "/.git/config", "/.git/HEAD", "/.gitignore", "/wp-config.php", "/config.php",
    "/configuration.php", "/settings.json", "/.htaccess", "/web.config",
    "/backup.zip", "/backup.tar.gz", "/db.sql", "/dump.sql", "/database.sql",
    "/admin/", "/administrator/", "/wp-admin/", "/phpmyadmin/",
    "/.aws/credentials", "/.ssh/id_rsa", "/.ssh/authorized_keys",
    "/swagger.json", "/api-docs", "/openapi.json",
    "/package.json", "/composer.json", "/Dockerfile", "/docker-compose.yml",
    "/.bash_history", "/.mysql_history", "/.npmrc", "/.dockercfg",
    "/install/", "/setup/", "/test/", "/temp/", "/tmp/", "/logs/",
    "/api/v1/", "/api/v2/", "/api/v3/", "/rest/", "/graphql",
    "/.svn/", "/.hg/", "/.bzr/", "/CVS/",
    "/server-status", "/server-info", "/.well-known/security.txt",
    "/crossdomain.xml", "/clientaccesspolicy.xml",
    "/.env~", "/.env.bak", "/.env.save", "/.env.sw", "/.env.swp",
    "/config.json", "/config.xml", "/config.yaml", "/config.yml",
    "/appsettings.json", "/appsettings.Development.json",
    "/.htpasswd", "/.htaccess.bak", "/.htaccess.txt",
    "/www.zip", "/www.tar.gz", "/site.zip", "/website.zip",
    "/old/", "/backup/", "/bak/", "/archive/", "/archives/",
    "/.DS_Store", "/Thumbs.db", "/.idea/", "/.vscode/",
    "/phpinfo.php", "/info.php", "/_profiler/", "/symfony/",
]

TECH_SIGS = {
    "WordPress": [("html", r'wp-content|wp-includes|wordpress'), ("header", r'x-powered-by.*wordpress')],
    "Drupal": [("html", r'drupal'), ("header", r'x-drupal')],
    "Laravel": [("header", r'laravel_session')],
    "Django": [("header", r'csrftoken|django'), ("html", r'csrfmiddlewaretoken')],
    "PHP": [("header", r'x-powered-by.*php|php/'), ("html", r'\.php\?')],
    "ASP.NET": [("header", r'x-aspnet|x-powered-by.*asp\.net|aspsessionid')],
    "Nginx": [("header", r'server.*nginx')],
    "Apache": [("header", r'server.*apache')],
    "IIS": [("header", r'server.*microsoft-iis')],
    "Cloudflare": [("header", r'cf-ray|cloudflare|cf-cache-status')],
    "jQuery": [("html", r'jquery[.-]\d+\.\d+')],
    "Bootstrap": [("html", r'bootstrap[./]')],
    "React": [("html", r'reactroot|data-react|react\.js')],
    "Vue.js": [("html", r'vue[.-]\d|data-v-|__VUE__')],
    "Angular": [("html", r'ng-\w+|angular[./]')],
}

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
        if ip.is_private or ip.is_loopback:
            raise ValueError("IP private bị chặn")
    except ValueError:
        pass
    if "@" in parsed.netloc:
        raise ValueError("URL chứa @ – bị chặn")
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

# ── Async Scanner ──
try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False
    print("[!] aiohttp chưa cài – pip install aiohttp")

async def fetch(session, url, headers=None, proxy=None, timeout=10):
    if not HAS_AIOHTTP:
        return "", 0, {}
    try:
        async with session.get(url, headers=headers, proxy=proxy, timeout=aiohttp.ClientTimeout(total=timeout), ssl=False) as r:
            return await r.text(), r.status, dict(r.headers)
    except Exception as e:
        return str(e)[:100], 0, {}

async def scan_ports(host):
    if not HAS_AIOHTTP:
        return []
    async def check(p):
        try:
            r, w = await asyncio.wait_for(asyncio.open_connection(host, p), timeout=1)
            w.close(); await w.wait_closed()
            return p
        except:
            return None
    return sorted([p for p in await asyncio.gather(*[check(p) for p in COMMON_PORTS]) if p])

def detect_tech(html, headers):
    techs = []
    hl = {k.lower(): str(v).lower() for k, v in headers.items()}
    html_l = (html or "").lower()
    for tech, sigs in TECH_SIGS.items():
        for st, pat in sigs:
            if st == "header":
                if any(re.search(pat, v) for v in hl.values()):
                    techs.append(tech); break
            elif st == "html" and re.search(pat, html_l):
                techs.append(tech); break
    return sorted(set(techs))

def detect_waf(headers, code, text):
    hs = str(headers).lower()
    wafs, recs = [], []
    if "cf-ray" in hs or "cloudflare" in hs:
        wafs.append("Cloudflare"); recs.append("Giảm concurrent xuống 5-8")
    if "x-amzn-requestid" in hs:
        wafs.append("AWS WAF")
    if code == 429:
        wafs.append("Rate Limit")
    return {"detected": wafs, "recommendations": recs, "should_slow_down": len(wafs) > 0}

async def deep_scan(target, custom_headers=None, proxy=None, timeout=10, allow_redirects=False, progress_cb=None):
    start = time.time()
    target = validate_target(target)
    result = {
        "target": target, "timestamp": datetime.now(timezone.utc).isoformat(),
        "main": {}, "leak": [], "robots": [], "links": [],
        "dirs": [], "brute": [], "ports": [], "technologies": [],
        "waf": {}, "errors": [], "duration_seconds": 0,
    }
    parsed = urlparse(target)
    host = parsed.hostname
    base = f"{parsed.scheme}://{parsed.netloc}"

    async def prog(phase, msg, current=0, total=0, found=0):
        if progress_cb:
            await progress_cb({"phase": phase, "message": msg, "current": current, "total": total, "found": found})

    if HAS_AIOHTTP:
        conn = aiohttp.TCPConnector(limit=50, limit_per_host=20, ssl=False)
        async with aiohttp.ClientSession(connector=conn, headers={"User-Agent": random.choice(USER_AGENTS)}) as session:
            await prog("main_page", "Đang tải trang chính...")
            main_text, main_code, main_headers = await fetch(session, target, custom_headers, proxy, timeout)
            result["main"] = {"code": main_code, "length": len(main_text) if main_text else 0, "headers": dict(main_headers)}
            if main_code == 0:
                result["errors"].append("Kết nối thất bại")
                result["duration_seconds"] = round(time.time()-start, 2)
                return result

            techs = detect_tech(main_text, main_headers)
            result["technologies"] = techs
            await prog("fingerprint", f"Tech: {', '.join(techs) if techs else 'Không xác định'}")

            waf = detect_waf(main_headers, main_code, main_text or "")
            result["waf"] = waf
            if waf["should_slow_down"]:
                await prog("waf", f"WAF: {', '.join(waf['detected'])} – Giảm tốc")

            limit = 5 if waf["should_slow_down"] else 15

            if host:
                await prog("ports", "Đang quét cổng...")
                result["ports"] = await scan_ports(host)
                await prog("ports_done", f"Cổng mở: {result['ports'] or 'Không có'}")

            await prog("leak_scan", f"Kiểm tra {len(LEAK_PATHS)} paths...", 0, len(LEAK_PATHS), 0)
            sem = asyncio.Semaphore(limit)
            found_count = 0

            async def check_path(path):
                nonlocal found_count
                async with sem:
                    url = urljoin(base, path)
                    text, code, h = await fetch(session, url, custom_headers, proxy, timeout)
                    if code in (200, 401, 403):
                        if code == 200:
                            found_count += 1
                        return {"path": path, "url": url, "code": code, "size": len(text) if text else 0,
                                "preview": (text[:500]+"..." if len(text)>500 else text) if code==200 else "",
                                "headers": dict(h) if code==200 else {}}
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

            await prog("robots", "Phân tích robots.txt...")
            rt, rc, _ = await fetch(session, urljoin(base, "/robots.txt"), custom_headers, proxy, timeout)
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
                for rp in paths[:10]:
                    full = urljoin(base, rp)
                    _, c, _ = await fetch(session, full, custom_headers, proxy, timeout)
                    if c == 200:
                        result["leak"].append({"path": rp, "url": full, "code": 200, "size": 0, "preview": "[robots.txt]", "headers": {}})

            if main_text:
                await prog("links", "Trích xuất liên kết...")
                links = set()
                for m in re.finditer(r'(?:href|src|action)\s*=\s*["\']([^"\']+)["\']', main_text, re.I):
                    u = m.group(1)
                    if u.startswith(("http://", "https://")):
                        links.add(u)
                    elif u.startswith("/") and not u.startswith("//"):
                        links.add(urljoin(base, u))
                    elif not u.startswith(("#", "javascript:", "mailto:", "data:", "tel:")):
                        links.add(urljoin(base, u))
                result["links"] = sorted([l for l in links if urlparse(l).netloc == parsed.netloc])[:50]

            await prog("dirs", "Kiểm tra directory listing...")
            dirs = ["/backup/", "/temp/", "/tmp/", "/admin/", "/uploads/", "/files/", "/logs/", "/config/"]
            async def check_dir(d):
                url = urljoin(base, d)
                t, c, _ = await fetch(session, url, custom_headers, proxy, timeout)
                if c == 200 and t and ("<title>Index of" in t or "Parent Directory" in t):
                    return {"url": url, "type": "dirlist"}
                return None
            result["dirs"] = [r for r in await asyncio.gather(*[check_dir(d) for d in dirs]) if r]

            await prog("brute", "Brute-force...")
            exts = [".php", ".html", ".txt", ".json", ".xml"]
            names = ["index", "admin", "login", "config", "test", "api", "backup"]
            bsem = asyncio.Semaphore(8)
            async def brute_one(n, e):
                path = f"/{n}{e}"
                url = urljoin(base, path)
                async with bsem:
                    _, c, _ = await fetch(session, url, custom_headers, proxy, timeout)
                    if c in (200, 403, 401):
                        return {"path": path, "code": c}
                    return None
            result["brute"] = [r for r in await asyncio.gather(*[brute_one(n, e) for n in names for e in exts]) if r]
    else:
        import requests
        requests.packages.urllib3.disable_warnings()
        try:
            r = requests.get(target, headers={"User-Agent": random.choice(USER_AGENTS)}, timeout=timeout, verify=False)
            main_text, main_code, main_headers = r.text, r.status_code, dict(r.headers)
        except Exception as e:
            main_text, main_code, main_headers = str(e), 0, {}
        result["main"] = {"code": main_code, "length": len(main_text), "headers": main_headers}
        result["technologies"] = detect_tech(main_text, main_headers)
        result["waf"] = detect_waf(main_headers, main_code, main_text)
        result["errors"].append("Chế độ đồng bộ – cài aiohttp để nhanh hơn")

    result["duration_seconds"] = round(time.time()-start, 2)
    await prog("completed", f"Hoàn thành – {len(result['leak'])} findings")
    return result

# ── SSE ──
progress_queues = {}
prog_lock = threading.Lock()
scan_results = {}

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

# ── HTML Template ──
PAGE_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Leak Scanner Pro v4.0</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e0e0e0;line-height:1.6;min-height:100vh}
.navbar{background:#1a1a2e;border-bottom:1px solid #2d3561;padding:0 16px;display:flex;justify-content:space-between;align-items:center;height:52px;position:sticky;top:0;z-index:100}
.nav-brand{display:flex;align-items:center;gap:8px;font-weight:700;font-size:16px}
.version{background:#00d4aa;color:#0f0f1a;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:800}
.container{max-width:900px;margin:0 auto;padding:16px}
.card{background:#16213e;border:1px solid #2d3561;border-radius:12px;padding:18px;margin-bottom:16px}
.card h1,.card h2{font-size:18px;margin-bottom:12px;background:linear-gradient(90deg,#00d4aa,#54a0ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.subtitle{color:#a0a0b0;font-size:14px;margin-bottom:16px}
.form-group{margin-bottom:14px}
.form-group label{display:block;font-size:13px;color:#a0a0b0;font-weight:600;margin-bottom:6px}
.form-group input{width:100%;padding:10px 12px;background:#0a0a12;border:1px solid #2d3561;border-radius:10px;color:#e0e0e0;font-size:14px;outline:none}
.form-group input:focus{border-color:#00d4aa}
.form-row{display:grid;grid-template-columns:1fr 2fr;gap:12px}
.btn{padding:10px 20px;border:none;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;display:inline-flex;align-items:center;gap:6px;text-decoration:none;border:1px solid transparent}
.btn-primary{background:linear-gradient(135deg,#00d4aa,#00b894);color:#0f0f1a}
.btn-primary:hover{transform:translateY(-1px);opacity:.9}
.btn-primary:disabled{opacity:.5;cursor:not-allowed;transform:none}
.btn-secondary{background:#1a1a2e;color:#00d4aa;border-color:#00d4aa}
.btn-secondary:hover{background:#00d4aa;color:#0f0f1a}
.progress-card{border-left:3px solid #00d4aa}
.progress-info{display:flex;justify-content:space-between;font-size:13px;color:#a0a0b0;margin-bottom:8px}
.progress-bar-bg{width:100%;height:6px;background:#0a0a12;border-radius:3px;overflow:hidden;margin-bottom:10px}
.progress-bar-fill{height:100%;background:linear-gradient(90deg,#00d4aa,#54a0ff);border-radius:3px;transition:width .3s;width:0%}
.progress-msg{font-size:13px;color:#a0a0b0}
.progress-found{font-size:13px;font-weight:700;color:#1dd1a1;margin-top:4px}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px}
.stat-box{text-align:center;padding:12px 8px;background:#1a1a2e;border:1px solid #2d3561;border-radius:10px}
.stat-number{font-size:22px;font-weight:800;color:#00d4aa}
.stat-label{font-size:11px;color:#888;margin-top:2px}
.section-title{font-size:14px;font-weight:700;margin:16px 0 10px;display:flex;align-items:center;gap:6px}
.tech-tag{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;margin:2px;background:rgba(0,212,170,.1);color:#00d4aa;border:1px solid rgba(0,212,170,.3)}
.port-badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:700;margin:2px;background:rgba(84,160,255,.15);color:#54a0ff;border:1px solid rgba(84,160,255,.3)}
.leak-item{padding:10px;background:#1a1a2e;border:1px solid #2d3561;border-radius:8px;margin-bottom:8px}
.leak-header{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.code-badge{padding:2px 8px;border-radius:4px;font-size:12px;font-weight:800;min-width:36px;text-align:center}
.code-200{background:rgba(29,209,161,.2);color:#1dd1a1}
.code-403{background:rgba(254,202,87,.2);color:#feca57}
.code-401{background:rgba(255,107,107,.2);color:#ff6b6b}
.code-404{background:rgba(160,160,176,.2);color:#888}
.leak-path{font-family:monospace;font-weight:700;font-size:13px}
.leak-size{font-size:11px;color:#888}
.leak-url{font-size:11px;color:#888;word-break:break-all;margin-top:2px}
.leak-preview summary{cursor:pointer;color:#00d4aa;font-size:12px}
.leak-preview pre{background:#0a0a12;padding:10px;border-radius:8px;font-size:12px;overflow-x:auto;margin-top:6px;max-height:200px;overflow-y:auto;color:#aed581}
.robots-content{background:#0a0a12;padding:10px;border-radius:8px;font-family:monospace;font-size:12px;max-height:200px;overflow-y:auto;white-space:pre-wrap}
.waf-info{background:rgba(255,107,107,.05);border:1px solid rgba(255,107,107,.2);border-radius:8px;padding:12px}
.alert{padding:12px;border-radius:8px;margin-bottom:12px}
.alert-error{background:rgba(255,107,107,.1);border:1px solid rgba(255,107,107,.3);color:#ff6b6b}
.empty-state{text-align:center;padding:24px;color:#888}
.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;margin:2px}
.badge-time{background:rgba(84,160,255,.12);color:#54a0ff}
.badge-waf{background:rgba(255,107,107,.12);color:#ff6b6b}
.footer{text-align:center;padding:16px;color:#888;font-size:12px;border-top:1px solid #2d3561;margin-top:16px}
.hidden{display:none!important}
@media(max-width:600px){.form-row{grid-template-columns:1fr}.stats-grid{grid-template-columns:repeat(2,1fr)}.container{padding:12px}}
</style>
</head>
<body>
<nav class="navbar">
<div class="nav-brand"><span>🔒</span><span>Web Leak Scanner <span class="version">v4.0</span></span></div>
</nav>
<main class="container">

<!-- Form -->
<div class="card">
<h1>🕵️ Quét lỗ hổng thông tin rò rỉ</h1>
<p class="subtitle">Async scanner với real-time progress, WAF detection & smart brute-force</p>
<form id="scanForm" method="post" action="/scan">
<div class="form-group"><label>🌐 URL mục tiêu</label><input type="text" name="target" placeholder="https://example.com" required></div>
<div class="form-row">
<div class="form-group"><label>⏱️ Timeout</label><input type="number" name="timeout" value="10" min="1" max="60"></div>
<div class="form-group"><label>🌐 Proxy</label><input type="text" name="proxy" placeholder="http://proxy:8080"></div>
</div>
<div class="form-group"><label>📋 Custom Headers</label><input type="text" name="headers" placeholder="User-Agent: MyBot; X-Forwarded-For: 1.2.3.4"></div>
<div class="form-group" style="display:flex;align-items:center;gap:8px"><input type="checkbox" name="redirect" value="yes" id="rd"><label for="rd" style="margin:0">Theo dõi redirect</label></div>
<button type="submit" class="btn btn-primary" id="scanBtn"><span class="btn-text">🔍 Bắt đầu quét</span><span class="btn-loading hidden">⏳ Đang quét...</span></button>
</form>
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
<footer class="footer">Web Leak Scanner Pro v4.0 – Async Security Scanner</footer>

<script>
document.getElementById('scanForm').addEventListener('submit', async function(e){
  e.preventDefault();
  const btn = document.getElementById('scanBtn');
  const progressPanel = document.getElementById('progressPanel');
  const resultsArea = document.getElementById('resultsArea');
  const bar = document.getElementById('progressBar');
  const phase = document.getElementById('progressPhase');
  const count = document.getElementById('progressCount');
  const msg = document.getElementById('progressMessage');
  const found = document.getElementById('progressFound');

  btn.disabled = true;
  document.querySelector('.btn-text').classList.add('hidden');
  document.querySelector('.btn-loading').classList.remove('hidden');
  progressPanel.classList.remove('hidden');
  resultsArea.innerHTML = '';

  const formData = new FormData(this);
  const resp = await fetch('/scan', {method:'POST', body:formData});
  const data = await resp.json();
  const scanId = data.scan_id;

  const evtSource = new EventSource('/progress/' + scanId);
  evtSource.onmessage = function(e){
    try{
      const d = JSON.parse(e.data);
      if(d.phase) phase.textContent = d.phase;
      if(d.total > 0){ bar.style.width = Math.round((d.current/d.total)*100)+'%'; count.textContent = d.current+'/'+d.total; }
      if(d.message) msg.textContent = d.message;
      if(d.found !== undefined){ found.classList.remove('hidden'); found.textContent = '🔍 Tìm thấy: '+d.found; }
      if(d.phase === 'completed' || d.phase === 'error'){
        evtSource.close();
        loadResult(scanId);
      }
    }catch(err){}
  };
});

async function loadResult(scanId){
  const resp = await fetch('/result/' + scanId);
  const html = await resp.text();
  document.getElementById('resultsArea').innerHTML = html;
  document.getElementById('scanBtn').disabled = false;
  document.querySelector('.btn-text').classList.remove('hidden');
  document.querySelector('.btn-loading').classList.add('hidden');
}
</script>
</body>
</html>
"""

RESULT_HTML = """
{% if result %}
<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
<h2 style="margin:0">📊 Kết quả cho {{ result.target }}</h2>
<div>
{% if result.duration_seconds %}<span class="badge badge-time">⏱️ {{ result.duration_seconds }}s</span>{% endif %}
{% if result.waf.detected %}<span class="badge badge-waf">🛡️ WAF: {{ result.waf.detected|join(", ") }}</span>{% endif %}
</div>
</div>

{% if result.error %}
<div class="alert alert-error"><strong>❌ Lỗi:</strong> {{ result.error }}</div>
{% else %}

<div class="stats-grid">
<div class="stat-box"><div class="stat-number">{{ result.main.code }}</div><div class="stat-label">Mã chính</div></div>
<div class="stat-box"><div class="stat-number">{{ result.leak|length }}</div><div class="stat-label">File nhạy cảm</div></div>
<div class="stat-box"><div class="stat-number">{{ result.ports|length }}</div><div class="stat-label">Cổng mở</div></div>
<div class="stat-box"><div class="stat-number">{{ result.dirs|length }}</div><div class="stat-label">Dir listing</div></div>
</div>

{% if result.technologies %}
<div class="section-title">🛠️ Công nghệ</div>
<div>{% for t in result.technologies %}<span class="tech-tag">{{ t }}</span>{% endfor %}</div>
{% endif %}

{% if result.waf.detected %}
<div class="section-title">🛡️ WAF / Bảo vệ</div>
<div class="waf-info">
<p><strong>Phát hiện:</strong> {{ result.waf.detected|join(", ") }}</p>
{% if result.waf.recommendations %}<ul style="margin-top:6px;margin-left:16px;color:#a0a0b0;font-size:13px">{% for r in result.waf.recommendations %}<li>{{ r }}</li>{% endfor %}</ul>{% endif %}
</div>
{% endif %}

{% if result.ports %}
<div class="section-title">🔌 Cổng mở</div>
<div>{% for p in result.ports %}<span class="port-badge">{{ p }}</span>{% endfor %}</div>
{% endif %}

<div class="section-title">📁 File nhạy cảm ({{ result.leak|length }})</div>
{% if result.leak %}
<div>{% for item in result.leak %}
<div class="leak-item">
<div class="leak-header">
<span class="code-badge code-{{ item.code }}">{{ item.code }}</span>
<span class="leak-path">{{ item.path }}</span>
{% if item.size > 0 %}<span class="leak-size">{{ item.size }} bytes</span>{% endif %}
</div>
<div class="leak-url">{{ item.url }}</div>
{% if item.preview %}<details class="leak-preview"><summary>Xem trước</summary><pre>{{ item.preview }}</pre></details>{% endif %}
</div>
{% endfor %}</div>
{% else %}<p class="empty-state">Không phát hiện file nhạy cảm.</p>{% endif %}

{% if result.robots %}
<div class="section-title">🤖 robots.txt ({{ result.robots|length }})</div>
<pre class="robots-content">{{ result.robots|join("\n") }}</pre>
{% endif %}

{% if result.links %}
<div class="section-title">🔗 Liên kết ({{ result.links|length }})</div>
<div style="max-height:200px;overflow-y:auto">{% for link in result.links %}<div style="padding:4px 0;font-size:12px"><a href="{{ link }}" target="_blank" style="color:#54a0ff;text-decoration:none;word-break:break-all">{{ link }}</a></div>{% endfor %}</div>
{% endif %}

{% if result.dirs %}
<div class="section-title">📂 Directory Listing</div>
{% for d in result.dirs %}<div class="leak-item"><div class="leak-header"><span>📂</span><a href="{{ d.url }}" target="_blank" style="color:#00d4aa;text-decoration:none">{{ d.url }}</a><span style="font-size:11px;color:#feca57">({{ d.type }})</span></div></div>{% endfor %}
{% endif %}

{% if result.brute %}
<div class="section-title">🔍 Brute-force ({{ result.brute|length }})</div>
<div>{% for f in result.brute %}<div style="padding:4px 0;font-size:13px"><span class="code-badge code-{{ f.code }}">{{ f.code }}</span> {{ f.path }}</div>{% endfor %}</div>
{% endif %}

<div class="actions">
<form method="post" action="/download_json" style="display:inline"><input type="hidden" name="json_data" value="{{ result|tojson|forceescape }}"><button type="submit" class="btn btn-secondary">⬇️ Tải JSON</button></form>
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
    except: timeout = 10
    allow_redirects = request.form.get("redirect") == "yes"

    scan_id = int(time.time() * 1000)

    with prog_lock:
        progress_queues[scan_id] = queue.Queue(maxsize=200)

    async def progress_cb(data):
        send_prog(scan_id, data)

    def do_scan():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(deep_scan(target, custom_headers, proxy, timeout, allow_redirects, progress_cb))
            scan_results[scan_id] = result
            send_prog(scan_id, {"phase": "completed", "message": f"Done in {result['duration_seconds']}s"})
        except Exception as e:
            scan_results[scan_id] = {"target": target, "error": str(e), "timestamp": datetime.now(timezone.utc).isoformat(), "duration_seconds": 0}
            send_prog(scan_id, {"phase": "error", "message": str(e)})
        finally:
            import time
            time.sleep(60)
            with prog_lock:
                progress_queues.pop(scan_id, None)
            scan_results.pop(scan_id, None)

    threading.Thread(target=do_scan, daemon=True).start()
    return jsonify({"scan_id": scan_id})

@app.route("/progress/<int:scan_id>")
def progress_stream(scan_id):
    def stream():
        import time
        time.sleep(0.2)
        with prog_lock:
            q = progress_queues.get(scan_id)
        if not q:
            yield fmt_sse(json.dumps({"phase": "completed", "message": "Scan đã hoàn thành hoặc không tồn tại"}))
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
                except: pass
            except queue.Empty:
                yield fmt_sse(json.dumps({"phase": "keepalive"}))
    return Response(stream(), mimetype="text/event-stream")

@app.route("/result/<int:scan_id>")
def result(scan_id):
    result = scan_results.get(scan_id, {})
    return render_template_string(RESULT_HTML, result=result)

@app.route("/download_json", methods=["POST"])
def download_json():
    d = request.form.get("json_data")
    if not d: return "No data", 400
    try:
        data = json.loads(d)
    except: return "Invalid JSON", 400
    data["scanner"] = "Web Leak Scanner Pro v4.0"
    data["exported_at"] = datetime.now(timezone.utc).isoformat()
    return Response(json.dumps(data, indent=2, ensure_ascii=False), mimetype="application/json",
                    headers={"Content-Disposition": "attachment; filename=scan_result.json"})

# ── Main ──
if __name__ == "__main__":
    print(f"🔒 Web Leak Scanner Pro v4.0 – Web Edition")
    print(f"   URL: http://{HOST}:{PORT}")
    print(f"   Mở trình duyệt điện thoại vào địa chỉ trên")
    print(f"   Press Ctrl+C to stop\n")
    app.run(host=HOST, port=PORT, debug=False, threaded=True)
