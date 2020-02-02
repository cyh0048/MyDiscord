import discord
import asyncio
import openpyxl
import os

from discord import Guild
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import bot

bot1 = discord.Client()

client1 = commands.Bot(command_prefix='/')


@bot1.event
async def on_ready():
    print("login")
    print(bot1.user.name)
    print(bot1.user.id)
    print("000----------")


@bot1.event
async def on_message(message):
    if message.content.startswith("!운영진"):
        embed = discord.Embed(title="단무지", color=0xF7FE2E)
        embed.add_field(name="이름", value="영환", inline=False)
        embed.add_field(name="좀비고닉네임", value="플2부터다시", inline=False)
        embed.add_field(name="역할", value="디코 봇 제작", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/283193429574418432/9905fb1f4fbdd4ea25800aea045bebce.png?size=128")

        embed1 = discord.Embed(title="클마", color=0xDF0101)
        embed1.add_field(name="이름", value="진우", inline=False)
        embed1.add_field(name="좀비고닉네임", value="카트충지누", inline=False)
        embed1.add_field(name="역할", value="가입문의", inline=False)
        embed1.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/542574486231318529/0f55203e2a3916498487d5fe86ed1af0.png?size=128")

        embed2 = discord.Embed(title="부마", color=0x00ff00)
        embed2.add_field(name="이름", value="상서", inline=False)
        embed2.add_field(name="좀비고닉네임", value="김상서", inline=False)
        embed2.add_field(name="역할", value="drawing picture", inline=False)
        embed2.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/652929821692919837/f5424135d42dd61419f9544c1b44ec54.png?size=128")

        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed)
    if "씨발" in message.content or "개새끼" in message.content or "샹년" in message.content \
            or "좆" in message.content or "Tlqkf" in message.content:
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
                    dogsae2.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                    dogsae2.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                    dogsae2.add_field(name="사용언어", value=message.content, inline=False)
                    dogsae2.add_field(name="상태", value="투아웃", inline=False)
                    dogsae2.set_thumbnail(url=message.author.avatar_url)
                    # await bot1.get_channel(int(672143900940697600)).send(embed=dogsae2)
                    await message.channel.send(embed=dogsae2)
                    break
                elif sheet["B" + str(i)].value == 3:
                    dogsae3 = discord.Embed(color=0xDF0101)
                    dogsae3.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                    dogsae3.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                    dogsae3.add_field(name="사용언어", value=message.content, inline=False)
                    dogsae3.add_field(name="상태", value="삼진아웃", inline=False)
                    dogsae3.set_thumbnail(url=message.author.avatar_url)
                    role = discord.utils.get(message.server.roles, name="bot")
                    await bot1.add_roles(message.author.id, role)
                    # await bot1.get_channel(int(672143900940697600)).send(embed=dogsae3)
                    await message.channel.send(embed=dogsae3)
                    await message.guild.ban(author)
                    break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.name)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                dogsae = discord.Embed(color=0xDF0101)
                dogsae.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                dogsae.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                dogsae.add_field(name="사용언어", value=message.content, inline=False)
                dogsae.add_field(name="상태", value="원아웃", inline=False)
                dogsae.set_thumbnail(url=message.author.avatar_url)
                # await bot1.get_channel(int(672143900940697600)).send(embed=dogsae)
                await message.channel.send(embed=dogsae)
                break
            i += 1

    if message.content.startswith("!내정보"):
        inf = discord.Embed(title=message.author.name + "님의 정보", color=0x013ADF)
        inf.add_field(name="디스코드 이름", value=message.author.name, inline=False)
        inf.add_field(name="디스코드 가입 날짜", value=message.author.created_at, inline=False)
        inf.add_field(name="서버 가입 날짜", value=message.author.joined_at, inline=False)
        inf.add_field(name="디스코드 역할", value=message.author.top_role, inline=False)
        inf.set_thumbnail(url=message.author.avatar_url)

        await message.channel.send(embed=inf)

    if message.content.startswith("!clear"):
        a = message.author.top_role
        if str(message.author.top_role) == "마스터":
            await message.channel.purge(limit=1000)
        elif str(message.author.top_role) == "부마스터":
            await message.channel.purge(limit=1000)
        elif str(message.author.top_role) == "단무지":
            await message.channel.purge(limit=1000)
        else:
            await message.channel.send("넌 권한없엉")

access_token = os.environ["BOT_TOKEN"]
bot1.run(access_token)
