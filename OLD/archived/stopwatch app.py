from textual.app import App, ComposeResult

# Button - which creates a clickable button, and Static which is a base class for a simple control. 
# We've also imported Container from textual.containers which is a Widget which contains other widgets.

from textual.containers import Container
from textual.widgets import Header, Footer, Button, Static


# The App class is where most of the logic of Textual apps is written. 
# It is responsible for loading configuration, setting up widgets, handling keys, and more.

class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    # compose() is where we construct a user interface with widgets. The compose() method may return 
    # a list of widgets, but it is generally easier to yield them (making this method a generator). 
    # In the example code we yield an instance of each of the widget classes we imported, i.e. Header() and Footer().
   
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()