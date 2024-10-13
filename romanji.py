from openpyxl import Workbook

# Creating a new workbook and selecting the active worksheet
wb = Workbook()
ws = wb.active

# Setting up the headers
ws.append(["Artist", "Song", "Song(English)", "links", "Publish Date", "Rating"])

# Adding data from the image
data = [
    ["wowaka feat. 初音ミク", "ローリンガール", "Rollin’ Girl", "14/2/2010", 1912],
    ["iroha(sasaki) feat. 鏡音リン", "炉心融解", "Meltdown", "19/12/2008", 1699],
    ["ハチ feat. 初音ミク, GUMI", "マトリョシカ", "Matryoshka", "19/8/2010", 1474],
    ["Neru feat. 鏡音リン Append (Power)", "ロストワンの号哭", "Lost one Gokoku", "4/3/2013", 1402],
    ["黒うさP feat. 初音ミク", "千本桜", "Thousand Cherry Blossoms", "17/9/2011", 1268],
    ["wowaka feat. 初音ミク, 鏡音リン", "アンノウン・マザーグース", "Unknown Mother Goose", "18/5/2010", 1262],
    ["Giga feat. 鏡音リン V3 (Solid)", "ビバハピ", "Viva Happy", "17/8/2014", 1195],
    ["ryo feat. 初音ミク", "ODDS&ENDS", "ODDS&ENDS", "14/8/2012", 1169],
    ["ryo, supercell feat. 初音ミク", "恋は戦争", "Love is War", "22/2/2008", 1148],
    ["doriko feat. 初音ミク", "ロミオとシンデレラ", "Romeo and Cinderella", "6/4/2009", 1088],
    ["ryo, supercell feat. 初音ミク", "ワールドイズマイン", "World is Mine", "31/5/2008", 1087],
    ["Giga, Reol feat. 鏡音リン Append (Power), V3 GUMI (Power)", "LUVORATORRRRRY!", "LUVORATORRRRRY!", "22/2/2014", 1074],
    ["Neru, それは何 feat. 鏡音リン Append (Power), 鏡音リン Append (Sweet)", "東京テディベア", "Tokyo Teddy Bear", "14/8/2011", 1062],
    ["wowaka, トリ音 feat. 初音ミク V4X (Dark)", "アンノウン・マザーグース", "Unknown Mother Goose", "22/8/2017", 1051],
    ["ryo feat. 初音ミク", "メルト", "Melt", "7/12/2007", 1002],
    ["ピノキオP feat. 初音ミク Append (Dark)", "ありふれたせかいせいふく", "Commonplace World Domination", "18/6/2012", 993],
    ["wowaka feat. 初音ミク", "裏表ラバーズ", "Two-Faced Lovers", "30/8/2009", 974],
    ["Crusher, CIRCRUSH feat. V3 GUMI (English)", "ECHO", "ECHO", "8/10/2014", 968],
    ["DECO*27 feat. GUMI", "モザイクロール", "Mozaik Role", "15/7/2010", 963],
    ["kemu feat. IA", "六兆年と一夜物語", "Six Trillion Years and One Night's Story", "11/4/2012", 958],
    ["kz feat. 初音ミク", "Tell Your World", "Tell Your World", "18/1/2012", 940],
    ["ハチ feat. 初音ミク", "砂の惑星", "Sand Planet", "20/7/2017", 896],
    ["DECO*27, Naoki Itai feat. 初音ミク V4X (Original)", "ゴーストルール", "Ghost Rule.", "8/1/2016", 893],
    ["うたたP feat. 初音ミク", "こちら、幸福安心委員会です。", "This is the Happiness Assurance Committee.", "15/6/2012", 886],
    ["40mP feat. 初音ミク", "からくりピエロ", "Karakuri Pierrot", "15/7/2011", 885],
]

# Adding rows to the worksheet
for row in data:
    ws.append(row)

# Saving the workbook
file_path = "vocaloid_songs.xlsx"
wb.save(file_path)