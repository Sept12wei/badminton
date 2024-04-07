# 导入 PySpark 相关包
from pyspark import SparkContext, SparkConf
import os
import json
# 为 PySpark 配置 Python 解释器
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
# 创建 PySpark 执行环境 入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 需求:球员能力值排名
file_rdd = sc.textFile("D:/球员数据.txt")
# 调用flatMap解除嵌套
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
player_with_capacity_rdd = dict_rdd.map(lambda x: (x['name'], int(x['capacity'])))
# 球员能力值进行降序操作
player_with_capacity_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# collect算子，输出为list对象
rdd_list: list = player_with_capacity_rdd.collect()
# 输出到文件中
rdd_list.saveAsTextFile("D:/output")


# 需求:球员积分排名
player_with_integral_rdd = dict_rdd.map(lambda x: (x['name'], int(x['integral'])))
# 积分加和操作
integral_result_rdd = player_with_integral_rdd.reduceByKey(lambda a, b: a + b)
# 球员能力值进行降序操作
integral_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

# 需求:球员lindan积分种类
# filter过滤想要的数据进行保留
lindan_rdd = dict_rdd.filter(lambda x: x['name'] == '林丹')
result = lindan_rdd.map(lambda x: x['category']).distinct()

# 需求:球员热度数据统计Top3
heat_rdd = sc.textFile("D:/search.txt")
result_1 = heat_rdd.map(lambda x: (x.split("\t")[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print("排名热度前三的球员", result_1)