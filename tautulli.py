import requests
import json
from config import host, apikey, username, libraries


def get_data(cmd, host=host, apikey=apikey):
    r = requests.get(
        "http://{}/api/v2?apikey={}&cmd={}".format(host, apikey, cmd))
    # print(r.status_code)
    return dict(data=json.loads(r.text), code=r.status_code)


def get_activity(host=host, apikey=apikey):
    return get_data("get_activity", host=host, apikey=apikey)['data']


def get_my_activity(host=host, apikey=apikey, username=username, libraries=libraries):
    data = get_activity(host=host, apikey=apikey)['response']['data']
    # TODO: Add support for more than one stream at once
    for stream in data['sessions']:
        if (len(libraries) == 0 or stream['library_name'] in libraries) and (username == "" or stream['user'] == username):
            print(json.dumps(stream, indent=4))
            return stream
    return None


def get_server_name(host=host, apikey=apikey):
    return get_data("get_server_friendly_name", host=host, apikey=apikey)['data']
