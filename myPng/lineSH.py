# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 15:26
# @Author  : xyx
# @Description:

from utils import get_total_data, get_all_data
from pyecharts.charts import Line
import pyecharts.options as opts
from pyecharts.globals import ThemeType


def time_data():
    data = get_total_data()
    confirm = []
    wzz = []
    time = []
    for d in data:
        time.append(d[0])
        confirm.append(d[1])
        wzz.append(d[2])
    return time, confirm, wzz


# print(get_total_data())

def dic_data():
    data = get_all_data()
    print(data)


def sh_total_line():
    time, confirm, wzz = time_data()
    line = (Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add_xaxis(time)
            .add_yaxis('确诊数量', confirm, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
            .add_yaxis('无症状数量', wzz, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
            .set_global_opts(title_opts=opts.TitleOpts(title="3月至%s每日新增确诊无症状数量" % time[-1]),
                             legend_opts=opts.LegendOpts(type_="scroll", pos_left="right", orient="vertical"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            )
    return line


if __name__ == '__main__':
    sh_total_line().render('line.html')
    # dic_data()
