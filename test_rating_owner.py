# A user must never read, change or delete the rating of another user.


# Another user trying to read the owner's rating is refused (4xx).
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    res = api.get(f"/api/ratings/{rating['id']}", headers=other_auth)
    assert 400 <= res.status_code <= 499
    # The rating is still intact for its owner.
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user trying to change the owner's rating is refused (4xx).
def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    res = api.put(f"/api/ratings/{rating['id']}", json={"stars": 1}, headers=other_auth)
    assert 400 <= res.status_code <= 499
    # The rating is unchanged for its owner.
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json()["stars"] == rating["stars"]


# Another user trying to delete the owner's rating is refused (4xx).
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    res = api.delete(f"/api/ratings/{rating['id']}", headers=other_auth)
    assert 400 <= res.status_code <= 499
    # The rating still exists for its owner.
    res = api.get(f"/api/ratings/{rating['id']}", headers=auth)
    assert res.status_code == 200
    assert res.json() == rating

