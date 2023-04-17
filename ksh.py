import pandas as pd
import matplotlib.pyplot as plt
import my_utils_PJ as mu
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

sql_conn = mu.connect_mysql('icia')
df = mu.mysql_execute_dict('select * from lol_mini', sql_conn)
sql_conn.close()
df = pd.DataFrame(df)

df
# 와드 설치, 파괴 갯수와 승률 상관관계
tmp_df = df[['wardsPlaced', 'wardsKilled', 'win', 'teamPosition']]
sort_win_df = tmp_df[(tmp_df['win'] == 'True') | (tmp_df['teamPosition'] == 'Support')]
sort_lose_df = tmp_df[(tmp_df['win'] == 'False') | (tmp_df['teamPosition'] == 'Support')]
sort_lose_df['win'].count()

plt.figure()
xdata = sort_win_df['wardsPlaced']
ydata = sort_win_df['wardsKilled']
plt.plot(xdata, ydata, color='b', marker='o', linestyle='None')

xdata2 = sort_lose_df['wardsPlaced']
ydata2 = sort_lose_df['wardsKilled']
plt.plot(xdata2, ydata2, color='r', marker='x', linestyle='None')
plt.xlabel('와드 설치')
plt.ylabel('와드 파괴')
plt.grid(True)

