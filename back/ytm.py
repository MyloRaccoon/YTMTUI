from ytmusicapi import YTMusic

YTM = YTMusic("browser.json")

def get_account_name() -> str:
	return YTM.get_account_info()['accountName']