# Outfit Studio

A small Flask app that recommends an outfit from your **vibe**, the **weather**,
and the **occasion**. Includes 27 curated combinations, accessible radio controls,
server-side validation, and a start-over link. No database or JavaScript required.

## Run locally

Use Python 3.10 or newer. From the project folder:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000). Stop with **Ctrl+C**.

For automatic reload during development:

```powershell
.venv\Scripts\python -m flask --app app run --debug
```

The built-in server is intended for local development.

## How it works

1. Select a vibe, weather, and occasion, then submit the form.
2. The server validates each choice and looks up its recommendation.
3. The page displays the outfit and retains your choices so you can adjust them.
4. **Start over** clears the form and recommendation.

Missing or unsupported choices display a helpful error and return HTTP 400.
The same selections always return the same curated outfit.

| Field | Options |
| --- | --- |
| Vibe | casual, classy, bold |
| Weather | hot, mild, cold |
| Occasion | class, hanging out, going out |

## Project layout

```text
app.py                 Routes, form choices, and validation
outfits.py             Recommendations grouped by vibe, weather, and occasion
templates/index.html   Form and result
static/style.css       Responsive styling and keyboard focus states
test_app.py            Recommendation and HTTP tests
requirements.txt       Flask dependency
```

To change an outfit, edit its entry in `outfits.py`. Keep an entry for every
combination defined by `CHOICES` in `app.py`.

## Run checks

```powershell
.venv\Scripts\python -m unittest -v
```

Tests cover all 27 combinations, form selection retention, invalid and missing
inputs, clearing the form, and loading the page and stylesheet.
