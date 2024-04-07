from pymysql import Connection
from Person_define import Player
from player_match import match_player
from player_database import player_database


# 构建Mysql链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Hww20041025",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("badminton")
# 组织SQL语句
# player_database.items() 用于同时遍历字典的键和值。
# player_database.values() 用于仅遍历字典的值。
for name, player in player_database.items():
    sql = f"insert into player(name, height, weight, style) " \
          f"values('{name}', {player.height}, {player.weight}, '{player.style}')"
    # 执行SQL语句
    cursor.execute(sql)


# 关闭Mysql链接对象
conn.close()