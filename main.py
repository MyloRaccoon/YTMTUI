from textual.events import Event
from textual.geometry import Spacing
from back.home import Home, home_loop, pull_home
from back.player import Player
from back.song import get_song, Song, get_watch_list
from back.ytm import get_account_name
from front.home_widget import HomeWidget
from front.player_widget import PlayerWidget

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Header, Label, LoadingIndicator, Button
import threading

class YTMTUI(App):

	CSS_PATH = 'front/app.tcss'

	TITLE = "YTMTUI"
	SUB_TITLE = "YouTube Music Textual User Interface"

	def __init__(self):
		self.loading = LoadingIndicator()
		self.home = None
		self.main_container = Container(self.loading, id="main-container")
		self.player_container = Container(id="player-container")
		self.player_widget = PlayerWidget()
		self.player = Player()
		super().__init__()

	async def on_mount(self) -> None:
		# self.theme = ("tokyo-night")
		threading.Thread(target=self.load_home, daemon=True).start()
		threading.Thread(target=home_loop, daemon=True).start()

	def load_home(self):
		self.home = HomeWidget(pull_home())
		self.call_from_thread(self.show_home, self.home)

	def show_home(self, home):
		self.loading.remove()
		self.main_container.mount(home)

	def play_song(self, song_id: str):
		self.player_widget.play(song_id)
		self.player_widget.watch_list = get_watch_list(song_id, 25)

	def compose(self) -> ComposeResult:
		yield Header()
		with Horizontal():
			yield Label(f'Hello {get_account_name()} !', classes='top-element')
			yield Button("reload", id="reload", classes='top-element')
			yield Button("quit", action="app.quit", classes='top-element')
		yield self.main_container
		yield self.player_widget
		yield Footer()

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id != 'reload':
			return

		if self.home == None:
			return

		self.home.remove()
		self.main_container.mount(self.loading)
		threading.Thread(target=self.load_home, daemon=True).start()


if __name__ == '__main__':
	app = YTMTUI()
	app.run()