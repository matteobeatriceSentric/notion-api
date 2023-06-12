from dataclasses import dataclass, field


@dataclass
class ConfigPlatforms:
    data_processing: str = field()
    website: str = field()
    database: str = field()
    app: str = field()
    api: str = field()
    backend: str = field()
    everywhere: str = field()
    admin: str = field()


@dataclass
class ConfigDatabases:
    new_releases: str = field()


@dataclass
class ConfigClass:
    databases: ConfigDatabases = field()
    platforms: ConfigPlatforms = field()


def build_config(raw_config: dict) -> ConfigClass:
    raw_config["databases"] = ConfigDatabases(**raw_config["databases"])
    raw_config["platforms"] = ConfigPlatforms(**raw_config["platforms"])
    return ConfigClass(**raw_config)
