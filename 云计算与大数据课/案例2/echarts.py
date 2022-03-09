import random

import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
import datetime
#%%

def get_time(x):
    return str(datetime.datetime.strptime(x, '%Y-%m-%d'))[:10]

data = pd.read_csv('./vegetable.csv')
data['date'] = data['date'].apply(get_time)
date_list = data['date'].values
date_list = list(map(get_time, list(date_list)))
date_list = sorted(list(set(date_list)))
veget = data['variety'].unique()
random.shuffle(veget)
data = data.groupby('variety')
#%%

line = (
    Line()
        .add_xaxis(xaxis_data=date_list)
        .set_global_opts(title_opts=opts.TitleOpts(title='蔬菜价格走势图-1'))
)
for v in range(20):
    v = veget[v]
    temp = data.get_group(v)[['date', 'price']]
    temp.sort_values(by='date', inplace=True, ascending=False)
    temp = temp.values
    x = temp[:, 0]
    y = temp[:, 1]
    line_1 = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name=v, y_axis=y, is_symbol_show=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       is_connect_nones=True)
            )
    line.overlap(line_1)
line.render('./render1.html')

line = (
    Line()
        .add_xaxis(xaxis_data=date_list)
        .set_global_opts(title_opts=opts.TitleOpts(title='蔬菜价格走势图-2'))
)
for v in range(20, 40):
    v = veget[v]
    temp = data.get_group(v)[['date', 'price']]
    temp.sort_values(by='date', inplace=True)
    temp = temp.values
    x = temp[:, 0]
    y = temp[:, 1]
    line_1 = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name=v, y_axis=y, is_symbol_show=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       is_connect_nones=True)
            )
    line.overlap(line_1)
line.render('./render2.html')
