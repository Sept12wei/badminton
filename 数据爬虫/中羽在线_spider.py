import requests
import csv
from lxml import etree
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
base_url = 'https://www.badmintoncn.com/ranking.php'
type_list = [6]
weeks_2024 = [f"2024/{str(week).zfill(2)}" for week in range(1, 14)]

# 写入CSV文件
with open('player_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Name', 'Game', 'Score'])  # 写入标题行
    for type in type_list:
        for rw in weeks_2024:
            params = {
                'type' : str(type),
                'rw' : str(rw)
            }
            response = requests.get(url=base_url,headers=headers,params=params)
            page_text = response.text


            tree = etree.HTML(page_text)
            tree.xpath('//tbody/tr/td[1]/text()')

            rank_list = tree.xpath('//tr/td[1]/text()')[11:]
            name_list = tree.xpath('//td/div/a/span/text()')
            game_list = tree.xpath('//td[5]/text()')[3:]
            game_list = [game.strip() for game in game_list]
            score_list = tree.xpath('//td[6]/text()')[4:]


            # 使用zip函数将两个列表拼接在一起
            player_list = list(zip(rank_list, name_list,game_list,score_list))

            # # 打印拼接后的列表
            # for player in player_list:
            #     print(player)
            for player in player_list:
                writer.writerow(player)

            # 获取球员的sid,便于转换网页
            sid_list = tree.xpath('//div[@class="player"]//a/@href')
            # 使用正则表达式提取数字并替换原始列表中的链接
            for i, link in enumerate(sid_list):
                match = re.search(r'\d+', link)  # 匹配数字部分
                if match:
                    extracted_id = match.group()  # 获取匹配的数字
                    sid_list[i] = extracted_id
#
# base_url = 'https://www.badmintoncn.com/cbo_star/star_view.php?sid='
# for sid in sid_list[0]:
#     url_player = base_url + str(sid)
#     response = requests.get(url=url_player,headers=headers)
#     page_text_player = response.text
#     tree = etree.HTML(page_text_player)
#     test = tree.xpath('//div/span[1]/span/text()')
#     print(test)


