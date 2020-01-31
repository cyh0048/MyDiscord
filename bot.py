import discord
import asyncio
import openpyxl
import os
from discord.ext import commands
from discord.ext.commands import bot

bot = discord.Client()


@bot.event
async def on_ready():
    print("login")
    print(bot.user.name)
    print(bot.user.id)
    print("000----------")


@bot.event
async def on_message(message):
    if message.content.startswith("!운영진"):
        embed = discord.Embed(color=0xF7FE2E)
        embed.add_field(name="이름", value="영환", inline=True)
        embed.add_field(name="좀비고닉네임", value="플2부터다시", inline=True)
        embed.add_field(name="운영", value="단무지", inline=True)
        embed.add_field(name="역할", value="디코 봇 제작", inline=True)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/283193429574418432/9905fb1f4fbdd4ea25800aea045bebce.png?size=128")

        embed1 = discord.Embed(color=0xDF0101)
        embed1.add_field(name="이름", value="진우", inline=True)
        embed1.add_field(name="좀비고닉네임", value="카트충지누", inline=True)
        embed1.add_field(name="운영", value="클마", inline=True)
        embed1.add_field(name="역할", value="가입문의", inline=True)
        embed1.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/542574486231318529/0f55203e2a3916498487d5fe86ed1af0.png?size=128")

        embed2 = discord.Embed(color=0x00ff00)
        embed2.add_field(name="이름", value="상서", inline=True)
        embed2.add_field(name="좀비고닉네임", value="김상서", inline=True)
        embed2.add_field(name="운영", value="부마", inline=True)
        embed2.add_field(name="역할", value="drawing picture", inline=True)
        embed2.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/652929821692919837/f5424135d42dd61419f9544c1b44ec54.png?size=128")

        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed)
    if "씨발" in message.content or "개새끼" in message.content or "심한욕설" in message.content\
            or "욕설" in message.content or "Tlqkf" in message.content:
        author = message.guild.get_member(int(message.author.id))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.name):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    dogsae2 = discord.Embed(color=0xDF0101)
                    dogsae2.add_field(name="디스코드 이름", value=message.author.name, inline=True)
                    dogsae2.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=True)
                    dogsae2.add_field(name="사용언어", value=message.content, inline=True)
                    dogsae2.add_field(name="상태", value="투아웃", inline=True)
                    dogsae2.set_thumbnail(url=message.author.avatar_url)
                    await bot.get_channel(int(672143900940697600)).send(embed=dogsae2)
                    await message.channel.send(embed=dogsae2)
                    break
                elif sheet["B" + str(i)].value == 3:
                    dogsae3 = discord.Embed(color=0xDF0101)
                    dogsae3.add_field(name="디스코드 이름", value=message.author.name, inline=True)
                    dogsae3.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=True)
                    dogsae3.add_field(name="사용언어", value=message.content, inline=True)
                    dogsae3.add_field(name="상태", value="삼진아웃", inline=True)
                    dogsae3.set_thumbnail(url=message.author.avatar_url)
                    await bot.get_channel(int(672143900940697600)).send(embed=dogsae3)
                    await message.channel.send(embed=dogsae3)
                    await message.guild.ban(author)
                    break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.name)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                dogsae = discord.Embed(color=0xDF0101)
                dogsae.add_field(name="디스코드 이름", value=message.author.name, inline=True)
                dogsae.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=True)
                dogsae.add_field(name="사용언어", value=message.content, inline=True)
                dogsae.add_field(name="상태", value="원아웃", inline=True)
                dogsae.set_thumbnail(url=message.author.avatar_url)
                await bot.get_channel(int(672143900940697600)).send(embed=dogsae)
                await message.channel.send(embed=dogsae)
                break
            i += 1


access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)