from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   

Title("Discord Webhook Delete")
webhook_url = input(f"{color.RED}\n{INPUT} URL Webhook -> {color.RESET}")
CheckWebhook(webhook_url)
try:
    response = requests.delete(webhook_url)
    response.raise_for_status()
    print(f"{color.RED}{INFO} Webhook Deleted.")
    Continue()
    Reset()
except:
    ErrorWebhook()