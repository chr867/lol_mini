import my_utils_PJ as mu
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'notebook_connected'
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)  # 윈도우

sql_conn = mu.connect_mysql('icia')
dic = mu.mysql_execute_dict('select * from lol_mini', sql_conn)
sql_conn.close()
df = pd.DataFrame(dic)
tmp_df = df[['profileIcon', 'win']]
group_df = tmp_df.groupby('profileIcon').count()
sort_df = group_df.sort_values(by=['win'], ascending=False).reset_index()
cut_df = sort_df[:5]

win = tmp_df[tmp_df['win'] == 'True']
win_count = win.groupby('profileIcon').count()
win_sort = win_count.sort_values(by=['win'], ascending=False)
win_cut = win_sort[:5]
cut_df.set_index('profileIcon', inplace=True)
win_cut['win'] = (win_cut['win']/cut_df['win']*100).round(2)
win_cut['win']
win_cut.reset_index(inplace=True)

fig = px.pie(values=cut_df['win'], names=cut_df['profileIcon'], title='상위권 유저들이 많이 사용한 프로필 아이콘')
fig2 = px.bar(win_cut, x=win_cut['profileIcon'], y=win_cut['win'], color='win', title='프로필 아이콘 승률')

fig.show(renderer='browser')
fig2.show(renderer='browser')