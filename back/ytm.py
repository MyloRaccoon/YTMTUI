from ytmusicapi import YTMusic
import ytmusicapi
from dotenv import load_dotenv
import os

load_dotenv()
headers = os.getenv('HEADERS')

ytmusicapi.setup(filepath="browser.json", headers_raw=headers)
YTM = YTMusic("browser.json")

def get_account_name() -> str:
	return YTM.get_account_info()['accountName']
