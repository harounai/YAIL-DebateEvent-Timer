import pathlib
import webbrowser


def main() -> None:
    html = pathlib.Path(__file__).parent.parent.parent / "timer.html"
    webbrowser.open(html.resolve().as_uri())
