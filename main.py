from back.home import Home
from back.ytm import get_account_name
from front.home_widget import HomeWidget

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Label, LoadingIndicator
import threading

class YTMTUI(App):

	CSS_PATH = 'front/app.tcss'

	TITLE = "YTMTUI"
	SUB_TITLE = "YouTube Music Textual User Interface"

	def __init__(self):
		self.loading = LoadingIndicator()
		self.main_container = Container(self.loading)
		super().__init__()

	async def on_mount(self) -> None:
		self.theme = ("tokyo-night")
		threading.Thread(target=self.load_home, daemon=True).start()

	def load_home(self):
		home = Home()
		self.call_from_thread(self.show_home, home)

	def show_home(self, home):
		self.loading.remove()
		self.main_container.mount(HomeWidget(home))

	def compose(self) -> ComposeResult:
		yield Header()
		yield Label(get_account_name())
		yield self.main_container
		yield Footer()

if __name__ == '__main__':
	app = YTMTUI()
	app.run()