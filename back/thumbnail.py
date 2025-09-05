class Thumbnail:

	def __init__(self, url: str, width: int, height: int) -> None:
		self.url = url
		self.width = width
		self.height = height

def get_thumbnail(json: dict) -> Thumbnail:
	return Thumbnail(
		json['url'],
		json['width'],
		json['height']
	)