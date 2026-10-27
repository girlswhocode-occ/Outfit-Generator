"""A small Flask app for choosing an outfit for the day."""

from flask import Flask, render_template, request

from outfits import OUTFITS

app = Flask(__name__)

# Shared by the form and server validation so their options stay in sync.
CHOICES = {
    "vibe": ("casual", "classy", "bold"),
    "weather": ("hot", "mild", "cold"),
    "occasion": ("class", "hanging out", "going out"),
}


def choose_outfit(vibe: str, weather: str, occasion: str) -> str:
    """Return the matching outfit, or raise ValueError for an invalid choice."""
    selections = {"vibe": vibe, "weather": weather, "occasion": occasion}
    for field, value in selections.items():
        if value not in CHOICES[field]:
            raise ValueError(f"Please choose a valid {field}.")

    return OUTFITS[vibe][weather][occasion]


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the form and, after a valid submission, its recommendation."""
    selections = {field: "" for field in CHOICES}
    result = None
    error = None

    if request.method == "POST":
        selections = {field: request.form.get(field, "") for field in CHOICES}
        try:
            result = choose_outfit(**selections)
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        choices=CHOICES,
        selections=selections,
        result=result,
        error=error,
    ), 400 if error else 200


if __name__ == "__main__":
    app.run()
