from back.player import play
from back.song import Song
from front.suggestion_item_widget import SuggestionItemWidget
from textual.widget import Widget
from textual.widgets import Button, Label
from textual.app import ComposeResult

class SongWidget(SuggestionItemWidget):

	def __init__(self, song: Song):
		self.song = song
		super().__init__(song.item_type, song.title, song.artist, "play")

	def action_play(self):
		play(self.song)