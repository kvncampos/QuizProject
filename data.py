import requests
import json

db_api = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
json_request = db_api.json()
pretty_json = json.dumps(json_request, indent=4)

json_list = json_request["results"]







