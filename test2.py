import matplotlib.pyplot as plt
import os
import json

# daily.jsonを読み込む関数------------------------------------------------------------------------------------------
def read_daily():
    path = "DailyTask\daily.json"
    # 作業ディレクトリをこのファイル直下に設定
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # daily.jsonの内容はself.daily_diに格納される
    daily_di = {}
    try:
        with open(path) as f:
            daily_di = json.load(f)
    except:
        print("エラー")
    return daily_di

# ダークモードにする
plt.style.use('dark_background')
# daily.jsonを読み込んdaily_diへ
daily_di = read_daily()
sort_date = sorted(daily_di)
y = []
x = []
for date in sort_date:
    x.append(date)
    date_count = len(daily_di[date])
    ok_count = 0
    for name in daily_di[date]:
        if daily_di[date][name]:
            ok_count += 1
    percent = ok_count / date_count * 100
    y.append(percent)
fig, ax = plt.subplots()
plt.xlabel("日付", fontname="MS Gothic")
plt.ylabel("達成率(%)", fontname="MS Gothic")
plt.ylim(0, 100)
ax.plot(x, y, marker='o')
for i, value in enumerate(y):
    ax.text(x[i], y[i]+3, round(value, 2))
plt.savefig('image.png')