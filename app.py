from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Akshit Soam | GKE Landing Page</title>
  <style>
    :root {
      --bg-1: #0b1020;
      --bg-2: #131a33;
      --accent-1: #7c3aed;
      --accent-2: #06b6d4;
      --accent-3: #f43f5e;
      --text: #f8fafc;
      --muted: #cbd5e1;
      --card: rgba(255, 255, 255, 0.08);
      --border: rgba(255, 255, 255, 0.14);
      --shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
      --maxw: 1180px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      scroll-behavior: smooth;
    }

    body {
      font-family: Arial, Helvetica, sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(124, 58, 237, 0.25), transparent 30%),
        radial-gradient(circle at top right, rgba(6, 182, 212, 0.2), transparent 25%),
        radial-gradient(circle at bottom center, rgba(244, 63, 94, 0.18), transparent 30%),
        linear-gradient(135deg, var(--bg-1), var(--bg-2));
      min-height: 100vh;
      overflow-x: hidden;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    .bg-grid {
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
      background-size: 36px 36px;
      mask-image: linear-gradient(to bottom, rgba(0,0,0,0.65), rgba(0,0,0,0.15));
      z-index: 0;
      pointer-events: none;
    }

    .orb {
      position: fixed;
      border-radius: 50%;
      filter: blur(55px);
      opacity: 0.5;
      pointer-events: none;
      z-index: 0;
      animation: drift 16s ease-in-out infinite alternate;
    }

    .orb.one {
      width: 220px;
      height: 220px;
      background: var(--accent-1);
      top: 10%;
      left: -40px;
    }

    .orb.two {
      width: 280px;
      height: 280px;
      background: var(--accent-2);
      top: 50%;
      right: -80px;
      animation-duration: 20s;
    }

    .orb.three {
      width: 180px;
      height: 180px;
      background: var(--accent-3);
      bottom: 5%;
      left: 18%;
      animation-duration: 14s;
    }

    @keyframes drift {
      from { transform: translateY(-10px) translateX(0) scale(1); }
      to { transform: translateY(18px) translateX(20px) scale(1.08); }
    }

    .container {
      width: min(var(--maxw), calc(100% - 32px));
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 10;
      backdrop-filter: blur(12px);
      background: rgba(11, 16, 32, 0.55);
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 72px;
      gap: 20px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 700;
      letter-spacing: 0.4px;
    }

    .brand-mark {
      width: 42px;
      height: 42px;
      border-radius: 14px;
      display: grid;
      place-items: center;
      background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
      box-shadow: 0 10px 25px rgba(124, 58, 237, 0.3);
      font-size: 20px;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 22px;
      color: var(--muted);
      font-size: 15px;
    }

    .nav-links a:hover {
      color: white;
    }

    .nav-actions {
      display: flex;
      gap: 12px;
      align-items: center;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 18px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.06);
      color: white;
      transition: transform 0.25s ease, background 0.25s ease, box-shadow 0.25s ease;
      cursor: pointer;
      font-weight: 700;
    }

    .btn:hover {
      transform: translateY(-2px);
      background: rgba(255,255,255,0.12);
      box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }

    .btn.primary {
      background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
      border: none;
    }

    .hero {
      padding: 82px 0 46px;
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 34px;
      align-items: center;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 8px 14px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.06);
      color: #e2e8f0;
      margin-bottom: 18px;
      font-size: 14px;
    }

    .eyebrow-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #22c55e;
      box-shadow: 0 0 12px #22c55e;
      animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.35); opacity: 0.7; }
    }

    .hero h1 {
      font-size: clamp(2.7rem, 5vw, 5.2rem);
      line-height: 1.03;
      letter-spacing: -1.6px;
      margin-bottom: 18px;
    }

    .gradient-text {
      background: linear-gradient(90deg, #fda4af, #c4b5fd, #67e8f9);
      background-size: 250% auto;
      color: transparent;
      -webkit-background-clip: text;
      background-clip: text;
      animation: shine 6s linear infinite;
    }

    @keyframes shine {
      to { background-position: 250% center; }
    }

    .hero p {
      color: var(--muted);
      font-size: 18px;
      line-height: 1.8;
      max-width: 640px;
      margin-bottom: 28px;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      margin-bottom: 26px;
    }

    .hero-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      color: #dbeafe;
      font-size: 14px;
    }

    .pill {
      padding: 10px 14px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.05);
    }

    .hero-card {
      position: relative;
      padding: 24px;
      border-radius: 28px;
      background: linear-gradient(180deg, rgba(255,255,255,0.11), rgba(255,255,255,0.06));
      border: 1px solid rgba(255,255,255,0.12);
      box-shadow: var(--shadow);
      overflow: hidden;
      min-height: 500px;
    }

    .hero-card::before {
      content: "";
      position: absolute;
      inset: auto -40px -40px auto;
      width: 180px;
      height: 180px;
      background: radial-gradient(circle, rgba(255,255,255,0.18), transparent 65%);
      border-radius: 50%;
    }

    .screen {
      border-radius: 22px;
      border: 1px solid rgba(255,255,255,0.12);
      overflow: hidden;
      background: rgba(9, 14, 28, 0.75);
    }

    .screen-top {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      background: rgba(255,255,255,0.04);
    }

    .dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: rgba(255,255,255,0.35);
    }

    .screen-body {
      padding: 22px;
    }

    .terminal-line {
      font-family: "Courier New", monospace;
      color: #bae6fd;
      margin-bottom: 12px;
      white-space: nowrap;
      overflow: hidden;
      border-right: 2px solid rgba(255,255,255,0.7);
      width: 0;
      animation: typing 4s steps(40, end) forwards, blink .8s step-end infinite;
    }

    .terminal-line:nth-child(2) { animation-delay: 1s; }
    .terminal-line:nth-child(3) { animation-delay: 2s; }
    .terminal-line:nth-child(4) { animation-delay: 3s; }

    @keyframes typing {
      from { width: 0; }
      to { width: 100%; }
    }

    @keyframes blink {
      50% { border-color: transparent; }
    }

    .status-grid {
      margin-top: 22px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }

    .mini-card {
      padding: 16px;
      border-radius: 18px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.08);
    }

    .mini-title {
      color: #cbd5e1;
      font-size: 13px;
      margin-bottom: 8px;
    }

    .mini-value {
      font-size: 24px;
      font-weight: 800;
    }

    section {
      padding: 42px 0;
    }

    .section-head {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 18px;
      margin-bottom: 24px;
    }

    .section-head h2 {
      font-size: clamp(1.9rem, 3vw, 3rem);
      margin-bottom: 8px;
    }

    .section-head p {
      color: var(--muted);
      max-width: 700px;
      line-height: 1.7;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }

    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 24px;
      box-shadow: var(--shadow);
      transition: transform 0.25s ease, border-color 0.25s ease;
    }

    .card:hover {
      transform: translateY(-4px);
      border-color: rgba(255,255,255,0.24);
    }

    .icon {
      width: 54px;
      height: 54px;
      border-radius: 16px;
      display: grid;
      place-items: center;
      margin-bottom: 16px;
      font-size: 24px;
      background: linear-gradient(135deg, rgba(124,58,237,0.35), rgba(6,182,212,0.25));
      border: 1px solid rgba(255,255,255,0.1);
    }

    .card h3 {
      margin-bottom: 10px;
      font-size: 22px;
    }

    .card p {
      color: var(--muted);
      line-height: 1.75;
      font-size: 15px;
    }

    .split {
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 20px;
      align-items: center;
    }

    .feature-list {
      display: grid;
      gap: 14px;
      margin-top: 18px;
    }

    .feature-item {
      display: flex;
      gap: 14px;
      padding: 16px 18px;
      border-radius: 18px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.08);
    }

    .feature-item strong {
      display: block;
      margin-bottom: 4px;
    }

    .stats-section {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }

    .stat {
      text-align: center;
      padding: 26px 18px;
      border-radius: 24px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.1);
    }

    .stat-number {
      font-size: clamp(2rem, 4vw, 3rem);
      font-weight: 800;
      margin-bottom: 8px;
      background: linear-gradient(90deg, #fda4af, #c4b5fd, #67e8f9);
      color: transparent;
      -webkit-background-clip: text;
      background-clip: text;
    }

    .stat-label {
      color: var(--muted);
      line-height: 1.5;
    }

    .timeline {
      display: grid;
      gap: 14px;
    }

    .timeline-item {
      display: grid;
      grid-template-columns: 90px 1fr;
      gap: 18px;
      padding: 18px;
      border-radius: 20px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.08);
    }

    .timeline-step {
      font-weight: 800;
      color: #c4b5fd;
    }

    .timeline-item h4 {
      margin-bottom: 6px;
      font-size: 20px;
    }

    .timeline-item p {
      color: var(--muted);
      line-height: 1.7;
    }

    .cta {
      padding: 32px;
      border-radius: 28px;
      background:
        linear-gradient(135deg, rgba(124,58,237,0.22), rgba(6,182,212,0.14)),
        rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      box-shadow: var(--shadow);
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 18px;
      align-items: center;
    }

    .cta h3 {
      font-size: clamp(1.8rem, 3vw, 2.8rem);
      margin-bottom: 12px;
    }

    .cta p {
      color: var(--muted);
      line-height: 1.8;
    }

    footer {
      padding: 32px 0 48px;
      color: #cbd5e1;
    }

    .footer-wrap {
      display: flex;
      justify-content: space-between;
      gap: 18px;
      align-items: center;
      flex-wrap: wrap;
      border-top: 1px solid rgba(255,255,255,0.08);
      padding-top: 24px;
    }

    .menu-toggle {
      display: none;
      background: transparent;
      border: 1px solid var(--border);
      color: white;
      padding: 10px 14px;
      border-radius: 12px;
      cursor: pointer;
    }

    @media (max-width: 980px) {
      .hero,
      .split,
      .cta,
      .grid-3,
      .stats-section {
        grid-template-columns: 1fr;
      }

      .hero-card {
        min-height: auto;
      }

      .nav-links {
        display: none;
        position: absolute;
        top: 72px;
        left: 16px;
        right: 16px;
        flex-direction: column;
        align-items: flex-start;
        padding: 18px;
        border-radius: 18px;
        background: rgba(11,16,32,0.96);
        border: 1px solid rgba(255,255,255,0.08);
      }

      .nav-links.show {
        display: flex;
      }

      .menu-toggle {
        display: inline-flex;
      }

      .nav-actions .btn.secondary {
        display: none;
      }
    }

    @media (max-width: 640px) {
      .hero {
        padding-top: 56px;
      }

      .section-head {
        flex-direction: column;
        align-items: flex-start;
      }

      .timeline-item {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="orb one"></div>
  <div class="orb two"></div>
  <div class="orb three"></div>

  <header>
    <div class="container nav">
      <a href="#" class="brand">
        <div class="brand-mark">⚡</div>
        <div>
          <div>Akshit Soam</div>
          <div style="font-size:12px;color:#cbd5e1;font-weight:500;">Flask • GKE • Cloud Native</div>
        </div>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="#features">Features</a>
        <a href="#about">About</a>
        <a href="#journey">Journey</a>
        <a href="#stats">Stats</a>
        <a href="/health">Health</a>
      </nav>

      <div class="nav-actions">
        <a class="btn secondary" href="/health">Health Check</a>
        <a class="btn primary" href="#cta">Launch In</a>
        <button class="menu-toggle" id="menuToggle">☰</button>
      </div>
    </div>
  </header>

  <main>
    <div class="container">
      <section class="hero">
        <div>
          <div class="eyebrow">
            <span class="eyebrow-dot"></span>
            Live on GKE with zero extra frontend libraries
          </div>

          <h1>
            Build bold.
            <span class="gradient-text">Deploy fast.</span>
            Shine brighter in the cloud.
          </h1>

          <p>
            Welcome to a full anime-inspired landing page built with plain Flask, HTML, CSS, and JavaScript.
            This app is lightweight, animated, responsive, and ready to run on Google Kubernetes Engine.
          </p>

          <div class="hero-actions">
            <a class="btn primary" href="#features">Explore Features</a>
            <a class="btn" href="/health">Check Service Status</a>
          </div>

          <div class="hero-meta">
            <span class="pill">⚙️ Python Flask</span>
            <span class="pill">☁️ Google Kubernetes Engine</span>
            <span class="pill">🚀 Cloud Native Delivery</span>
          </div>
        </div>

        <div class="hero-card">
          <div class="screen">
            <div class="screen-top">
              <div class="dot"></div>
              <div class="dot"></div>
              <div class="dot"></div>
            </div>
            <div class="screen-body">
              <div class="terminal-line">$ git push origin main</div>
              <div class="terminal-line">$ cloud build triggered successfully</div>
              <div class="terminal-line">$ deployment rolling out to GKE...</div>
              <div class="terminal-line">$ status: LIVE • READY • HEALTHY</div>

              <div class="status-grid">
                <div class="mini-card">
                  <div class="mini-title">Environment</div>
                  <div class="mini-value">Production</div>
                </div>
                <div class="mini-card">
                  <div class="mini-title">Cluster State</div>
                  <div class="mini-value">Healthy</div>
                </div>
                <div class="mini-card">
                  <div class="mini-title">App Version</div>
                  <div class="mini-value">v1.0</div>
                </div>
                <div class="mini-card">
                  <div class="mini-title">Energy Level</div>
                  <div class="mini-value">9000+</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="features">
        <div class="section-head">
          <div>
            <h2>Core features</h2>
            <p>
              Designed as a polished landing page with motion, glow, depth, and a clear story.
              Everything is handwritten without any additional UI or animation library.
            </p>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <div class="icon">🎨</div>
            <h3>Stylish UI</h3>
            <p>
              Glassmorphism cards, glowing gradients, animated backgrounds, and clean visual hierarchy
              give the page a vivid anime-inspired identity.
            </p>
          </div>
          <div class="card">
            <div class="icon">⚡</div>
            <h3>Lightweight Motion</h3>
            <p>
              Smooth transitions, pulsing indicators, drifting background orbs, and typing effects
              bring the page to life while keeping it dependency-free.
            </p>
          </div>
          <div class="card">
            <div class="icon">☁️</div>
            <h3>Cloud Ready</h3>
            <p>
              The app stays simple to deploy in containers, works well with health checks,
              and is easy to run behind services, load balancers, and Kubernetes deployments.
            </p>
          </div>
        </div>
      </section>

      <section id="about">
        <div class="split">
          <div class="card">
            <div class="section-head" style="margin-bottom:8px;">
              <div>
                <h2>About this page</h2>
              </div>
            </div>
            <p style="color:var(--muted); line-height:1.9;">
              This landing page is crafted for a modern developer portfolio or demo application.
              It feels energetic and expressive, while still being simple enough to maintain in one Python file.
              That makes it ideal for testing CI/CD, GKE deployments, and health monitoring without adding frontend complexity.
            </p>

            <div class="feature-list">
              <div class="feature-item">
                <div>🌌</div>
                <div>
                  <strong>Immersive visuals</strong>
                  Animated background layers create motion and depth from the moment the page loads.
                </div>
              </div>
              <div class="feature-item">
                <div>🛡️</div>
                <div>
                  <strong>Operationally friendly</strong>
                  The `/health` route remains simple and probe-safe for Kubernetes readiness and liveness checks.
                </div>
              </div>
              <div class="feature-item">
                <div>🧩</div>
                <div>
                  <strong>Easy to extend</strong>
                  You can add sections, testimonials, pricing blocks, contact forms, or deployment data later.
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="icon">🔥</div>
            <h3 style="font-size:28px; margin-bottom:12px;">Anime energy, engineering discipline</h3>
            <p>
              The visual language draws inspiration from cinematic anime intros:
              dramatic contrast, luminous colors, dynamic motion, and a sense of forward movement.
              At the same time, the implementation stays practical and minimal for real cloud deployments.
            </p>
            <div style="margin-top:20px; display:grid; gap:12px;">
              <div class="pill">Responsive layout for desktop and mobile</div>
              <div class="pill">Single Flask file for fast testing</div>
              <div class="pill">No CSS frameworks, no JS libraries</div>
              <div class="pill">Easy integration with Docker and GKE</div>
            </div>
          </div>
        </div>
      </section>

      <section id="stats">
        <div class="section-head">
          <div>
            <h2>Live-style highlights</h2>
            <p>
              These counters give the page the feeling of a launch dashboard while staying fully static and dependency-free.
            </p>
          </div>
        </div>

        <div class="stats-section">
          <div class="stat">
            <div class="stat-number" data-target="99">0</div>
            <div class="stat-label">Uptime confidence feel</div>
          </div>
          <div class="stat">
            <div class="stat-number" data-target="3">0</div>
            <div class="stat-label">Core stack layers</div>
          </div>
          <div class="stat">
            <div class="stat-number" data-target="100">0</div>
            <div class="stat-label">Percent handcrafted UI</div>
          </div>
          <div class="stat">
            <div class="stat-number" data-target="8080">0</div>
            <div class="stat-label">Service port energy</div>
          </div>
        </div>
      </section>

      <section id="journey">
        <div class="section-head">
          <div>
            <h2>From code to cluster</h2>
            <p>
              A clean deployment journey makes this app a great fit for demonstrating CI/CD, containers, and Kubernetes delivery.
            </p>
          </div>
        </div>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-step">STEP 01</div>
            <div>
              <h4>Write the app</h4>
              <p>
                Start with a lightweight Flask service that serves the landing page and a health endpoint.
              </p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-step">STEP 02</div>
            <div>
              <h4>Containerize</h4>
              <p>
                Package it with Docker so the exact same app can run locally, in CI, and on GKE.
              </p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-step">STEP 03</div>
            <div>
              <h4>Build and release</h4>
              <p>
                Use Cloud Build to create the image and Cloud Deploy to roll it out across your environments.
              </p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-step">STEP 04</div>
            <div>
              <h4>Scale and evolve</h4>
              <p>
                Add namespaces, services, ingress, autoscaling, or observability as the app grows.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section id="cta">
        <div class="cta">
          <div>
            <h3>Ready to power this up on GKE?</h3>
            <p>
              This landing page is a strong starting point for a polished demo app.
              It looks modern, feels animated, and remains simple enough to test, containerize, and deploy quickly.
            </p>
          </div>
          <div style="display:flex; gap:14px; justify-content:flex-start; flex-wrap:wrap;">
            <a class="btn primary" href="/">Open Home</a>
            <a class="btn" href="/health">Run Health Check</a>
          </div>
        </div>
      </section>
    </div>
  </main>

  <footer>
    <div class="container footer-wrap">
      <div>
        <strong>Akshit Soam</strong><br />
        <span style="color:#94a3b8;">Built with Flask, styled by hand, deployed for the cloud.</span>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <a class="pill" href="#features">Features</a>
        <a class="pill" href="#about">About</a>
        <a class="pill" href="#journey">Journey</a>
        <a class="pill" href="/health">Health</a>
      </div>
    </div>
  </footer>

  <script>
    const toggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    toggle.addEventListener("click", function () {
      navLinks.classList.toggle("show");
    });

    const counters = document.querySelectorAll(".stat-number");
    const animateCounter = (el) => {
      const target = Number(el.getAttribute("data-target"));
      const duration = 1400;
      const start = 0;
      const startTime = performance.now();

      function update(now) {
        const progress = Math.min((now - startTime) / duration, 1);
        const value = Math.floor(start + (target - start) * progress);
        el.textContent = value;
        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          el.textContent = target;
        }
      }
      requestAnimationFrame(update);
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.6 });

    counters.forEach((counter) => observer.observe(counter));
  </script>
</body>
</html>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)