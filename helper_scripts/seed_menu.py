"""
Seed script to import menu items from menu.json into MongoDB.
Usage:
    python helper_scripts/seed_menu.py
"""

import os
import json
import pymongo

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MENU_FILE = os.path.join(SCRIPT_DIR, "menu.json")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")


def seed_database():
    if not os.path.exists(MENU_FILE):
        print(f"Error: menu file not found at {MENU_FILE}")
        return

    with open(MENU_FILE, "r", encoding="utf-8") as f:
        menu_items = json.load(f)

    print(f"Connecting to MongoDB at {MONGO_URI}...")
    client = pymongo.MongoClient(MONGO_URI)
    db = client["restaurant"]
    menu_collection = db["menu"]

    # Clear existing menu items to prevent duplicates
    deleted = menu_collection.delete_many({})
    print(f"Cleared {deleted.deleted_count} previous items from 'menu' collection.")

    if menu_items:
        result = menu_collection.insert_many(menu_items)
        print(f"Successfully inserted {len(result.inserted_ids)} menu items into 'restaurant.menu'.")
    else:
        print("No items found in menu.json.")


if __name__ == "__main__":
    seed_database()
