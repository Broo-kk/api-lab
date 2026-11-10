# api-lab

API testing lab for ITCS386 — Software Verification and Validation.

## Setup

Requires Python 3.10 or newer and Git.

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\activate

pip install -r requirements.txt
```

## Running the tests

```bash
pytest -v
```

To save an HTML report:

```bash
pytest -v --html=report.html --self-contained-html
```

## Input domain model — POST /api/ratings

| Characteristic | Blocks | Values in the tests | Test that covers it |
|---|---|---|---|
| C1 Value of `stars` | below 1 | 0 | `test_stars_out_of_range[0]` |
| | 1 to 5 **(base)** | 3 | `test_base_choice_is_saved` |
| | above 5 | 6 | `test_stars_out_of_range[6]` |
| C2 Type of `stars` | whole number **(base)** | 3 | `test_base_choice_is_saved` |
| | decimal | 3.5 | `test_decimal_stars_refused` |
| | text | `"3"` | `test_text_stars_refused` |
| | missing | (no field) | `test_missing_stars_refused` |
| C3 Pizza | exists **(base)** | a new pizza | `test_base_choice_is_saved` |
| | does not exist | 999999999 | `test_nonexistent_pizza_refused` |
| C4 Token | user's own **(base)** | from `auth` fixture | `test_base_choice_is_saved` |
| | none | (no header) | `test_no_token_refused` |
| | wrong / short | `token abc` | `test_short_token_refused` |
