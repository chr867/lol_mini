import pandas as pd
import matplotlib.pyplot as plt
import my_utils_PJ as mu
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

sql_conn = mu.connect_mysql('lol')
df = mu.mysql_execute_dict('select * from lol_mini', sql_conn)
df = pd.DataFrame(df)

df
# 와드 설치, 파괴 갯수와 승률 상관관계
tmp_df = df[['wardsPlaced', 'wardsKilled', 'win']]
sort_win_df = tmp_df[tmp_df['win'] == 'True']
sort_lose_df = tmp_df[tmp_df['win'] == 'False']
sort_lose_df['win'].count()

plt.figure()
plt.plot(xdata = tmp_df['wardsPlaced'], ydata = sort_win_df['wardsKilled'], color = 'b', marker = 'o', linestyle = 'None')
plt.plot(xdata = tmp_df['wardsPlaced'], ydata = sort_lose_df['wardsKilled'], color = 'r', marker = 'x', linestyle = 'None')
plt.xlabel('와드 설치')
plt.ylabel('와드 파괴')
plt.grid(True)

