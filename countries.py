# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-25 15:25:29
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-25 15:59:17
"""
Pygal中的地图制作工具要求数据为特定的格式: 用国别码表示国家
，以用数字表示人口数量。 papulation_data.json中的国别码是三个
字母，因此不能使用。 Pygal使用的国别码存储在pygal.i18n模块中
(internationalization的缩写)
需要注意的是，现在已经没有pygal.i18n模块了
因此需要使用pip install pygal_maps_world 用这个模块中的就可以了
关于Python基础知识我是不想讲的，但是害怕新手看不懂我就带着大家看文档
刚好我也复习一下
COUNTRIES是一个字典，键是国别码，值是国家名
sorted(iterable, [, key], [, reverse])
Return a new sorted list from the items in iterable.
注意这里是返回一个排序好了的列表，并不改变iterable,和list.sort()方法不一样偶
key specifies a function of one argument that is used to extract a comparison
key form each list element. The default value is None.(compare the elements directly)
reverse is a boolean value If set to True, then the list elements are sorted as if each 
comparion were reversed.
也就是说key指定一个接受一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认值为None
key你传入函数名就好了(函数地址) reverse默认是False,从小到大排序(字符串的话第一个字母的ASCILL)
True就是从到小排序
"""
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])

