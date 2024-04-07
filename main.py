from Person_define import Player
from player_match import match_player
from player_database import player_database
from pymysql import Connection

user_name = str(input("请输入你的姓名: "))
user_height = int(input("请输入你的身高: "))
user_weight = int(input("请输入你的体重: "))
user_style = str(input("请输入你理想的类型: "))

# 调用匹配函数并获取最接近的球员
matched_player = match_player(player_database, user_height, user_weight, user_style)

# 输出结果
if matched_player:
    print(f"与您最接近的现役球员是：{matched_player}")
else:
    print("没有找到匹配的现役球员。")
