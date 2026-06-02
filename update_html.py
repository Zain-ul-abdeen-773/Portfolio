import sys

with open("index.html", "r", encoding="utf-8") as f:
    data = f.read()

replacements = [
    ("<title>Zain Ul Abdeen | Sci-Fi Portfolio</title>", "<title>Zain Ul Abdeen | Software Engineer</title>"),
    ('<!-- Custom Cursor -->\n    <div id="custom-cursor"></div>\n    <div id="custom-cursor-trail"></div>', ""),
    ('<!-- Background System -->\n    <div class="bg-layer bg-layer-1"></div>\n    <div class="bg-layer bg-layer-2"></div>\n    <div class="bg-layer bg-layer-3"></div>\n    <div class="bg-layer bg-layer-4" id="particles-container">\n        <!-- Add standard CSS particles via JS or static inline (doing a few statically here) -->\n        <div class="particle" style="left: 10%; animation-duration: 15s;"></div>\n        <div class="particle" style="left: 20%; animation-duration: 22s; animation-delay: 2s"></div>\n        <div class="particle" style="left: 35%; animation-duration: 18s; animation-delay: 5s"></div>\n        <div class="particle" style="left: 50%; animation-duration: 25s; animation-delay: 1s"></div>\n        <div class="particle" style="left: 65%; animation-duration: 19s; animation-delay: 8s"></div>\n        <div class="particle" style="left: 80%; animation-duration: 21s; animation-delay: 3s"></div>\n        <div class="particle" style="left: 90%; animation-duration: 16s; animation-delay: 6s"></div>\n    </div>\n    <div class="bg-layer bg-layer-5"></div>', ""),
    ('<div class="status-indicator">\n            <span class="status-dot"></span> System Online\n        </div>', ""),
    ('<h1 class="glitch-text">Zain Ul Abdeen</h1>', '<h1>Zain Ul Abdeen</h1>'),
    ('<div class="typewriter-text">> INIT_PROTOCOL: AI Data Pipeline Engineer...</div>', '<div class="subtitle-text" style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 1.5rem;">Software Engineer & Data Specialist</div>'),
    ('Initialize.Projects', 'View Projects'),
    ('> Comm.Link', '> Contact'),
    ('01. About Entity', 'About Me'),
    ('<div class="bracket-accent"></div>', ''),
    ('<div style="position: absolute; top: -20px; right: -20px; font-size: 8rem; opacity: 0.03; font-family: monospace; user-select: none;">AI</div>', ''),
    ('<h3 style="color: var(--primary); font-size: 1.5rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 2px;">Architecting the Future of Intelligence</h3>', '<h3 style="color: var(--primary); font-size: 1.5rem; margin-bottom: 1rem;">Bridging the gap between data and systems</h3>'),
    ('> Core_Directives', 'Engineering Focus'),
    ('> Field_Experience', 'Professional Experience'),
    ('"Transforming complex neural architectures into resilient, real-world applications."', 'Passionate about building robust software infrastructure and data architectures.'),
    ('02. Skill Matrix', 'Technical Skills'),
    ('03. Project Database', 'Featured Projects'),
    ('> ACTIVE EXPERIMENTS [AI/ML]', 'Software & Data Engineering'),
    ('> INFRASTRUCTURE [DEVOPS]', 'Infrastructure & DevOps'),
    ('> ARCHIVE LOGS [PREVIOUS]', 'Archive & Previous Works'),
    ('04. Neural Training [Experience & Education]', 'Experience & Education'),
    ('2022 - Expected 2026', '2023 - 2027'),
    ('05. Certification Array', 'Certifications'),
    ('06. Comm.Link', 'Contact Me'),
    ('Establish Connection', 'Get in Touch'),
    ('Transmit Data', 'Email Me'),
    ('[ EOF  ] System Shutdown. Zain Ul Abdeen 2026.', '&copy; Zain Ul Abdeen 2026.'),
    ('I am a <strong>BS Artificial Intelligence</strong> student (6th Semester) at the prestigious <span style="color: var(--primary);">Ghulam Ishaq Khan Institute of Engineering Sciences & Technology (GIKI)</span>.', 'I am a Software Engineering and Data specialist currently completing my degree at the <span style="color: var(--primary);">Ghulam Ishaq Khan Institute of Engineering Sciences & Technology (GIKI)</span>.'),
    ('Extract.CV', 'Download Resume'),
    ('Comm.Link', 'Contact')
]

for old, new in replacements:
    data = data.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(data)
