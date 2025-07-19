#!/usr/bin/env python3
import os
from dotenv import load_dotenv

from lolpredictor.api_client import LoLEsportsAPIClient

def main():
    load_dotenv()
    client = LoLEsportsAPIClient()
    data = client.get_leagues()
    print("Leagues fetched:", len(data.get("data", {}).get("leagues", [])))
    for league in data["data"]["leagues"]:
        print(f" - {league['name']} ({league['region']})")

if __name__ == "__main__":
    main()
