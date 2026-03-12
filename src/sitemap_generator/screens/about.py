"""About-Dialog fuer den Sitemap Generator."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Static

from .. import __version__
from ..i18n import t


class AboutScreen(ModalScreen):
    """Zeigt Versionsinformationen und Tastenkuerzel."""

    DEFAULT_CSS = """
    AboutScreen {
        align: center middle;
    }

    AboutScreen > Vertical {
        width: 72;
        height: auto;
        max-height: 38;
        background: $surface;
        border: thick $accent;
        padding: 1 2;
    }

    AboutScreen #about-title {
        height: 3;
        content-align: center middle;
        text-style: bold;
        background: $accent;
        color: $text;
        margin-bottom: 1;
    }

    AboutScreen #about-content {
        height: auto;
        padding: 1;
    }

    AboutScreen #about-footer {
        height: 1;
        content-align: center middle;
        color: $text-muted;
        margin-top: 1;
    }
    """

    BINDINGS = [
        Binding("escape", "close", "Close"),
        Binding("q", "close", "Close"),
    ]

    def compose(self) -> ComposeResult:
        """Erstellt das About-Layout."""
        with Vertical():
            yield Static(f"Sitemap Generator v{__version__}", id="about-title")
            yield Static(
                f"{t('about.description')}\n"
                "\n"
                f"{t('about.quote')}\n"
                "\n"
                "[dim]https://github.com/michaelblaess/sitemap-generator[/dim]",
                id="about-content",
            )
            yield Static(t("about.footer"), id="about-footer")

    def action_close(self) -> None:
        """Schliesst den Dialog."""
        self.dismiss()
