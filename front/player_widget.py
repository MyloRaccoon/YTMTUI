from back.item import Item
from textual.widget import Widget
from textual.widgets import Button, Label
from textual.app import ComposeResult

from back.player import play

class Player(Widget):

	def __init__(self, song: Song) -> None:
		self.song = song
		super().__init__()

	def compose(self) -> ComposeResult:
		yield Label(self.song.title)

	def on_mount(self) -> None:
		play(self.song)