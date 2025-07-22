# lolpredictor/api_client.py

import os
from urllib.parse import urljoin
from typing import List, Optional, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


class LoLEsportsAPIClient:
    """
    Simple wrapper for the Unofficial LoLEsports API.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://esports-api.lolesports.com/persisted/gw/",
    ):
        self.api_key = api_key or os.getenv("LOLESPORTS_API_KEY")
        if not self.api_key:
            raise ValueError("Must provide LOLESPORTS_API_KEY via env or parameter.")
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": self.api_key})

    def _get(self, path: str, params: dict) -> dict:
        url = urljoin(self.base_url, path)
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get_leagues(self, hl: str = "en-US") -> Dict:
        """
        GET /getLeagues
        """
        return self._get("getLeagues", {"hl": hl})

    def get_tournaments_for_league(self, league_id: int, hl: str = "en-US") -> Dict:
        """
        GET /getTournamentsForLeague
        """
        return self._get("getTournamentsForLeague", {"leagueId": league_id, "hl": hl})

    def get_schedule(
        self,
        league_ids: List[int],
        hl: str = "en-US",
        page_token: Optional[str] = None,
    ) -> Dict:
        """
        GET /getSchedule
        """
        params = {"leagueId": league_ids, "hl": hl}
        if page_token:
            params["pageToken"] = page_token
        return self._get("getSchedule", params)

    def get_event_details(self, event_id: int, hl: str = "en-US") -> Dict:
        """
        GET /getEventDetails
        """
        return self._get("getEventDetails", {"id": event_id, "hl": hl})

    def get_game_draft(self, event_id: int, game_id: int, hl: str = "en-US") -> Dict:
        """Return blue and red side picks for a game within a match."""
        details = self.get_event_details(event_id, hl=hl)
        games = (
            details.get("data", {})
            .get("event", {})
            .get("match", {})
            .get("games", [])
        )
        for game in games:
            if str(game.get("id")) == str(game_id):
                draft = game.get("draft")
                if not draft:
                    raise ValueError("Draft info missing for game")
                return self._parse_draft_picks(draft)
        raise ValueError(f"Game {game_id} not found in event {event_id}")

    @staticmethod
    def _parse_draft_picks(draft: Dict) -> Dict[str, List[str]]:
        blue, red = [], []
        for action_set in draft.get("actions", []):
            for action in action_set:
                if action.get("type") != "pick" or not action.get("completed"):
                    continue
                champ = action.get("championId")
                team = str(action.get("teamId"))
                if team in {"100", "blue", "Blue"}:
                    blue.append(champ)
                else:
                    red.append(champ)
        return {"blue_side": blue, "red_side": red}

    # TODO: add other endpoints (standings, live, completedEvents, etc.)
