from SONALI.core.bot import RAUSHAN
from SONALI.core.dir import dirr
from SONALI.core.git import git
from SONALI.core.userbot import Userbot
from SONALI.misc import dbb, heroku


from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAUSHAN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
