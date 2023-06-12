from notion_client import Client

from .config import ConfigClass


NEW_ICON = {"type": "emoji", "emoji": "\ud83c\udd95"}
"""Default icon of the new release pages. Should be put under the key 'icon'"""


def build_parent_database_id(database_id: str) -> dict:
    """
    Builds the parent object to attach the page to the specified db.

    Args:
        database_id (str): The id of the database parent of this page

    Returns:
        dict: parent database. Should be put under the key 'parent'
    """
    return {"type": "database_id", "database_id": database_id}


def new_release_properties(page_name: str, platform: str) -> dict:
    """Build the properties for a page for the New Releases database

    Args:
        page_name (str): Title of the new page
        platform (str): Multi select field of the Platform of the release

    Returns:
        dict: Properties of the page. Should be put under the key 'properties'
    """
    platform_property = {
        "multi_select": [{"name": platform}],
    }
    name_property = {"title": [{"text": {"content": page_name}}]}

    return {"Name": name_property, "Platform": platform_property}


def build_simple_page_content_with_list(title: str, content: list[str]) -> list:
    """Builds content of a simple page with an H1 and a bulleted list

    Args:
        title (str): H1 title
        content (list[str]): Items of the bulleted list

    Returns:
        list: List of blocks of the page. Should be put under the key 'children'
    """
    out: list = [{"heading_1": {"rich_text": [{"text": {"content": title}}]}}]
    out.extend({"bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": item}}], "color": "default"}} for item in content)

    return out


class NotionNewReleases:
    def __init__(self, cfg: ConfigClass, notion_token: str) -> None:
        self.database_id = cfg.databases.new_releases
        self.notion = Client(auth=notion_token)

    def create_new_release_page(self, name: str, platform: str, h1: str, list_items: list[str], icon: dict = NEW_ICON):
        page = {
            "icon": icon,
            "parent": build_parent_database_id(self.database_id),
            "properties": new_release_properties(name, platform),
            "children": build_simple_page_content_with_list(h1, list_items),
        }
        return self.notion.pages.create(**page)
