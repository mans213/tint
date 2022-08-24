import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "11265059"))
API_HASH = getenv("API_HASH", "3d566d6fe2e6b6a522f13e875bd2eb61")
BOT_TOKEN = getenv("BOT_TOKEN", "5351917074:AAFwS64L_Lc4C0M9a00Cwhsfearc6Iqm6hU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BABlFPfUw89tPGIH4VgKImxcC_fE65sHeCvdMiKomrioEg_mXFG4AJNF0qvMsmeTofw3snuUV8Za1yqtFBlsmDjV_ruEsW3xYACqKaIWFCrXF35KKKMctTUK9QE7pOYulKLFcy1ezW4ltxCphd3ies3tBO-qwTloGeZb0AD8GfMklAjzSXZRFEveUte8jYo2qsm7IT0TouOOvW7oFATFQ4iu5SpECB8XfGxS6FQheSUWtz6BMsQ8Z4Usf551Xg5_CctN_J-noqmAkIxofBELqG0lDr47SGmbm1nph499MmPJjooa5EoLMDPDRj-QwK4aiIUQZ2Na9CsKTWAsPQgO4uMtAAAAAUvBdQYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
