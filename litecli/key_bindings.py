from __future__ import annotations
import logging
from typing import Any

from prompt_toolkit.enums import EditingMode
from prompt_toolkit.filters import completion_is_selected
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

_logger = logging.getLogger(__name__)


def cli_bindings(cli: Any) -> KeyBindings:
    """Custom key bindings for cli."""
    kb = KeyBindings()

    @kb.add("f3")
    def _(_event: KeyPressEvent) -> None:
        """Enable/Disable Multiline Mode."""
        pass

    @kb.add("f4")
    def _(event: KeyPressEvent) -> None:
        """Toggle between Vi and Emacs mode."""
        pass

    @kb.add("tab")
    def _(event: KeyPressEvent) -> None:
        """Force autocompletion at cursor."""
        pass

    @kb.add("s-tab")
    def _(event: KeyPressEvent) -> None:
        """Force autocompletion at cursor."""
        pass

    @kb.add("c-space")
    def _(event: KeyPressEvent) -> None:
        """
        Initialize autocompletion at cursor.

        If the autocompletion menu is not showing, display it with the
        appropriate completions for the context.

        If the menu is showing, select the next completion.
        """
        pass

    @kb.add("enter", filter=completion_is_selected)
    def _(event: KeyPressEvent) -> None:
        """Makes the enter key work as the tab key only when showing the menu.

        In other words, don't execute query when enter is pressed in
        the completion dropdown menu, instead close the dropdown menu
        (accept current selection).

        """
        pass

    @kb.add("right", filter=completion_is_selected)
    def _(event: KeyPressEvent) -> None:
        """Accept the completion that is selected in the dropdown menu."""
        pass

    return kb
