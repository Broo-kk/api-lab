import pytest


# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize("excluded", [["Knife"], ["Scissors"], ["Pizza cutter"],
                                       ["Knife", "Scissors"], ["Knife", "Pizza cutter"],
                                       ["Scissors", "Pizza cutter"]])
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


# Excluding all three tools leaves no tool available; the API must refuse with 400 and a message.
@pytest.mark.xfail(reason="Defect 1: excluding all tools returns 500 with empty body instead of 400 with a message", strict=True)
def test_all_tools_excluded_returns_400(api, auth):
    body = {"excludedTools": ["Knife", "Scissors", "Pizza cutter"]}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 400
    assert res.json() != {}

