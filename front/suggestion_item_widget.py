from back.item import Item
from textual.widget import Widget
from textual.widgets import Button, Label
from textual.app import ComposeResult

class SuggestionItemWidget(Widget):

	def __init__(self, title, btn, subtitle, action):
		self.title = title
		self.subtitle = subtitle
		self.btn = btn
		self.btn_id = None
		self.action = action
		super().__init__()

	def compose(self) -> ComposeResult:
		yield Button(self.btn, id=self.btn_id, action=self.action)

	def on_mount(self) -> None:
		self.border_title = self.title
		self.border_subtitle = self.subtitle

	# def on_button_pressed(self, event: Button.Pressed) -> None:
	# 	if event.button.id == self.btn.id and self.action is not None:
	# 		self.action()