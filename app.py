from flask import Flask, render_template, request, redirect, url_for, session
from translations import get_translation
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session

# Initialize planets list with their types and positions
planets = [
    {'name': 'Mercury', 'type': 'Rocky', 'position': 1},
    {'name': 'Venus', 'type': 'Rocky', 'position': 2},
    {'name': 'Earth', 'type': 'Rocky', 'position': 3},
    {'name': 'Mars', 'type': 'Rocky', 'position': 4},
    {'name': 'Jupiter', 'type': 'Gas Giant', 'position': 5},
    {'name': 'Saturn', 'type': 'Gas Giant', 'position': 6},
    {'name': 'Uranus', 'type': 'Gas Giant', 'position': 7},
    {'name': 'Neptune', 'type': 'Gas Giant', 'position': 8}
]

def get_language():
    """Get the current language from URL parameter or session."""
    lang = request.args.get('lang', session.get('lang', 'uz'))
    if lang not in ['uz', 'ru']:
        lang = 'uz'
    session['lang'] = lang
    return lang

def get_planet_slug(name):
    """Convert planet name to URL-safe slug."""
    return re.sub(r'[^a-z0-9]+', '-', name.lower())

@app.route("/")
def index():
    lang = get_language()
    return render_template("index.html", 
                         planets=planets,
                         lang=lang,
                         t=lambda key: get_translation(lang, key))

@app.route("/planet/<planet_slug>")
def planet_info(planet_slug):
    lang = get_language()
    planet = next((p for p in planets if get_planet_slug(p['name']) == planet_slug), None)
    if planet:
        return render_template("planet.html", 
                             planet=planet,
                             lang=lang,
                             t=lambda key: get_translation(lang, key))
    return redirect(url_for("index"))

@app.route("/add", methods=["GET", "POST"])
def add_planet():
    lang = get_language()
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            # Determine type and position based on existing planets
            position = len(planets) + 1
            planet_type = "Rocky" if position <= 4 else "Gas Giant"
            planets.append({
                'name': name,
                'type': planet_type,
                'position': position
            })
            return redirect(url_for("index"))
    return render_template("form.html",
                         lang=lang,
                         t=lambda key: get_translation(lang, key))

if __name__ == "__main__":
    app.run(debug=True)