# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 16:00
# @Author  : xyx
# @Description:
import os
from random import randrange

from flask.json import jsonify
from flask import Flask, render_template
from flask import request
from utils import get_today_data
import pandas as pd
from myPng.lineSH import sh_total_line
from myPng.mapSH import sh_cov_cofirm_map, sh_cov_wzz_map

app = Flask(__name__)


@app.route("/")
def index():
    u = get_today_data()
    return render_template("index.html", u=u)


@app.route("/linechart")
def get_line():
    c = sh_total_line()
    return c.dump_options_with_quotes()


@app.route("/confirmmap")
def get_cmap():
    c = sh_cov_cofirm_map()
    return c.dump_options_with_quotes()


@app.route("/wzzmap")
def get_wmap():
    c = sh_cov_wzz_map()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()
