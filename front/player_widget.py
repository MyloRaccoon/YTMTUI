from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button, Label, ProgressBar
from textual.app import ComposeResult

from back.song import Song, get_song, get_watch_list
from back.player import Player


class PlayerWidget(Widget):

	progress = reactive(0.0)
	finished = reactive(False)

	def __init__(self) -> None:
		self.progress_bar = ProgressBar(total=100, show_percentage=False, show_eta=False)
		self.started = False
		self.current_song_id = None
		self.watch_list = []
		self.played_song = []
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
			self.current_song_id = None
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
			yield Button("⏮", id='previous', classes="player-btn", disabled=True)
			yield Button("⏪", id="minus", classes="player-btn")
			yield Button("⏸", id="pause", classes="player-btn")
			yield Button("⏩", id="plus", classes="player-btn")
			yield Button("⏭", id='next', classes="player-btn")


	def play(self, song_id):
		song = get_song(song_id)
		self.query_one('#title_label').update(song.title)
		self.query_one('#artist_label').update(song.artist)
		self.app.player.send("play", song.url)
		self.current_song_id = song_id

	def play_next(self):
		self.played_song.append(self.current_song_id)
		if len(self.watch_list) != 0:
			song_id = self.watch_list.pop(0)
			self.play(song_id)
			if len(self.watch_list) == 0:
				self.watch_list = get_watch_list(song_id, 25)

	# def play_previous(self):
	# 	if len(self.played_song) != 0:
	# 		song_id = self.played_song.pop(-1)
	# 		self.current_song_id = song_id
	# 		self.play(song_id)


	async def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "pause":
			self.app.player.send("pause")
			btn = self.query_one('#pause')
			btn.label = '⏸' if btn.label == '▶' else '▶'
		elif event.button.id == "plus":
			self.app.player.send("+10")
		elif event.button.id == "minus":
			self.app.player.send("-10")
		elif event.button.id == "next":
			self.play_next()
		# elif event.button.id == "previous":
		# 	self.play_previous()
		self.update_progress()