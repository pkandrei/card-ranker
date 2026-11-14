import logging
import tomllib
from functools import cache
from pathlib import Path

PLACEHOLDER = "unknown"

logger = logging.getLogger(__name__)


def retrieve_version(path: Path):
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)
        return data["project"]["version"]
    except FileNotFoundError:
        logger.warning("File %s not found.", path)
        return PLACEHOLDER
    except tomllib.TOMLDecodeError:
        logger.warning("File %s is not a valid TOML file.", path)
        return PLACEHOLDER
    except KeyError:
        logger.warning("File %s has no 'version' entry under [project].", path)
        return PLACEHOLDER
    except OSError as error:
        logger.warning("Could not read file %s: %s", path, error)
        return PLACEHOLDER


@cache
def get_version():
    app_dir = Path(__file__).parent
    return retrieve_version(app_dir.parent / "pyproject.toml")
