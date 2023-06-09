from notion_client import Client
import toml, json

from .config import build_config

with open("Data/notion_token.txt") as notion_token:
    notion = Client(auth=notion_token.readline())

with open("Data/config.toml") as config_file:
    cfg = build_config(toml.load(config_file))

print(json.dumps(notion.databases.query(
    **{
        "database_id": f"{cfg.databases.new_releases}",
    }), indent=2))


def create_new_version_page(title: str, body: str, platform: str, database: str):
    # https://developers.notion.com/reference/post-page
    # https://developers.notion.com/reference/page-property-values
    pass
