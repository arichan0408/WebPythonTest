import pytest
from app import app, Result


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_result_class():
    result = Result(4, 6)
    assert result.a == 4
    assert result.b == 6
    assert result.sum == 10
    assert result.ave == 5


def test_index_get(client):
    res = client.get("/")
    assert res.status_code == 200


def test_index_post(client):
    res = client.post("/", data={"a": "4", "b": "6"})
    assert res.status_code == 200

    # HTMLに計算結果が含まれているか（index.html次第）
    assert b"10" in res.data
    assert b"5" in res.data
