import matplotlib.pyplot as plt
import os
import json

# daily.jsonを読み込む関数------------------------------------------------------------------------------------------
def read_daily():
    path = "daily.json"
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

plt.style.use('dark_background')
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

fig, ax = plt.subplots(figsize = (8, 6))

#グラデーションで表現するためのカラーリストの定義
rect = ax.bar(list(range(1,len(y)+1)), y, width = 0.5, alpha = 0.80)
ax.set_ylim(80, 105)
ax.set_yticks(range(0,  110, 20))

#軸ラベル(tick)の変更とサイズ変更
ax.set_xticks(list(range(1,len(x)+1)))
ax.set_xticklabels(x)
ax.tick_params(labelsize = 15)

ax.set_ylabel("達成率(%)", fontsize = 18,fontname="MS Gothic")
ax.set_xlabel("日付", fontsize = 18,fontname="MS Gothic")

plt.ylim(0, 100)

#数字の挿入(アノテーション)
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        #annotationで文字やその位置を定義。
        ax.annotate(round(height, 2),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=14)
autolabel(rect)
plt.savefig('image.png')