from notion_client import Client
import toml

from config import build_config

with open("notion_token.txt") as notion_token:
    notion = Client(auth=notion_token.readline())

with open("config.toml") as config_file:
    cfg = build_config(toml.load(config_file))
    print(cfg.databases.new_releases)
