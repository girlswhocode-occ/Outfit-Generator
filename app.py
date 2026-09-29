from flask import Flask, render_template, request
app = Flask(__name__)
# =============================================================================
# CLUB TASK: write the recommendation rules inside choose_outfit()
# Do not change the function name or arguments. Return a string.
# =============================================================================
def choose_outfit(vibe, weather, occasion):
    """Return an outfit recommendation string from the three form choices."""
    # TODO: Replace the placeholder below with if/elif/else logic that uses
    # vibe (casual, classy, bold), weather (hot, mild, cold), and
    # occasion (class, hanging out, going out) to pick a real outfit.
    return (
        "Placeholder look: your club will fill this in. "
        f"(You picked {vibe}, {weather}, {occasion}.)"
    )
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
