import tautulli
import config
import time
from config import client_id
from pypresence import Presence

RPC = Presence(client_id)

def main():
    RPC.connect()
    print("Check discord")
    while True:
        current_activity = tautulli.get_my_activity()
        if current_activity is not None:
            to_send = dict(state=current_activity['title'])
            if current_activity['grandparent_title'] != "":
                to_send['details'] = current_activity['grandparent_title']
            RPC.update(**to_send)
        else:
            RPC.clear()
        time.sleep(15) # rich presence is limited to once per 15 seconds

if __name__ == "__main__":
    main()
# print(get_data("get_server_friendly_name"))