# -*- coding: utf-8 -*-
import discord
import psutil
import socket
import asyncio
import requests

# create an Intents object with the required flags
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=discord.Intents.all())

# Insert your Discord bot token
TOKEN = ''

# Insert the channel ID where the bot will send messages
CHANNEL_ID = 


def get_disk_usage():
    # Get information about the disk space of the root partition
    disk_usage = psutil.disk_usage('/')
    # Calculate the free space in percentage
    used_space_percent = round(disk_usage.used / disk_usage.total * 100, 2)
    # Get the external IP address of the server
    ip_address = requests.get('https://api.ipify.org').text
    # Define the color of the status circle based on the used space percentage
    if used_space_percent < 70:
        color = '\U0001F7E2'
    elif used_space_percent < 90:
        color = '\U0001F7E1'
    else:
        color = '\U0001F534'

    # Create a string with information about the disk usage and the server's IP address
    message = f'{color} **{used_space_percent}%** of disk space is used. Server IP address: **{ip_address}**'
    return message

async def send_message():
    # Get the Discord channel object to send the message
    channel = client.get_channel(CHANNEL_ID)
    # Send the message with information about the free space on the disk and the server's IP address
    await channel.send(f'{get_disk_usage()}')

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    # Endless loop that sends a message every day
    while True:
        await send_message()
        await asyncio.sleep(86400) # 86400 seconds = 1 day

client.run(TOKEN)
