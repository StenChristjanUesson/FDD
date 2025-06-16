from flask import Flask, render_template_string, request

app = Flask(__name__)

base_template = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <title>TTHK</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        header { background: #003366; color: white; padding: 1em; text-align: center; }
        nav { background: #0055a5; padding: 1em; text-align: center; }
        nav a { color: white; margin: 0 1em; text-decoration: none; }
        main { padding: 2em; }
        footer { background: #003366; color: white; text-align: center; padding: 1em; margin-top: 2em; }
        .lang-switch { float: right; margin-top: -2.5em; margin-right: 1em; }
    </style>
</head>
<body>
    <header>
        <h1>TTHK Kooli Koduleht</h1>
        <!-- F003: Language Switch -->
        <div class="lang-switch">
            <a href="?lang=et">ET</a> | <a href="?lang=en">EN</a>
        </div>
    </header>
    <nav>
        <a href="/?lang={{ lang }}">Avaleht</a>
        <a href="/erialad?lang={{ lang }}">Erialad</a>
        <a href="/uudised?lang={{ lang }}">Uudised</a>
        <a href="/kontakt?lang={{ lang }}">Kontakt</a>
    </nav>
    <main>{{ content|safe }}</main>
    <footer>&copy; 2025 TTHK</footer>
</body>
</html>
"""

translations = {
    "et": {
        "home": "<h2>Tere tulemast TTHK kodulehele</h2><p>Siit leiad info kooli ja õppimisvõimaluste kohta.</p>", 
        "contact": "<h2>Kontakt</h2><p>Email: info@tthk.ee<br>Telefon: +372 600 1234<br>Aadress: Pärnu mnt 57, Tallinn</p>",  
        "fields": "<h2>Erialad</h2><ul><li>IT-süsteemide spetsialist</li><li>Autotehnik</li><li>Elektrik</li><li>Kokk</li></ul>",  
        "news": "<h2>Uudised</h2><ul><li>04.05.2025 – Vastuvõtt on alanud</li><li>27.05.2025 – Koolilõpuaktus</li><li>01.09.2025 – Uue õppeaasta algus</li></ul>" 
    },
    "en": {
        "home": "<h2>Welcome to TTHK School Website</h2><p>Here you will find information about the school and learning opportunities.</p>", 
        "contact": "<h2>Contact</h2><p>Email: info@tthk.ee<br>Phone: +372 600 1234<br>Address: Pärnu mnt 57, Tallinn</p>",  
        "fields": "<h2>Study Fields</h2><ul><li>IT Systems Specialist</li><li>Car Mechanic</li><li>Electrician</li><li>Chef</li></ul>", 
        "news": "<h2>News</h2><ul><li>May 4, 2025 – Admission has started</li><li>May 27, 2025 – Graduation Ceremony</li><li>Sept 1, 2025 – New academic year begins</li></ul>"
    }
}

def get_lang():
    return request.args.get('lang', 'et')

@app.route("/")
def home():
    lang = get_lang()
    content = translations[lang]["home"]
    return render_template_string(base_template, content=content, lang=lang)

@app.route("/kontakt")
def kontakt():
    lang = get_lang()
    content = translations[lang]["contact"]
    return render_template_string(base_template, content=content, lang=lang)

@app.route("/erialad")
def erialad():
    lang = get_lang()
    content = translations[lang]["fields"]
    return render_template_string(base_template, content=content, lang=lang)

@app.route("/uudised")
def uudised():
    lang = get_lang()
    content = translations[lang]["news"]
    return render_template_string(base_template, content=content, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
