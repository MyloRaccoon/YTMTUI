class Thumbnail:

	def __init__(self, url: str, width: int, height: int) -> None:
		self.url = url
		self.width = width
		self.height = height

	def to_data(self) -> dict:
		return {
			'url': self.url,
			'width': self.width,
			'height': self.height
		}

def get_thumbnail(json: dict) -> Thumbnail:
	return Thumbnail(
		json['url'],
		json['width'],
		json['height']
	)