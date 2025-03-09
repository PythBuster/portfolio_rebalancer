"""All helper functions are located here."""

import tomllib
from functools import cache
from pathlib import Path
from typing import Any

from matplotlib import pyplot as plt

from src.custom_types import AppEnvVariables


def generate_colors(num_colors: int) -> list[tuple[int, int, int]]:
    """Generates a list of different colors as RGB-tupel (0-255).

    :param num_colors: Amount of color tuples in result.
    :type num_colors: :class:`int`
    :return: A list of tuples (rgb values).
    :rtype: :class:`list[tuple[int, int, int]]`
    """

    cmap = plt.get_cmap("tab10")
    colors = [cmap(i % 10)[:3] for i in range(num_colors)]
    return [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

def rgb_to_hex(rgb_colors: list[tuple[int, int, int]]) -> list[str]:
    """Converts a list of RGB-Tupeln (0-255) to HTML-Hex-Colors.

    :param rgb_colors: a list of rgb tuples.
    :type rgb_colors: :class:`list[tuple[int, int, int]]`
    :return: List of hex colors.
    :rtype: :class:`ist[str]`
    """

    return [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_colors]


def get_database_url(db_settings: AppEnvVariables) -> str:
    """Create a database connection string based on db_settings.

    :param db_settings: Includes the database credentials.
    :type db_settings: :class:`AppEnvVariables`
    :return: A database connection string
    :rtype: :class:`str`

    :raises ValueError: if db_driver in settings is not supported.
    """

    if "postgres" in db_settings.db_driver:
        return f"{db_settings.db_driver}://{db_settings.db_user}:{db_settings.db_password.get_secret_value()}@{db_settings.db_host}:{db_settings.db_port}/{db_settings.db_name}"  # noqa: ignore  # pylint: disable=line-too-long

    raise ValueError(f"Not supported database driver: {db_settings.db_driver}")


@cache
def get_app_data() -> dict[str, Any]:
    """Extract app information from pyproject.toml.

    :return: The app data section from pyproject.toml as dict
    :rtype: :class:`dict[str, Any]`
    """

    pyproject_file_path: Path = Path(__file__).resolve().parent.parent / "pyproject.toml"

    with pyproject_file_path.open(mode="rb") as pyproject_file:
        pyproject_data: dict[str, Any] = tomllib.load(pyproject_file)

    return pyproject_data["tool"]["poetry"]
