import rich

import os, sys
import time

from rich.console import Console


console = Console()

console.print("Botnet belongs to the channel: https://t.me/pepe_devs\n")

exactly = console.input(
"[bold red]Install exactly? [white](y/n) "
)

if exactly == "y":

   console.print("[bold green][ ~ ] [white]Cloning repo...\n")
   os.system("git clone https://github.com/Madara225/telegram-raid-botnet-pyrogram\n")
   console.print("[bold green][ + ] [white]Installed\n")

   console.print("[bold green][ ~ ] [white]Running...\n")
   os.system("pip3 install phonenumbers\n")
   os.system("cd telegram-raid-botnet-pyrogram && pip3 install -r requirements.txt && cat README.md && python3 main.py\n")
   console.print("[bold green][ + ] [white]Installed\n")


elif exactly == "n":
     sys.exit()
