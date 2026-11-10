import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"


# Updating stars to boundary and out-of-range values: 0 and 6 are refused,
# 1 and 5 are saved; a refused update must leave the original stars unchanged.
@pytest.mark.parametrize("stars,expected_status", [(0, 400), (1, 200), (5, 200), (6, 400)])
def test_update_stars_boundary(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    if expected_status == 400:
        assert res.json() == {"error": STARS_ERROR}
        # Rating must be unchanged after a refused update.
        res = api.get(path, headers=auth)
        assert res.status_code == 200
        assert res.json()["stars"] == rating["stars"]
    else:
        assert res.json()["stars"] == stars

