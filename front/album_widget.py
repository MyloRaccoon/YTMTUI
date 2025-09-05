from back.album import Album
from back.artist import get_artist
from front.suggestion_item_widget import SuggestionItemWidget
from textual.widget import Widget
from textual.widgets import Button, Label
from textual.app import ComposeResult

class AblumWidget(SuggestionItemWidget):

	def __init__(self, album: Album):
		self.album = album
		super().__init__(album.item_type, album.title)