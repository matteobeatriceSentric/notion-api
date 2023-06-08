from dataclasses import dataclass, field


@dataclass
class ConfigDatabases:
    new_releases: str = field()


@dataclass
class ConfigClass:
    databases: ConfigDatabases = field()


def build_config(raw_config: dict) -> ConfigClass:
    raw_config["databases"] = ConfigDatabases(**raw_config["databases"])
    return ConfigClass(**raw_config)
