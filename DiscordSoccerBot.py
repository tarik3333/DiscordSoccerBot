# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:58:27 2021

@author: Tarık Buğra Tufan
"""
import discord
import json
import requests

url = "https://elenasport-io1.p.rapidapi.com/v2/seasons/2567/inplay"

querystring = {"page": "1"}

headers = {
    'x-rapidapi-key': "rapidapi key",
    'x-rapidapi-host': "elenasport-io1.p.rapidapi.com"
}

#response = requests.request("GET", url, headers=headers, params=querystring)

client = discord.Client()


@client.event
async def on_ready():
    print("giriş yapıldı{0.user}".format(client))


@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    if message.content.startswith('$sonuc'):
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    params=querystring)
        json_data = json.loads(response.text)
        data = json_data["data"]
        if (len(data) == 0):
            await message.channel.send('No games Playing')
        else:
            await message.channel.send(json_data)


client.run("discord token")
