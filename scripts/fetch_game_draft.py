#!/usr/bin/env python3
import sys
from dotenv import load_dotenv
from lolpredictor.api_client import LoLEsportsAPIClient


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/fetch_game_draft.py <event_id> <game_id>")
        return
    event_id = int(sys.argv[1])
    game_id = int(sys.argv[2])
    load_dotenv()
    client = LoLEsportsAPIClient()
    draft = client.get_game_draft(event_id, game_id)
    print("Blue side picks:", draft["blue_side"])
    print("Red side picks:", draft["red_side"])


if __name__ == "__main__":
    main()
