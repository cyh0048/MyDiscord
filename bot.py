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
        embed = discord.Embed(title="단무지", color=0xF7FE2E)
        embed.add_field(name="이름", value="영환\n", inline=False)
        embed.add_field(name="좀비고닉네임", value="플2부터다시\n", inline=False)
        embed.add_field(name="역할", value="디코 봇 제작\n", inline=False)
        embed.set_thumbnail(url=mesage.author.avatar_url)

        embed1 = discord.Embed(title="클마", color=0xDF0101)
        embed1.add_field(name="이름", value="진우", inline=False)
        embed1.add_field(name="좀비고닉네임", value="카트충지누", inline=False)
        embed1.add_field(name="역할", value="가입문의", inline=False)
        embed1.set_thumbnail(url=message.author.avatar_url)

        embed2 = discord.Embed(title="부마", color=0x00ff00)
        embed2.add_field(name="이름", value="상서", inline=False)
        embed2.add_field(name="좀비고닉네임", value="김상서", inline=False)
        embed2.add_field(name="역할", value="drawing picture", inline=False)
        embed2.set_thumbnail(url=message.author.avatar_url)

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
                    dogsae2.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                    dogsae2.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                    dogsae2.add_field(name="사용언어", value=message.content, inline=False)
                    dogsae2.add_field(name="상태", value="투아웃", inline=False)
                    dogsae2.set_thumbnail(url=message.author.avatar_url)
                    await bot.get_channel(int(672143900940697600)).send(embed=dogsae2)
                    await message.channel.send(embed=dogsae2)
                    break
                elif sheet["B" + str(i)].value == 3:
                    dogsae3 = discord.Embed(color=0xDF0101)
                    dogsae3.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                    dogsae3.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                    dogsae3.add_field(name="사용언어", value=message.content, inline=False)
                    dogsae3.add_field(name="상태", value="삼진아웃", inline=False)
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
                dogsae.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                dogsae.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                dogsae.add_field(name="사용언어", value=message.content, inline=False)
                dogsae.add_field(name="상태", value="원아웃", inline=False)
                dogsae.set_thumbnail(url=message.author.avatar_url)
                await bot.get_channel(int(672143900940697600)).send(embed=dogsae)
                await message.channel.send(embed=dogsae)
                break
            i += 1


access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)