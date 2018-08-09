# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-25 16:51:39
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-25 16:58:58
"""
为了在地图上呈现数字数据，创建一幅地图，显示三个北美国家的人口数量
"""
import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = "Populations of Countries in North America"
# 第二个实参传递了一个字典而不是列表 pygal会根据数据自动给不同国家以深浅不一样的颜色
wm.add("North America", {'ca' : 34126000, 'us' : 309349000, 'mx' : 113423000})

wm.render_to_file('na_population.svg')