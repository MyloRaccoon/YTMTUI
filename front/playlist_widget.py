from back.playlist import Playlist
from front.suggestion_item_widget import SuggestionItemWidget

class PlaylistWidget(SuggestionItemWidget):

	def __init__(self, playlist: Playlist):
		self.playlist = playlist
		super().__init__(playlist.item_type, playlist.title)