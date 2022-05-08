# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 14:51
# @Author  : xyx
# @Description:
from utils import get_dic_total_data
from pyecharts.charts import Map
import pyecharts.options as opts


def shdata():
    confirm = []
    wzz = []
    data = get_dic_total_data()
    for d in data:
        if d[0] == '浦东':
            confirm.append((d[0] + '新区', d[1]))
            wzz.append((d[0] + '新区', d[2]))
        else:
            confirm.append((d[0] + '区', d[1]))
            wzz.append((d[0] + '区', d[2]))
    return confirm, wzz


def sh_cov_cofirm_map():
    confirm = shdata()[0]
    # print(confirm,wzz)
    c = (
        Map()
            .add('', confirm, maptype='上海')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='上海3月至今疫情分布图（确诊）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,

                                              is_calculable=True,
                                              is_piecewise=True,
                                              range_text=['High', 'Low'],
                                              border_color='#000',
                                              split_number=6,

                                              pos_top='center',
                                              pieces=[
                                                  {'min': 7000, 'color': '#7f1818'},  # 不指定 max
                                                  {'min': 6000, 'max': 7000},
                                                  {'min': 5000, 'max': 6000},
                                                  {'min': 4000, 'max': 5000},
                                                  {'min': 1700, 'max': 4000},
                                                  {'min': 0, 'max': 1700}]
                                              )

        )
    )

    return c


def sh_cov_wzz_map():
    wzz = shdata()[1]
    c = (
        Map()
            .add('', wzz, maptype='上海')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='上海3月至今疫情分布图（无症状）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,

                                              is_calculable=True,
                                              is_piecewise=True,
                                              range_text=['High', 'Low'],
                                              border_color='#000',
                                              split_number=6,

                                              pos_top='center',
                                              pieces=[
                                                  {'min': 60000, 'color': '#7f1818'},
                                                  {'min': 30000, 'max': 60000},
                                                  {'min': 10000, 'max': 30000},
                                                  {'min': 6000, 'max': 10000},
                                                  {'min': 3000, 'max': 6000},
                                                  {'min': 0, 'max': 3000}]
                                              )

        )
    )
    return c


if __name__ == '__main__':
    sh_cov_wzz_map().render('wzz.html')
    sh_cov_cofirm_map().render('confirm.html')
