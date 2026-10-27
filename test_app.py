"""Check the full recommendation matrix and the HTTP form flow."""

from itertools import product
import unittest

from app import CHOICES, app, choose_outfit


class OutfitTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_and_stylesheet_load(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Generate my outfit", response.data)
        with self.client.get("/static/style.css") as stylesheet:
            self.assertEqual(stylesheet.status_code, 200)
            self.assertIn("text/css", stylesheet.content_type)

    def test_every_combination_renders_its_recommendation(self):
        for values in product(*CHOICES.values()):
            with self.subTest(values=values):
                selections = dict(zip(CHOICES, values))
                outfit = choose_outfit(**selections)
                self.assertTrue(outfit.strip())
                response = self.client.post("/", data=selections)
                self.assertEqual(response.status_code, 200)
                self.assertIn(outfit, response.get_data(as_text=True))
                self.assertEqual(response.data.count(b"checked"), 3)

    def test_missing_and_invalid_choices_are_rejected(self):
        valid = {field: options[0] for field, options in CHOICES.items()}
        for field in CHOICES:
            for value in (None, "", "unknown", "<script>alert(1)</script>"):
                with self.subTest(field=field, value=value):
                    selections = valid.copy()
                    if value is None:
                        selections.pop(field)
                    else:
                        selections[field] = value
                    response = self.client.post("/", data=selections)
                    self.assertEqual(response.status_code, 400)
                    self.assertIn(b'role="alert"', response.data)
                    self.assertNotIn(b"<script>", response.data)
                    self.assertNotIn(b'class="result-body"', response.data)

    def test_function_rejects_invalid_choices(self):
        with self.assertRaises(ValueError):
            choose_outfit("unknown", "mild", "class")

    def test_start_over_clears_choices(self):
        self.client.post(
            "/", data={"vibe": "bold", "weather": "cold", "occasion": "class"}
        )
        response = self.client.get("/")
        self.assertNotIn(b"checked", response.data)
        self.assertNotIn(b'class="result-body"', response.data)


if __name__ == "__main__":
    unittest.main()
