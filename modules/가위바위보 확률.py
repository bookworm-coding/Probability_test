import streamlit as st
from random import randint
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("가위바위보를 2명이 할 때 A가 이길 확률, 비길 확률, 질 확률")


def rcp():
    global number, l
    n1 = n2 = n3 = 0
    for i in range(1, number):
        a, b = randint(0, 2), randint(0, 2)
        if a == b:
            n2 += 1
        elif a == 2 and b == 0:
            n3 += 1
        elif a == 0 and b == 2:
            n1 += 1
        elif a > b:
            n1 += 1
        else:
            n3 += 1
        l.append([fraction(n1, i).float, fraction(n2, i).float, fraction(n3, i).float])


number = st.slider(label="가위바위보 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=rcp)

l = []
rcp()

f = fraction(1, 3)

chart_data = df(l, columns=["이김", "비김", "짐"])
st.plotly_chart(line(chart_data, f.float), use_container_width=True)

st.write("A와 B가 ", number, "번 가위바위보를 했을 때 A가 이긴 확률은 ", l[-1][0], "이고 A와 B가 비긴 확률은 ", l[-1][1], "이고 A가 진 확률은 ",
         l[-1][2], "이다. ")
st.write("이론상 확률은 모두 ", r"$\frac{1}{3}$", "≈", f.float, "이다. ")
