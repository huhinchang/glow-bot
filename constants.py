from datetime import timedelta, timezone
from dotenv import load_dotenv
from os import getenv
import pytz

load_dotenv()

# ENV Vars for Bot
GUILD = int(getenv("GUILD_ID"))
TOKEN = getenv("DISCORD_TOKEN")
GLENTRE_STATUS_CHANNEL_ID = int(getenv("GLENTRE_STATUS_CHANNEL_ID"))

# Glentre closing task constants
EST = pytz.timezone("US/Eastern")
GLENTRE_PREFIX = "glentre-"
GLENTRE_CLOSED_IDENTIFIER = "closed"
GLENTRE_CLOSED_STATUS = "closed ❌"
GLENTRE_OPEN_STATUS = "open ✅"

# Kissing constants
KISS_NIGHT_REACTION = "‼️"

# Wishing constants
WISH_CHANNEL_ID = int(getenv("WISH_CHANNEL_ID"))
WISH_INVALID = "❓"
WISH_SPECIAL = { # must be ordered in decreasing length so that there are no conficts because of substrings 
    "distinguish" : "🕵️",
    "horseradish" : "🥪",
    "impoverish" : "🥀",
    "accomplish" : "🏆",
    "extinguish" : "🧯",
    "outlandish" : "🤨",
    "gibberish" : "🥴",
    "stockfish" : "♟️",
    "shellfish" : "🦪",
    "replenish" : "🌱",
    "establish" : "🏦",
    "squeamish" : "😖",
  # "jellyfish" : "🪼", # not available in discord
    "astonish" : "🤯",
    "crayfish" : "🦞",
    "sluggish" : "🐌",
    "flourish" : "😎",
    "skirmish" : "🤺",
    "snobbish" : "🧐",
    "vanquish" : "⚔️",
    "starfish" : "⭐",
    "demolish" : "💥",
    "british" : "🇬🇧",
    "anguish" : "💀",
    "finnish" : "🇫🇮",
    "bullish" : "📈",
    "bearish" : "📉",
    "abolish" : "🙅",
    "publish" : "📰",
    "garnish" : "🍝",
    "stylish" : "🤵",
    "rubbish" : "🗑️",
    "furnish" : "🪑",
    "selfish" : "👿",
    "swedish" : "🇸🇪",
    "delish" : "😋",
    "perish" : "🪦",
    "squish" : "🥺",
    "famish" : "😫",
    "radish" : "🥗",
    "polish" : "🇵🇱",
    "fetish" : "😳",
    "elvish" : "🧝",
    "relish" : "🌭",
    "vanish" : "🫥",
    "banish" : "🚶",
    "finish" : "🏁",
    "lavish" : "🍾",
    "jewish" : "🕎",
    "irish" : "🇮🇪",
    "phish" : "📧",
    "swish" : "💫",
    "amish" : "👨‍🌾",
    "wish" : "🙏",
    "fish" : "🐟",
    "dish" : "🍽️",
    "bish" : "😢",
}