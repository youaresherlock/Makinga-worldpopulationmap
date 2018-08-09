# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-25 16:20:41
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-25 16:54:44
"""
Pygal提供了图表类型Worldmap,我们先举一个简单突出北美、中美和
南美的简单地图
"""
import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = "North, Central, and South America"

# 每次调用add()方法都将为指定的国家选择一种颜色
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf'
	, 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')