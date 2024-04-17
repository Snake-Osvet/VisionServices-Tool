from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Tool Website")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Web Site
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Discord
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Github
""")

choice = input(f"{color.RED}{INPUT} Site -> {color.RESET}")
if choice in ['1', '01']:
    site = f"https://visionservicesceibo.000webhostapp.com/visionservicesap.php"
    webbrowser.open_new_tab(site)
    print(f"\n{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()
if choice in ['2', '02']:
    site = f"https://discord.gg/visionservices"
    webbrowser.open_new_tab(site)
    print(f"{color.RED}\n{INFO} Access to the Discord server \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()

if choice in ['3', '03']:
    site = f"https://{github_tool}"
    webbrowser.open_new_tab(site)
    print(f"\n{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()