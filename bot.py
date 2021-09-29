import discord
import asyncio
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='낫마야 ')

@bot.event
async def on_ready():
    print('다음으로 로그인: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

client = discord.Client()

token = "ODkxNTEwMTY0NTgxMTIyMDg4.YU_Zig.hh1KlLfRgzDY72OjmIVAi8t1IT8"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇 성공')
    game = discord.Game('낫마야 도움말을 사용해보세요!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "낫마야 저녁뭐먹을까?":
        await message.channel.send("그걸 왜 저한테 물어보세요?")
    if message.content == "낫마야":
        await message.channel.send(f"네? {message.author.mention}님")
    if message.content == "낫마야 안녕":
        await message.channel.send(f"안녕하세요! {message.author.mention}님!")
    if message.content == "낫마야 죠죠":
        await message.channel.send("씹덕")
    if message.content == "낫마야 저작권":
        await message.channel.send("씨부레")
    if message.content == "낫마야 도움말":
        await message.channel.send("명령어들 낫마야 안녕 낫마야 죠죠 낫마야 저작권 낫마야 닌텐도 낫마야 운빨망겜 50,25,10,1")
    if message.content == "낫마야 닌텐도":
        await message.channel.send("나만없어..")
    if message.content == "낫마야 올타디":
        await message.channel.send("제냥님이 즐겨하는 게임입니다.")
    if message.content == "낫마야 제냥":
        await message.channel.send("우리 핳하의 아주 위대한 서버 오너님이십니다.")
    if message.content == "낫마야 리학":
        await message.channel.send("밥이네")
    if message.content == "낫마야 낫마":
        await message.channel.send("이봇을 만든 (자칭)위대한 사람입니다")
    if message.content == "낫마야 워리":
        await message.channel.send("김치네")
    if message.content == "낫마야 심바":
        await message.channel.send("스팸이네")
    
    if message.content == "낫마야 운빨망겜 50":
        ran = random.randint(0,1)
        if ran == 0:
            d = "ㅋ실패"
        if ran == 1:
            d = "오성공"
        await message.channel.send(d)
    if message.content == "낫마야 운빨망겜 25":
        ran = random.randint(0,3)
        if ran == 0:
            d = "ㅋ실패"
        if ran == 1:
            d = "ㅋ실패"
        if ran == 2:
            d = "ㅋ실패"
        if ran == 3:
            d = "오성공"
        await message.channel.send(d)
    if message.content == "낫마야 운빨망겜 10":
        ran = random.randint(0,9)
        if ran == 0:
            d = "ㅋ실패"
        if ran == 1:
            d = "ㅋ실패"
        if ran == 2:
            d = "ㅋ실패"
        if ran == 3:
            d = "ㅋ실패"
        if ran == 4:
            d = "ㅋ실패"
        if ran == 5:
            d = "ㅋ실패"
        if ran == 6:
            d = "ㅋ실패"
        if ran == 7:
            d = "ㅋ실패"
        if ran == 8:
            d = "ㅋ실패"
        if ran == 9:
            d = "오성공"
        await message.channel.send(d)
    if message.content == "낫마야 운빨망겜 1":
        ran = random.randint(0,99)
        if ran == 0:
            d = "ㅋ실패"
        if ran == 1:
            d = "ㅋ실패"
        if ran == 2:
            d = "ㅋ실패"
        if ran == 3:
            d = "ㅋ실패"
        if ran == 4:
            d = "ㅋ실패"
        if ran == 5:
            d = "ㅋ실패"
        if ran == 6:
            d = "ㅋ실패"
        if ran == 7:
            d = "ㅋ실패"
        if ran == 8:
            d = "ㅋ실패"
        if ran == 9:
            d = "ㅋ실패"
        if ran == 10:
            d = "ㅋ실패"
        if ran == 11:
            d = "ㅋ실패"
        if ran == 12:
            d = "ㅋ실패"
        if ran == 13:
            d = "ㅋ실패"
        if ran == 14:
            d = "ㅋ실패"
        if ran == 15:
            d = "ㅋ실패"
        if ran == 16:
            d = "ㅋ실패"
        if ran == 17:
            d = "ㅋ실패"
        if ran == 18:
            d = "ㅋ실패"
        if ran == 19:
            d = "ㅋ실패"
        if ran == 20:
            d = "ㅋ실패"
        if ran == 21:
            d = "ㅋ실패"
        if ran == 22:
            d = "ㅋ실패"
        if ran == 23:
            d = "ㅋ실패"
        if ran == 24:
            d = "ㅋ실패"
        if ran == 25:
            d = "ㅋ실패"
        if ran == 26:
            d = "ㅋ실패"
        if ran == 27:
            d = "ㅋ실패"
        if ran == 28:
            d = "ㅋ실패"
        if ran == 29:
            d = "ㅋ실패"
        if ran == 30:
            d = "ㅋ실패"
        if ran == 31:
            d = "ㅋ실패"
        if ran == 32:
            d = "ㅋ실패"
        if ran == 33:
            d = "ㅋ실패"
        if ran == 34:
            d = "ㅋ실패"
        if ran == 35:
            d = "ㅋ실패"
        if ran == 36:
            d = "ㅋ실패"
        if ran == 37:
            d = "ㅋ실패"
        if ran == 38:
            d = "ㅋ실패"
        if ran == 39:
            d = "ㅋ실패"
        if ran == 40:
            d = "ㅋ실패"
        if ran == 41:
            d = "ㅋ실패"
        if ran == 42:
            d = "ㅋ실패"
        if ran == 43:
            d = "ㅋ실패"
        if ran == 44:
            d = "ㅋ실패"
        if ran == 45:
            d = "ㅋ실패"
        if ran == 46:
            d = "ㅋ실패"
        if ran == 47:
            d = "ㅋ실패"
        if ran == 48:
            d = "ㅋ실패"
        if ran == 49:
            d = "ㅋ실패"
        if ran == 50:
            d = "ㅋ실패"
        if ran == 51:
            d = "ㅋ실패"
        if ran == 52:
            d = "ㅋ실패"
        if ran == 53:
            d = "ㅋ실패"
        if ran == 54:
            d = "ㅋ실패"
        if ran == 55:
            d = "ㅋ실패"
        if ran == 56:
            d = "ㅋ실패"
        if ran == 57:
            d = "ㅋ실패"
        if ran == 58:
            d = "ㅋ실패"
        if ran == 59:
            d = "ㅋ실패"
        if ran == 60:
            d = "ㅋ실패"
        if ran == 61:
            d = "ㅋ실패"
        if ran == 62:
            d = "ㅋ실패"
        if ran == 63:
            d = "ㅋ실패"
        if ran == 64:
            d = "ㅋ실패"
        if ran == 65:
            d = "ㅋ실패"
        if ran == 66:
            d = "ㅋ실패"
        if ran == 67:
            d = "ㅋ실패"
        if ran == 68:
            d = "ㅋ실패"
        if ran == 69:
            d = "ㅋ실패"
        if ran == 70:
            d = "ㅋ실패"
        if ran == 71:
            d = "ㅋ실패"
        if ran == 72:
            d = "ㅋ실패"
        if ran == 73:
            d = "ㅋ실패"
        if ran == 74:
            d = "ㅋ실패"
        if ran == 75:
            d = "ㅋ실패"
        if ran == 76:
            d = "ㅋ실패"
        if ran == 77:
            d = "ㅋ실패"
        if ran == 78:
            d = "ㅋ실패"
        if ran == 79:
            d = "ㅋ실패"
        if ran == 80:
            d = "ㅋ실패"
        if ran == 81:
            d = "ㅋ실패"
        if ran == 82:
            d = "ㅋ실패"
        if ran == 83:
            d = "ㅋ실패"
        if ran == 84:
            d = "ㅋ실패"
        if ran == 85:
            d = "ㅋ실패"
        if ran == 86:
            d = "ㅋ실패"
        if ran == 87:
            d = "ㅋ실패"
        if ran == 88:
            d = "ㅋ실패"
        if ran == 89:
            d = "ㅋ실패"
        if ran == 90:
            d = "ㅋ실패"
        if ran == 91:
            d = "ㅋ실패"
        if ran == 92:
            d = "ㅋ실패"
        if ran == 93:
            d = "ㅋ실패"
        if ran == 94:
            d = "ㅋ실패"
        if ran == 95:
            d = "ㅋ실패"
        if ran == 96:
            d = "ㅋ실패"
        if ran == 97:
            d = "ㅋ실패"
        if ran == 98:
            d = "ㅋ실패"
        if ran == 99:
            d = "ㅋ실패"
        await message.channel.send(d)
    if message.content == "낫마야 운빨망겜 0.1":
        ran = random.randint(0,999)
        if ran == 0:
            d = "ㅋ실패"
        if ran == 1:
            d = "ㅋ실패"
        if ran == 2:
            d = "ㅋ실패"
        if ran == 3:
            d = "ㅋ실패"
        if ran == 4:
            d = "ㅋ실패"
        if ran == 5:
            d = "ㅋ실패"
        if ran == 6:
            d = "ㅋ실패"
        if ran == 7:
            d = "ㅋ실패"
        if ran == 8:
            d = "ㅋ실패"
        if ran == 9:
            d = "ㅋ실패"
        if ran == 10:
            d = "ㅋ실패"
        if ran == 11:
            d = "ㅋ실패"
        if ran == 12:
            d = "ㅋ실패"
        if ran == 13:
            d = "ㅋ실패"
        if ran == 14:
            d = "ㅋ실패"
        if ran == 15:
            d = "ㅋ실패"
        if ran == 16:
            d = "ㅋ실패"
        if ran == 17:
            d = "ㅋ실패"
        if ran == 18:
            d = "ㅋ실패"
        if ran == 19:
            d = "ㅋ실패"
        if ran == 20:
            d = "ㅋ실패"
        if ran == 21:
            d = "ㅋ실패"
        if ran == 22:
            d = "ㅋ실패"
        if ran == 23:
            d = "ㅋ실패"
        if ran == 24:
            d = "ㅋ실패"
        if ran == 25:
            d = "ㅋ실패"
        if ran == 26:
            d = "ㅋ실패"
        if ran == 27:
            d = "ㅋ실패"
        if ran == 28:
            d = "ㅋ실패"
        if ran == 29:
            d = "ㅋ실패"
        if ran == 30:
            d = "ㅋ실패"
        if ran == 31:
            d = "ㅋ실패"
        if ran == 32:
            d = "ㅋ실패"
        if ran == 33:
            d = "ㅋ실패"
        if ran == 34:
            d = "ㅋ실패"
        if ran == 35:
            d = "ㅋ실패"
        if ran == 36:
            d = "ㅋ실패"
        if ran == 37:
            d = "ㅋ실패"
        if ran == 38:
            d = "ㅋ실패"
        if ran == 39:
            d = "ㅋ실패"
        if ran == 40:
            d = "ㅋ실패"
        if ran == 41:
            d = "ㅋ실패"
        if ran == 42:
            d = "ㅋ실패"
        if ran == 43:
            d = "ㅋ실패"
        if ran == 44:
            d = "ㅋ실패"
        if ran == 45:
            d = "ㅋ실패"
        if ran == 46:
            d = "ㅋ실패"
        if ran == 47:
            d = "ㅋ실패"
        if ran == 48:
            d = "ㅋ실패"
        if ran == 49:
            d = "ㅋ실패"
        if ran == 50:
            d = "ㅋ실패"
        if ran == 51:
            d = "ㅋ실패"
        if ran == 52:
            d = "ㅋ실패"
        if ran == 53:
            d = "ㅋ실패"
        if ran == 54:
            d = "ㅋ실패"
        if ran == 55:
            d = "ㅋ실패"
        if ran == 56:
            d = "ㅋ실패"
        if ran == 57:
            d = "ㅋ실패"
        if ran == 58:
            d = "ㅋ실패"
        if ran == 59:
            d = "ㅋ실패"
        if ran == 60:
            d = "ㅋ실패"
        if ran == 61:
            d = "ㅋ실패"
        if ran == 62:
            d = "ㅋ실패"
        if ran == 63:
            d = "ㅋ실패"
        if ran == 64:
            d = "ㅋ실패"
        if ran == 65:
            d = "ㅋ실패"
        if ran == 66:
            d = "ㅋ실패"
        if ran == 67:
            d = "ㅋ실패"
        if ran == 68:
            d = "ㅋ실패"
        if ran == 69:
            d = "ㅋ실패"
        if ran == 70:
            d = "ㅋ실패"
        if ran == 71:
            d = "ㅋ실패"
        if ran == 72:
            d = "ㅋ실패"
        if ran == 73:
            d = "ㅋ실패"
        if ran == 74:
            d = "ㅋ실패"
        if ran == 75:
            d = "ㅋ실패"
        if ran == 76:
            d = "ㅋ실패"
        if ran == 77:
            d = "ㅋ실패"
        if ran == 78:
            d = "ㅋ실패"
        if ran == 79:
            d = "ㅋ실패"
        if ran == 80:
            d = "ㅋ실패"
        if ran == 81:
            d = "ㅋ실패"
        if ran == 82:
            d = "ㅋ실패"
        if ran == 83:
            d = "ㅋ실패"
        if ran == 84:
            d = "ㅋ실패"
        if ran == 85:
            d = "ㅋ실패"
        if ran == 86:
            d = "ㅋ실패"
        if ran == 87:
            d = "ㅋ실패"
        if ran == 88:
            d = "ㅋ실패"
        if ran == 89:
            d = "ㅋ실패"
        if ran == 90:
            d = "ㅋ실패"
        if ran == 91:
            d = "ㅋ실패"
        if ran == 92:
            d = "ㅋ실패"
        if ran == 93:
            d = "ㅋ실패"
        if ran == 94:
            d = "ㅋ실패"
        if ran == 95:
            d = "ㅋ실패"
        if ran == 96:
            d = "ㅋ실패"
        if ran == 97:
            d = "ㅋ실패"
        if ran == 98:
            d = "ㅋ실패"
        if ran == 99:
            d = "ㅋ실패"
        if ran == 100:
            d = "ㅋ실패"
        if ran == 101:
            d = "ㅋ실패"
        if ran == 102:
            d = "ㅋ실패"
        if ran == 103:
            d = "ㅋ실패"
        if ran == 104:
            d = "ㅋ실패"
        if ran == 105:
            d = "ㅋ실패"
        if ran == 106:
            d = "ㅋ실패"
        if ran == 107:
            d = "ㅋ실패"
        if ran == 108:
            d = "ㅋ실패"
        if ran == 109:
            d = "ㅋ실패"
        if ran == 110:
            d = "ㅋ실패"
        if ran == 111:
            d = "ㅋ실패"
        if ran == 112:
            d = "ㅋ실패"
        if ran == 113:
            d = "ㅋ실패"
        if ran == 114:
            d = "ㅋ실패"
        if ran == 115:
            d = "ㅋ실패"
        if ran == 116:
            d = "ㅋ실패"
        if ran == 117:
            d = "ㅋ실패"
        if ran == 118:
            d = "ㅋ실패"
        if ran == 119:
            d = "ㅋ실패"
        if ran == 120:
            d = "ㅋ실패"
        if ran == 121:
            d = "ㅋ실패"
        if ran == 122:
            d = "ㅋ실패"
        if ran == 123:
            d = "ㅋ실패"
        if ran == 124:
            d = "ㅋ실패"
        if ran == 125:
            d = "ㅋ실패"
        if ran == 126:
            d = "ㅋ실패"
        if ran == 127:
            d = "ㅋ실패"
        if ran == 128:
            d = "ㅋ실패"
        if ran == 129:
            d = "ㅋ실패"
        if ran == 130:
            d = "ㅋ실패"
        if ran == 131:
            d = "ㅋ실패"
        if ran == 132:
            d = "ㅋ실패"
        if ran == 133:
            d = "ㅋ실패"
        if ran == 134:
            d = "ㅋ실패"
        if ran == 135:
            d = "ㅋ실패"
        if ran == 136:
            d = "ㅋ실패"
        if ran == 137:
            d = "ㅋ실패"
        if ran == 138:
            d = "ㅋ실패"
        if ran == 139:
            d = "ㅋ실패"
        if ran == 140:
            d = "ㅋ실패"
        if ran == 141:
            d = "ㅋ실패"
        if ran == 142:
            d = "ㅋ실패"
        if ran == 143:
            d = "ㅋ실패"
        if ran == 144:
            d = "ㅋ실패"
        if ran == 145:
            d = "ㅋ실패"
        if ran == 146:
            d = "ㅋ실패"
        if ran == 147:
            d = "ㅋ실패"
        if ran == 148:
            d = "ㅋ실패"
        if ran == 149:
            d = "ㅋ실패"
        if ran == 150:
            d = "ㅋ실패"
        if ran == 151:
            d = "ㅋ실패"
        if ran == 152:
            d = "ㅋ실패"
        if ran == 153:
            d = "ㅋ실패"
        if ran == 154:
            d = "ㅋ실패"
        if ran == 155:
            d = "ㅋ실패"
        if ran == 156:
            d = "ㅋ실패"
        if ran == 157:
            d = "ㅋ실패"
        if ran == 158:
            d = "ㅋ실패"
        if ran == 159:
            d = "ㅋ실패"
        if ran == 160:
            d = "ㅋ실패"
        if ran == 161:
            d = "ㅋ실패"
        if ran == 162:
            d = "ㅋ실패"
        if ran == 163:
            d = "ㅋ실패"
        if ran == 64:
            d = "ㅋ실패"
        if ran == 165:
            d = "ㅋ실패"
        if ran == 166:
            d = "ㅋ실패"
        if ran == 167:
            d = "ㅋ실패"
        if ran == 168:
            d = "ㅋ실패"
        if ran == 169:
            d = "ㅋ실패"
        if ran == 170:
            d = "ㅋ실패"
        if ran == 171:
            d = "ㅋ실패"
        if ran == 172:
            d = "ㅋ실패"
        if ran == 173:
            d = "ㅋ실패"
        if ran == 174:
            d = "ㅋ실패"
        if ran == 175:
            d = "ㅋ실패"
        if ran == 176:
            d = "ㅋ실패"
        if ran == 177:
            d = "ㅋ실패"
        if ran == 178:
            d = "ㅋ실패"
        if ran == 179:
            d = "ㅋ실패"
        if ran == 180:
            d = "ㅋ실패"
        if ran == 181:
            d = "ㅋ실패"
        if ran == 182:
            d = "ㅋ실패"
        if ran == 183:
            d = "ㅋ실패"
        if ran == 184:
            d = "ㅋ실패"
        if ran == 185:
            d = "ㅋ실패"
        if ran == 186:
            d = "ㅋ실패"
        if ran == 187:
            d = "ㅋ실패"
        if ran == 188:
            d = "ㅋ실패"
        if ran == 189:
            d = "ㅋ실패"
        if ran == 190:
            d = "ㅋ실패"
        if ran == 191:
            d = "ㅋ실패"
        if ran == 192:
            d = "ㅋ실패"
        if ran == 193:
            d = "ㅋ실패"
        if ran == 194:
            d = "ㅋ실패"
        if ran == 195:
            d = "ㅋ실패"
        if ran == 196:
            d = "ㅋ실패"
        if ran == 197:
            d = "ㅋ실패"
        if ran == 198:
            d = "ㅋ실패"
        if ran == 199:
            d = "ㅋ실패"
        if ran == 200:
            d = "오성공"
        if ran == 201:
            d = "ㅋ실패"
        if ran == 202:
            d = "ㅋ실패"
        if ran == 203:
            d = "ㅋ실패"
        if ran == 204:
            d = "ㅋ실패"
        if ran == 205:
            d = "ㅋ실패"
        if ran == 206:
            d = "ㅋ실패"
        if ran == 207:
            d = "ㅋ실패"
        if ran == 208:
            d = "ㅋ실패"
        if ran == 209:
            d = "ㅋ실패"
        if ran == 210:
            d = "ㅋ실패"
        if ran == 211:
            d = "ㅋ실패"
        if ran == 212:
            d = "ㅋ실패"
        if ran == 213:
            d = "ㅋ실패"
        if ran == 214:
            d = "ㅋ실패"
        if ran == 215:
            d = "ㅋ실패"
        if ran == 216:
            d = "ㅋ실패"
        if ran == 217:
            d = "ㅋ실패"
        if ran == 218:
            d = "ㅋ실패"
        if ran == 219:
            d = "ㅋ실패"
        if ran == 220:
            d = "ㅋ실패"
        if ran == 221:
            d = "ㅋ실패"
        if ran == 222:
            d = "ㅋ실패"
        if ran == 223:
            d = "ㅋ실패"
        if ran == 224:
            d = "ㅋ실패"
        if ran == 225:
            d = "ㅋ실패"
        if ran == 226:
            d = "ㅋ실패"
        if ran == 227:
            d = "ㅋ실패"
        if ran == 228:
            d = "ㅋ실패"
        if ran == 229:
            d = "ㅋ실패"
        if ran == 230:
            d = "ㅋ실패"
        if ran == 231:
            d = "ㅋ실패"
        if ran == 232:
            d = "ㅋ실패"
        if ran == 233:
            d = "ㅋ실패"
        if ran == 234:
            d = "ㅋ실패"
        if ran == 235:
            d = "ㅋ실패"
        if ran == 236:
            d = "ㅋ실패"
        if ran == 237:
            d = "ㅋ실패"
        if ran == 238:
            d = "ㅋ실패"
        if ran == 239:
            d = "ㅋ실패"
        if ran == 240:
            d = "ㅋ실패"
        if ran == 241:
            d = "ㅋ실패"
        if ran == 242:
            d = "ㅋ실패"
        if ran == 243:
            d = "ㅋ실패"
        if ran == 244:
            d = "ㅋ실패"
        if ran == 245:
            d = "ㅋ실패"
        if ran == 246:
            d = "ㅋ실패"
        if ran == 247:
            d = "ㅋ실패"
        if ran == 248:
            d = "ㅋ실패"
        if ran == 249:
            d = "ㅋ실패"
        if ran == 250:
            d = "ㅋ실패"
        if ran == 251:
            d = "ㅋ실패"
        if ran == 252:
            d = "ㅋ실패"
        if ran == 253:
            d = "ㅋ실패"
        if ran == 254:
            d = "ㅋ실패"
        if ran == 255:
            d = "ㅋ실패"
        if ran == 256:
            d = "ㅋ실패"
        if ran == 257:
            d = "ㅋ실패"
        if ran == 258:
            d = "ㅋ실패"
        if ran == 259:
            d = "ㅋ실패"
        if ran == 260:
            d = "ㅋ실패"
        if ran == 261:
            d = "ㅋ실패"
        if ran == 262:
            d = "ㅋ실패"
        if ran == 263:
            d = "ㅋ실패"
        if ran == 264:
            d = "ㅋ실패"
        if ran == 265:
            d = "ㅋ실패"
        if ran == 266:
            d = "ㅋ실패"
        if ran == 267:
            d = "ㅋ실패"
        if ran == 268:
            d = "ㅋ실패"
        if ran == 269:
            d = "ㅋ실패"
        if ran == 270:
            d = "ㅋ실패"
        if ran == 271:
            d = "ㅋ실패"
        if ran == 272:
            d = "ㅋ실패"
        if ran == 273:
            d = "ㅋ실패"
        if ran == 274:
            d = "ㅋ실패"
        if ran == 275:
            d = "ㅋ실패"
        if ran == 276:
            d = "ㅋ실패"
        if ran == 277:
            d = "ㅋ실패"
        if ran == 278:
            d = "ㅋ실패"
        if ran == 279:
            d = "ㅋ실패"
        if ran == 280:
            d = "ㅋ실패"
        if ran == 281:
            d = "ㅋ실패"
        if ran == 282:
            d = "ㅋ실패"
        if ran == 283:
            d = "ㅋ실패"
        if ran == 284:
            d = "ㅋ실패"
        if ran == 285:
            d = "ㅋ실패"
        if ran == 286:
            d = "ㅋ실패"
        if ran == 287:
            d = "ㅋ실패"
        if ran == 288:
            d = "ㅋ실패"
        if ran == 289:
            d = "ㅋ실패"
        if ran == 290:
            d = "ㅋ실패"
        if ran == 291:
            d = "ㅋ실패"
        if ran == 292:
            d = "ㅋ실패"
        if ran == 293:
            d = "ㅋ실패"
        if ran == 294:
            d = "ㅋ실패"
        if ran == 295:
            d = "ㅋ실패"
        if ran == 296:
            d = "ㅋ실패"
        if ran == 297:
            d = "ㅋ실패"
        if ran == 298:
            d = "ㅋ실패"
        if ran == 299:
            d = "ㅋ실패"
        if ran == 300:
            d = "ㅋ실패"
        if ran == 301:
            d = "ㅋ실패"
        if ran == 302:
            d = "ㅋ실패"
        if ran == 303:
            d = "ㅋ실패"
        if ran == 304:
            d = "ㅋ실패"
        if ran == 305:
            d = "ㅋ실패"
        if ran == 306:
            d = "ㅋ실패"
        if ran == 307:
            d = "ㅋ실패"
        if ran == 308:
            d = "ㅋ실패"
        if ran == 309:
            d = "ㅋ실패"
        if ran == 310:
            d = "ㅋ실패"
        if ran == 311:
            d = "ㅋ실패"
        if ran == 312:
            d = "ㅋ실패"
        if ran == 313:
            d = "ㅋ실패"
        if ran == 314:
            d = "ㅋ실패"
        if ran == 315:
            d = "ㅋ실패"
        if ran == 316:
            d = "ㅋ실패"
        if ran == 317:
            d = "ㅋ실패"
        if ran == 318:
            d = "ㅋ실패"
        if ran == 319:
            d = "ㅋ실패"
        if ran == 320:
            d = "ㅋ실패"
        if ran == 321:
            d = "ㅋ실패"
        if ran == 322:
            d = "ㅋ실패"
        if ran == 323:
            d = "ㅋ실패"
        if ran == 324:
            d = "ㅋ실패"
        if ran == 325:
            d = "ㅋ실패"
        if ran == 326:
            d = "ㅋ실패"
        if ran == 327:
            d = "ㅋ실패"
        if ran == 328:
            d = "ㅋ실패"
        if ran == 329:
            d = "ㅋ실패"
        if ran == 330:
            d = "ㅋ실패"
        if ran == 331:
            d = "ㅋ실패"
        if ran == 332:
            d = "ㅋ실패"
        if ran == 333:
            d = "ㅋ실패"
        if ran == 334:
            d = "ㅋ실패"
        if ran == 335:
            d = "ㅋ실패"
        if ran == 336:
            d = "ㅋ실패"
        if ran == 337:
            d = "ㅋ실패"
        if ran == 338:
            d = "ㅋ실패"
        if ran == 339:
            d = "ㅋ실패"
        if ran == 340:
            d = "ㅋ실패"
        if ran == 341:
            d = "ㅋ실패"
        if ran == 342:
            d = "ㅋ실패"
        if ran == 343:
            d = "ㅋ실패"
        if ran == 344:
            d = "ㅋ실패"
        if ran == 345:
            d = "ㅋ실패"
        if ran == 346:
            d = "ㅋ실패"
        if ran == 347:
            d = "ㅋ실패"
        if ran == 348:
            d = "ㅋ실패"
        if ran == 349:
            d = "ㅋ실패"
        if ran == 350:
            d = "ㅋ실패"
        if ran == 351:
            d = "ㅋ실패"
        if ran == 352:
            d = "ㅋ실패"
        if ran == 353:
            d = "ㅋ실패"
        if ran == 354:
            d = "ㅋ실패"
        if ran == 355:
            d = "ㅋ실패"
        if ran == 356:
            d = "ㅋ실패"
        if ran == 357:
            d = "ㅋ실패"
        if ran == 358:
            d = "ㅋ실패"
        if ran == 359:
            d = "ㅋ실패"
        if ran == 360:
            d = "ㅋ실패"
        if ran == 361:
            d = "ㅋ실패"
        if ran == 362:
            d = "ㅋ실패"
        if ran == 363:
            d = "ㅋ실패"
        if ran == 364:
            d = "ㅋ실패"
        if ran == 365:
            d = "ㅋ실패"
        if ran == 366:
            d = "ㅋ실패"
        if ran == 367:
            d = "ㅋ실패"
        if ran == 368:
            d = "ㅋ실패"
        if ran == 369:
            d = "ㅋ실패"
        if ran == 370:
            d = "ㅋ실패"
        if ran == 371:
            d = "ㅋ실패"
        if ran == 372:
            d = "ㅋ실패"
        if ran == 373:
            d = "ㅋ실패"
        if ran == 374:
            d = "ㅋ실패"
        if ran == 375:
            d = "ㅋ실패"
        if ran == 376:
            d = "ㅋ실패"
        if ran == 377:
            d = "ㅋ실패"
        if ran == 378:
            d = "ㅋ실패"
        if ran == 379:
            d = "ㅋ실패"
        if ran == 380:
            d = "ㅋ실패"
        if ran == 381:
            d = "ㅋ실패"
        if ran == 382:
            d = "ㅋ실패"
        if ran == 383:
            d = "ㅋ실패"
        if ran == 384:
            d = "ㅋ실패"
        if ran == 385:
            d = "ㅋ실패"
        if ran == 386:
            d = "ㅋ실패"
        if ran == 387:
            d = "ㅋ실패"
        if ran == 388:
            d = "ㅋ실패"
        if ran == 389:
            d = "ㅋ실패"
        if ran == 390:
            d = "ㅋ실패"
        if ran == 391:
            d = "ㅋ실패"
        if ran == 392:
            d = "ㅋ실패"
        if ran == 393:
            d = "ㅋ실패"
        if ran == 394:
            d = "ㅋ실패"
        if ran == 395:
            d = "ㅋ실패"
        if ran == 396:
            d = "ㅋ실패"
        if ran == 397:
            d = "ㅋ실패"
        if ran == 398:
            d = "ㅋ실패"
        if ran == 399:
            d = "ㅋ실패"
        if ran == 400:
            d = "ㅋ실패"
        if ran == 401:
            d = "ㅋ실패"
        if ran == 402:
            d = "ㅋ실패"
        if ran == 403:
            d = "ㅋ실패"
        if ran == 404:
            d = "ㅋ실패"
        if ran == 405:
            d = "ㅋ실패"
        if ran == 406:
            d = "ㅋ실패"
        if ran == 407:
            d = "ㅋ실패"
        if ran == 408:
            d = "ㅋ실패"
        if ran == 409:
            d = "ㅋ실패"
        if ran == 410:
            d = "ㅋ실패"
        if ran == 411:
            d = "ㅋ실패"
        if ran == 412:
            d = "ㅋ실패"
        if ran == 413:
            d = "ㅋ실패"
        if ran == 414:
            d = "ㅋ실패"
        if ran == 415:
            d = "ㅋ실패"
        if ran == 416:
            d = "ㅋ실패"
        if ran == 417:
            d = "ㅋ실패"
        if ran == 418:
            d = "ㅋ실패"
        if ran == 419:
            d = "ㅋ실패"
        if ran == 420:
            d = "ㅋ실패"
        if ran == 421:
            d = "ㅋ실패"
        if ran == 422:
            d = "ㅋ실패"
        if ran == 423:
            d = "ㅋ실패"
        if ran == 424:
            d = "ㅋ실패"
        if ran == 425:
            d = "ㅋ실패"
        if ran == 426:
            d = "ㅋ실패"
        if ran == 427:
            d = "ㅋ실패"
        if ran == 428:
            d = "ㅋ실패"
        if ran == 429:
            d = "ㅋ실패"
        if ran == 430:
            d = "ㅋ실패"
        if ran == 431:
            d = "ㅋ실패"
        if ran == 432:
            d = "ㅋ실패"
        if ran == 433:
            d = "ㅋ실패"
        if ran == 434:
            d = "ㅋ실패"
        if ran == 435:
            d = "ㅋ실패"
        if ran == 436:
            d = "ㅋ실패"
        if ran == 437:
            d = "ㅋ실패"
        if ran == 438:
            d = "ㅋ실패"
        if ran == 439:
            d = "ㅋ실패"
        if ran == 440:
            d = "ㅋ실패"
        if ran == 441:
            d = "ㅋ실패"
        if ran == 442:
            d = "ㅋ실패"
        if ran == 443:
            d = "ㅋ실패"
        if ran == 444:
            d = "ㅋ실패"
        if ran == 445:
            d = "ㅋ실패"
        if ran == 446:
            d = "ㅋ실패"
        if ran == 447:
            d = "ㅋ실패"
        if ran == 448:
            d = "ㅋ실패"
        if ran == 449:
            d = "ㅋ실패"
        if ran == 450:
            d = "ㅋ실패"
        if ran == 451:
            d = "ㅋ실패"
        if ran == 452:
            d = "ㅋ실패"
        if ran == 453:
            d = "ㅋ실패"
        if ran == 454:
            d = "ㅋ실패"
        if ran == 455:
            d = "ㅋ실패"
        if ran == 456:
            d = "ㅋ실패"
        if ran == 457:
            d = "ㅋ실패"
        if ran == 458:
            d = "ㅋ실패"
        if ran == 459:
            d = "ㅋ실패"
        if ran == 460:
            d = "ㅋ실패"
        if ran == 461:
            d = "ㅋ실패"
        if ran == 462:
            d = "ㅋ실패"
        if ran == 463:
            d = "오성공"
        if ran == 464:
            d = "ㅋ실패"
        if ran == 465:
            d = "4실패"
        if ran == 466:
            d = "ㅋ실패"
        if ran == 467:
            d = "ㅋ실패"
        if ran == 468:
            d = "ㅋ실패"
        if ran == 469:
            d = "ㅋ실패"
        if ran == 470:
            d = "ㅋ실패"
        if ran == 471:
            d = "ㅋ실패"
        if ran == 472:
            d = "ㅋ실패"
        if ran == 473:
            d = "ㅋ실패"
        if ran == 474:
            d = "ㅋ실패"
        if ran == 475:
            d = "ㅋ실패"
        if ran == 476:
            d = "ㅋ실패"
        if ran == 477:
            d = "ㅋ실패"
        if ran == 478:
            d = "ㅋ실패"
        if ran == 479:
            d = "ㅋ실패"
        if ran == 480:
            d = "ㅋ실패"
        if ran == 481:
            d = "ㅋ실패"
        if ran == 482:
            d = "ㅋ실패"
        if ran == 483:
            d = "ㅋ실패"
        if ran == 484:
            d = "ㅋ실패"
        if ran == 485:
            d = "ㅋ실패"
        if ran == 486:
            d = "ㅋ실패"
        if ran == 487:
            d = "ㅋ실패"
        if ran == 488:
            d = "ㅋ실패"
        if ran == 489:
            d = "ㅋ실패"
        if ran == 490:
            d = "ㅋ실패"
        if ran == 491:
            d = "ㅋ실패"
        if ran == 492:
            d = "ㅋ실패"
        if ran == 493:
            d = "ㅋ실패"
        if ran == 494:
            d = "ㅋ실패"
        if ran == 495:
            d = "ㅋ실패"
        if ran == 496:
            d = "ㅋ실패"
        if ran == 497:
            d = "ㅋ실패"
        if ran == 498:
            d = "ㅋ실패"
        if ran == 499:
            d = "ㅋ실패"
        if ran == 500:
            d = "ㅋ실패"
        if ran == 501:
            d = "ㅋ실패"
        if ran == 502:
            d = "ㅋ실패"
        if ran == 503:
            d = "ㅋ실패"
        if ran == 504:
            d = "ㅋ실패"
        if ran == 505:
            d = "ㅋ실패"
        if ran == 506:
            d = "ㅋ실패"
        if ran == 507:
            d = "ㅋ실패"
        if ran == 508:
            d = "ㅋ실패"
        if ran == 509:
            d = "ㅋ실패"
        if ran == 510:
            d = "ㅋ실패"
        if ran == 511:
            d = "ㅋ실패"
        if ran == 512:
            d = "ㅋ실패"
        if ran == 513:
            d = "ㅋ실패"
        if ran == 514:
            d = "ㅋ실패"
        if ran == 515:
            d = "ㅋ실패"
        if ran == 516:
            d = "ㅋ실패"
        if ran == 517:
            d = "ㅋ실패"
        if ran == 518:
            d = "ㅋ실패"
        if ran == 519:
            d = "ㅋ실패"
        if ran == 520:
            d = "ㅋ실패"
        if ran == 521:
            d = "ㅋ실패"
        if ran == 522:
            d = "ㅋ실패"
        if ran == 523:
            d = "ㅋ실패"
        if ran == 524:
            d = "ㅋ실패"
        if ran == 525:
            d = "ㅋ실패"
        if ran == 526:
            d = "ㅋ실패"
        if ran == 527:
            d = "ㅋ실패"
        if ran == 528:
            d = "ㅋ실패"
        if ran == 529:
            d = "ㅋ실패"
        if ran == 530:
            d = "ㅋ실패"
        if ran == 531:
            d = "ㅋ실패"
        if ran == 532:
            d = "ㅋ실패"
        if ran == 533:
            d = "ㅋ실패"
        if ran == 534:
            d = "ㅋ실패"
        if ran == 535:
            d = "ㅋ실패"
        if ran == 536:
            d = "ㅋ실패"
        if ran == 537:
            d = "ㅋ실패"
        if ran == 538:
            d = "ㅋ실패"
        if ran == 539:
            d = "ㅋ실패"
        if ran == 540:
            d = "ㅋ실패"
        if ran == 541:
            d = "ㅋ실패"
        if ran == 542:
            d = "ㅋ실패"
        if ran == 543:
            d = "ㅋ실패"
        if ran == 544:
            d = "ㅋ실패"
        if ran == 545:
            d = "ㅋ실패"
        if ran == 546:
            d = "ㅋ실패"
        if ran == 547:
            d = "ㅋ실패"
        if ran == 548:
            d = "ㅋ실패"
        if ran == 549:
            d = "ㅋ실패"
        if ran == 550:
            d = "ㅋ실패"
        if ran == 551:
            d = "ㅋ실패"
        if ran == 552:
            d = "ㅋ실패"
        if ran == 553:
            d = "ㅋ실패"
        if ran == 554:
            d = "ㅋ실패"
        if ran == 555:
            d = "ㅋ실패"
        if ran == 556:
            d = "ㅋ실패"
        if ran == 557:
            d = "ㅋ실패"
        if ran == 558:
            d = "ㅋ실패"
        if ran == 559:
            d = "ㅋ실패"
        if ran == 560:
            d = "ㅋ실패"
        if ran == 561:
            d = "ㅋ실패"
        if ran == 562:
            d = "ㅋ실패"
        if ran == 563:
            d = "ㅋ실패"
        if ran == 564:
            d = "ㅋ실패"
        if ran == 565:
            d = "ㅋ실패"
        if ran == 566:
            d = "ㅋ실패"
        if ran == 567:
            d = "ㅋ실패"
        if ran == 568:
            d = "ㅋ실패"
        if ran == 569:
            d = "ㅋ실패"
        if ran == 570:
            d = "ㅋ실패"
        if ran == 571:
            d = "ㅋ실패"
        if ran == 572:
            d = "ㅋ실패"
        if ran == 573:
            d = "ㅋ실패"
        if ran == 574:
            d = "ㅋ실패"
        if ran == 575:
            d = "ㅋ실패"
        if ran == 576:
            d = "ㅋ실패"
        if ran == 577:
            d = "ㅋ실패"
        if ran == 578:
            d = "ㅋ실패"
        if ran == 579:
            d = "ㅋ실패"
        if ran == 580:
            d = "ㅋ실패"
        if ran == 581:
            d = "ㅋ실패"
        if ran == 582:
            d = "ㅋ실패"
        if ran == 583:
            d = "ㅋ실패"
        if ran == 584:
            d = "ㅋ실패"
        if ran == 585:
            d = "ㅋ실패"
        if ran == 586:
            d = "ㅋ실패"
        if ran == 587:
            d = "ㅋ실패"
        if ran == 588:
            d = "ㅋ실패"
        if ran == 589:
            d = "ㅋ실패"
        if ran == 590:
            d = "ㅋ실패"
        if ran == 591:
            d = "ㅋ실패"
        if ran == 592:
            d = "ㅋ실패"
        if ran == 593:
            d = "ㅋ실패"
        if ran == 594:
            d = "ㅋ실패"
        if ran == 595:
            d = "ㅋ실패"
        if ran == 596:
            d = "ㅋ실패"
        if ran == 597:
            d = "ㅋ실패"
        if ran == 598:
            d = "ㅋ실패"
        if ran == 599:
            d = "ㅋ실패"
        if ran == 600:
            d = "ㅋ실패"
        if ran == 601:
            d = "ㅋ실패"
        if ran == 602:
            d = "ㅋ실패"
        if ran == 603:
            d = "ㅋ실패"
        if ran == 604:
            d = "ㅋ실패"
        if ran == 605:
            d = "ㅋ실패"
        if ran == 606:
            d = "ㅋ실패"
        if ran == 607:
            d = "ㅋ실패"
        if ran == 608:
            d = "ㅋ실패"
        if ran == 609:
            d = "ㅋ실패"
        if ran == 610:
            d = "ㅋ실패"
        if ran == 611:
            d = "ㅋ실패"
        if ran == 612:
            d = "ㅋ실패"
        if ran == 613:
            d = "ㅋ실패"
        if ran == 614:
            d = "ㅋ실패"
        if ran == 615:
            d = "ㅋ실패"
        if ran == 616:
            d = "ㅋ실패"
        if ran == 617:
            d = "ㅋ실패"
        if ran == 618:
            d = "ㅋ실패"
        if ran == 619:
            d = "ㅋ실패"
        if ran == 620:
            d = "ㅋ실패"
        if ran == 621:
            d = "ㅋ실패"
        if ran == 622:
            d = "ㅋ실패"
        if ran == 623:
            d = "ㅋ실패"
        if ran == 624:
            d = "ㅋ실패"
        if ran == 625:
            d = "ㅋ실패"
        if ran == 626:
            d = "ㅋ실패"
        if ran == 627:
            d = "ㅋ실패"
        if ran == 628:
            d = "ㅋ실패"
        if ran == 629:
            d = "ㅋ실패"
        if ran == 630:
            d = "ㅋ실패"
        if ran == 631:
            d = "ㅋ실패"
        if ran == 632:
            d = "ㅋ실패"
        if ran == 633:
            d = "ㅋ실패"
        if ran == 634:
            d = "ㅋ실패"
        if ran == 635:
            d = "ㅋ실패"
        if ran == 636:
            d = "ㅋ실패"
        if ran == 637:
            d = "ㅋ실패"
        if ran == 638:
            d = "ㅋ실패"
        if ran == 639:
            d = "ㅋ실패"
        if ran == 640:
            d = "ㅋ실패"
        if ran == 641:
            d = "ㅋ실패"
        if ran == 642:
            d = "ㅋ실패"
        if ran == 643:
            d = "ㅋ실패"
        if ran == 644:
            d = "ㅋ실패"
        if ran == 645:
            d = "ㅋ실패"
        if ran == 646:
            d = "ㅋ실패"
        if ran == 647:
            d = "ㅋ실패"
        if ran == 648:
            d = "ㅋ실패"
        if ran == 649:
            d = "ㅋ실패"
        if ran == 650:
            d = "ㅋ실패"
        if ran == 651:
            d = "ㅋ실패"
        if ran == 652:
            d = "ㅋ실패"
        if ran == 653:
            d = "ㅋ실패"
        if ran == 654:
            d = "ㅋ실패"
        if ran == 655:
            d = "ㅋ실패"
        if ran == 656:
            d = "ㅋ실패"
        if ran == 657:
            d = "ㅋ실패"
        if ran == 658:
            d = "ㅋ실패"
        if ran == 659:
            d = "ㅋ실패"
        if ran == 660:
            d = "ㅋ실패"
        if ran == 661:
            d = "ㅋ실패"
        if ran == 662:
            d = "ㅋ실패"
        if ran == 663:
            d = "ㅋ실패"
        if ran == 664:
            d = "ㅋ실패"
        if ran == 665:
            d = "ㅋ실패"
        if ran == 666:
            d = "ㅋ실패"
        if ran == 667:
            d = "ㅋ실패"
        if ran == 668:
            d = "ㅋ실패"
        if ran == 669:
            d = "ㅋ실패"
        if ran == 670:
            d = "ㅋ실패"
        if ran == 671:
            d = "ㅋ실패"
        if ran == 672:
            d = "ㅋ실패"
        if ran == 673:
            d = "ㅋ실패"
        if ran == 674:
            d = "ㅋ실패"
        if ran == 675:
            d = "ㅋ실패"
        if ran == 676:
            d = "ㅋ실패"
        if ran == 677:
            d = "ㅋ실패"
        if ran == 678:
            d = "ㅋ실패"
        if ran == 679:
            d = "ㅋ실패"
        if ran == 680:
            d = "ㅋ실패"
        if ran == 681:
            d = "ㅋ실패"
        if ran == 682:
            d = "ㅋ실패"
        if ran == 683:
            d = "ㅋ실패"
        if ran == 684:
            d = "ㅋ실패"
        if ran == 685:
            d = "ㅋ실패"
        if ran == 686:
            d = "ㅋ실패"
        if ran == 687:
            d = "ㅋ실패"
        if ran == 688:
            d = "ㅋ실패"
        if ran == 689:
            d = "ㅋ실패"
        if ran == 690:
            d = "ㅋ실패"
        if ran == 691:
            d = "ㅋ실패"
        if ran == 692:
            d = "ㅋ실패"
        if ran == 693:
            d = "ㅋ실패"
        if ran == 694:
            d = "ㅋ실패"
        if ran == 695:
            d = "ㅋ실패"
        if ran == 696:
            d = "ㅋ실패"
        if ran == 697:
            d = "ㅋ실패"
        if ran == 698:
            d = "ㅋ실패"
        if ran == 699:
            d = "ㅋ실패"
        if ran == 700:
            d = "ㅋ실패"
        if ran == 701:
            d = "ㅋ실패"
        if ran == 702:
            d = "ㅋ실패"
        if ran == 703:
            d = "ㅋ실패"
        if ran == 704:
            d = "ㅋ실패"
        if ran == 705:
            d = "ㅋ실패"
        if ran == 706:
            d = "ㅋ실패"
        if ran == 707:
            d = "ㅋ실패"
        if ran == 708:
            d = "ㅋ실패"
        if ran == 709:
            d = "ㅋ실패"
        if ran == 710:
            d = "ㅋ실패"
        if ran == 711:
            d = "ㅋ실패"
        if ran == 712:
            d = "ㅋ실패"
        if ran == 713:
            d = "ㅋ실패"
        if ran == 714:
            d = "ㅋ실패"
        if ran == 715:
            d = "ㅋ실패"
        if ran == 716:
            d = "ㅋ실패"
        if ran == 717:
            d = "ㅋ실패"
        if ran == 718:
            d = "ㅋ실패"
        if ran == 719:
            d = "ㅋ실패"
        if ran == 720:
            d = "ㅋ실패"
        if ran == 721:
            d = "ㅋ실패"
        if ran == 722:
            d = "ㅋ실패"
        if ran == 723:
            d = "ㅋ실패"
        if ran == 724:
            d = "ㅋ실패"
        if ran == 725:
            d = "ㅋ실패"
        if ran == 726:
            d = "ㅋ실패"
        if ran == 727:
            d = "ㅋ실패"
        if ran == 728:
            d = "ㅋ실패"
        if ran == 729:
            d = "ㅋ실패"
        if ran == 730:
            d = "ㅋ실패"
        if ran == 731:
            d = "ㅋ실패"
        if ran == 732:
            d = "ㅋ실패"
        if ran == 733:
            d = "ㅋ실패"
        if ran == 734:
            d = "ㅋ실패"
        if ran == 735:
            d = "ㅋ실패"
        if ran == 736:
            d = "ㅋ실패"
        if ran == 737:
            d = "ㅋ실패"
        if ran == 738:
            d = "ㅋ실패"
        if ran == 739:
            d = "ㅋ실패"
        if ran == 740:
            d = "ㅋ실패"
        if ran == 741:
            d = "ㅋ실패"
        if ran == 742:
            d = "ㅋ실패"
        if ran == 743:
            d = "ㅋ실패"
        if ran == 744:
            d = "ㅋ실패"
        if ran == 745:
            d = "ㅋ실패"
        if ran == 746:
            d = "ㅋ실패"
        if ran == 747:
            d = "ㅋ실패"
        if ran == 748:
            d = "ㅋ실패"
        if ran == 749:
            d = "ㅋ실패"
        if ran == 750:
            d = "ㅋ실패"
        if ran == 751:
            d = "ㅋ실패"
        if ran == 752:
            d = "ㅋ실패"
        if ran == 753:
            d = "ㅋ실패"
        if ran == 754:
            d = "ㅋ실패"
        if ran == 755:
            d = "ㅋ실패"
        if ran == 756:
            d = "ㅋ실패"
        if ran == 757:
            d = "ㅋ실패"
        if ran == 758:
            d = "ㅋ실패"
        if ran == 759:
            d = "ㅋ실패"
        if ran == 760:
            d = "ㅋ실패"
        if ran == 761:
            d = "ㅋ실패"
        if ran == 762:
            d = "ㅋ실패"
        if ran == 763:
            d = "ㅋ실패"
        if ran == 764:
            d = "ㅋ실패"
        if ran == 765:
            d = "ㅋ실패"
        if ran == 766:
            d = "ㅋ실패"
        if ran == 767:
            d = "ㅋ실패"
        if ran == 768:
            d = "ㅋ실패"
        if ran == 769:
            d = "ㅋ실패"
        if ran == 770:
            d = "ㅋ실패"
        if ran == 771:
            d = "ㅋ실패"
        if ran == 772:
            d = "ㅋ실패"
        if ran == 773:
            d = "ㅋ실패"
        if ran == 774:
            d = "ㅋ실패"
        if ran == 775:
            d = "ㅋ실패"
        if ran == 776:
            d = "ㅋ실패"
        if ran == 777:
            d = "ㅋ실패"
        if ran == 778:
            d = "ㅋ실패"
        if ran == 779:
            d = "ㅋ실패"
        if ran == 780:
            d = "ㅋ실패"
        if ran == 781:
            d = "ㅋ실패"
        if ran == 782:
            d = "ㅋ실패"
        if ran == 783:
            d = "ㅋ실패"
        if ran == 784:
            d = "ㅋ실패"
        if ran == 785:
            d = "ㅋ실패"
        if ran == 786:
            d = "ㅋ실패"
        if ran == 787:
            d = "ㅋ실패"
        if ran == 788:
            d = "ㅋ실패"
        if ran == 789:
            d = "ㅋ실패"
        if ran == 790:
            d = "ㅋ실패"
        if ran == 791:
            d = "ㅋ실패"
        if ran == 792:
            d = "ㅋ실패"
        if ran == 793:
            d = "ㅋ실패"
        if ran == 794:
            d = "ㅋ실패"
        if ran == 795:
            d = "ㅋ실패"
        if ran == 796:
            d = "ㅋ실패"
        if ran == 797:
            d = "ㅋ실패"
        if ran == 798:
            d = "ㅋ실패"
        if ran == 799:
            d = "ㅋ실패"
        if ran == 800:
            d = "ㅋ실패"
        if ran == 801:
            d = "ㅋ실패"
        if ran == 802:
            d = "ㅋ실패"
        if ran == 803:
            d = "ㅋ실패"
        if ran == 804:
            d = "ㅋ실패"
        if ran == 805:
            d = "ㅋ실패"
        if ran == 806:
            d = "ㅋ실패"
        if ran == 807:
            d = "ㅋ실패"
        if ran == 808:
            d = "ㅋ실패"
        if ran == 809:
            d = "ㅋ실패"
        if ran == 810:
            d = "ㅋ실패"
        if ran == 811:
            d = "ㅋ실패"
        if ran == 812:
            d = "ㅋ실패"
        if ran == 813:
            d = "ㅋ실패"
        if ran == 814:
            d = "ㅋ실패"
        if ran == 815:
            d = "ㅋ실패"
        if ran == 816:
            d = "ㅋ실패"
        if ran == 817:
            d = "ㅋ실패"
        if ran == 818:
            d = "ㅋ실패"
        if ran == 819:
            d = "ㅋ실패"
        if ran == 820:
            d = "ㅋ실패"
        if ran == 821:
            d = "ㅋ실패"
        if ran == 822:
            d = "ㅋ실패"
        if ran == 823:
            d = "ㅋ실패"
        if ran == 824:
            d = "ㅋ실패"
        if ran == 825:
            d = "ㅋ실패"
        if ran == 826:
            d = "ㅋ실패"
        if ran == 827:
            d = "ㅋ실패"
        if ran == 828:
            d = "ㅋ실패"
        if ran == 829:
            d = "ㅋ실패"
        if ran == 830:
            d = "ㅋ실패"
        if ran == 831:
            d = "ㅋ실패"
        if ran == 832:
            d = "ㅋ실패"
        if ran == 833:
            d = "ㅋ실패"
        if ran == 834:
            d = "ㅋ실패"
        if ran == 835:
            d = "ㅋ실패"
        if ran == 836:
            d = "ㅋ실패"
        if ran == 837:
            d = "ㅋ실패"
        if ran == 838:
            d = "ㅋ실패"
        if ran == 839:
            d = "ㅋ실패"
        if ran == 840:
            d = "ㅋ실패"
        if ran == 841:
            d = "ㅋ실패"
        if ran == 842:
            d = "ㅋ실패"
        if ran == 843:
            d = "ㅋ실패"
        if ran == 844:
            d = "ㅋ실패"
        if ran == 845:
            d = "ㅋ실패"
        if ran == 846:
            d = "ㅋ실패"
        if ran == 847:
            d = "ㅋ실패"
        if ran == 848:
            d = "ㅋ실패"
        if ran == 849:
            d = "ㅋ실패"
        if ran == 850:
            d = "ㅋ실패"
        if ran == 851:
            d = "ㅋ실패"
        if ran == 852:
            d = "ㅋ실패"
        if ran == 853:
            d = "ㅋ실패"
        if ran == 854:
            d = "ㅋ실패"
        if ran == 855:
            d = "ㅋ실패"
        if ran == 856:
            d = "ㅋ실패"
        if ran == 857:
            d = "ㅋ실패"
        if ran == 858:
            d = "ㅋ실패"
        if ran == 859:
            d = "ㅋ실패"
        if ran == 860:
            d = "ㅋ실패"
        if ran == 861:
            d = "ㅋ실패"
        if ran == 862:
            d = "ㅋ실패"
        if ran == 863:
            d = "ㅋ실패"
        if ran == 864:
            d = "ㅋ실패"
        if ran == 865:
            d = "ㅋ실패"
        if ran == 866:
            d = "ㅋ실패"
        if ran == 867:
            d = "ㅋ실패"
        if ran == 868:
            d = "ㅋ실패"
        if ran == 869:
            d = "ㅋ실패"
        if ran == 870:
            d = "ㅋ실패"
        if ran == 871:
            d = "ㅋ실패"
        if ran == 872:
            d = "ㅋ실패"
        if ran == 873:
            d = "ㅋ실패"
        if ran == 874:
            d = "ㅋ실패"
        if ran == 875:
            d = "ㅋ실패"
        if ran == 876:
            d = "ㅋ실패"
        if ran == 877:
            d = "ㅋ실패"
        if ran == 878:
            d = "ㅋ실패"
        if ran == 879:
            d = "ㅋ실패"
        if ran == 880:
            d = "ㅋ실패"
        if ran == 881:
            d = "ㅋ실패"
        if ran == 882:
            d = "ㅋ실패"
        if ran == 883:
            d = "ㅋ실패"
        if ran == 884:
            d = "ㅋ실패"
        if ran == 885:
            d = "ㅋ실패"
        if ran == 886:
            d = "ㅋ실패"
        if ran == 887:
            d = "ㅋ실패"
        if ran == 888:
            d = "ㅋ실패"
        if ran == 889:
            d = "ㅋ실패"
        if ran == 890:
            d = "ㅋ실패"
        if ran == 891:
            d = "ㅋ실패"
        if ran == 892:
            d = "ㅋ실패"
        if ran == 893:
            d = "ㅋ실패"
        if ran == 894:
            d = "ㅋ실패"
        if ran == 895:
            d = "ㅋ실패"
        if ran == 896:
            d = "ㅋ실패"
        if ran == 897:
            d = "ㅋ실패"
        if ran == 898:
            d = "ㅋ실패"
        if ran == 899:
            d = "ㅋ실패"
        if ran == 900:
            d = "ㅋ실패"
        if ran == 901:
            d = "ㅋ실패"
        if ran == 902:
            d = "ㅋ실패"
        if ran == 903:
            d = "ㅋ실패"
        if ran == 904:
            d = "ㅋ실패"
        if ran == 905:
            d = "ㅋ실패"
        if ran == 906:
            d = "ㅋ실패"
        if ran == 907:
            d = "ㅋ실패"
        if ran == 908:
            d = "ㅋ실패"
        if ran == 909:
            d = "ㅋ실패"
        if ran == 910:
            d = "ㅋ실패"
        if ran == 911:
            d = "ㅋ실패"
        if ran == 912:
            d = "ㅋ실패"
        if ran == 913:
            d = "ㅋ실패"
        if ran == 914:
            d = "ㅋ실패"
        if ran == 915:
            d = "ㅋ실패"
        if ran == 916:
            d = "ㅋ실패"
        if ran == 917:
            d = "ㅋ실패"
        if ran == 918:
            d = "ㅋ실패"
        if ran == 919:
            d = "ㅋ실패"
        if ran == 920:
            d = "ㅋ실패"
        if ran == 921:
            d = "ㅋ실패"
        if ran == 922:
            d = "ㅋ실패"
        if ran == 923:
            d = "ㅋ실패"
        if ran == 924:
            d = "ㅋ실패"
        if ran == 925:
            d = "ㅋ실패"
        if ran == 926:
            d = "ㅋ실패"
        if ran == 927:
            d = "ㅋ실패"
        if ran == 928:
            d = "ㅋ실패"
        if ran == 929:
            d = "ㅋ실패"
        if ran == 930:
            d = "ㅋ실패"
        if ran == 931:
            d = "ㅋ실패"
        if ran == 932:
            d = "ㅋ실패"
        if ran == 933:
            d = "ㅋ실패"
        if ran == 934:
            d = "ㅋ실패"
        if ran == 935:
            d = "ㅋ실패"
        if ran == 936:
            d = "ㅋ실패"
        if ran == 937:
            d = "ㅋ실패"
        if ran == 938:
            d = "ㅋ실패"
        if ran == 939:
            d = "ㅋ실패"
        if ran == 940:
            d = "ㅋ실패"
        if ran == 941:
            d = "ㅋ실패"
        if ran == 942:
            d = "ㅋ실패"
        if ran == 943:
            d = "ㅋ실패"
        if ran == 944:
            d = "ㅋ실패"
        if ran == 945:
            d = "ㅋ실패"
        if ran == 946:
            d = "ㅋ실패"
        if ran == 947:
            d = "ㅋ실패"
        if ran == 948:
            d = "ㅋ실패"
        if ran == 949:
            d = "ㅋ실패"
        if ran == 950:
            d = "ㅋ실패"
        if ran == 951:
            d = "ㅋ실패"
        if ran == 952:
            d = "ㅋ실패"
        if ran == 953:
            d = "ㅋ실패"
        if ran == 954:
            d = "ㅋ실패"
        if ran == 955:
            d = "ㅋ실패"
        if ran == 956:
            d = "ㅋ실패"
        if ran == 957:
            d = "ㅋ실패"
        if ran == 958:
            d = "ㅋ실패"
        if ran == 959:
            d = "ㅋ실패"
        if ran == 960:
            d = "ㅋ실패"
        if ran == 961:
            d = "ㅋ실패"
        if ran == 962:
            d = "ㅋ실패"
        if ran == 963:
            d = "ㅋ실패"
        if ran == 964:
            d = "ㅋ실패"
        if ran == 965:
            d = "ㅋ실패"
        if ran == 966:
            d = "ㅋ실패"
        if ran == 967:
            d = "ㅋ실패"
        if ran == 968:
            d = "ㅋ실패"
        if ran == 969:
            d = "ㅋ실패"
        if ran == 970:
            d = "ㅋ실패"
        if ran == 971:
            d = "ㅋ실패"
        if ran == 972:
            d = "ㅋ실패"
        if ran == 973:
            d = "ㅋ실패"
        if ran == 974:
            d = "ㅋ실패"
        if ran == 975:
            d = "ㅋ실패"
        if ran == 976:
            d = "ㅋ실패"
        if ran == 977:
            d = "ㅋ실패"
        if ran == 978:
            d = "ㅋ실패"
        if ran == 979:
            d = "ㅋ실패"
        if ran == 980:
            d = "ㅋ실패"
        if ran == 981:
            d = "ㅋ실패"
        if ran == 982:
            d = "ㅋ실패"
        if ran == 983:
            d = "ㅋ실패"
        if ran == 984:
            d = "ㅋ실패"
        if ran == 985:
            d = "ㅋ실패"
        if ran == 986:
            d = "ㅋ실패"
        if ran == 987:
            d = "ㅋ실패"
        if ran == 988:
            d = "ㅋ실패"
        if ran == 989:
            d = "ㅋ실패"
        if ran == 990:
            d = "ㅋ실패"
        if ran == 991:
            d = "ㅋ실패"
        if ran == 992:
            d = "ㅋ실패"
        if ran == 993:
            d = "ㅋ실패"
        if ran == 994:
            d = "ㅋ실패"
        if ran == 995:
            d = "ㅋ실패"
        if ran == 996:
            d = "ㅋ실패"
        if ran == 997:
            d = "ㅋ실패"
        if ran == 998:
            d = "ㅋ실패"
        if ran == 999:
            d = "ㅋ실패"        
        await message.channel.send(d)

@bot.command()
async def 따라해(ctx, *, text):
    await ctx.send(text)


bot.run('ODkxNTEwMTY0NTgxMTIyMDg4.YU_Zig.hh1KlLfRgzDY72OjmIVAi8t1IT8')
client.run(token)