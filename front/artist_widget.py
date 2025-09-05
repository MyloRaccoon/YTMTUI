from back.artist import Artist
from back.artist import get_artist
from front.suggestion_item_widget import SuggestionItemWidget
from textual.widget import Widget
from textual.widgets import Button
from textual.app import ComposeResult

class ArtistWidget(SuggestionItemWidget):

	def __init__(self, artist: Artist):
		self.artist = artist
		super().__init__(artist.item_type, artist.name, artist.subscribers)