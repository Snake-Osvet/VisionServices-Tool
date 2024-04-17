from Config.Util import *
from Config.Config import *
try:
    import requests
    import json
except Exception as e:
   ErrorModule(e)
   
Title("Roblox Cookie Info")

cookie = input(f"{color.RED}\n{INPUT} Cookie -> {color.WHITE}")
print(f"{color.RED}{WAIT} Information Recovery..{reset}")
try:
    info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
    print(info.json())
    information = json.loads(info.text)
    status = "Valid"
except:
    status = "Invalid"

try:
    username_roblox = information['UserName']
except:
    username_roblox = "None"

try:
    user_id_roblox = information["UserID"]
except:
    user_id_roblox = "None"

try:
    robux_roblox = information["RobuxBalance"]
except:
    robux_roblox = "None"
try:
    premium_roblox = information["IsPremium"]
except:
    premium_roblox = "None"

try:
    avatar_roblox = information["ThumbnailUrl"]
except:
    avatar_roblox = "None"

try:
    builders_club_roblox = information["IsAnyBuildersClubMember"]
except:
    builders_club_roblox = "None"


print(f"""
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Status        : {color.WHITE}{status}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Username      : {color.WHITE}{username_roblox}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Id            : {color.WHITE}{user_id_roblox}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Robux         : {color.WHITE}{robux_roblox}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Premium       : {color.WHITE}{premium_roblox}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Builders Club : {color.WHITE}{builders_club_roblox}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar        : {color.WHITE}{avatar_roblox}{color.RED}
""")
Continue()
Reset()