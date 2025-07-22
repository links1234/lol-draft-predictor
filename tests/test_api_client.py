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
    event_payload = {
        "data": {
            "event": {
                "match": {
                    "games": [
                        {
                            "id": 1,
                            "draft": {
                                "actions": [
                                    [
                                        {
                                            "type": "pick",
                                            "completed": True,
                                            "championId": "A",
                                            "teamId": "100",
                                        },
                                        {
                                            "type": "pick",
                                            "completed": True,
                                            "championId": "B",
                                            "teamId": "200",
                                        },
                                    ],
                                    [
                                        {
                                            "type": "pick",
                                            "completed": True,
                                            "championId": "C",
                                            "teamId": "100",
                                        },
                                        {
                                            "type": "pick",
                                            "completed": True,
                                            "championId": "D",
                                            "teamId": "200",
                                        },
                                    ],
                                ]
                            },
                        }
                    ]
                }
            }
        }
    }

    def _fake(self, url, params=None, **kwargs):
        if url.endswith("getEventDetails"):
            return DummyResponse(event_payload)
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


def test_get_game_draft_parses_picks():
    client = LoLEsportsAPIClient(api_key="fake-key")
    draft = client.get_game_draft(event_id=123, game_id=1)
    assert draft["blue_side"] == ["A", "C"]
    assert draft["red_side"] == ["B", "D"]
