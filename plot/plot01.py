import numpy as np
import matplotlib.pyplot as plt

plt.rc('font',family='NanumGothic')
plt.rc("axes",unicode_minus=False)

year = ["2017 1/4","2017 2/4","2017 3/4","2017 4/4","2018 1/4","2018 2/4","2018 3/4","2018 4/4","2019 1/4","2019 2/4","2019 3/4","2019 4/4","2020 1/4","2020 2/4","2020 3/4","2020 4/4","2021 1/4","2021 2/4"]

value=[14426447,15146207,15924113,17152579,17295346,18047681,18596341,20849526,20957737,22068020,22910575,25481435,25963848,27430400,29562172,32955130,33270157,34770110]

plt.figure(figsize = (10, 5))
plt.xticks(rotation=45)

plt.title("분기별 인터넷 쇼핑몰 총 거래액 추이(2017년 1분기 ~ 2021년 2분기)")
plt.plot(year, value)
plt.xlabel("분기")
plt.ylabel("백만원")
plt.show()