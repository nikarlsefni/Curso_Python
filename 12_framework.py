from flask import Flask, render_template_string, render_template

# Criação do app Flask
app = Flask(__name__)

# Rota para a pagina principal
# esse arroba é um decorator
@app.route('/')
def home():
    return "<h1> Bem vindo a minha SuuPeeR pagina <3 </h1>"

# Rota para a pagina sobre!
@app.route('/sobre')
def sobre():
    return render_template_string("""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sobre o Autor | thorfinn</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap');

        :root {
            --bg: #08090e;
            --surface: #11131c;
            --surface2: #171a26;
            --primary: #a78bfa;
            --secondary: #818cf8;
            --text: #f0efff;
            --muted: #9293a8;
            --border: rgba(167,139,250,.15);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            z-index: -2;
            background:
                radial-gradient(ellipse at 15% 15%, rgba(124,58,237,.16), transparent 40%),
                radial-gradient(ellipse at 85% 65%, rgba(99,102,241,.12), transparent 40%),
                radial-gradient(ellipse at 50% 100%, rgba(167,139,250,.08), transparent 45%);
        }

        #particles {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: -1;
        }

        ::selection {
            background: var(--primary);
            color: #08090e;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            width: min(1100px, 90%);
            margin: auto;
        }

        /* NAVBAR */

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 100;
            padding: 20px 0;
            background: rgba(8,9,14,.75);
            backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--border);
        }

        .nav-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            font-family: 'JetBrains Mono', monospace;
            font-size: 19px;
            font-weight: 700;
            color: var(--primary);
        }

        .logo span {
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 28px;
            list-style: none;
        }

        .nav-links a {
            color: var(--muted);
            font-size: 13px;
            transition: .3s;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .status {
            font-size: 11px;
            color: #86efac;
            border: 1px solid rgba(134,239,172,.2);
            background: rgba(134,239,172,.06);
            padding: 8px 13px;
            border-radius: 30px;
        }

        .status i {
            font-size: 8px;
            margin-right: 6px;
            animation: pulse 1.5s infinite;
        }

        /* HERO */

        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding: 140px 0 90px;
        }

        .hero-content {
            max-width: 850px;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            color: var(--primary);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            margin-bottom: 25px;
            padding: 10px 15px;
            border: 1px solid var(--border);
            border-radius: 30px;
            background: rgba(167,139,250,.06);
        }

        .hero h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(48px, 8vw, 88px);
            line-height: 1.05;
            letter-spacing: -5px;
            margin-bottom: 25px;
        }

        .gradient {
            background: linear-gradient(100deg, #c4b5fd, #818cf8, #e879f9);
            background-size: 200%;
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: gradient 5s ease infinite;
        }

        .hero-description {
            max-width: 630px;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.9;
            margin-bottom: 35px;
        }

        .hero-description strong {
            color: white;
        }

        .buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 14px 22px;
            border-radius: 9px;
            font-size: 13px;
            font-weight: 600;
            transition: .3s;
        }

        .btn-primary {
            background: var(--primary);
            color: #100c1b;
        }

        .btn-primary:hover {
            background: #c4b5fd;
            transform: translateY(-4px);
            box-shadow: 0 10px 35px rgba(167,139,250,.2);
        }

        .btn-outline {
            border: 1px solid var(--border);
            color: white;
        }

        .btn-outline:hover {
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-4px);
        }

        .scroll-indicator {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            color: var(--muted);
            font-size: 11px;
            letter-spacing: 2px;
            animation: float 2s infinite;
        }

        /* SECTION */

        section {
            padding: 100px 0;
        }

        .section-label {
            font-family: 'JetBrains Mono', monospace;
            color: var(--primary);
            font-size: 12px;
            margin-bottom: 15px;
        }

        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(30px, 5vw, 48px);
            letter-spacing: -2px;
            margin-bottom: 18px;
        }

        .section-description {
            color: var(--muted);
            line-height: 1.8;
            max-width: 600px;
            font-size: 14px;
        }

        /* ABOUT */

        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin-top: 45px;
        }

        .card {
            background: linear-gradient(145deg, rgba(23,26,38,.9), rgba(13,15,24,.9));
            border: 1px solid var(--border);
            padding: 30px;
            border-radius: 16px;
            transition: .4s;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--primary), transparent);
            transition: .6s;
        }

        .card:hover::before {
            left: 100%;
        }

        .card:hover {
            transform: translateY(-7px);
            border-color: rgba(167,139,250,.4);
            box-shadow: 0 15px 45px rgba(0,0,0,.25);
        }

        .card-icon {
            width: 45px;
            height: 45px;
            border-radius: 12px;
            background: rgba(167,139,250,.12);
            display: grid;
            place-items: center;
            color: var(--primary);
            font-size: 19px;
            margin-bottom: 22px;
        }

        .card h3 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 19px;
            margin-bottom: 13px;
        }

        .card p {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.9;
        }

        /* SKILLS */

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
            margin-top: 45px;
        }

        .skill {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 22px;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            transition: .3s;
        }

        .skill:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
        }

        .skill i {
            font-size: 25px;
            color: var(--primary);
        }

        .skill h4 {
            font-size: 13px;
            margin-bottom: 5px;
        }

        .skill span {
            font-size: 11px;
            color: var(--muted);
        }

        /* JOURNEY */

        .timeline {
            margin-top: 45px;
            border-left: 1px solid rgba(167,139,250,.3);
            padding-left: 30px;
        }

        .timeline-item {
            position: relative;
            padding-bottom: 35px;
        }

        .timeline-item::before {
            content: "";
            position: absolute;
            left: -36px;
            top: 5px;
            width: 11px;
            height: 11px;
            background: var(--primary);
            border-radius: 50%;
            box-shadow: 0 0 15px var(--primary);
        }

        .timeline-item h3 {
            font-size: 16px;
            margin-bottom: 8px;
        }

        .timeline-item p {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.8;
        }

        .timeline-item small {
            display: block;
            font-family: 'JetBrains Mono', monospace;
            color: var(--primary);
            font-size: 10px;
            margin-bottom: 10px;
        }

        /* TERMINAL */

        .terminal {
            margin-top: 45px;
            background: #090b12;
            border: 1px solid var(--border);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 20px 70px rgba(0,0,0,.3);
        }

        .terminal-header {
            padding: 15px 20px;
            background: #151722;
            display: flex;
            align-items: center;
            gap: 7px;
            border-bottom: 1px solid var(--border);
        }

        .dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }

        .red { background: #fb7185; }
        .yellow { background: #fbbf24; }
        .green { background: #4ade80; }

        .terminal-name {
            color: var(--muted);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            margin: auto;
        }

        .terminal-body {
            padding: 28px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            line-height: 2.3;
            overflow-x: auto;
        }

        .code-purple { color: #c4b5fd; }
        .code-green { color: #86efac; }
        .code-gray { color: #777b91; }
        .code-white { color: #f0efff; }

        .cursor {
            display: inline-block;
            width: 7px;
            height: 15px;
            background: var(--primary);
            vertical-align: middle;
            animation: blink 1s infinite;
        }

        /* GITHUB */

        .github-card {
            margin-top: 45px;
            padding: 40px;
            background: linear-gradient(120deg, rgba(124,58,237,.15), rgba(99,102,241,.07));
            border: 1px solid var(--border);
            border-radius: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 25px;
        }

        .github-card h3 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 25px;
            margin-bottom: 12px;
        }

        .github-card p {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.8;
        }

        .github-icon {
            font-size: 65px;
            color: white;
        }

        /* FOOTER */

        footer {
            padding: 35px 0;
            border-top: 1px solid var(--border);
            text-align: center;
            color: var(--muted);
            font-size: 11px;
        }

        footer span {
            color: var(--primary);
        }

        /* ANIMATIONS */

        @keyframes pulse {
            50% { opacity: .3; }
        }

        @keyframes blink {
            50% { opacity: 0; }
        }

        @keyframes float {
            50% { transform: translate(-50%, -10px); }
        }

        @keyframes gradient {
            50% { background-position: 100% 50%; }
        }

        .reveal {
            opacity: 0;
            transform: translateY(35px);
            transition: opacity .8s ease, transform .8s ease;
        }

        .reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }

        #backTop {
            position: fixed;
            bottom: 25px;
            right: 25px;
            width: 43px;
            height: 43px;
            background: var(--primary);
            color: #100c1b;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            opacity: 0;
            pointer-events: none;
            transition: .3s;
            z-index: 99;
        }

        #backTop.show {
            opacity: 1;
            pointer-events: all;
        }

        #backTop:hover {
            transform: translateY(-5px);
        }

        @media(max-width: 750px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                letter-spacing: -3px;
            }

            .about-grid {
                grid-template-columns: 1fr;
            }

            .skills-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .github-card {
                flex-direction: column;
                align-items: flex-start;
            }

            .github-icon {
                display: none;
            }

            section {
                padding: 75px 0;
            }
        }

        @media(max-width: 430px) {
            .skills-grid {
                grid-template-columns: 1fr;
            }

            .terminal-body {
                font-size: 10px;
                padding: 18px;
            }
        }

        @media(prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: .01ms !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
                transition-duration: .01ms !important;
            }

            .reveal {
                opacity: 1;
                transform: none;
            }
        }
    </style>
</head>

<body>

<canvas id="particles"></canvas>

<nav>
    <div class="container nav-content">
        <a href="#" class="logo">&lt;<span>thorfinn</span> /&gt;</a>

        <ul class="nav-links">
            <li><a href="#sobre">Sobre</a></li>
            <li><a href="#interesses">Interesses</a></li>
            <li><a href="#jornada">Jornada</a></li>
            <li><a href="#github">GitHub</a></li>
        </ul>

        <div class="status">
            <i class="fa-solid fa-circle"></i> Em aprendizado
        </div>
    </div>
</nav>

<header class="hero">
    <div class="container hero-content">

        <div class="eyebrow">
            <i class="fa-solid fa-code"></i>
            UM POUCO SOBRE QUEM ESTÁ POR TRÁS DO CÓDIGO
        </div>

        <h1>
            Olá, eu sou<br>
            <span class="gradient">thorfinn.</span>
        </h1>

        <p class="hero-description">
            Sou uma pessoa curiosa, apaixonada por tecnologia e movida
            pela vontade de aprender. Atualmente estou explorando o
            universo da programação com <strong>Python</strong>,
            desenvolvendo minha lógica e dando meus primeiros passos
            no mundo do desenvolvimento.
            <br><br>
            Acredito que cada linha de código representa uma nova
            possibilidade. Ainda estou no começo da jornada, mas
            tenho muitos projetos e ideias pela frente.
        </p>

        <div class="buttons">
            <a href="#sobre" class="btn btn-primary">
                Conheça minha jornada <i class="fa-solid fa-arrow-down"></i>
            </a>

            <a href="https://github.com/nikarlsefni"
               target="_blank" rel="noopener noreferrer"
               class="btn btn-outline">
                <i class="fa-brands fa-github"></i> Meu GitHub
            </a>
        </div>
    </div>

    <div class="scroll-indicator">
        SCROLL PARA EXPLORAR ↓
    </div>
</header>

<section id="sobre">
    <div class="container">

        <div class="reveal">
            <div class="section-label">// 01 — SOBRE MIM</div>
            <h2 class="section-title">Muito além de uma linha de código.</h2>

            <p class="section-description">
                Por trás de cada projeto existe alguém aprendendo,
                experimentando, errando e descobrindo novas maneiras
                de transformar ideias em realidade.
            </p>
        </div>

        <div class="about-grid">

            <div class="card reveal">
                <div class="card-icon">
                    <i class="fa-solid fa-brain"></i>
                </div>
                <h3>Mente curiosa</h3>
                <p>
                    Gosto de aprender coisas novas, entender como as
                    tecnologias funcionam e explorar assuntos diferentes.
                    A curiosidade é uma das minhas maiores motivações.
                </p>
            </div>

            <div class="card reveal">
                <div class="card-icon">
                    <i class="fa-solid fa-terminal"></i>
                </div>
                <h3>Aprendizado constante</h3>
                <p>
                    Estou construindo minha base na programação,
                    estudando Python, praticando lógica e desenvolvendo
                    minhas habilidades passo a passo.
                </p>
            </div>

            <div class="card reveal">
                <div class="card-icon">
                    <i class="fa-solid fa-lightbulb"></i>
                </div>
                <h3>Criatividade</h3>
                <p>
                    Gosto de transformar ideias em projetos e experimentar
                    possibilidades. Acredito que tecnologia e criatividade
                    combinam muito bem.
                </p>
            </div>

            <div class="card reveal">
                <div class="card-icon">
                    <i class="fa-solid fa-rocket"></i>
                </div>
                <h3>Olhar para o futuro</h3>
                <p>
                    Meu objetivo é continuar evoluindo, conhecer novas
                    linguagens e desenvolver projetos cada vez mais
                    interessantes e completos.
                </p>
            </div>

        </div>
    </div>
</section>

<section id="interesses">
    <div class="container">

        <div class="reveal">
            <div class="section-label">// 02 — TECNOLOGIAS E INTERESSES</div>
            <h2 class="section-title">O que me move?</h2>
            <p class="section-description">
                Algumas das áreas que fazem parte dos meus estudos,
                interesses e planos para o futuro.
            </p>
        </div>

        <div class="skills-grid">

            <div class="skill reveal">
                <i class="fa-brands fa-python"></i>
                <div>
                    <h4>Python</h4>
                    <span>Estudando atualmente</span>
                </div>
            </div>

            <div class="skill reveal">
                <i class="fa-brands fa-html5"></i>
                <div>
                    <h4>HTML</h4>
                    <span>Quero aprender</span>
                </div>
            </div>

            <div class="skill reveal">
                <i class="fa-solid fa-code"></i>
                <div>
                    <h4>C++</h4>
                    <span>Interesse futuro</span>
                </div>
            </div>

            <div class="skill reveal">
                <i class="fa-solid fa-palette"></i>
                <div>
                    <h4>Desenho</h4>
                    <span>Criatividade e arte</span>
                </div>
            </div>

            <div class="skill reveal">
                <i class="fa-solid fa-gamepad"></i>
                <div>
                    <h4>Games</h4>
                    <span>Uma das minhas paixões</span>
                </div>
            </div>

            <div class="skill reveal">
                <i class="fa-solid fa-earth-americas"></i>
                <div>
                    <h4>Geopolítica</h4>
                    <span>Interesse por política mundial</span>
                </div>
            </div>

        </div>
    </div>
</section>

<section id="jornada">
    <div class="container">

        <div class="reveal">
            <div class="section-label">// 03 — MINHA JORNADA</div>
            <h2 class="section-title">Tudo começa em algum lugar.</h2>

            <p class="section-description">
                Minha trajetória na tecnologia está apenas começando.
                Cada etapa é uma oportunidade de aprender e evoluir.
            </p>
        </div>

        <div class="timeline">

            <div class="timeline-item reveal">
                <small>01 / FUNDAMENTOS</small>
                <h3>Descobrindo a programação</h3>
                <p>
                    Começando a entender a lógica de programação,
                    os algoritmos e a maneira como os computadores
                    executam instruções.
                </p>
            </div>

            <div class="timeline-item reveal">
                <small>02 / ESTUDOS ATUAIS</small>
                <h3>Explorando Python</h3>
                <p>
                    Estudando Python, praticando exercícios e conhecendo
                    conceitos fundamentais para desenvolver meus
                    primeiros programas.
                </p>
            </div>

            <div class="timeline-item reveal">
                <small>03 / PRÓXIMOS PASSOS</small>
                <h3>HTML, CSS e desenvolvimento web</h3>
                <p>
                    Quero aprofundar meus conhecimentos em desenvolvimento
                    web, aprender a construir interfaces e criar páginas
                    cada vez mais completas.
                </p>
            </div>

            <div class="timeline-item reveal">
                <small>04 / OBJETIVO FUTURO</small>
                <h3>Expandindo horizontes</h3>
                <p>
                    Conhecer C++, desenvolver projetos maiores e continuar
                    explorando diferentes áreas da tecnologia.
                </p>
            </div>

        </div>

    </div>
</section>

<section id="codigo">
    <div class="container">

        <div class="reveal">
            <div class="section-label">// 04 — UM POUCO DE CÓDIGO</div>
            <h2 class="section-title">Minha filosofia de programação.</h2>
            <p class="section-description">
                Não preciso saber tudo agora. Preciso apenas continuar
                aprendendo.
            </p>
        </div>

        <div class="terminal reveal">

            <div class="terminal-header">
                <div class="dot red"></div>
                <div class="dot yellow"></div>
                <div class="dot green"></div>
                <div class="terminal-name">thorfinn.py</div>
            </div>

            <div class="terminal-body">
                <div><span class="code-gray"># Um pequeno resumo sobre mim</span></div>

                <div>
                    <span class="code-purple">class</span>
                    <span class="code-green">Programador</span>:
                </div>

                <div>&nbsp;&nbsp;&nbsp;&nbsp;nome = <span class="code-green">"thorfinn"</span></div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;linguagem = <span class="code-green">"Python"</span></div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;objetivo = <span class="code-green">"Aprender sempre"</span></div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;mentalidade = <span class="code-green">"Nunca desistir"</span></div>

                <br>

                <div>
                    &nbsp;&nbsp;&nbsp;&nbsp;<span class="code-purple">def</span>
                    <span class="code-green">evoluir</span>(self):
                </div>

                <div>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <span class="code-purple">return</span>
                    <span class="code-green">"Um código de cada vez."</span>
                </div>

                <br>

                <div class="code-gray">
                    # O futuro ainda está sendo escrito...
                </div>

                <div>
                    <span class="code-white">>>> </span>
                    <span class="code-green">continuar_aprendendo()</span>
                    <span class="cursor"></span>
                </div>
            </div>

        </div>
    </div>
</section>

<section id="github">
    <div class="container">

        <div class="reveal">
            <div class="section-label">// 05 — MEU ESPAÇO NA COMUNIDADE</div>
            <h2 class="section-title">Acompanhe minha evolução.</h2>
            <p class="section-description">
                O GitHub é onde compartilho meus estudos, exercícios
                e projetos. Cada repositório representa mais um passo
                nessa jornada.
            </p>
        </div>

        <div class="github-card reveal">

            <div>
                <h3>Vamos nos conectar?</h3>

                <p>
                    Meus códigos, experimentos e aprendizados estão
                    disponíveis no GitHub. Fique à vontade para
                    conhecer meus projetos e acompanhar minha evolução.
                </p>

                <br>

                <a href="https://github.com/nikarlsefni"
                   target="_blank" rel="noopener noreferrer"
                   class="btn btn-primary">
                    <i class="fa-brands fa-github"></i>
                    github.com/nikarlsefni
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>

            <i class="fa-brands fa-github github-icon"></i>

        </div>

    </div>
</section>

<footer>
    <div class="container">
        <p>
            Desenvolvido com <span>♥</span> e muitas linhas de código.
        </p>
        <br>
        <p>
            © <span id="year"></span> thorfinn — Todos os direitos reservados.
        </p>
        <br>
        <p style="font-family: 'JetBrains Mono', monospace;">
            keep_learning(); // keep_evolving();
        </p>
    </div>
</footer>

<button id="backTop" aria-label="Voltar ao topo">
    <i class="fa-solid fa-arrow-up"></i>
</button>

<script>
    // ANO AUTOMÁTICO
    document.getElementById("year").textContent =
        new Date().getFullYear();

    // ANIMAÇÃO DE ENTRADA
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.12
    });

    document.querySelectorAll(".reveal").forEach(element => {
        observer.observe(element);
    });

    // BOTÃO VOLTAR AO TOPO
    const backTop = document.getElementById("backTop");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 400) {
            backTop.classList.add("show");
        } else {
            backTop.classList.remove("show");
        }
    });

    backTop.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });

    // PARTÍCULAS ANIMADAS
    const canvas = document.getElementById("particles");
    const ctx = canvas.getContext("2d");

    let particles = [];
    let animationId;

    function resizeCanvas() {
        const dpr = Math.min(window.devicePixelRatio || 1, 2);

        canvas.width = window.innerWidth * dpr;
        canvas.height = window.innerHeight * dpr;

        canvas.style.width = window.innerWidth + "px";
        canvas.style.height = window.innerHeight + "px";

        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        particles = [];

        const amount = Math.min(
            Math.floor(window.innerWidth / 12),
            90
        );

        for (let i = 0; i < amount; i++) {
            particles.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                radius: Math.random() * 1.8 + .5,
                speedX: (Math.random() - .5) * .35,
                speedY: (Math.random() - .5) * .35,
                opacity: Math.random() * .5 + .1
            });
        }
    }

    function animateParticles() {
        ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

        particles.forEach((particle, index) => {
            particle.x += particle.speedX;
            particle.y += particle.speedY;

            if (particle.x < 0 || particle.x > window.innerWidth) {
                particle.speedX *= -1;
            }

            if (particle.y < 0 || particle.y > window.innerHeight) {
                particle.speedY *= -1;
            }

            ctx.beginPath();
            ctx.arc(
                particle.x,
                particle.y,
                particle.radius,
                0,
                Math.PI * 2
            );

            ctx.fillStyle = `rgba(167,139,250,${particle.opacity})`;
            ctx.fill();

            for (let j = index + 1; j < particles.length; j++) {
                const other = particles[j];

                const dx = particle.x - other.x;
                const dy = particle.y - other.y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 115) {
                    ctx.beginPath();
                    ctx.moveTo(particle.x, particle.y);
                    ctx.lineTo(other.x, other.y);

                    ctx.strokeStyle =
                        `rgba(167,139,250,${.09 * (1 - distance / 115)})`;

                    ctx.lineWidth = .7;
                    ctx.stroke();
                }
            }
        });

        animationId = requestAnimationFrame(animateParticles);
    }

    resizeCanvas();

    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        animateParticles();
    }

    window.addEventListener("resize", resizeCanvas);

    // EFEITO DE TEXTO NO TÍTULO
    const title = document.querySelector(".gradient");

    title.addEventListener("mouseenter", () => {
        title.style.filter = "drop-shadow(0 0 20px rgba(167,139,250,.5))";
    });

    title.addEventListener("mouseleave", () => {
        title.style.filter = "none";
    });
</script>

</body>
</html>
""")

# rota com variaveis na URL
@app.route('/ola/<nome>')
def saudacao(nome):
    return f"<h1> Seja bem vindo ♪(^∇^*)♪ </h1> {nome}"


if __name__ == '__main__':
    app.run(debug=True)