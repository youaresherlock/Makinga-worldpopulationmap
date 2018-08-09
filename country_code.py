# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-25 15:59:37
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-25 16:16:24
"""
编写一个函数，传入国家名，返回二个字母的国别码
"""

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
	"""根据指定的国家，返回pygal使用的两个字母的国别码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	# 没有找到返回None
	return None
