import uuid
import requests

SITE = "https://quickpizza.grafana.com"


def _make_user(api):
    """Create a fresh user via the session and return (session, credentials)."""
    name = "lab-" + uuid.uuid4().hex[:12]
    creds = {"username": name, "password": "Pizza-2026"}
    return creds


# A second user with a name that is already taken gets status 400.
def test_duplicate_username_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# Logging in with a wrong password gets status 401.
def test_wrong_password_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    bad = {"username": name, "password": "WrongPassword-999"}
    res = api.post("/api/users/token/login", json=bad)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# A user with an empty name gets status 400.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}

