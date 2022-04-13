import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# 准备数据
c = ["美国",'中国','日本','德国','英国','印度','法国','意大利','加拿大','韩国']
num = [209366,147227,50577,38060,27077,26229,26030,18864,16434,16305]
color_series = ['#FAE927','#E9E416','#C9DA36','#9ECB3C','#6DBC49',
                '#37B44E','#3DBA78','#14ADCF','#209AC9','#1E91CA',]
             
df = pd.DataFrame({'c': c, 'num': num})
df.sort_values(by='num', ascending=False, inplace=True)
v = df['c'].values.tolist()
d = df['num'].values.tolist()
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie1.set_colors(color_series)
pie1.add("", [list(z) for z in zip(v, d)],
        radius=["30%", "135%"],
        center=["50%", "65%"],
        rosetype="area"
        )
pie1.set_global_opts(title_opts=opts.TitleOpts(title='2020年国家GDP排名'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}亿美元", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ))

pie1.render_embed()
