from __future__ import annotations


import os
import subprocess


def handle_cd_command(arg: str) -> tuple[bool, str | None]:
    """Handles a `cd` shell command by calling python's os.chdir."""
    pass


def format_uptime(uptime_in_seconds: str) -> str:
    """Format number of seconds into human-readable string.

    :param uptime_in_seconds: The server uptime in seconds.
    :returns: A human-readable string representing the uptime.

    >>> uptime = format_uptime('56892')
    >>> print(uptime)
    15 hours 48 min 12 sec
    """
    pass


def check_if_sqlitedotcommand(command: object) -> bool:
    """Does a check if the command supplied is in the list of SQLite dot commands.

    :param command: A command (str) supplied from the user
    :returns: True/False
    """

    sqlite3dotcommands = [
        ".archive",
        ".auth",
        ".backup",
        ".bail",
        ".binary",
        ".cd",
        ".changes",
        ".check",
        ".clone",
        ".connection",
        ".databases",
        ".dbconfig",
        ".dbinfo",
        ".dump",
        ".echo",
        ".eqp",
        ".excel",
        ".exit",
        ".expert",
        ".explain",
        ".filectrl",
        ".fullschema",
        ".headers",
        ".help",
        ".import",
        ".imposter",
        ".indexes",
        ".limit",
        ".lint",
        ".load",
        ".log",
        ".mode",
        ".nonce",
        ".nullvalue",
        ".once",
        ".open",
        ".output",
        ".parameter",
        ".print",
        ".progress",
        ".prompt",
        ".quit",
        ".read",
        ".recover",
        ".restore",
        ".save",
        ".scanstats",
        ".schema",
        ".selftest",
        ".separator",
        ".session",
        ".sha3sum",
        ".shell",
        ".show",
        ".stats",
        ".system",
        ".tables",
        ".testcase",
        ".testctrl",
        ".timeout",
        ".timer",
        ".trace",
        ".vfsinfo",
        ".vfslist",
        ".vfsname",
        ".width",
    ]

    if isinstance(command, str):
        head = command.split(" ", 1)[0].lower()
        return head in sqlite3dotcommands
    return False
