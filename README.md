# Plex Rich Presence Integration

### What does this do?

This shows what you're currently listening to / watching on Plex, using Tautulli's API, as a rich presence in Discord.

### Requirements

- Tautulli
- Discord
- Python 3.5+

### Installation

1. Clone / download this repo
2. Change directory to where you downloaded it
3. Run `pip install -r requirements.txt`
4. Change config options (copy config.example.json to config.json, and fill it out - details of how to do this are below)
5. Run `python main.py`

We recommend you use a virtual environment. If you don't, you may need admin/root rights to run `pip install`, and your binary may be `pip3` and `python3` respectively.

### Config options

The main JSON file should be something like so:

```json
{
    "apikey": "changeme",
    "host" : "127.0.0.1:8181",
    "username" : "",
    "client_id" : "changeme",
    "libraries": []
}
```
Below is a table with a description of each config option, and what it means.

| Config key | Description                                                                                                                               | Example                             |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| apikey     | The API key for your Tautulli instance. Find it under Settings > Web Interface                                                            | N/A                                 |
| host       | The host Tautulli is being hosted. Make sure this includes the base URL if you use one.                                                   | 192.168.1.2:8181/tautulli           |
| username   | The username of the Plex user you want to show on your profile. If you leave "", we'll show data from any user                            | PlexUsername                        |
| client_id  | Client ID for your Discord Application. Find it in your Discord Developer console.                                                        | N/A                                 |
| libraries  | List of libraries you want to restrict displaying media from. If you leave this as [], your playback will be shown, no matter the library | ["TV Shows", "Music", "Audiobooks"] |

### FAQ

#### Why does it take a while for Discord to show what I'm playing?

Discord only allows for updates of rich presence to be sent every 15 seconds. As such, we restrict our updates to be courteous of this, so you have to wait (maximum) 15 seconds before any updates will display on your profile.

#### Why do I need Tautulli?

I use Tautulli because it's really great for wrapping any changes being made on Plex's side of things, as well as handling all the fancy stuff like getting tokens, and authenticating with Plex. It's also great to have if you happen to want to look at bandwidth monitoring, or just logging in Plex, and so most heavy users of Plex will have it installed anyway.

### License

This project is licensed under the MIT license.
