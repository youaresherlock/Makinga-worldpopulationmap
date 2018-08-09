# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-25 14:57:53
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-25 18:29:04
"""
绘制世界人口地图
1.使用Pygal地图创建工具对人口数据进行可视化，以探索全球人口的分布情况

population_data.json是一个json文件，里面有一个很长的Python列表
其中每个元素都是一个包含四个键的字典:国家名 国别码 年份 人口数量
下面是world_population.py代码
import json

from country_code import get_country_code

# 将数据加载到一个列表中 
filename = "population_data.json"
with open(filename) as f:
	# 函数json.load()将数据转换为Python能够处理的格式
	pop_data = json.load(f)

for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		# print(country_name + ": " + str(population))
		# print(country_name + ": " + population)

		'''
		导致错误的消息有两个原因: 并非所有人口数量对应的都是国家，
		也可能是地区和经济类群。 有些数据使用了不完整的国家名
		'''
		code  = get_country_code(country_name)
		if code:
			print(code + ": " + str(population))
		else:
			print("ERROR - " + country_name)

打印出来的数据是
...
ERROR - Pacific island small states
ERROR - Small states
ERROR - South Asia
ERROR - Sub-Saharan Africa (all income levels)
ERROR - Sub-Saharan Africa (developing only)
ERROR - Upper middle income
ERROR - World
af: 34385000
al: 3205000
dz: 35468000
ERROR - American Samoa
ad: 84864
......
我们要将字符串转化成数字值方便pygal处理
但是int()不能转化带小数点的字符串
int('589011025.857512') 会出现ValueError异常
因此我们用int(float('589011025.857512'))

2. 创建countries.py获取两个字母的国别码

3. 制作一个简单的世界地图americas.py

4. 在世界地图上呈现数据na_populations.py

5.绘制完整的世界人口地图 
要呈现其他国家的人口数量，需要将前面的数据转换为Pygal要求的字典格式:
键为两个字母的国别码， 值为人口数量 
下来我们修改world_population.py

5.可以看出步骤4图中只有中国和印度人口是红色的，其他的颜色区分并不明显 因此
我们将根据人口数量将国家分组，再分别给每个组着色
接下来根据人口数量分成三组(少于1000万的，介于1000万到10亿之间，超过十亿的)

6.让地图的颜色更加一致，更容易区分不同组
使用pygal.style中的RotateStyle
"""

# 打印每个国家2010年人口的数量信息
import json

from country_code import get_country_code

import pygal.maps.world
from pygal.style import RotateStyle, LightColorizedStyle, RotateStyle

# 将数据加载到一个列表中 
filename = "population_data.json"
with open(filename) as f:
	# 函数json.load()将数据转换为Python能够处理的格式
	pop_data = json.load(f)

# 包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		# print(country_name + ": " + str(population))
		# print(country_name + ": " + population)

		'''
		导致错误的消息有两个原因: 并非所有人口数量对应的都是国家，
		也可能是地区和经济类群。 有些数据使用了不完整的国家名
		'''
		code  = get_country_code(country_name)
		if code:
			cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# base_style使用较亮的主体
wm_style = RotateStyle("#336688", base_style = LightColorizedStyle)
wm = pygal.maps.world.World(style = wm_style)

wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')