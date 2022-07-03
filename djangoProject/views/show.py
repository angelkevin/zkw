# from django.shortcuts import render
# from django.http import HttpResponse
# from pyecharts import options as opts
# from pyecharts.charts import Bar, Map, Page, Pie, WordCloud, Line
# from pyecharts.globals import ThemeType
# import pymysql
# from pyhive import hive
# from pyhive import hive
# import pandas as pd
#
# conn = hive.connect(host="192.168.170.133", port=10000, auth="LDAP", database="default", username="root",
#                     password="123456")
# query_sql = "select * from goods"
# curosr = conn.cursor()
# curosr.execute(query_sql)
#
# clumns = curosr.description
# # ('华为智慧屏 SE 55英寸 超薄电视 广色域鸿鹄画质 4K超高清智能液晶电视机 HD55DESA 2+16GB搭载 HarmonyOS 2', 1499.0, '华为京东自营官方旗舰店', 200000)
# data = pd.DataFrame()
#
# list_data = []
# for result in curosr.fetchall():
#     list_data.append(list(result))
# data = pd.DataFrame(list_data)
#
#
# def pie_plot():
#     d1 = data[2].value_counts()
#     result_list = [(i, j) for i, j in zip(d1.index.to_list(), d1.values.tolist())]
#     a = Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#     a.add(series_name='年份',
#           data_pair=result_list,
#           rosetype='radius',
#           radius='70%',
#           )
#     a.set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item', formatter='{a} <br/>{b}:{c} ({d}%)'))
#     return a
#
#
# def bar_plot():
#     d2 = data.sort_values(by=3, ascending=False)
#     d2 = d2[0:10]
#     bar = (
#         Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))  # 设置主题
#             .add_xaxis(d2[2].tolist())
#             .add_yaxis("评论数", d2[3].tolist())
#             .add_yaxis("价格", d2[1].tolist())
#             .set_global_opts(title_opts=opts.TitleOpts(title="评论数量前十及其价格"))
#     )
#     return bar
#
#
# dic = {'四川': 239.0, '浙江': 231.0, '福建': 203.0, '江苏': 185.0, '湖南': 152.0, '山东': 131.0, '安徽': 100.0, '广东': 89.0,
#        '河北': 87.0, '湖北': 84.0, '吉林': 75.0,
#        '上海': 70.0, '江西': 64.0, '广西': 64.0, '贵州': 64.0, '北京': 63.0, '云南': 53.0, '重庆': 49.0, '河南': 48.0, '陕西': 38.0,
#        '山西': 37.0, '辽宁': 33.0, '新疆': 25.0,
#        '内蒙古': 23.0, '黑龙江': 20.0, '天津': 19.0, '甘肃': 13.0, '海南': 9.0, '青海': 7.0, '宁夏': 4.0, '西藏': 0.0}
#
#
# def map_plot():
#     world_map = (
#         Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))  # 设置主题
#             .add("", list(dic.items()), "china", is_map_symbol_show=False,
#                  is_roam=False)
#             .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="个个省份的销量"),
#             visualmap_opts=opts.VisualMapOpts(max_=200))
#     )
#     return world_map
#
#
# def wordcloud():
#     d3 = data[2].value_counts()
#     c = (
#         WordCloud(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#             .add(series_name='旗舰店云图',
#                  data_pair=list(zip(d3.index.tolist(), d3.values.tolist())),
#                  word_size_range=[20, 45])
#             .set_global_opts(
#             title_opts=opts.TitleOpts(
#                 title='旗舰店云图',
#                 title_textstyle_opts=opts.TextStyleOpts(font_size=23)
#             )
#         )
#     )
#     return c
#
#
# def line_plot():
#     d2 = data.sort_values(by=3, ascending=False)
#     d2 = d2[0:15]
#     line = (
#         Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#             .add_xaxis([i for i in range(0,15)])
#             .add_yaxis("价格", d2[1].tolist())
#             .set_global_opts(title_opts=opts.TitleOpts(title="评论数量前前十五价格"))
#     )
#     return line
#
#
# def title():
#     pie = (
#         Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#             .set_global_opts(title_opts=opts.TitleOpts(title="可视化实训", subtitle='张凯文,晋菱漪,潘洪博,郭子凝,史仁桢'))
#     )
#     return pie
#
#
# def page_simple_layout():
#     page = Page(layout=Page.DraggablePageLayout)
#     page.add(
#         bar_plot(),
#         map_plot(),
#         pie_plot(),
#         wordcloud(),
#         line_plot(),
#         title(),
#
#     )
#     page.render("page.html")
#
#
#
# def change_page():
#     page = Page.save_resize_html("page.html",
#                                  cfg_file="chart_config.json",
#                                  dest="all.html")
#     return page
#
#
