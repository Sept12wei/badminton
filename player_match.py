from player_database import player_database
from Person_define import Player
# 定义匹配球员的函数
def match_player(database, height, weight, style) -> Player:
    closest_player = None
    min_diff = float('inf')  # 正无穷大的意思

    # 遍历数据库中的每个球员
    for name, player in database.items():
        # 计算身高、体重和年龄的差的绝对值之和
        diff = abs(player.height - height) + abs(player.weight - weight)

        # 如果当前球员的差异值更小，则更新最接近的球员和最小差异值
        if diff < min_diff:
            min_diff = diff
            closest_player = player

    return closest_player

