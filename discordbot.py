import discord
import os
from datetime import date
import random

client = discord.Client()
alt_names = {
    'shion':    ['紫咲シオン', 'シオン', 'クソガキ'],
    'haato':    ['赤井はあと', 'はあちゃま', 'はあと'],
    'aqua':     ['湊あくあ', 'あくたん', 'あくあ'],
    'matsuri':  ['夏色まつり', 'まつり', 'まつりちゃん'],
    'ayame':    ['百鬼あやめ', 'あやめ', '余', 'パコ余', 'あやめ', 'お嬢'],
    'aloe':     ['魔乃アロエ', 'アロエ'],
    'lamy':     ['雪花ラミィ', 'ラミィ'],
    'nene':     ['桃鈴ねね', 'ねねち', 'ねね', '馬場なつみ', 'ガイジ'],
    'suisei':   ['星街すいせい', 'すいちゃん', '星街', 'すいせい'],
    'okayu':    ['猫又おかゆ', 'おかゆ'],
    'roboco':   ['ロボ子'],
    "miko":     ['さくらみこ','みこち', 'みこ', 'ましろ', 'ましろちゃん'],
    "noel":     ['白銀ノエル', 'ノエル', '日南', '団長'],
    "luna":     ['姫森ルーナ', 'バシの嫁', 'ルーナ'],
    "towa":     ['常闇トワ', 'ドブ', 'トワ'],
    "choco":    ['癒月ちょこ', 'ちょこ'],
    "pekora":   ['兎田ぺこら', '110ちゃん', 'ぺこら', 'ぺっさん'],
    "marine":   ['宝鍾マリン', 'マリン', 'みかりん'],
    "mel":      ['夜空メル', 'メル', 'メルさん'], 
    "polka":    ['尾丸ポルカ', 'ポルカ'],
    "azki":     ['Azki'],
    "sora":     ['ときのそら', 'そら', '天皇'],
    "rusia":    ['潤羽るしあ', 'るしあ', 'る', '!', '！'],
    "flare":    ['不知火フレア', 'フレア', 'ふーたん'],
    "coco":     ['桐生ココ', 'ココ', 'コっさん', 'ココさん'],
    "watame":   ['角巻わため', 'わため', 'みけたま'],
    "akirose":  ['アキ・ローゼンタール', 'アキロゼ'],
    "fubuki":   ['白上フブキ', 'フブキ', 'フブちゃん', '親方'],
    "mio":      ['大神ミオ', 'ミオシャ', 'ミオ'],
    "korone":   ['戌神ころね', 'ころね', 'ころさん', '宮助'],
    "botan":    ['獅白ぼたん', 'ぼたん', 'ぼっさん'],
    "kanata":   ['UNDEFINED'],
    "subaru":   ['UNDEFINED'],
}
HolomemBirthdayDict = {
    "shion": date(2002, 6, 3),
    "haato": date(2001, 11, 5),
    "aqua": date(1999, 12, 7),
    "matsuri": date(1999, 1, 25),
    "ayame": date(1998, 10, 16),
    "aloe": date(1998, 8, 11),
    "lamy": date(1997, 11, 3),
    "nene": date(1997, 9, 2),
    "suisei": date(1997, 4, 18),
    "okayu": date(1997, 4, 13),
    "roboco": date(1996, 4, 2),
    "miko": date(1996, 2, 27),
    "noel": date(1995, 5, 15),
    "luna": date(1994, 12, 3),
    "towa": date(1994, 11, 28),
    "choco": date(1994, 9, 17),
    "pekora": date(1994, 3, 3),
    "marine": date(1992, 12, 25),
    "mel": date(1992, 7, 28),
    "polka": date(1991, 10, 5),
    "azki": date(1991, 9, 27),
    "sora": date(1989, 5, 15),
    "rusia": date(1989, 1, 18),
    "flare": date(1988, 11, 15),
    "coco": date(1988, 6, 8),
    "watame": date(1987, 11, 27),
    "akirose": date(1987, 10, 7),
    "fubuki": date(1987, 1, 6),
    "mio": date(1985, 9, 12),
    "korone": date(1984, 10, 10),
    "botan": date(1984, 4, 13),
    "kanata": None,
    "subaru": None,
}

def ReturnAgeOnly(key: str) -> str:
    return str(int((date.today() - HolomemBirthdayDict[key]).days / 365))

All = f'''
```
2002/06/03 {ReturnAgeOnly("shion")}歳 紫咲シオン
2001/11/05 {ReturnAgeOnly("haato")}歳 赤井はあと
1999/12/07 {ReturnAgeOnly("aqua")}歳 湊あくあ
1999/01/25 {ReturnAgeOnly("matsuri")}歳 夏色まつり
1998/10/16 {ReturnAgeOnly("ayame")}歳 百鬼あやめ
1998/08/11 {ReturnAgeOnly("aloe")}歳 魔乃アロエ
1997/11/03 {ReturnAgeOnly("lamy")}歳 雪花ラミィ
1997/09/02 {ReturnAgeOnly("nene")}歳 桃鈴ねね
1997/04/18 {ReturnAgeOnly("suisei")}歳 星街すいせい
1997/04/13 {ReturnAgeOnly("okayu")}歳 猫又おかゆ
1996/04/02 {ReturnAgeOnly("roboco")}歳 ロボ子さん
1996/02/27 {ReturnAgeOnly("miko")}歳 さくらみこ
1995/05/15 {ReturnAgeOnly("noel")}歳 白銀ノエル
1994/12/03 {ReturnAgeOnly("luna")}歳 姫森ルーナ
1994/11/28 {ReturnAgeOnly("towa")}歳 常闇トワ
1994/09/17 {ReturnAgeOnly("choco")}歳 癒月ちょこ
1994/03/03 {ReturnAgeOnly("pekora")}歳 兎田ぺこら
1992/12/25 {ReturnAgeOnly("marine")}歳 宝鐘マリン
1992/07/28 {ReturnAgeOnly("mel")}歳 夜空メル
1991/10/05 {ReturnAgeOnly("polka")}歳 尾丸ポルカ
1991/09/27 {ReturnAgeOnly("azki")}歳 AZKi
1989/05/15 {ReturnAgeOnly("sora")}歳 ときのそら
1989/01/18 {ReturnAgeOnly("rusia")}歳 潤羽るしあ
1988/11/15 {ReturnAgeOnly("flare")}歳 不知火フレア
1988/06/08 {ReturnAgeOnly("coco")}歳 桐生ココ
1987/11/27 {ReturnAgeOnly("watame")}歳 角巻わため
1987/10/07 {ReturnAgeOnly("akirose")}歳 アキ・ローゼンタール
1987/01/06 {ReturnAgeOnly("fubuki")}歳 白上フブキ
1985/09/12 {ReturnAgeOnly("mio")}歳 大神ミオ
1984/10/10 {ReturnAgeOnly("korone")}歳 戌神ころね
1984/04/13 {ReturnAgeOnly("botan")}歳 獅白ぼたん
```
'''
def CalcAge(query: str) -> str:
    def QueryToKey(query:str) -> str:
        # k: 'miko', v: [nicknames]
        for k, v in alt_names.items():
            if query in v:
                return (k, v[0], query)    
        return (query, query, query)

    key, jp_name, original_query = QueryToKey(query)
    # if key exists
    if key in HolomemBirthdayDict.keys() and HolomemBirthdayDict[key]:
        # calculate age
        age = int((date.today() - HolomemBirthdayDict[key]).days / 365)
        # create bd_string
        temp = str(HolomemBirthdayDict[key]).split('-')
        bd_string = temp[0] + '年' + temp[1] + '月' + temp[2] + '日'
        # randomly display JP name or nickname
        output_name = jp_name if random.randint(0,1)==1 else original_query
        
        # put them all together
        output = f"{output_name}は{bd_string}生まれの{age}歳だよ"
        return output
    # all
    if key=='all':
        return All
    # other cases
    if key=='黒人':
        return '眷属と一緒に死んだよ'
    else:
        return random.choice([
            "黙れ", 
            "んにゃぴ...",
            "ところで仕事どうだった？",
            "うんうん",
            f"{key}って何？",
            f"昔は好きだったけどな、{key}"
        ])


def write_to_history(buff:list, entry:str):
    if len(entry)<=1:
        return

    if len(buff) <= 800:
        buff.append(entry)
    else:
        buff[random.randint(0,798)] = entry

chat_buffer = []

@client.event
async def on_ready():
    print('Gay peko...')

@client.event
async def on_message(message):
    if not '%gay' in message.content:
        write_to_history(chat_buffer, message.content)    

    if message.author == client.user:
        return

    if message.content.startswith('%gay'):
        query = message.content.split(' ')[1]
        answer = CalcAge(query)
        await message.channel.send(answer)
    
    if '死ね' in message.content:
        ahoy = discord.utils.get(client.emojis, name='ahoy1')
        fubuchan = discord.utils.get(client.emojis, name='emoji_3')
        if ahoy or fubuchan:
            if random.randint(0,1)==1:
                await message.add_reaction(ahoy)
            else:
                await message.add_reaction(fubuchan)
                
    # implement random message sending here
    if random.randint(0,100)==50:
        msg = random.choice(chat_buffer)
        await message.channel.send(msg)

token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
