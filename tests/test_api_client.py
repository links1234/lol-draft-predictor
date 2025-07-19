import pytest
from lolpredictor.api_client import LoLEsportsAPIClient

class DummyResponse:
    def __init__(self, payload):
        self._payload = payload
        self.status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return self._payload

@pytest.fixture(autouse=True)
def fake_get(monkeypatch):
    def _fake(url, params=None):
        # return a dummy "leagues" payload for any endpoint
        return DummyResponse({"data": {"leagues": []}})
    import lolpredictor.api_client as mod
    monkeypatch.setattr(mod.requests.Session, "get", _fake)
    return _fake

def test_get_leagues_returns_data():
    client = LoLEsportsAPIClient(api_key="fake-key")
    result = client.get_leagues()
    assert "data" in result
    assert "leagues" in result["data"]
    assert isinstance(result["data"]["leagues"], list)
