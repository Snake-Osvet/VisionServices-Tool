from Settings.Program.Config.Config import *
from Settings.Program.Config.Util import *
try:
   import requests
   import re
   import webbrowser
except Exception as e:
   ErrorModule(e)

Clear()
Title("Menu")
try:
   url = url_config
   response = requests.get(url)
   if response.status_code == 200:
       content = response.text
       match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
       if match:
           current_version = match.group(1)
           if current_version != version_tool:
               print(f"{color.RED}[!] | Please download the new version of the tool ! {color.WHITE}{version_tool}{color.LIGHTYELLOW_EX} -> {color.WHITE}{current_version}{color.RED}")
               webbrowser.open(github_tool)
               time.sleep(2)
               webbrowser.open(url_downloads)
               input(f"{color.RED}[!] | Enter to still use this version -> {color.RESET}")
               popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {color.WHITE}{version_tool}{color.LIGHTYELLOW_EX} -> {color.WHITE}{current_version}{color.RED}"
           else:
               popup_version = ""
       else:
           popup_version = ""
   else:
       popup_version = ""
except:
   popup_version = ""

option_01 = "Tool-Info"
option_02 = "Tool-Website"
option_03 = "Ip-Info"
option_04 = "Ip-Pinger"
option_05 = "Ip-Generator"
option_06 = "Ip-Website"
option_07 = "Dox-Tracker"
option_08 = "Dox-Create"
option_09 = "Number-Info"
option_10 = "Email-Info"     
option_11 = "Builder-Stealer"
option_12 = "Sql-Vulnerability"
option_13 = "Search-In-DataBase"
option_14 = "Illegal-Website"
option_15 = "Discord-Get-Your-Token"
option_16 = "Discord-Token-Info"
option_17 = "Discord-Token-Nuker"
option_18 = "Discord-Token-Joiner"
option_19 = "Discord-Token-Leaver"
option_20 = "Discord-Token-Login"
option_21 = "Discord-Token-To-Id-And-Brute"
option_22 = "Discord-Token-Server-Raid"
option_23 = "Discord-Token-Spammer"
option_24 = "Discord-Token-Delete-Friends"
option_25 = "Discord-Token-Block-Friends"
option_26 = "Discord-Token-Mass-Dm"
option_27 = "Discord-Token-Delete-Dm"
option_28 = "Discord-Token-Status-Changer"
option_29 = "Discord-Token-Language-Changer"
option_32 = "Discord-Token-House-Changer"
option_33 = "Discord-Token-Theme-Changer"
option_34 = "Discord-Token-Generator"
option_35 = "Discord-Bot-Server-Nuker"
option_36 = "Discord-Bot-Invite-To-Id"
option_37 = "Discord-Server-Info"
option_38 = "Discord-Nitro-Generator"
option_39 = "Discord-Webhook-Info"
option_40 = "Discord-Webhook-Delete"
option_41 = "Discord-Webhook-Spammer"
option_42 = "Discord-Webhook-Generator"
option_43 = "Roblox-Cookie-Login"
option_44 = "Roblox-Cookie-Info"
option_45 = "Roblox-User-Info"
option_46 = "Roblox-Id-Info"
option_47 = ""
option_48 = ""
option_49 = ""
option_50 = ""
option_61 = "" 
option_62 = ""
option_63 = ""
option_64 = ""
option_65 = ""
option_66 = ""
option_67 = ""
option_68 = ""
option_69 = ""

option_next = "Next Page >>"
option_previous = "<< Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = option_29.ljust(30)[:30].replace("-", " ")

option_32_txt = option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = option_39.ljust(30)[:30].replace("-", " ")
option_40_txt = option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = option_49.ljust(30)[:30].replace("-", " ")
option_50_txt = option_50.ljust(30)[:30].replace("-", " ")
option_61_txt = option_61.ljust(30)[:30].replace("-", " ")
option_62_txt = option_62.ljust(30)[:30].replace("-", " ")
option_63_txt = option_63.ljust(30)[:30].replace("-", " ")
option_64_txt = option_64.ljust(30)[:30].replace("-", " ")
option_65_txt = option_65.ljust(30)[:30].replace("-", " ")
option_66_txt = option_66.ljust(30)[:30].replace("-", " ")
option_67_txt = option_67.ljust(30)[:30].replace("-", " ")
option_68_txt = option_68.ljust(30)[:30].replace("-", " ")
option_69_txt = option_69.ljust(30)[:30].replace("-", " ")

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

page1 = f"""{white}[{red}Page n°1{white}]
   {white}[{red}01{white}] {red}->{white} {option_01_txt} {white}[{red}11{white}] {red}->{white} {option_11_txt} {white}[{red}21{white}] {red}->{white} {option_21_txt}
   {white}[{red}02{white}] {red}->{white} {option_02_txt} {white}[{red}12{white}] {red}->{white} {option_12_txt} {white}[{red}22{white}] {red}->{white} {option_22_txt}
   {white}[{red}03{white}] {red}->{white} {option_03_txt} {white}[{red}13{white}] {red}->{white} {option_13_txt} {white}[{red}23{white}] {red}->{white} {option_23_txt}
   {white}[{red}04{white}] {red}->{white} {option_04_txt} {white}[{red}14{white}] {red}->{white} {option_14_txt} {white}[{red}24{white}] {red}->{white} {option_24_txt}
   {white}[{red}05{white}] {red}->{white} {option_05_txt} {white}[{red}15{white}] {red}->{white} {option_15_txt} {white}[{red}25{white}] {red}->{white} {option_25_txt}
   {white}[{red}06{white}] {red}->{white} {option_06_txt} {white}[{red}16{white}] {red}->{white} {option_16_txt} {white}[{red}26{white}] {red}->{white} {option_26_txt}
   {white}[{red}07{white}] {red}->{white} {option_07_txt} {white}[{red}17{white}] {red}->{white} {option_17_txt} {white}[{red}27{white}] {red}->{white} {option_27_txt}
   {white}[{red}08{white}] {red}->{white} {option_08_txt} {white}[{red}18{white}] {red}->{white} {option_18_txt} {white}[{red}28{white}] {red}->{white} {option_28_txt}
   {white}[{red}09{white}] {red}->{white} {option_09_txt} {white}[{red}19{white}] {red}->{white} {option_19_txt} {white}[{red}29{white}] {red}->{white} {option_29_txt}
   {white}[{red}10{white}] {red}->{white} {option_10_txt} {white}[{red}20{white}] {red}->{white} {option_20_txt} {white}[{red}30{white}] {red}-> {option_next_txt}"""

page2 = f"""{white}[{red}Page n°2{white}]
   {white}[{red}31{white}] {red}-> {option_previous_txt} {white}[{red}41{white}] {red}->{white} {option_41_txt} {white}[{red}61{white}] {red}->{white} {option_61_txt}
   {white}[{red}32{white}] {red}->{white} {option_32_txt} {white}[{red}42{white}] {red}->{white} {option_42_txt} {white}[{red}62{white}] {red}->{white} {option_62_txt}
   {white}[{red}33{white}] {red}->{white} {option_33_txt} {white}[{red}43{white}] {red}->{white} {option_43_txt} {white}[{red}63{white}] {red}->{white} {option_63_txt}
   {white}[{red}34{white}] {red}->{white} {option_34_txt} {white}[{red}44{white}] {red}->{white} {option_44_txt} {white}[{red}64{white}] {red}->{white} {option_64_txt}
   {white}[{red}35{white}] {red}->{white} {option_35_txt} {white}[{red}45{white}] {red}->{white} {option_45_txt} {white}[{red}65{white}] {red}->{white} {option_65_txt}
   {white}[{red}36{white}] {red}->{white} {option_36_txt} {white}[{red}46{white}] {red}->{white} {option_46_txt} {white}[{red}66{white}] {red}->{white} {option_66_txt}
   {white}[{red}37{white}] {red}->{white} {option_37_txt} {white}[{red}47{white}] {red}->{white} {option_47_txt} {white}[{red}67{white}] {red}->{white} {option_67_txt}
   {white}[{red}38{white}] {red}->{white} {option_38_txt} {white}[{red}48{white}] {red}->{white} {option_48_txt} {white}[{red}68{white}] {red}->{white} {option_68_txt}
   {white}[{red}39{white}] {red}->{white} {option_39_txt} {white}[{red}49{white}] {red}->{white} {option_49_txt} {white}[{red}69{white}] {red}->{white} {option_69_txt}
   {white}[{red}40{white}] {red}->{white} {option_40_txt} {white}[{red}50{white}] {red}->{white} {option_50_txt} {white}[{red}60{white}] {red}-> {option_next_txt}"""

while True:
   try:
      with open("Settings/Program/Config/Page.txt", "r") as file:
         page = file.read()
      if page in ["1"]:
         page = page1
         Title("Page 1")
      elif page in ["2"]:
         page = page2
         Title("Page 2")
      else:
         page = page1
         Title("Page 1")
   except:
      page = page1
      Title("Page 1")
   Clear()
   print(f"""{popup_version}{red}                                                                                                  

 /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$        /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$  /$$$$$$ 
| $$   | $$|_  $$_/ /$$__  $$|_  $$_/ /$$__  $$| $$$ | $$       /$$__  $$| $$_____/| $$__  $$| $$   | $$|_  $$_/ /$$__  $$| $$_____/ /$$__  $$
| $$   | $$  | $$  | $$  \__/  | $$  | $$  \ $$| $$$$| $$      | $$  \__/| $$      | $$  \ $$| $$   | $$  | $$  | $$  \__/| $$      | $$  \__/
|  $$ / $$/  | $$  |  $$$$$$   | $$  | $$  | $$| $$ $$ $$      |  $$$$$$ | $$$$$   | $$$$$$$/|  $$ / $$/  | $$  | $$      | $$$$$   |  $$$$$$ 
 \  $$ $$/   | $$   \____  $$  | $$  | $$  | $$| $$  $$$$       \____  $$| $$__/   | $$__  $$ \  $$ $$/   | $$  | $$      | $$__/    \____  $$
  \  $$$/    | $$   /$$  \ $$  | $$  | $$  | $$| $$\  $$$       /$$  \ $$| $$      | $$  \ $$  \  $$$/    | $$  | $$    $$| $$       /$$  \ $$
   \  $/    /$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/| $$ \  $$      |  $$$$$$/| $$$$$$$$| $$  | $$   \  $/    /$$$$$$|  $$$$$$/| $$$$$$$$|  $$$$$$/
    \_/    |______/ \______/ |______/ \______/ |__/  \__/       \______/ |________/|__/  |__/    \_/    |______/ \______/ |________/ \______/ 

                                           	  	   {white}discord.gg/visionservices
                                                     	     	{white}╔════════════╗
                                                     	     	{white}║ {red}Multi-Tool{white} ║
                                                     	     	{white}╚════════════╝
   {page}
""")
   choice = input(f"""{red}┌───({white}{username_pc}@visionservices{red})─[{white}~{red}]
└──{white}$ {reset}""")

   if choice in ['1', '01']:
      StartProgram(f"{option_01}.py")

   elif choice in ['2', '02']:
      StartProgram(f"{option_02}.py")

   elif choice in ['3', '03']:
      StartProgram(f"{option_03}.py")

   elif choice in ['4', '04']:
      StartProgram(f"{option_04}.py")

   elif choice in ['5', '05']:
      StartProgram(f"{option_05}.py")

   elif choice in ['6', '06']:
      StartProgram(f"{option_06}.py")

   elif choice in ['7', '07']:
      StartProgram(f"{option_07}.py")

   elif choice in ['8', '08']:
      StartProgram(f"{option_08}.py")

   elif choice in ['9', '09']:
      StartProgram(f"{option_09}.py")

   elif choice in ['10']:
      StartProgram(f"{option_10}.py")

   elif choice in ['11']:
      StartProgram(f"{option_11}.py")

   elif choice in ['12']:
      StartProgram(f"{option_12}.py")

   elif choice in ['13']:
      StartProgram(f"{option_13}.py")

   elif choice in ['14']:
      StartProgram(f"{option_14}.py")

   elif choice in ['15']:
      StartProgram(f"{option_15}.py")

   elif choice in ['16']:
      StartProgram(f"{option_16}.py")

   elif choice in ['17']:
      StartProgram(f"{option_17}.py")

   elif choice in ['18']:
      StartProgram(f"{option_18}.py")

   elif choice in ['19']:
      StartProgram(f"{option_19}.py")
      
   elif choice in ['20']:
      StartProgram(f"{option_20}.py")
      
   elif choice in ['21']:
      StartProgram(f"{option_21}.py")
      
   elif choice in ['22']:
      StartProgram(f"{option_22}.py")
      
   elif choice in ['23']:
      StartProgram(f"{option_23}.py")
      
   elif choice in ['24']:
      StartProgram(f"{option_24}.py")
      
   elif choice in ['25']:
      StartProgram(f"{option_25}.py")
      
   elif choice in ['26']:
      StartProgram(f"{option_26}.py")
      
   elif choice in ['27']:
      StartProgram(f"{option_27}.py")
      
   elif choice in ['28']:
      StartProgram(f"{option_28}.py")
      
   elif choice in ['29']:
      StartProgram(f"{option_29}.py")
      

   elif choice in ['30']:
      page = page2
      with open("Settings/Program/Config/Page.txt", "w") as file:
         file.write("2")
         Title("Page 2")

   elif choice in ['31']:
      page = page1
      with open("Settings/Program/Config/Page.txt", "w") as file:
         file.write("1")
         Title("Page 1")


   elif choice in ['32']:
      StartProgram(f"{option_32}.py")
      
   elif choice in ['33']:
      StartProgram(f"{option_33}.py")
      
   elif choice in ['34']:
      StartProgram(f"{option_34}.py")

   elif choice in ['35']:
      StartProgram(f"{option_35}.py")

   elif choice in ['36']:
      StartProgram(f"{option_36}.py")

   elif choice in ['37']:
      StartProgram(f"{option_37}.py")

   elif choice in ['38']:
      StartProgram(f"{option_38}.py")

   elif choice in ['39']:
      StartProgram(f"{option_39}.py")

   elif choice in ['40']:
      StartProgram(f"{option_40}.py")

   elif choice in ['41']:
      StartProgram(f"{option_41}.py")

   elif choice in ['42']:
      StartProgram(f"{option_42}.py")

   elif choice in ['43']:
      StartProgram(f"{option_43}.py")
   
   elif choice in ['44']:
      StartProgram(f"{option_44}.py")

   elif choice in ['45']:
      StartProgram(f"{option_45}.py")

   else:
      ErrorChoiceStart()