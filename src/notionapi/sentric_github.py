from github import Github


class SentricGithub:
    DATA_PROCESSING = "sentricsrl/data-processing"
    CASPER_LOGGER = "sentricsrl/casper-logger"
    CASPER_SCRAPERS = "sentricsrl/casper-scrapers"
    NOTION_API = "matteobeatriceSentric/notion-api"

    def __init__(self, token: str) -> None:
        g = Github(token)
        self.data_processing = g.get_repo(self.DATA_PROCESSING)
        self.casper_logger = g.get_repo(self.CASPER_LOGGER)
        self.casper_scrapers = g.get_repo(self.CASPER_SCRAPERS)
        self.notion_api = g.get_repo(self.NOTION_API)
