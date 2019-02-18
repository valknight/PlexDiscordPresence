import json

with open("config.json") as f:
    config = json.loads(f.read())

apikey = config['apikey'] # tautulli API key
host = config['host'] # host and port of tautulli (include base URL for reverse proxy)
username = config['username'] # if blank, any user will be reported on your profile
client_id = config['client_id']
libraries = config['libraries'] # set this to [] if you want to use any library