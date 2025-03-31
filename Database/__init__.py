from Database.core.bot import Anony
from Database.core.dir import dirr
from Database.core.git import git
from Database.core.userbot import Userbot
from Database.misc import dbb, heroku

from .logging import LOGGER

dirr()
#git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
HELPABLE = {}
