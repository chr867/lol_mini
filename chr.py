import my_utils_PJ as mu
import pandas as pd

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font) # 윈도우

sql_conn = mu.connect_mysql('lol_icia')
dic = mu.mysql_execute_dict('select * from lol_mini', sql_conn)
df = pd.DataFrame(dic)

tmp_df = df[['profileIcon', 'win']]
group_df = tmp_df.groupby('profileIcon').count().reset_index()
sort_df = group_df.sort_values(by=['win'], ascending=False)

