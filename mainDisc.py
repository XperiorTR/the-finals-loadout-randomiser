import random # RNG
import discord
import os
from discord.ext import commands

class classes: # Class for the classes
    def __init__(self, weapons, specialisations, gadgets, name) -> None:
        self.weapons = weapons
        self.specialisations = specialisations
        self.gadgets = gadgets
        self.name = name

# //////////////////////////////////////////////////////////////////////////////

# Finals Random Loadout Generator by XperiorTR
# Run this in an Online Python Interpreter
# Edit Classes Here
        
# If you want to make a thing more probable, just add more copies, ik its scuffed but lol cant be bothered to implement
# You can also remove a thing to make it not appear

# //////////////////////////////////////////////////////////////////////////////
Light = classes( # Light Class
[ # Weapons 
"V9S", "M11", "LH1", "Sawed-Off Shotgun", ".30-06",
"Assasin's Dagger", "Sword", "Throwing Knives", "XP-54"
],
[ # Specialisations
"Cloaking Device", "Grappling Hook", "Evasive Dash"
], 
[ # Gadgets
"Frag Grenade", "Flashbang", "Incindiary Grenade", "Goo Grenade",
"Gas Grenade", "Smoke Grenade", "Glitch Grenade", "Breaching Charge",
"Proximity Sensor", "Stun Gun", "Thermal Vision"
], "Light")
# //////////////////////////////////////////////////////////////////////////////
Medium = classes( # Medium Class
[ # Weapons
"AKM", "FCAR", "Repeater", "CL-40", "Riot Shield",
"R .357"
],
[ # Specialisations (i hope im spelling that right)
"Healing Beam", "Guardian Turret", "Recon Senses"
],
[ # Gadgets
"Frag Grenade", "Flashbang", "Incindiary Grenade", "Goo Grenade", "Gas Grenade",
"Sonar Grenade", "Explosive Mine", "Gas Mine", "Glitch Trap", "Zipline",
"Jump Pad", "Defibilirator", "Tracking Dart", "APS Turret", "Night Vision"
], "Medium")
# //////////////////////////////////////////////////////////////////////////////
Heavy = classes( # Heavy Class
[ # Weapons
"M60", "SA1216", "M32 Grenade Launcher", "Flamethrower", "Sledgehammer"
],
[ # Specialisations
"Charge 'n' Slam", "Goo Gun", "Mesh Shield"
],
[ # Gadgets
"Frag Grenade", "Flashbang", "Incindiary Grenade", "Gas Grenade", "C4",
"Explosive Mine", "Incindiary Mine", "Barricade", "RPG-7", "Dome Shield", "Night Vision"
], "Heavy")
# //////////////////////////////////////////////////////////////////////////////

classesList = [Light, Medium, Heavy]
client = commands.Bot(command_prefix="+", intents=discord.Intents.all())


def funny(message):
    final = "```////////////////////\nClass:\n"
    classSelected = classesList[random.randrange(len(classesList))]
    final += f"{classSelected.name}" "\n"
    weaponList = classSelected.weapons
    weaponListRand = random.randrange(len(classSelected.weapons))
    final += "////////////////////\n"
    final += "Weapon:\n"
    final += f"{weaponList[weaponListRand]}" "\n"
    weaponList.pop(weaponListRand)
    curGadgets = classSelected.gadgets
    final += "////////////////////\n"
    final += "Gadgets:\n"
    for i in range(3):
        rand = random.randrange(len(curGadgets))
        thing = curGadgets[rand]
        final += f"{thing}" "\n"
        curGadgets.pop(rand)
    reserve = curGadgets + weaponList
    final += "////////////////////\n"
    final += "Reserve:\n"
    for i in range(4):
        rand = random.randrange(len(reserve))
        thing = reserve[rand]
        final += f"{thing}" "\n"
        reserve.pop(rand)
    final += "////////////////////```"
    return final


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$loadout'):
        await message.channel.send(funny(message))

client.run('key goes here')
        



