# Outfit Studio

A small Flask app that recommends an outfit from three choices: **vibe**, **weather**, and **occasion**. The page is HTML and CSS; Flask handles the form. There is no database, login, or JavaScript.

## Run locally

You need Python 3.

```powershell
cd C:\Users\May\outfit-generator
python -m pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

Stop the server with **Ctrl+C** in the terminal.

## How it works

1. The form posts `vibe`, `weather`, and `occasion` to `/`.
2. `choose_outfit(vibe, weather, occasion)` in `app.py` picks a string with `if` / `elif` / `else`.
3. The same page shows the result.

**Choices**

| Field | Options |
| --- | --- |
| Vibe | casual, classy, bold |
| Weather | hot, mild, cold |
| Occasion | class, hanging out, going out |

To change what gets recommended, edit `choose_outfit` in `app.py`. Flask debug mode reloads after you save.

## Files

```text
outfit-generator/
  app.py                 Flask app and outfit rules
  requirements.txt       Flask
  templates/index.html   Form and result
  static/style.css       Layout and styling
```
