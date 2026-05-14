from flask import Flask

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✨ 崔诗雅的小宇宙</title>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fdf7f2;
            --card-bg: #ffffff;
            --text: #3d3a4a;
            --text-light: #6b6578;
            --text-muted: #9a94a8;
            --accent: #d4957b;
            --accent-soft: #f2d5c6;
            --accent-light: #fdf0ea;
            --rose: #e8b4b8;
            --rose-light: #fce8ea;
            --lavender: #c4bfd6;
            --lavender-light: #f0eef6;
            --mint: #b7cfc4;
            --mint-light: #e8f2ec;
            --sunshine: #f0d78c;
            --sunshine-light: #fef9ed;
            --border-radius: 20px;
            --border-radius-sm: 12px;
            --shadow-sm: 0 2px 12px rgba(60,40,30,0.05);
            --shadow-md: 0 6px 28px rgba(60,40,30,0.08);
            --shadow-lg: 0 14px 40px rgba(60,40,30,0.10);
            --shadow-glow: 0 0 40px rgba(212,149,123,0.15);
            --transition: 0.35s cubic-bezier(0.25,0.1,0.25,1);
            --font-body: "PingFang SC","Microsoft YaHei",sans-serif;
            --font-heading: "STKaiti","KaiTi",serif;
            --font-cute: "ZCOOL KuaiLe","STYuanti",sans-serif;
            --font-quote: "Georgia","KaiTi",serif;
            --font-english: "Pacifico",cursive;
            --placeholder-bg: #f5f0ec;
            --placeholder-color: #b8a99f;
        }
        * { margin:0; padding:0; box-sizing:border-box; }
        html { scroll-behavior:smooth; }
        body { font-family:var(--font-body); background:var(--bg); color:var(--text); overflow-x:hidden; }

        /* 登录界面 */
        .login-screen {
            position:fixed; top:0; left:0; width:100%; height:100%;
            background: url('/static/login-bg.jpg') center/cover no-repeat;
            display:flex; align-items:center; justify-content:center; z-index:10000;
        }
        .login-box {
            background: rgba(255,255,255,0.15); backdrop-filter:blur(12px);
            border-radius:28px; padding:2.5rem 2rem; text-align:center;
            width:90%; max-width:380px; box-shadow:0 20px 50px rgba(0,0,0,0.2);
            border:1px solid rgba(255,255,255,0.3);
        }
        .login-avatar {
            width:100px; height:100px; border-radius:50%;
            background: url('/static/touxiang.jpg') center/cover no-repeat;
            margin:0 auto 1rem; border:3px solid white;
        }
        .login-id { color:white; font-size:1.6rem; font-weight:500; letter-spacing:0.08em; font-family:var(--font-heading); margin-bottom:0.3rem; }
        .login-hint { color:rgba(255,255,255,0.85); font-size:0.85rem; letter-spacing:0.05em; margin-bottom:1.8rem; font-style:italic; }
        .login-input {
            width:100%; padding:12px 16px; margin-bottom:1rem;
            background:rgba(255,255,255,0.2); border:1px solid rgba(255,255,255,0.4);
            border-radius:12px; color:white; font-size:1rem; outline:none; transition:0.3s;
        }
        .login-input::placeholder { color:rgba(255,255,255,0.7); }
        .login-input:focus { background:rgba(255,255,255,0.3); border-color:white; }
        .login-btn {
            width:100%; padding:12px; background:rgba(255,255,255,0.25);
            border:1px solid white; border-radius:30px; color:white; font-size:1rem;
            letter-spacing:0.1em; cursor:pointer; transition:0.3s; font-weight:500;
        }
        .login-btn:hover { background:rgba(255,255,255,0.45); }
        .login-error { color:#ffe0e0; font-size:0.8rem; margin-top:0.5rem; display:none; }

        /* 生日动画屏幕 */
        .birthday-screen {
            position:fixed; top:0; left:0; width:100%; height:100%;
            background: #fce8ea;
            background-image: radial-gradient(circle at 30% 40%, #fdf0ea 10%, transparent 50%),
                              radial-gradient(circle at 70% 60%, #f2d5c6 10%, transparent 50%);
            display:none; flex-direction:column; align-items:center; justify-content:center; z-index:9999;
            overflow:hidden;
        }
        .confetti-container {
            position:absolute; top:0; left:0; width:100%; height:100%;
            pointer-events:none; z-index:1;
        }
        .confetti-piece {
            position:absolute;
            width:10px;
            height:30px;
            top:-10%;
            animation: confettiFall linear infinite;
            opacity:0.7;
        }
        @keyframes confettiFall {
            0% { transform: translateY(0) rotate(0deg); opacity:1; }
            100% { transform: translateY(110vh) rotate(720deg); opacity:0; }
        }
        .firework {
            position:absolute;
            border-radius:50%;
            animation: fireworkBurst 1.5s ease-out forwards;
            pointer-events:none;
            z-index:1;
        }
        @keyframes fireworkBurst {
            0% { transform:scale(0); opacity:1; }
            100% { transform:scale(1); opacity:0; }
        }
        .firework-particle {
            position:absolute;
            width:8px;
            height:8px;
            border-radius:50%;
            animation: particleOut 1.2s ease-out forwards;
        }
        @keyframes particleOut {
            0% { transform:translate(0,0) scale(1); opacity:1; }
            100% { transform:translate(var(--tx), var(--ty)) scale(0); opacity:0; }
        }
        .cd-container {
            position:relative;
            width:45vw; height:45vw;
            max-width:600px; max-height:600px;
            margin:0 auto 0.5rem;
            z-index:2;
        }
        @media (max-width: 600px) {
            .cd-container {
                width:80vw; height:80vw;
            }
        }
        .cd-disc {
            width:100%; height:100%; border-radius:50%;
            background: conic-gradient(from 0deg, #fff, #f8e8e8, #fff, #fce8ea, #fff, #f8e8e8, #fff, #fce8ea);
            box-shadow: 0 0 0 8px #fcccd1, 0 0 0 16px #ffb6c1, 0 0 0 24px #ffa07a, 0 0 50px rgba(255,105,180,0.6), inset 0 0 30px rgba(255,255,255,0.9);
            animation: spinCD 4s linear infinite;
            display:flex; align-items:center; justify-content:center; position:relative;
        }
        .cd-disc::after {
            content:''; position:absolute;
            width:18%; height:18%;
            background:linear-gradient(145deg, #fff5f5, #fdd);
            border-radius:50%; border:5px solid #d4957b;
            box-shadow:inset 0 0 20px rgba(0,0,0,0.15), 0 0 15px rgba(255,140,0,0.5);
            z-index:3;
        }
        .cd-text {
            position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
            text-align:center; z-index:2; width:80%;
        }
        .cn-birthday {
            font-family:var(--font-cute);
            font-size:clamp(2rem, 10vw, 4.5rem);
            color:#d6336c;
            text-shadow:0 0 15px white, 0 0 25px #ffb6c1;
        }
        .en-birthday {
            font-family:var(--font-english);
            font-size:clamp(1.5rem, 7vw, 3rem);
            color:#c2185b;
            text-shadow:0 0 10px white, 0 0 20px #ffb6c1;
            margin:0.3rem 0;
        }
        .birthday-date {
            font-family:var(--font-english);
            font-size:clamp(1.2rem, 5vw, 2rem);
            color:#b0306a;
            text-shadow:0 0 10px white;
        }
        @keyframes spinCD { from{transform:rotate(0deg);} to{transform:rotate(360deg);} }
        .cd-container::before,
        .cd-container::after {
            content:''; position:absolute; border-radius:50%; pointer-events:none;
            animation: spinReverse 8s linear infinite;
        }
        .cd-container::before {
            top:-15px; left:-15px; right:-15px; bottom:-15px;
            border:4px dashed transparent;
            border-top-color:#ff69b4; border-right-color:#ffe81a;
            border-bottom-color:#00e5ff; border-left-color:#ff9100;
        }
        .cd-container::after {
            top:-30px; left:-30px; right:-30px; bottom:-30px;
            border:3px dotted #ff4081;
            animation: spinReverse 12s linear infinite;
        }
        @keyframes spinReverse { from{transform:rotate(0deg);} to{transform:rotate(-360deg);} }
        .floating-emoji {
            position:absolute;
            font-size:2.2rem;
            animation: floatEmoji 3.5s ease-in-out infinite alternate;
            opacity:0.85;
            z-index:3;
            pointer-events:none;
        }
        @keyframes floatEmoji {
            0% { transform:translateY(0) rotate(0deg); }
            100% { transform:translateY(-25px) rotate(15deg); }
        }
        .birthday-msg {
            font-family:var(--font-cute);
            font-size:clamp(2rem, 8vw, 3.5rem);
            color:#d4957b;
            margin-top:0.5rem;
            animation:floatText 2s ease-in-out infinite alternate;
            z-index:4;
        }
        @keyframes floatText {
            0%{transform:translateY(0);} 100%{transform:translateY(-10px);}
        }
        .skip-birthday {
            margin-top:1.5rem; background:none; border:2px solid #d4957b;
            color:#d4957b; padding:10px 30px; border-radius:30px;
            cursor:pointer; font-size:1rem; font-weight:bold;
            letter-spacing:0.05em; transition:0.3s; z-index:5;
        }
        .skip-birthday:hover { background:#d4957b; color:white; }
        .cute-animals {
            position:absolute; bottom:20px; right:20px; display:flex; gap:15px;
            opacity:0.8; z-index:5;
        }
        .cute-animals img { width:60px; height:60px; object-fit:contain; animation:bounceAnimal 2s ease-in-out infinite alternate; }
        @keyframes bounceAnimal { 0%{transform:translateY(0);} 100%{transform:translateY(-8px);} }

        /* 主站包装 */
        #mainSite { display:none; }

        body::before,
        body::after {
            content: '';
            position: fixed;
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
        }
        body::before {
            top: -180px; right: -120px; width: 500px; height: 500px;
            background: radial-gradient(circle, rgba(232,180,184,0.12) 0%, transparent 70%);
        }
        body::after {
            bottom: -160px; left: -100px; width: 450px; height: 450px;
            background: radial-gradient(circle, rgba(212,149,123,0.10) 0%, transparent 70%);
        }
        .navbar {
            position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
            background: rgba(255,255,255,0.75);
            backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid rgba(200,180,170,0.18);
            padding: 0 2rem; transition: var(--transition);
        }
        .navbar-inner {
            max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; height: 58px;
        }
        .nav-logo {
            font-family: var(--font-cute); font-size: 1.35rem; font-weight: 700; color: var(--accent);
            text-decoration: none; display: flex; align-items: center; gap: 8px;
        }
        .nav-logo .logo-dot {
            display: inline-block; width: 10px; height: 10px; background: var(--rose);
            border-radius: 50%; animation: logoPulse 2.5s ease-in-out infinite;
        }
        @keyframes logoPulse {
            0%,100%{transform: scale(1); opacity: 0.8;} 50%{transform: scale(1.8); opacity: 1;}
        }
        .nav-links { display: flex; list-style: none; gap: 1.6rem; align-items: center; }
        .nav-links a {
            text-decoration: none; color: var(--text-light); font-size: 0.92rem; font-weight: 500;
            letter-spacing: 0.03em; transition: var(--transition); position: relative; padding: 4px 0;
        }
        .nav-links a::after {
            content: ''; position: absolute; bottom: -2px; left: 0; width: 0%; height: 2px;
            background: var(--accent); border-radius: 2px; transition: var(--transition);
        }
        .nav-links a:hover { color: var(--accent); }
        .nav-links a:hover::after { width: 100%; }
        .nav-toggle { display: none; background: none; border: none; font-size: 1.6rem; cursor: pointer; color: var(--text); padding: 4px; }
        @media (max-width: 768px) {
            .nav-links {
                position: fixed; top: 58px; left: 0; right: 0; background: rgba(255,255,255,0.95);
                backdrop-filter: blur(18px); flex-direction: column; gap: 0; padding: 0;
                max-height: 0; overflow: hidden; transition: max-height 0.4s ease, padding 0.4s ease;
                border-bottom: 1px solid rgba(200,180,170,0.15);
            }
            .nav-links.active { max-height: 420px; padding: 1rem 0; }
            .nav-links li { width: 100%; text-align: center; }
            .nav-links a { display: block; padding: 0.8rem 2rem; font-size: 1rem; }
            .nav-links a::after { display: none; }
            .nav-toggle { display: block; }
        }

        .main-container { position: relative; z-index: 1; max-width: 1080px; margin: 0 auto; padding: 80px 1.5rem 3rem; }
        .section { margin-bottom: 3.5rem; position: relative; }
        .section-header { text-align: center; margin-bottom: 2.2rem; }
        .section-tag {
            display: inline-block; font-family: var(--font-cute); font-size: 0.8rem; letter-spacing: 0.08em;
            color: var(--accent); background: var(--accent-light); padding: 5px 16px; border-radius: 20px;
            margin-bottom: 0.6rem; font-weight: 600;
        }
        .section-title { font-family: var(--font-heading); font-size: 2rem; font-weight: 500; letter-spacing: 0.04em; margin: 0; }
        .section-subtitle { font-size: 0.95rem; color: var(--text-muted); margin-top: 0.35rem; letter-spacing: 0.03em; font-weight: 400; }
        .card {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 2rem 2.2rem;
            box-shadow: var(--shadow-sm); transition: var(--transition); position: relative; overflow: hidden;
        }
        .card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
        .bounce-once { animation: bounceOnce 0.6s ease; }
        @keyframes bounceOnce {
            0%{transform: translateY(0);} 30%{transform: translateY(-12px);}
            50%{transform: translateY(0);} 70%{transform: translateY(-5px);} 100%{transform: translateY(0);}
        }
        .particle {
            position: fixed; pointer-events: none; z-index: 9999; font-size: 1.5rem;
            animation: particleFloat 1s ease-out forwards; will-change: transform, opacity;
        }
        @keyframes particleFloat {
            0%{opacity: 1; transform: translate(0,0) scale(1);}
            100%{opacity: 0; transform: translate(var(--tx), var(--ty)) scale(0);}
        }

        .hero {
            display: flex; align-items: center; gap: 2.5rem; min-height: 380px;
            background: var(--card-bg); border-radius: var(--border-radius); padding: 2.8rem 2.5rem;
            box-shadow: var(--shadow-lg); position: relative; overflow: hidden; margin-bottom: 3.5rem;
        }
        .hero::before {
            content: ''; position: absolute; top: -60px; right: -60px; width: 260px; height: 260px;
            background: radial-gradient(circle, var(--rose-light) 0%, transparent 70%); border-radius: 50%; pointer-events: none;
        }
        .hero::after {
            content: ''; position: absolute; bottom: -40px; left: 30%; width: 180px; height: 180px;
            background: radial-gradient(circle, var(--accent-light) 0%, transparent 70%); border-radius: 50%; pointer-events: none;
        }
        .hero-avatar {
            flex-shrink: 0; width: 170px; height: 170px; border-radius: 50%;
            background: var(--placeholder-bg); display: flex; align-items: center; justify-content: center;
            font-size: 4rem; position: relative; z-index: 1; box-shadow: var(--shadow-glow);
            overflow: hidden; cursor: pointer; transition: var(--transition);
            color: var(--placeholder-color);
        }
        .hero-avatar:hover { transform: scale(1.04); box-shadow: 0 0 60px rgba(212,149,123,0.25); }
        .hero-avatar img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
        .hero-content { position: relative; z-index: 1; flex: 1; }
        .hero-greeting {
            font-family: var(--font-cute); font-size: 0.85rem; letter-spacing: 0.06em;
            color: var(--accent); font-weight: 600; margin-bottom: 0.3rem;
        }
        .hero-name {
            font-family: var(--font-heading); font-size: 2.8rem; font-weight: 500;
            letter-spacing: 0.05em; color: var(--text); margin: 0 0 0.4rem; line-height: 1.2;
        }
        .hero-desc { font-size: 1.05rem; color: var(--text-light); line-height: 1.6; max-width: 500px; }
        .hero-badges { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1rem; }
        .hero-badge {
            font-family: var(--font-cute); font-size: 0.78rem; padding: 6px 14px; border-radius: 20px;
            background: var(--accent-light); color: var(--accent); font-weight: 600;
            letter-spacing: 0.04em; cursor: default; transition: var(--transition);
        }
        .hero-badge:hover { background: var(--accent-soft); transform: translateY(-1px); }
        @media (max-width: 700px) {
            .hero { flex-direction: column; text-align: center; padding: 2rem 1.5rem; gap: 1.5rem; min-height: auto; }
            .hero-avatar { width: 130px; height: 130px; font-size: 3rem; }
            .hero-name { font-size: 2.1rem; }
            .hero-desc { max-width: 100%; font-size: 0.95rem; }
            .hero-badges { justify-content: center; }
        }

        .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
        @media (max-width: 650px) { .about-grid { grid-template-columns: 1fr; } }
        .about-card {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 1.8rem 2rem;
            box-shadow: var(--shadow-sm); transition: var(--transition); text-align: center;
            position: relative; overflow: hidden;
        }
        .about-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
        .about-card.mbti-card { border-top: 4px solid var(--lavender); }
        .about-card.zodiac-card { border-top: 4px solid var(--rose); }
        .about-card-icon { font-size: 3rem; margin-bottom: 0.6rem; display: block; }
        .about-card-label {
            font-family: var(--font-cute); font-size: 0.78rem; letter-spacing: 0.06em;
            color: var(--text-muted); text-transform: uppercase; font-weight: 600;
        }
        .about-card-value {
            font-family: var(--font-heading); font-size: 1.8rem; font-weight: 500;
            color: var(--text); margin: 0.2rem 0; letter-spacing: 0.04em;
        }
        .about-card-desc { font-size: 0.9rem; color: var(--text-light); line-height: 1.5; margin-top: 0.4rem; }
        .about-intro {
            grid-column: 1 / -1; background: var(--card-bg); border-radius: var(--border-radius);
            padding: 2rem 2.2rem; box-shadow: var(--shadow-sm); transition: var(--transition);
            border-left: 4px solid var(--accent);
        }
        .about-intro:hover { box-shadow: var(--shadow-md); }
        .about-intro h4 {
            font-family: var(--font-heading); font-size: 1.3rem; font-weight: 500;
            margin-bottom: 0.6rem; letter-spacing: 0.03em;
        }
        .about-intro p { font-size: 0.95rem; color: var(--text-light); line-height: 1.7; }

        .timeline { position: relative; padding-left: 3rem; }
        .timeline::before {
            content: ''; position: absolute; left: 20px; top: 0; bottom: 0; width: 3px;
            background: linear-gradient(to bottom, var(--accent-soft), var(--rose-light), var(--lavender-light), var(--accent-soft));
            border-radius: 3px;
        }
        .timeline-item {
            position: relative; margin-bottom: 2rem; background: var(--card-bg);
            border-radius: var(--border-radius); padding: 1.5rem 1.8rem; box-shadow: var(--shadow-sm);
            transition: var(--transition); cursor: default;
        }
        .timeline-item:hover { box-shadow: var(--shadow-md); transform: translateX(3px); }
        .timeline-item::before {
            content: ''; position: absolute; left: -2.2rem; top: 1.8rem; width: 14px; height: 14px;
            background: var(--accent); border-radius: 50%; border: 3px solid #fff;
            box-shadow: 0 0 0 6px var(--accent-light); transition: var(--transition);
        }
        .timeline-item:hover::before { background: var(--rose); box-shadow: 0 0 0 10px var(--rose-light); }
        .timeline-item.future-node::before {
            background: var(--lavender); box-shadow: 0 0 0 6px var(--lavender-light);
            animation: futurePulse 2s ease-in-out infinite;
        }
        @keyframes futurePulse {
            0%,100% { box-shadow: 0 0 0 6px var(--lavender-light); }
            50% { box-shadow: 0 0 0 16px rgba(196,191,214,0.25); }
        }
        .timeline-year {
            font-family: var(--font-cute); font-size: 0.78rem; letter-spacing: 0.06em;
            color: var(--accent); font-weight: 700; display: inline-block;
            background: var(--accent-light); padding: 3px 12px; border-radius: 14px; margin-bottom: 0.5rem;
        }
        .timeline-title { font-family: var(--font-heading); font-size: 1.15rem; font-weight: 500; letter-spacing: 0.03em; margin: 0 0 0.3rem; }
        .timeline-desc { font-size: 0.9rem; color: var(--text-light); line-height: 1.6; }
        @media (max-width: 600px) {
            .timeline { padding-left: 2.2rem; }
            .timeline::before { left: 12px; }
            .timeline-item::before { left: -1.55rem; width: 11px; height: 11px; top: 1.5rem; }
            .timeline-item { padding: 1.2rem; }
        }

        .gallery-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.8rem;
            position: relative;
        }
        .gallery-nav-btn {
            background: var(--card-bg);
            border: 1px solid var(--accent-soft);
            border-radius: 50%;
            width: 44px;
            height: 44px;
            font-size: 1.2rem;
            color: var(--accent);
            cursor: pointer;
            transition: var(--transition);
            box-shadow: var(--shadow-sm);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            flex-shrink: 0;
        }
        .gallery-nav-btn:hover { background: var(--accent-light); box-shadow: var(--shadow-md); transform: scale(1.08); }
        .gallery-nav-btn:active { transform: scale(0.96); }
        .gallery-pages-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            height: 500px;
            margin: 0 auto;
            overflow: hidden;
        }
        .gallery-photo-card {
            position: absolute;
            background: var(--card-bg);
            border-radius: var(--border-radius-sm);
            overflow: hidden;
            box-shadow: var(--shadow-md);
            transition: transform 0.4s ease, box-shadow 0.4s ease, opacity 0.8s ease;
            cursor: pointer;
            will-change: transform, opacity;
            animation: fadeInCard 0.8s ease both;
        }
        .gallery-photo-card img { width: 100%; height: 100%; object-fit: cover; display: block; }
        .gallery-photo-card:hover { transform: scale(1.05) !important; box-shadow: var(--shadow-lg); z-index: 20 !important; }
        @keyframes fadeInCard { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
        .gallery-dots { display: flex; justify-content: center; gap: 0.5rem; margin-top: 1.2rem; }
        .gallery-dot {
            width: 10px; height: 10px; border-radius: 50%;
            background: var(--accent-soft); cursor: pointer; transition: var(--transition);
        }
        .gallery-dot.active { background: var(--accent); transform: scale(1.3); }
        @media (max-width: 600px) { .gallery-pages-container { height: 380px; } }

        .idol-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 1.2rem; }
        .idol-card {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 1.4rem;
            text-align: center; box-shadow: var(--shadow-sm); transition: var(--transition); cursor: pointer;
        }
        .idol-card:hover { box-shadow: var(--shadow-md); transform: translateY(-3px); }
        .idol-card .idol-img {
            width: 90px; height: 90px; border-radius: 50%; background: var(--placeholder-bg);
            margin: 0 auto 0.8rem; display: flex; align-items: center; justify-content: center;
            font-size: 2.5rem; overflow: hidden; color: var(--placeholder-color);
        }
        .idol-card .idol-img img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
        .idol-card .idol-name { font-family: var(--font-heading); font-weight: 500; font-size: 1rem; color: var(--text); }
        .idol-card .idol-tag { font-size: 0.75rem; color: var(--text-muted); margin-top: 2px; }

        .wishlist { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 1rem; }
        .wish-card {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 1.4rem 1.6rem;
            box-shadow: var(--shadow-sm); transition: var(--transition); display: flex; align-items: flex-start;
            gap: 0.8rem; cursor: default; position: relative; overflow: hidden;
        }
        .wish-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
        .wish-card:nth-child(4n+1) { border-left: 4px solid var(--rose); }
        .wish-card:nth-child(4n+2) { border-left: 4px solid var(--mint); }
        .wish-card:nth-child(4n+3) { border-left: 4px solid var(--sunshine); }
        .wish-card:nth-child(4n+4) { border-left: 4px solid var(--lavender); }
        .wish-emoji { font-size: 1.8rem; flex-shrink: 0; }
        .wish-text { font-size: 0.95rem; color: var(--text); line-height: 1.5; }
        .wish-status {
            font-family: var(--font-cute); font-size: 0.7rem; letter-spacing: 0.05em;
            padding: 3px 10px; border-radius: 12px; background: var(--mint-light);
            color: #6b9e85; font-weight: 600; display: inline-block; margin-top: 6px;
        }
        .wish-status.pending { background: var(--sunshine-light); color: #b8983d; }

        .memories-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.2rem; }
        .memory-card {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 1.6rem 1.8rem;
            box-shadow: var(--shadow-sm); transition: var(--transition); cursor: default; position: relative; overflow: hidden;
        }
        .memory-card:hover { box-shadow: var(--shadow-md); transform: translateY(-3px); }
        .memory-card.ten-years {
            border: 2px dashed var(--accent-soft); background: var(--accent-light); text-align: center;
            grid-column: 1 / -1; max-width: 600px; margin: 0 auto;
        }
        .memory-date {
            font-family: var(--font-cute); font-size: 0.75rem; letter-spacing: 0.05em;
            color: var(--text-muted); font-weight: 600;
        }
        .memory-text { font-size: 0.93rem; color: var(--text); margin-top: 0.5rem; line-height: 1.6; }

        .quote-block {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 2.2rem 2.5rem;
            box-shadow: var(--shadow-md); text-align: center; position: relative; overflow: hidden; margin-bottom: 1.5rem;
        }
        .quote-block::before {
            content: '"'; position: absolute; top: -10px; left: 20px; font-size: 8rem;
            color: var(--accent-soft); opacity: 0.4; font-family: Georgia, serif; line-height: 1; pointer-events: none;
        }
        .quote-block.heartfelt::before { color: var(--rose-light); opacity: 0.5; }
        .quote-label {
            font-family: var(--font-cute); font-size: 0.78rem; letter-spacing: 0.06em;
            color: var(--accent); font-weight: 600; text-transform: uppercase; margin-bottom: 0.8rem;
        }
        .quote-text {
            font-family: var(--font-quote); font-size: 1.25rem; font-weight: 400; color: var(--text);
            line-height: 1.8; letter-spacing: 0.04em; position: relative; z-index: 1;
            max-width: 650px; margin: 0 auto; font-style: italic;
        }

        .music-player {
            background: var(--card-bg); border-radius: var(--border-radius); padding: 1.6rem 2rem;
            box-shadow: var(--shadow-md); display: flex; align-items: center; gap: 1.2rem; flex-wrap: wrap;
            transition: var(--transition);
        }
        .music-player:hover { box-shadow: var(--shadow-lg); }
        .music-cover {
            width: 80px; height: 80px; border-radius: var(--border-radius-sm);
            background: var(--placeholder-bg); flex-shrink: 0; display: flex; align-items: center;
            justify-content: center; font-size: 2.5rem; overflow: hidden; color: var(--placeholder-color);
        }
        .music-cover img { width: 100%; height: 100%; object-fit: cover; display: none; }
        .music-info { flex: 1; min-width: 150px; }
        .music-title { font-family: var(--font-heading); font-weight: 500; font-size: 1.05rem; margin: 0; color: var(--text); }
        .music-artist { font-size: 0.8rem; color: var(--text-light); margin-top: 4px; }
        .music-controls { display: flex; align-items: center; gap: 0.8rem; }
        .music-btn {
            width: 42px; height: 42px; border-radius: 50%; border: none; background: var(--accent-light);
            color: var(--accent); font-size: 1.2rem; cursor: pointer; transition: var(--transition);
            display: flex; align-items: center; justify-content: center;
        }
        .music-btn:hover { background: var(--accent-soft); transform: scale(1.08); }
        .music-btn.play-btn {
            width: 50px; height: 50px; background: var(--accent); color: #fff; font-size: 1.3rem;
        }
        .music-btn.play-btn:hover { background: #c58165; transform: scale(1.1); }
        .music-progress {
            width: 100%; height: 4px; background: var(--accent-soft); border-radius: 2px;
            margin-top: 0.8rem; cursor: pointer; position: relative;
        }
        .music-progress-fill { height: 100%; background: var(--accent); border-radius: 2px; width: 0%; transition: width 0.1s linear; }

        .video-wrapper {
            background: var(--placeholder-bg); border-radius: var(--border-radius); overflow: hidden;
            box-shadow: var(--shadow-md); aspect-ratio: 16 / 9; display: flex; align-items: center;
            justify-content: center; position: relative; cursor: pointer; transition: var(--transition);
        }
        .video-wrapper:hover { box-shadow: var(--shadow-lg); }
        .video-placeholder { text-align: center; color: var(--placeholder-color); }
        .video-placeholder .play-icon { font-size: 4rem; display: block; margin-bottom: 0.5rem; opacity: 0.7; }
        .video-placeholder span { font-family: var(--font-cute); letter-spacing: 0.04em; font-size: 0.9rem; }
        .video-wrapper video { width: 100%; height: 100%; object-fit: cover; }

        .site-footer {
            text-align: center; padding: 2.5rem 1.5rem 1.5rem; color: var(--text-muted);
            font-size: 0.85rem; letter-spacing: 0.04em; position: relative; z-index: 1;
        }
        .site-footer .footer-heart { display: inline-block; animation: heartbeat 1.2s ease-in-out infinite; color: var(--rose); }
        @keyframes heartbeat {
            0%,100%{transform: scale(1);} 15%{transform: scale(1.25);} 30%{transform: scale(1);} 45%{transform: scale(1.15);} 60%{transform: scale(1);}
        }

        .lightbox {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(30,20,15,0.85); z-index: 9999; display: flex; align-items: center;
            justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; cursor: pointer;
        }
        .lightbox.active { opacity: 1; pointer-events: auto; }
        .lightbox img { max-width: 90vw; max-height: 85vh; border-radius: var(--border-radius-sm); box-shadow: 0 20px 60px rgba(0,0,0,0.5); object-fit: contain; }
        .lightbox-close {
            position: absolute; top: 20px; right: 30px; font-size: 2.5rem; color: #fff;
            cursor: pointer; z-index: 10000; background: none; border: none; line-height: 1;
        }

        .fade-in {
            opacity: 0; transform: translateY(30px);
            transition: opacity 0.7s ease, transform 0.7s ease;
        }
        .fade-in.visible { opacity: 1; transform: translateY(0); }
        .divider-dots {
            text-align: center; margin: 1rem 0; letter-spacing: 8px;
            color: var(--accent-soft); font-size: 0.6rem; user-select: none;
        }
        @media (max-width: 480px) {
            .section-title { font-size: 1.5rem; }
            .card { padding: 1.3rem 1.2rem; }
            .hero-name { font-size: 1.7rem; }
            .quote-text { font-size: 1.05rem; }
            .music-player { flex-direction: column; text-align: center; }
        }

        /* CD 音乐墙 */
        .cd-wall {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 2rem 1.5rem;
            margin-top: 2rem;
        }
        .cd-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
        }
        .cd-cover {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: #fff;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            overflow: hidden;
            position: relative;
            transition: transform 0.4s;
            margin-bottom: 0.8rem;
        }
        .cd-cover.playing {
            animation: spinCD 3s linear infinite;
        }
        .cd-cover img {
            width: 100%; height: 100%;
            object-fit: cover;
            border-radius: 50%;
        }
        .cd-song-title { font-weight: 600; font-size: 1rem; color: var(--text); }
        .cd-lyric { font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem; font-style: italic; }

        /* 礼物盒样式 */
        .gift-section {
            text-align: center;
            padding: 3rem 0 4rem;
        }
        .gift-box-wrap {
            position: relative;
            width: 220px;
            height: 200px;
            margin: 0 auto;
            cursor: pointer;
        }
        .gift-box {
            position: relative;
            width: 180px;
            height: 140px;
            background: #fce0e4;
            margin: 60px auto 0;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(220,160,175,0.3);
            transition: transform 0.4s ease;
        }
        .gift-box-wrap:hover .gift-box {
            transform: translateY(-8px);
        }
        .gift-lid {
            position: absolute;
            top: 0;
            left: 0;
            width: 180px;
            height: 50px;
            background: #f8c8d0;
            border-radius: 8px 8px 0 0;
            transform-origin: center bottom;
            transition: transform 0.8s cubic-bezier(0.65,0,0.35,1);
            z-index: 2;
        }
        .gift-ribbon {
            position: absolute;
            top: 0;
            left: 50%;
            width: 12px;
            height: 100%;
            background: #e898a8;
            transform: translateX(-50%);
            z-index: 3;
        }
        .gift-bow {
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 3rem;
            z-index: 4;
        }
        .gift-box-wrap.open .gift-lid {
            transform: rotateX(-110deg);
        }
        .gift-heart {
            position: absolute;
            font-size: 1.5rem;
            pointer-events: none;
            animation: giftHeartFly 2.5s ease-out forwards;
            opacity: 0;
        }
        @keyframes giftHeartFly {
            0% { opacity: 1; transform: translateY(0) scale(1); }
            100% { opacity: 0; transform: translateY(-180px) scale(1.5); }
        }

        /* 爱豆照片弹窗 */
        #idolPhotoModal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.75);
            z-index: 9999;
            align-items: center;
            justify-content: center;
            cursor: pointer;
        }
        #idolPhotoImg {
            max-width: 90vw;
            max-height: 85vh;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            object-fit: contain;
        }
    </style>
</head>
<body>

<audio id="bgAudio" loop></audio>
<audio id="idolAudio"></audio>

<!-- 登录界面 -->
<div class="login-screen" id="loginScreen">
    <div class="login-box">
        <div class="login-avatar"></div>
        <div class="login-id">Cui Shi ya</div>
        <div class="login-hint">Welcome to my personal website.<br>If you want to know more, please click Enter.</div>
        <input type="text" class="login-input" id="usernameInput" placeholder="账号">
        <input type="password" class="login-input" id="passwordInput" placeholder="密码">
        <button class="login-btn" id="loginBtn">Enter</button>
        <p class="login-error" id="loginError">账号或密码错误</p>
    </div>
</div>

<!-- 生日动画屏幕 -->
<div class="birthday-screen" id="birthdayScreen">
    <div class="confetti-container" id="confettiContainer"></div>
    <div id="fireworkLayer" style="position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:1;"></div>

    <span class="floating-emoji" style="top:5%; left:5%;">🌟</span>
    <span class="floating-emoji" style="top:15%; left:20%; animation-delay:0.5s;">🎀</span>
    <span class="floating-emoji" style="top:10%; right:10%; animation-delay:1s;">🐾</span>
    <span class="floating-emoji" style="top:30%; left:2%; animation-delay:1.5s;">💖</span>
    <span class="floating-emoji" style="top:45%; right:8%; animation-delay:0.8s;">🌸</span>
    <span class="floating-emoji" style="top:60%; left:7%; animation-delay:2.2s;">🎈</span>
    <span class="floating-emoji" style="top:75%; right:15%; animation-delay:1.3s;">✨</span>
    <span class="floating-emoji" style="top:85%; left:25%; animation-delay:0.3s;">🍀</span>
    <span class="floating-emoji" style="top:12%; left:70%; animation-delay:1.8s;">🐶</span>
    <span class="floating-emoji" style="top:50%; left:45%; animation-delay:0.7s;">🎵</span>
    <span class="floating-emoji" style="top:22%; right:30%; animation-delay:2.5s;">💎</span>
    <span class="floating-emoji" style="top:80%; right:35%; animation-delay:1.1s;">🏵️</span>
    <span class="floating-emoji" style="top:40%; left:80%; animation-delay:0.4s;">🎁</span>

    <div class="cd-container">
        <div class="cd-disc">
            <div class="cd-text">
                <div class="cn-birthday">生日快乐</div>
                <div class="en-birthday">Happy Birthday</div>
                <div class="birthday-date">2006 · 09 · 18</div>
            </div>
        </div>
    </div>
    <div class="birthday-msg">🎂 崔诗雅 · 永远闪闪发光 🎂</div>
    <button class="skip-birthday" id="skipBirthday">进入小宇宙 →</button>
</div>

<!-- 主站内容 -->
<div id="mainSite">
    <nav class="navbar" id="navbar">
        <div class="navbar-inner">
            <a href="#hero" class="nav-logo"><span class="logo-dot"></span> 诗雅的小宇宙</a>
            <button class="nav-toggle" id="navToggle" aria-label="菜单">☰</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="#about">关于她</a></li>
                <li><a href="#timeline">时间轴</a></li>
                <li><a href="#gallery">美照</a></li>
                <li><a href="#idol">爱豆</a></li>
                <li><a href="#wishes">愿望</a></li>
                <li><a href="#memories">回忆</a></li>
                <li><a href="#heartfelt">心里话</a></li>
            </ul>
        </div>
    </nav>
    <div class="main-container">
        <!-- HERO -->
        <section class="hero fade-in" id="hero">
            <div class="hero-avatar"><img src="/static/touxiang.jpg" alt="崔诗雅"></div>
            <div class="hero-content">
                <p class="hero-greeting">💫 我最好的朋友</p>
                <h1 class="hero-name">崔诗雅</h1>
                <p class="hero-desc">拥有强大的精神世界，总是积极阳光地面对任何事情，理性与温暖在她身上奇妙共存，像一只永远摇着尾巴的快乐小狗，把阳光洒进每个人的角落。正所谓“灯塔不灭，精神不死”</p>
                <div class="hero-badges">
                    <span class="hero-badge">🧩 ENFP · 快乐小狗</span>
                    <span class="hero-badge">🌟 处女座 · 土象</span>
                    <span class="hero-badge">🎂 生日：9月18日</span>
                </div>
            </div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 关于她 -->
        <section class="section fade-in" id="about">
            <div class="section-header">
                <span class="section-tag">ABOUT HER</span>
                <h2 class="section-title">关于她 <span class="emoji">💌</span></h2>
                <p class="section-subtitle">用她自己的话认识她</p>
            </div>
            <div class="about-grid">
                <div class="about-intro">
                    <h4>📝 她的自述</h4>
                    <p>嗨！我是崔诗雅。<br>朋友们都说我像一只停不下来的快乐小狗——没错，我对世界永远好奇，脑子里同时运行着十个平行宇宙。我喜欢把看似不相关的东西拼接成新创意，也喜欢在深夜和好友聊人生聊到忘记时间。<br>处女座的强迫症让我容忍不了错别字和凌乱的书桌，但 ENFP 的自由魂又让我讨厌按部就班。我的梦想？也许明天会变，但此刻是：和最好的朋友一起，把每一个平凡日子都过成冒险。</p>
                </div>
                <div class="about-card mbti-card">
                    <span class="about-card-icon">🧩</span>
                    <span class="about-card-label">MBTI 人格</span>
                    <p class="about-card-value">ENFP</p>
                    <p class="about-card-desc">竞选者 · 热情洋溢的造梦师。<br>对世界保持童真，对朋友掏心掏肺。总是能在无聊中找到乐趣，在绝望中种下希望。</p>
                </div>
                <div class="about-card zodiac-card">
                    <span class="about-card-icon">🌟</span>
                    <span class="about-card-label">星座</span>
                    <p class="about-card-value">处女座 ♍</p>
                    <p class="about-card-desc">土象的温柔完美主义者。<br>理性与感性交织，挑剔是因为在乎。她的细致让天马行空的想象力稳稳落地。</p>
                </div>
            </div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 时间轴 -->
        <section class="section fade-in" id="timeline">
            <div class="section-header">
                <span class="section-tag">TIMELINE</span>
                <h2 class="section-title">她的时间轴 <span class="emoji">⏳</span></h2>
                <p class="section-subtitle">那些闪闪发光的重要时刻</p>
            </div>
            <div class="timeline">
                <div class="timeline-item fade-in"><span class="timeline-year">🎀 2006年9月18日</span><h4 class="timeline-title">来到这个世界的日子</h4><p class="timeline-desc">一个在秋天出生的处女座女孩，从第一声啼哭就带着对世界的好奇。每年的这一天，蛋糕和鬼马点子都会一起登场。</p></div>
                <div class="timeline-item fade-in"><span class="timeline-year">🤝 相遇那年：2014年</span><h4 class="timeline-title">我们的故事开始</h4><p class="timeline-desc">她顶着独特的短发走进教室，在厕所我们意外地碰头，一声“啊”从此介入进彼此的生活。</p></div>
                <div class="timeline-item fade-in"><span class="timeline-year">💎 十周年</span><h4 class="timeline-title">友谊十周年纪念</h4><p class="timeline-desc">我们无数次写下“以后一定要一起生活，一起工作”。虽然到现在还没实现，但不远了对吗？十周年我们一起幸福地过了一个盛大的纪念日，“Time will prove love”</p></div>
                <div class="timeline-item future-node fade-in"><span class="timeline-year">🚀 2026</span><h4 class="timeline-title">一起踏上新旅程</h4><p class="timeline-desc">我们约定，2026年还要一起去干很多事，去旅行，去看演唱会，去提升遇见更好的自己，去继续书写属于我们的下一章。</p></div>
            </div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 照片墙 -->
        <section class="section fade-in" id="gallery">
            <div class="section-header">
                <span class="section-tag">GALLERY</span>
                <h2 class="section-title">她的美照 <span class="emoji">📸</span></h2>
                <p class="section-subtitle">每一帧都是心动的瞬间 · 自动翻页或手动切换</p>
            </div>
            <div class="gallery-controls">
                <button class="gallery-nav-btn" id="prevPageBtn"><span>◀</span></button>
                <div class="gallery-pages-container" id="galleryPages"></div>
                <button class="gallery-nav-btn" id="nextPageBtn"><span>▶</span></button>
            </div>
            <div class="gallery-dots" id="galleryDots"></div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 爱豆 -->
        <section class="section fade-in" id="idol">
            <div class="section-header">
                <span class="section-tag">HER IDOLS</span>
                <h2 class="section-title">那些年犯过的花痴 <span class="emoji">💖</span></h2>
                <p class="section-subtitle">让她眼里有星星的人</p>
            </div>
            <div class="idol-grid">
                <div class="idol-card" onclick="toggleIdolMedia(0)">
                    <div class="idol-img">
                        <span>🎤</span>
                    </div>
                    <p class="idol-name">薛之谦</p>
                    <p class="idol-tag">歌手/演员</p>
                </div>

                <div class="idol-card" onclick="toggleIdolMedia(1)">
                    <div class="idol-img">
                        <span>🌟</span>
                    </div>
                    <p class="idol-name">博君一肖</p>
                    <p class="idol-tag">cp</p>
                </div>
            </div>
        </section>

        <!-- 爱豆照片弹窗 -->
        <div id="idolPhotoModal" onclick="closeIdolMedia()">
            <img id="idolPhotoImg" src="">
        </div>

        <div class="divider-dots">• • •</div>
        <!-- 愿望清单 -->
        <section class="section fade-in" id="wishes">
            <div class="section-header">
                <span class="section-tag">WISH LIST</span>
                <h2 class="section-title">她的愿望清单 <span class="emoji">🎈</span></h2>
                <p class="section-subtitle">每一个愿望都值得被认真对待</p>
            </div>
            <div class="wishlist">
                <div class="wish-card fade-in"><span class="wish-emoji">😎</span><div><p class="wish-text">接发！！！刻不容缓！！！</p><span class="wish-status pending">✨ 待实现</span></div></div>
                <div class="wish-card fade-in"><span class="wish-emoji">🙂</span><div><p class="wish-text">削骨？真的假的？</p><span class="wish-status pending">✨ 待实现</span></div></div>
                <div class="wish-card fade-in"><span class="wish-emoji">🎤</span><div><p class="wish-text">去每一场演唱会见小值钱~</p><span class="wish-status pending">✨ 马上实现</span></div></div>
                <div class="wish-card fade-in"><span class="wish-emoji">🐶</span><div><p class="wish-text">想谈恋爱是你阶段性的愿望</p><span class="wish-status pending">✨ 可实现</span></div></div>
            </div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 回忆 -->
        <section class="section fade-in" id="memories">
            <div class="section-header">
                <span class="section-tag">MEMORIES</span>
                <h2 class="section-title">我们的回忆 <span class="emoji">🫧</span></h2>
                <p class="section-subtitle">那些笑过、哭过、一起走过的日子</p>
            </div>
            <div class="memories-grid">
                <div class="memory-card fade-in"><p class="memory-date">📅 一起吃的每一顿饭，看的每一场电影</p><p class="memory-text">“菜上完了吗？饿死了，先吃吧”“票根！！！拍照！！这样好看!!!”</p></div>
                <div class="memory-card fade-in"><p class="memory-date">📅 每个互相治愈的深夜</p><p class="memory-text">”因为各种各样的烦心琐事情绪崩溃，我们互相开导对方，治愈彼此”</p></div>
                <div class="memory-card fade-in"><p class="memory-date">📅 一起走过的每一座城市</p><p class="memory-text">“山西，太原，威海，菏泽...以后还要走更多”</p></div>
                <div class="memory-card ten-years fade-in"><span class="memory-emoji">💎</span><p class="memory-date">🎉 十周年纪念</p><p class="memory-text" style="font-family:var(--font-quote);font-size:1.05rem;font-style:italic;">“十年了，我们是彼此青春的见证人。无论未来多远，你永远是我计划里最重要的一环。”</p></div>
            </div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 心里话 -->
        <section class="section fade-in" id="heartfelt">
            <div class="section-header">
                <span class="section-tag">WORDS FROM HEART</span>
                <h2 class="section-title">心里话 <span class="emoji">💌</span></h2>
            </div>
            <div class="quote-block fade-in">
                <p class="quote-label">✍️ 我想对你说</p>
                <p class="quote-text">“亲爱的帕拉斯弈星，<br>无论发生什么事，一定一定不要对自己失望，也一定一定要告诉我，因为什么都不知道你我会很焦急，帮不到你我也会很难过。<br>每件事可能都不可能百分之百圆满或完美，但一定有这样发生的理由。<br>不管你做什么，我都支持你。”</p>
            </div>
            <div class="quote-block heartfelt fade-in">
                <p class="quote-label">💎 最后的最后</p>
                <p class="quote-text">“谢谢你，只有你“<br>（对了，你知道帕拉斯弈星的意思吗？和艺术生对缪斯女神差不多）”</p>
            </div>
        </section>
        <div class="divider-dots">• • •</div>
        <!-- 音乐角落 -->
        <section class="section fade-in" id="music">
            <div class="section-header">
                <span class="section-tag">MUSIC</span>
                <h2 class="section-title">音乐角落 <span class="emoji">🎵</span></h2>
                <p class="section-subtitle">点击CD播放，与播放器同步</p>
            </div>
            <div class="music-player" id="musicPlayer">
                <div class="music-cover">
                    <span>🎶</span>
                    <img src="" alt="封面">
                </div>
                <div class="music-info">
                    <p class="music-title" id="musicTitle">歌曲标题</p>
                    <p class="music-artist" id="musicArtist">歌手</p>
                    <div class="music-progress" id="musicProgress"><div class="music-progress-fill" id="musicProgressFill"></div></div>
                </div>
                <div class="music-controls">
                    <button class="music-btn" id="musicPrev">⏮️</button>
                    <button class="music-btn play-btn" id="musicPlay">▶️</button>
                    <button class="music-btn" id="musicNext">⏭️</button>
                </div>
            </div>
            <div class="cd-wall" id="cdWall"></div>
        </section>
        <div class="divider-dots">• • •</div>

        <!-- 视频 -->
        <section class="section fade-in" id="video">
            <div class="section-header">
                <span class="section-tag">VIDEO</span>
                <h2 class="section-title">珍贵影像 <span class="emoji">🎬</span></h2>
                <p class="section-subtitle">点击播放，重温美好瞬间</p>
            </div>
            <div class="video-wrapper">
                <video id="videoElement" controls width="100%" style="width:100%;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,0.1);"></video>
            </div>
        </section>

        <!-- 礼物盒模块 -->
        <div class="divider-dots">• • •</div>
        <section class="section fade-in">
            <div class="gift-section">
                <div class="section-title">💌 最后送你的礼物</div>
                <div style="margin:1rem auto 2rem; color:#888;">点击礼物盒打开惊喜</div>

                <div class="gift-box-wrap" id="giftBox">
                    <div class="gift-box">
                        <div class="gift-lid"></div>
                        <div class="gift-ribbon"></div>
                        <div class="gift-bow">🎀</div>
                    </div>
                </div>

                <br><br>
                <button onclick="openLetter()" 
                style="padding: 12px 32px;
                       border:none;
                       border-radius: 30px;
                       background: linear-gradient(135deg, #f8d7e4, #f6c2d1);
                       color: #fff;
                       font-size: 16px;
                       font-weight: bold;
                       cursor: pointer;
                       transition: all 0.3s ease;
                       box-shadow: 0 6px 15px rgba(240, 140, 170, 0.25);
                       text-shadow: 0 1px 2px rgba(0,0,0,0.1);"
                onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(240, 140, 170, 0.35)';"
                onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 6px 15px rgba(240, 140, 170, 0.25)';">
                💌 打开礼物
                </button>

                <div id="letterModal" 
                style="display: none;
                       position: fixed;
                       top: 50%;
                       left: 50%;
                       transform: translate(-50%, -50%) scale(0.7);
                       opacity: 0;
                       width: 90%;
                       max-width: 620px;
                       max-height: 80vh;
                       padding: 35px 30px;
                       background: #fff8fa;
                       border-radius: 18px;
                       overflow-y: auto;
                       line-height: 1.9;
                       font-size: 15px;
                       z-index: 9999;
                       transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1.2);
                       box-shadow: 0 15px 40px rgba(0,0,0,0.15);">

                    <button style="position: absolute;top: 18px;right: 20px;border:none;background:transparent;font-size: 26px;cursor:pointer;color:#999;" onclick="closeLetter()">×</button>
                    <div class="letter-title" style="text-align:center;font-size:18px;font-weight:bold;margin-bottom:20px;color:#d6336c;">致My Love</div>

                    一直要说给你做一个属于你自己的网站，可是总是咯吱咯吱在何止（哈哈哈什么破输入法）是搁置搁置再搁置，因为这是一个不小的工程，需要做框架，存照片，选歌曲，写文案，排版，加创意，回忆，原本以为我会放弃，毕竟要做的东西太多了，又怕匆匆做完是不完美的，所以迟迟没有开始。<br><br>
                    一开始有这个念头，诚实说是一时兴起，因为当时在学这个，想说我要给我的好闺闺做一个！独一无二的，独属于她自己的网站，我要看到她幸福的样子，我想只要看到，再麻烦我也不怕。我总是想对你好一点再好一点，总怕对你不够好你就会不开心不幸福，我感觉我好像一点也不能接受这样的你，只要你開心幸福，我就开心，幸福。<br><br>
                    于是我开始行动。第一步就遇到了难题。我做网页的软件找不到了，真的很神奇，我并没有删它，它却这样悄悄地消失在我的电脑…（呜呜呜），没办法我只好找我身边的舍友要，哎后面的事你也知道了，发生了一些不好的事情，没事儿，第二天上课的时候，我故意没给她打开电脑嘻嘻让她手忙脚乱地上了第一节课hhhh但是后面她给我要上节课的文件，我还是不懂得拒绝，说我心软也好，还是没脾气，哎我好像总是对外好说话，却对最亲近的人“伤害”最深。<br><br>
                    没关系，最后还是完美解决了这个问题，我换了个软件，一开始写好的框架也变了种语言，看着处处要我填满的文字，照片，歌曲，特效，我感觉这就是包装礼物的过程呀，一点点把准备好的东西放进去，缠上丝带，设置上你的专属密码，完美的组装成一份独属于你自己的礼物。我感觉我都能想象到你看到这份惊喜的样子，会哭吗？还是会啊啊啊大叫？还是会愣在那里？我好像只顾自己一股脑的送出去就什么也不管了，完全不顾你的死活哈哈哈哈哈<br><br>
                    嗯，我的照片好像也没有多少，虽然你一直给我发一些搞怪的照片，完全没有偶像包袱一样一股脑的塞给我，最有趣的是，每次见完面，我总是会在我的手机相册里找到你偷偷留给我的“小惊喜”，总是趁我不注意把你的分身封印进我的手机，那种事后发现的乐趣，好像吃了最好吃的糖一样，甜滋滋的！我只找了一些，你偶像包袱最重的照片，换句话说是最装的样子，那些非常搞怪的样子我没放上去，我怕你会哭着哭着突然笑出来，也怕某一天万一有闲的蛋疼的黑客莫名其妙黑了我的网站，万一看到你这样的照片自戳双目怎么办？如果都是美照，我想还是亮瞎他的狗眼比较好！！！嘿嘿<br><br>
                    啊啊啊啊啊啊啊啊啊啊啊怎么让你写一段自己是个什么样的人啊？难道要在一个夜深人静的时候，给你来一场灵魂上的交流吗？其他地方我没有写太多文字，还好我的电脑一直不会关机，不然一直运行着，没有保存，万一某天突然全部消失了我找谁哭去！！！<br><br>
                    开始选音乐了，其实，我快高考的那段时间录过三段语音，我原本导到qq音乐上，想拿来做素材的，但是不知道为什么这个手机没法听。。。没办法了，哈哈也没啥有营养的内容，就是一些碎碎念。算了算了。我去抖音搜了一些处女座土象四部曲，不太满意，感觉有点不符合此时此刻，最后我想去偷偷观察你的歌单，我记得你有分享歌曲的习惯，（呜呜🥺）你怎么可以这样🥹🥹🥹🥹猜猜我发现了什么？呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜我看到你给我写的了，网易云我几乎没有打开过，因为不常用，但是我今天打开了，看到了你写的那段话，🥹🥹🥹如果我没有打开，没有去找，你是不是一辈子都不告诉我，我也永远都不知道你写过这个，，呜呜呜我眼睛要尿尿了，好感动，下午不想去上课了，原来我是这么又傻又可爱的小女孩儿吗？🤔关于让座的问题，嗯…我确实是这么想的，现实也正如你所说…我总是发一些莫名其妙的东西，别人都会觉得幼稚，无聊，都会因为一些事情忽略不见，只有你认真回答，一点也不敷衍，虽然我傻傻的呆呆的，但是只有在你这里，我才能轻松做自己。<br><br>
                    完了我也要爱你一辈子了，网上都说时间是给一个人最好的礼物，我一直给你送这些手工，就是想给你好多好多爱，弥补你缺失的所有的爱，填补你的缝隙，虽然你很强大，但也有破碎的时候，值得庆幸的是，你愿意让我看到自己破碎的那一面，我这个又傻又呆的小🐟，会一片一片捡起这些碎片，帮你拼好，这片重要，那片也不能少<br><br>
                    为什么？？？？我的电脑你快点振作起来吧！！！我需要你呀！！！你补药离开我啊，你怎么黑屏噜？我需要重启吗？别这样，我不想这样对你……你快点起来战斗啊！！！！！！<br><br>
                    制作快到尾声了，这段时间里，我空了就打开电脑，每次修改都是两个小时起步，每次运行，这些内容我都会从头到尾看一遍，这些东西我看了不下一百次，总是会觉得这里不够好，那里也不是特别完美，总是会想你喜欢吗？哪种风格是你的最爱？这份礼物会走进你的心吗？其实我知道你是个爱丢东西，大大咧咧的女生，但是当我看到我送你的东西你都好好保存着，我真的！特别！特别！说不上来，好感动，我们都有好好对待彼此。很幸运，我们能在茫茫人海中遇见彼此，成为朋友，成为家人，你说infj是最好的，其实你也是最好的，你对我来说就是苏轼与之张怀民，想你的时候，你必须是张怀民，至于是不是赏月不重要，在雨中奔跑也很洒脱。至于只有我一个人的时候，可能会突然半夜出门，去看一场日出，但我不会赏月了。因为，赏月，我们，二者缺一不可。<br><br>
                    世界如此辽阔 爱如此浅薄<br><br>
                    谢谢你的出现，谢谢你成为我的帕拉斯弈星
                </div>
            </div>
        </section>
    </div>
    <footer class="site-footer">
        <p>致 <span class="footer-year">崔诗雅</span> —— 我最好的朋友</p>
        <p>用 <span class="footer-heart">❤️</span> 精心制作 · 我们的故事未完待续</p>
    </footer>
</div>

<div class="lightbox" id="lightbox">
    <button class="lightbox-close" id="lightboxClose">&times;</button>
    <img src="" alt="照片放大查看" id="lightboxImg">
</div>

<script>
    const idolMediaConfig = [
        { audio: "/static/薛1(1).m4a", photo: "/static/xuezhiqian.jpg" },
        { audio: "/static/bx(1).m4a", photo: "/static/bjyixiao.jpg" }
    ];

    let currentPlayingIndex = -1;
    const bgAudio = document.getElementById('bgAudio');
    const idolAudio = document.getElementById('idolAudio');
    const idolPhotoModal = document.getElementById('idolPhotoModal');
    const idolPhotoImg = document.getElementById('idolPhotoImg');

    function toggleIdolMedia(index) {
        const wasBgPlaying = !bgAudio.paused;

        if (currentPlayingIndex === index) {
            idolAudio.pause();
            idolPhotoModal.style.display = 'none';
            currentPlayingIndex = -1;
            if (wasBgPlaying) bgAudio.play();
            return;
        }

        bgAudio.pause();
        const config = idolMediaConfig[index];
        idolAudio.src = config.audio;
        idolAudio.play().catch(err => console.log("音频播放失败：", err));

        idolPhotoImg.src = config.photo;
        idolPhotoModal.style.display = 'flex';
        currentPlayingIndex = index;
    }

    function closeIdolMedia() {
        idolAudio.pause();
        idolPhotoModal.style.display = 'none';
        if (bgAudio.paused) bgAudio.play().catch(()=>{});
        currentPlayingIndex = -1;
    }

    let isMusicActivated = false;

    window.addEventListener('DOMContentLoaded', () => {
        playBgMusic('/static/dating_myself.mp3');
        const video = document.getElementById('videoElement');
        video.src = "/static/0513-03.mp4";
    });

    document.addEventListener('click', (e) => {
        if (e.target.id === 'loginBtn') return;
        if (!isMusicActivated) {
            isMusicActivated = true;
            bgAudio.play().catch(() => {});
        }
    });

    function playBgMusic(src) {
        bgAudio.src = src;
        if (isMusicActivated) {
            bgAudio.play().catch(() => {});
        }
    }

    (function() {
        document.getElementById('loginBtn').addEventListener('click', () => {
            const user = document.getElementById('usernameInput').value.trim();
            const pass = document.getElementById('passwordInput').value.trim();
            if (user === 'cuishiya' && pass === '20060918') {
                document.getElementById('loginScreen').style.display = 'none';
                document.getElementById('birthdayScreen').style.display = 'flex';
                playBgMusic('/static/生日快乐-SING女团.mp3');
                spawnConfetti();
                startFireworks();
            } else {
                document.getElementById('loginError').style.display = 'block';
            }
        });

        document.getElementById('skipBirthday').addEventListener('click', () => {
            enterMainSite();
        });

        setTimeout(() => {
            if (document.getElementById('birthdayScreen').style.display === 'flex') {
                enterMainSite();
            }
        }, 5000);

        function enterMainSite() {
            document.getElementById('birthdayScreen').style.display = 'none';
            document.getElementById('mainSite').style.display = 'block';
            playBgMusic('/static/Angel-陶喆.mp3');
            initMainSite();
        }
    })();

    function spawnConfetti() {
        const container = document.getElementById('confettiContainer');
        const colors = ['#ff6b6b','#ffd93d','#6bcb77','#4d96ff','#ff8fe0','#fc7a1e','#9b5de5'];
        for (let i = 0; i < 80; i++) {
            const piece = document.createElement('div');
            piece.className = 'confetti-piece';
            piece.style.left = Math.random() * 100 + '%';
            piece.style.background = colors[Math.floor(Math.random() * colors.length)];
            piece.style.animationDuration = (Math.random() * 3 + 3) + 's';
            piece.style.animationDelay = Math.random() * 2 + 's';
            piece.style.width = (Math.random() * 8 + 6) + 'px';
            piece.style.height = (Math.random() * 25 + 15) + 'px';
            container.appendChild(piece);
        }
    }

    function startFireworks() {
        const layer = document.getElementById('fireworkLayer');
        function createFirework() {
            const firework = document.createElement('div');
            firework.className = 'firework';
            const x = Math.random() * 100;
            const y = Math.random() * 80 + 10;
            firework.style.left = x + '%';
            firework.style.top = y + '%';
            const size = Math.random() * 80 + 50;
            firework.style.width = size + 'px';
            firework.style.height = size + 'px';
            firework.style.background = `radial-gradient(circle, #fff, #ff69b4, #ffd700, transparent)`;
            layer.appendChild(firework);
            for (let i=0;i<12;i++) {
                const particle = document.createElement('div');
                particle.className = 'firework-particle';
                particle.style.left = '50%';
                particle.style.top = '50%';
                const angle = (i / 12) * Math.PI * 2;
                const dist = 40 + Math.random()*40;
                particle.style.setProperty('--tx', Math.cos(angle)*dist + 'px');
                particle.style.setProperty('--ty', Math.sin(angle)*dist + 'px');
                particle.style.background = ['#ff6b6b','#ffd700','#ff8fe0','#4d96ff'][Math.floor(Math.random()*4)];
                firework.appendChild(particle);
            }
            setTimeout(() => firework.remove(), 1500);
        }
        setInterval(createFirework, 1200);
    }

    let giftOpened = false;
    const giftBox = document.getElementById('giftBox');
    giftBox.addEventListener('click', () => {
        if(giftOpened) return;
        giftOpened = true;
        giftBox.classList.add('open');
        for(let i=0;i<12;i++){
            let h = document.createElement('div');
            h.innerText = '💖';
            h.className = 'gift-heart';
            h.style.left = Math.random()*80 + 10 + '%';
            h.style.top = Math.random()*40 + 40 + 'px';
            giftBox.appendChild(h);
        }
    });

    let mainSiteReady = false;
    let currentSongIndex = 0;
    let cdWallSongs = [];
    let currentCdCover = null;
    let userPlayed = false;

    function initMainSite() {
        if (mainSiteReady) return;
        mainSiteReady = true;

        cdWallSongs = [
            { title:"匿名的朋友", artist:"杨丞琳", lyric:"不能握的手 从此匿名的朋友", src:"/static/匿名的好友-杨丞琳.mp3", cover:"/static/cd1.jpg" },
        { title:"My Love", artist:"田馥甄", lyric:"My love 我看见了 你的笑容", src:"/static/My_Love-田馥甄.mp3", cover:"/static/cd2.jpg" },
        { title:"小幸运", artist:"田馥甄", lyric:"原来你是我最想留住的幸运", src:"/static/小幸运-田馥甄.mp3", cover:"/static/cd3.jpg" },
        { title:"Honey Honey", artist:"孙燕姿", lyric:"Honey Honey 要对你说声对不起", src:"/static/Honey_Honey-孙燕姿.mp3", cover:"/static/cd4.jpg" },
        { title:"心墙", artist:"林俊杰", lyric:"你的心有一道墙 但我发现一扇窗", src:"/static/心墙-林俊杰.mp3", cover:"/static/cd5.jpg" },
        { title:"遇见", artist:"孙燕姿", lyric:"我遇见谁 会有怎样的对白", src:"/static/遇见-孙燕姿.mp3", cover:"/static/cd6.jpg" },
        { title:"带我走", artist:"杨丞琳", lyric:"带我走 到遥远的以后", src:"/static/带我走-杨丞琳.mp3", cover:"/static/cd7.jpg" },
        { title:"陪你去流浪", artist:"薛之谦", lyric:"快告诉我 你在赶来的路上", src:"/static/陪你去流浪-薛之谦.mp3", cover:"/static/cd8.jpg" }
        ];
        const navToggle = document.getElementById('navToggle');
        const navLinks = document.getElementById('navLinks');
        navToggle.addEventListener('click', () => navLinks.classList.toggle('active'));
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.navbar')) navLinks.classList.remove('active');
        });
        navLinks.querySelectorAll('a[href^="#"]').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const target = document.getElementById(targetId);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                    setTimeout(() => {
                        target.classList.add('bounce-once');
                        setTimeout(() => target.classList.remove('bounce-once'), 600);
                    }, 600);
                }
                navLinks.classList.remove('active');
            });
        });

        const fadeElements = document.querySelectorAll('.fade-in');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
        fadeElements.forEach(el => observer.observe(el));

        function spawnEffect(x, y, type = 'heart', count = 8) {
            const emojiSets = {
                heart: ['❤️','💕','💖','💘','💝'],
                star: ['✨','⭐','🌟','💫'],
                note: ['🎵','🎶','♫','♪'],
                sparkle: ['✨','💖','🌸','🌷']
            };
            const items = emojiSets[type] || emojiSets.heart;
            for (let i = 0; i < count; i++) {
                const particle = document.createElement('span');
                particle.className = 'particle';
                particle.textContent = items[Math.floor(Math.random() * items.length)];
                particle.style.left = x + 'px';
                particle.style.top = y + 'px';
                const angle = (Math.PI * 2 * i) / count;
                const distance = 30 + Math.random() * 60;
                particle.style.setProperty('--tx', Math.cos(angle) * distance + 'px');
                particle.style.setProperty('--ty', Math.sin(angle) * distance - 20 - Math.random() * 30 + 'px');
                particle.style.animationDuration = (0.8 + Math.random() * 0.6) + 's';
                document.body.appendChild(particle);
                particle.addEventListener('animationend', () => particle.remove());
            }
        }

        const clickEffectRules = [
            { selector: '.hero-avatar', type: 'heart', count: 14 },
            { selector: '.gallery-photo-card', type: 'star', count: 10 },
            { selector: '.music-btn', type: 'note', count: 8 },
            { selector: '.idol-card', type: 'star', count: 8 },
            { selector: '.memory-card', type: 'heart', count: 8 },
            { selector: '.wish-card', type: 'sparkle', count: 6 },
            { selector: '.quote-block', type: 'heart', count: 8 },
            { selector: '.about-card', type: 'sparkle', count: 6 },
            { selector: '.about-intro', type: 'sparkle', count: 6 },
            { selector: '.timeline-item', type: 'star', count: 6 },
            { selector: '.video-wrapper', type: 'sparkle', count: 8 }
        ];
        document.addEventListener('click', (e) => {
            for (let rule of clickEffectRules) {
                if (e.target.closest(rule.selector)) {
                    spawnEffect(e.clientX, e.clientY, rule.type, rule.count);
                    break;
                }
            }
        });

        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightboxImg');
        const lightboxClose = document.getElementById('lightboxClose');
        lightboxClose.addEventListener('click', () => lightbox.classList.remove('active'));
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) lightbox.classList.remove('active');
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') lightbox.classList.remove('active');
        });

        // 照片墙
        (function() {
            const photoList = [
                "1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg",
                "11.jpg","12.jpg","13.jpg","14.jpg","15.jpg","16.jpg","17.jpg","18.jpg","19.jpg","20.png",
                "21.jpg","22.jpg","23.jpg","24.jpg","25.jpg","26.jpg","27.jpg","28.jpg","29.jpg","30.jpg",
                "31.jpg","32.jpg","33.jpg","34.jpg","35.jpg","36.jpg","71.jpg","38.jpg","39.jpg","40.jpg",
                "41.jpg","42.jpg","43.jpg","44.jpg","45.jpg","46.jpg","47.jpg","48.jpg","49.jpg","50.jpg",
                "51.jpg","52.jpg","53.jpg","54.jpg","55.jpg","56.jpg","57.jpg","58.jpg","59.jpg","60.jpg",
                "61.jpg","62.jpg","63.jpg","64.jpg","65.jpg","66.jpg","67.jpg","68.jpg","69.jpg","70.jpg",
                "72.jpg","73.jpg","74.jpg","75.jpg","76.jpg","77.jpg","78.jpg","79.jpg","80.jpg","81.jpg",
                "82.jpg","83.jpg","84.jpg","85.jpg","86.jpg"
            ];
            const PER_PAGE = 10;
            const totalPages = Math.ceil(photoList.length / PER_PAGE);
            let currentPage = 0, autoTimer;
            const container = document.getElementById('galleryPages');
            const dotsContainer = document.getElementById('galleryDots');
            const prevBtn = document.getElementById('prevPageBtn');
            const nextBtn = document.getElementById('nextPageBtn');
            for (let i = 0; i < totalPages; i++) {
                const dot = document.createElement('span');
                dot.className = 'gallery-dot';
                dot.dataset.page = i;
                dot.addEventListener('click', () => goToPage(i));
                dotsContainer.appendChild(dot);
            }
            function renderPage(pageIndex) {
                currentPage = pageIndex;
                container.innerHTML = '';
                const start = pageIndex * PER_PAGE;
                const end = Math.min(start + PER_PAGE, photoList.length);
                const photos = photoList.slice(start, end);
                const positions = [
                    { top:'8%', left:'5%', rotate:'-6deg', zIndex:1 },
                    { top:'15%', left:'35%', rotate:'5deg', zIndex:2 },
                    { top:'5%', left:'65%', rotate:'-3deg', zIndex:3 },
                    { top:'25%', left:'20%', rotate:'8deg', zIndex:4 },
                    { top:'20%', left:'55%', rotate:'-8deg', zIndex:5 },
                    { top:'35%', left:'5%', rotate:'4deg', zIndex:6 },
                    { top:'45%', left:'40%', rotate:'-4deg', zIndex:7 },
                    { top:'40%', left:'70%', rotate:'7deg', zIndex:8 },
                    { top:'60%', left:'15%', rotate:'-5deg', zIndex:9 },
                    { top:'55%', left:'60%', rotate:'2deg', zIndex:10 }
                ];
                photos.forEach((filename, idx) => {
                    const card = document.createElement('div');
                    card.className = 'gallery-photo-card';
                    card.style.width = '180px';
                    card.style.height = '220px';
                    const img = document.createElement('img');
                    img.src = '/static/' + filename;
                    img.alt = '照片';
                    img.loading = 'lazy';
                    card.appendChild(img);
                    const pos = positions[idx % 10];
                    card.style.top = pos.top;
                    card.style.left = pos.left;
                    card.style.transform = `rotate(${pos.rotate})`;
                    card.style.zIndex = pos.zIndex;
                    card.addEventListener('click', (e) => {
                        lightboxImg.src = img.src;
                        lightbox.classList.add('active');
                        e.stopPropagation();
                    });
                    container.appendChild(card);
                });
                document.querySelectorAll('.gallery-dot').forEach((dot,i) => dot.classList.toggle('active', i===pageIndex));
            }
            function goToPage(idx) {
                if (idx < 0 || idx >= totalPages) return;
                renderPage(idx);
                resetAutoPlay();
            }
            function nextPage() { goToPage(currentPage+1 >= totalPages ? 0 : currentPage+1); }
            function prevPage() { goToPage(currentPage-1 < 0 ? totalPages-1 : currentPage-1); }
            function resetAutoPlay() { clearInterval(autoTimer); autoTimer = setInterval(nextPage, 10000); }
            nextBtn.addEventListener('click', nextPage);
            prevBtn.addEventListener('click', prevPage);
            if (photoList.length) { renderPage(0); resetAutoPlay(); }
            let touchStart = 0;
            container.addEventListener('touchstart', e => touchStart = e.changedTouches[0].screenX, {passive:true});
            container.addEventListener('touchend', e => {
                const delta = e.changedTouches[0].screenX - touchStart;
                if (delta > 50) prevPage();
                else if (delta < -50) nextPage();
            });
        })();

        // 👇 视频播放时控制背景音乐（新增部分）
        const videoEl = document.getElementById('videoElement');
        let bgWasPlaying = false;
        videoEl.addEventListener('play', () => {
            bgWasPlaying = !bgAudio.paused;
            if (bgWasPlaying) bgAudio.pause();
        });
        videoEl.addEventListener('pause', () => {
            if (bgWasPlaying && bgAudio.paused) bgAudio.play().catch(() => {});
        });
        videoEl.addEventListener('ended', () => {
            if (bgWasPlaying && bgAudio.paused) bgAudio.play().catch(() => {});
        });

        window.addEventListener('scroll', () => {
            document.getElementById('navbar').style.boxShadow = window.scrollY > 10 ? '0 2px 20px rgba(60,40,30,0.08)' : 'none';
        });
        initMusicPlayer();
    }

    function initMusicPlayer() {
        const audio = new Audio();
        const playBtn = document.getElementById('musicPlay');
        const prevBtn = document.getElementById('musicPrev');
        const nextBtn = document.getElementById('musicNext');
        const titleEl = document.getElementById('musicTitle');
        const artistEl = document.getElementById('musicArtist');
        const coverImg = document.querySelector('.music-cover img');
        const coverIcon = document.querySelector('.music-cover span');
        const progress = document.getElementById('musicProgress');
        const progressFill = document.getElementById('musicProgressFill');
        const cdWall = document.getElementById('cdWall');

        cdWallSongs.forEach((song, idx) => {
            const card = document.createElement('div');
            card.className = 'cd-card';
            card.innerHTML = `
                <div class="cd-cover" data-index="${idx}">
                    <img src="${song.cover}" alt="${song.title}">
                </div>
                <div class="cd-song-title">${song.title}</div>
                <div class="cd-lyric">${song.lyric}</div>
            `;
            card.addEventListener('click', () => playSong(idx));
            cdWall.appendChild(card);
        });

        function playSong(index) {
            if (index < 0 || index >= cdWallSongs.length) return;
            currentSongIndex = index;
            const song = cdWallSongs[index];

            bgAudio.pause();
            if (currentCdCover) currentCdCover.classList.remove('playing');

            audio.src = song.src;
            audio.play().catch(err => console.log(err));
            userPlayed = true;

            titleEl.textContent = song.title;
            artistEl.textContent = song.artist;
            coverImg.src = song.cover;
            coverImg.style.display = 'block';
            coverIcon.style.display = 'none';
            playBtn.innerHTML = '⏸️';

            currentCdCover = document.querySelector(`.cd-cover[data-index="${index}"]`);
            currentCdCover.classList.add('playing');
        }

        playBtn.addEventListener('click', () => {
            if (!userPlayed) {
                playSong(0);
                return;
            }
            if (audio.paused) {
                audio.play();
                playBtn.innerHTML = '⏸️';
                if (currentCdCover) currentCdCover.classList.add('playing');
            } else {
                audio.pause();
                playBtn.innerHTML = '▶️';
                if (currentCdCover) currentCdCover.classList.remove('playing');
            }
        });

        prevBtn.addEventListener('click', () => {
            playSong(currentSongIndex - 1 < 0 ? cdWallSongs.length - 1 : currentSongIndex - 1);
        });

        nextBtn.addEventListener('click', () => {
            playSong(currentSongIndex + 1 >= cdWallSongs.length ? 0 : currentSongIndex + 1);
        });

        audio.addEventListener('timeupdate', () => {
            const percent = (audio.currentTime / audio.duration) * 100;
            progressFill.style.width = percent + '%';
        });

        progress.addEventListener('click', (e) => {
            const rect = progress.getBoundingClientRect();
            const pos = (e.clientX - rect.left) / rect.width;
            audio.currentTime = pos * audio.duration;
        });

        audio.addEventListener('ended', () => {
            playBtn.innerHTML = '▶️';
            if (currentCdCover) currentCdCover.classList.remove('playing');
        });
    }

    function openLetter(){
        const modal = document.getElementById("letterModal");
        modal.style.display = "block";
        setTimeout(() => {
            modal.style.opacity = "1";
            modal.style.transform = "translate(-50%, -50%) scale(1)";
        }, 10);
    }

    function closeLetter(){
        const modal = document.getElementById("letterModal");
        modal.style.opacity = "0";
        modal.style.transform = "translate(-50%, -50%) scale(0.8)";
        setTimeout(() => {
            modal.style.display = "none";
        }, 400);
    }
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_CONTENT

if __name__ == '__main__':
    print("🌐 崔诗雅的小宇宙 · 访问 http://127.0.0.1:5000")
    app.run(debug=True)