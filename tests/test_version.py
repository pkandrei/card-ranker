import tomllib
from pathlib import Path

from app.version import PLACEHOLDER, get_version, read_file_for_version


def test_valid_file_returns_version(tmp_path: Path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """\
[project]
name = "test"
version = "9.9.9"
requires-python = ">=3.14"
dependencies = []
""",
        encoding="utf-8",
    )

    version = read_file_for_version(pyproject)

    assert version == "9.9.9"


def test_missing_path_returns_placeholder_and_warns(tmp_path: Path, caplog):
    pyproject = tmp_path / "pyproject.toml"

    version = read_file_for_version(pyproject)

    assert version == PLACEHOLDER
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "pyproject.toml" in caplog.messages[0]
    assert "not found" in caplog.messages[0]


def test_invalid_toml_returns_placeholder_and_warns(tmp_path: Path, caplog):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """\
[project
name = "test"
version = "9.9.9"
requires-python = ">=3.14"
dependencies = []
""",
        encoding="utf-8",
    )

    version = read_file_for_version(pyproject)

    assert version == PLACEHOLDER
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "pyproject.toml" in caplog.messages[0]
    assert "is not a valid TOML file" in caplog.messages[0]


def test_missing_version_returns_placeholder_and_warns(tmp_path: Path, caplog):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """\
[project]
name = "test"
requires-python = ">=3.14"
dependencies = []
""",
        encoding="utf-8",
    )

    version = read_file_for_version(pyproject)

    assert version == PLACEHOLDER
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "pyproject.toml" in caplog.messages[0]
    assert "has no 'version' entry under [project]" in caplog.messages[0]


def test_unreadable_path_returns_placeholder_and_warns(tmp_path: Path, caplog):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.mkdir()

    version = read_file_for_version(pyproject)

    assert version == PLACEHOLDER
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "pyproject.toml" in caplog.messages[0]
    assert "Could not read file" in caplog.messages[0]


def test_path_reaches_the_project_pyproject():
    project_root = Path(__file__).parent.parent

    with (project_root / "pyproject.toml").open("rb") as file:
        expected = tomllib.load(file)["project"]["version"]

    assert get_version() == expected
