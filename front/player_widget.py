from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button, Label, ProgressBar
from textual.app import ComposeResult
import threading, asyncio
from textual.containers import Container, Center

from back.song import Song, get_next_song, get_song
from back.player import Player


class PlayerWidget(Widget):

	progress = reactive(0.0)
	finished = reactive(False)

	def __init__(self) -> None:
		self.progress_bar = ProgressBar(total=100, show_percentage=False, show_eta=False)
		self.started = False

		super().__init__()

	def on_mount(self):
		self.update_timer = self.set_interval(0.5, self.update_progress, pause = False)
		self.set_interval(0.1, self.update_finished, pause = False)


	def update_finished(self):
		if not self.started:
			self.finished = False
			if self.app.player.is_finished() is False:
				self.started = True
		else:
			self.finished = self.app.player.is_finished()


	def watch_finished(self):
		if self.finished:
			self.started = False
			self.play_next()


	def update_progress(self):
		position = self.app.player.get_position()
		duration = self.app.player.get_duration()
		if duration != 0:
			self.progress = position / duration * 100
		

	def watch_progress(self):
		position = self.app.player.get_position()
		duration = self.app.player.get_duration()
		pos_format = f'{position//60}:{position%60}'
		dur_format = f'{duration//60}:{duration%60}'
		self.query_one('#position_label').update(pos_format)
		self.query_one('#duration_label').update(dur_format)
		self.progress_bar.update(progress=self.progress)
		
	
		

	def compose(self) -> ComposeResult:
		with Horizontal():
			yield Label('---', id='title_label', classes='player_label')
			yield Label('---', id='artist_label', classes='player_label')
		with Horizontal():
			yield Label('0', id='position_label')
			yield self.progress_bar
			yield Label('0', id='duration_label')
		with Horizontal():
			yield Button("- 10", id="minus", classes="player-btn")
			yield Button("⏸", id="pause", classes="player-btn")
			yield Button("+ 10", id="plus", classes="player-btn")


	def play(self, song_id):
		song = get_song(song_id)
		self.query_one('#title_label').update(song.title)
		self.query_one('#artist_label').update(song.artist)
		self.app.player.send("play", song.url)
		self.current_song_id = song_id

	def play_next(self):
		if self.current_song_id is not None:
			self.play(get_next_song(self.current_song_id))


	async def on_button_pressed(self, event: Button.Pressed) -> None:
		self.update_progress()
		if event.button.id == "pause":
			self.app.player.send("pause")
			btn = self.query_one('#pause')
			btn.label = '⏸' if btn.label == '▶' else '▶'
		elif event.button.id == "plus":
			self.app.player.send("+10")
		elif event.button.id == "minus":
			self.app.player.send("-10")
