from flask import Flask, render_template, request

app = Flask(__name__)


def choose_outfit(vibe, weather, occasion):
    """Return an outfit recommendation string from the three form choices."""
    if vibe == "casual":
        if weather == "hot":
            if occasion == "class":
                return "Light linen shorts, a plain cotton tee, and canvas sneakers. Bring a tote for your notebook."
            elif occasion == "hanging out":
                return "A tank or short-sleeve henley, relaxed shorts, slide sandals, and a baseball cap."
            else:
                return "A breathable camp-collar shirt, tailored shorts, and clean white sneakers."
        elif weather == "mild":
            if occasion == "class":
                return "Straight jeans, a soft crewneck tee, a light denim jacket, and low-profile sneakers."
            elif occasion == "hanging out":
                return "Joggers, a hoodie, and chunky sneakers. Easy layers you can peel off."
            else:
                return "Dark jeans, a knit polo, a light overshirt, and leather sneakers."
        else:
            if occasion == "class":
                return "Warm sweatpants or thick denim, a long-sleeve tee, a puffer or fleece, and boots."
            elif occasion == "hanging out":
                return "A heavy hoodie, lined joggers, a beanie, and winter sneakers or boots."
            else:
                return "Dark jeans, a merino sweater, a wool overcoat, and chelsea boots."

    elif vibe == "classy":
        if weather == "hot":
            if occasion == "class":
                return "Lightweight chinos, a tucked short-sleeve button-up, a slim belt, and loafers."
            elif occasion == "hanging out":
                return "A silk-blend blouse or crisp polo, wide linen trousers, and leather sandals."
            else:
                return "A linen blazer over a fine tee, tailored shorts or trousers, and suede loafers."
        elif weather == "mild":
            if occasion == "class":
                return "Pressed trousers, a collared shirt, a lightweight cardigan, and oxfords or loafers."
            elif occasion == "hanging out":
                return "A cashmere crewneck, straight trousers, a trench or light coat, and clean loafers."
            else:
                return "A tailored blazer, silk shirt or knit, dark trousers, and polished dress shoes."
        else:
            if occasion == "class":
                return "Wool trousers, a turtleneck, a structured coat, and leather boots."
            elif occasion == "hanging out":
                return "A long wool coat, knit dress or trousers with a sweater, tights if you like, and ankle boots."
            else:
                return "A tuxedo-adjacent look: black trousers, a satin-trim blazer or wrap coat, and dress boots."

    else:
        if weather == "hot":
            if occasion == "class":
                return "Color-blocked tee, cargo or graphic shorts, statement sneakers, and a bright backpack."
            elif occasion == "hanging out":
                return "A printed mesh or graphic tank, wide-leg shorts, bold socks, and high-tops."
            else:
                return "A saturated silk shirt, sharp shorts or a mini skirt, metallic accessories, and sleek sneakers."
        elif weather == "mild":
            if occasion == "class":
                return "A graphic long-sleeve, contrast cargos, a cropped jacket, and loud sneakers."
            elif occasion == "hanging out":
                return "A vintage band tee, leather or vinyl jacket, barrel jeans, and platform boots."
            else:
                return "A jewel-tone blazer, black trousers or a short dress, stacked jewelry, and pointed boots."
        else:
            if occasion == "class":
                return "A bright knit under a long coat, dark jeans, a patterned scarf, and combat boots."
            elif occasion == "hanging out":
                return "An oversized graphic hoodie, a statement puffer, wide pants, and chunky winter boots."
            else:
                return "A dramatic coat, fitted black layers, a pop of color at the collar or bag, and heeled boots."


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    vibe = weather = occasion = ""

    if request.method == "POST":
        vibe = request.form.get("vibe", "")
        weather = request.form.get("weather", "")
        occasion = request.form.get("occasion", "")
        result = choose_outfit(vibe, weather, occasion)

    return render_template(
        "index.html",
        result=result,
        vibe=vibe,
        weather=weather,
        occasion=occasion,
    )


if __name__ == "__main__":
    app.run(debug=True)
