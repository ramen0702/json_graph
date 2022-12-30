import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import os
import json

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('matplotlib graph')

        #-----------------------------------------------
        
        # matplotlib配置用フレーム
        frame = tk.Frame(self.master)
        
        # matplotlibの描画領域の作成
        fig = Figure()
        # 座標軸の作成
        self.ax = fig.add_subplot(1, 1, 1)
        self.ax.set_facecolor("white")
        self.ax.set_xlabel("日付", fontname="MS Gothic")
        self.ax.set_ylabel("達成率(%)", fontname="MS Gothic")
        self.ax.set_ylim(0, 100)
        # matplotlibの描画領域とウィジェット(Frame)の関連付け
        self.fig_canvas = FigureCanvasTkAgg(fig, frame)
        # matplotlibのツールバーを作成
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, frame)
        # matplotlibのグラフをフレームに配置
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # フレームをウィンドウに配置
        frame.pack()

        # daily.jsonを読み込んdaily_diへ
        daily_di = self.read_daily()
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
        # グラフの描画
        self.ax.plot(x, y, marker='o')
        for i, value in enumerate(y):
            self.ax.text(x[i], y[i]+3, round(value, 2))
        # 表示
        self.fig_canvas.draw()
    
    # daily.jsonを読み込む関数------------------------------------------------------------------------------------------
    def read_daily(self):
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

root = tk.Tk()
app = Application(master=root)
app.mainloop()