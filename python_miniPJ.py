import my_utils_PJ as mu
import auto_insert_PJ as ai
from tqdm import tqdm
import imp
imp.reload(ai)

raw_df = ai.get_rawdata('MASTER')
mt_df = ai.get_match_timeline_df(raw_df)

sql_conn = mu.connect_mysql('icia')
sql_create = '''
CREATE TABLE 
LOL_MINI ( gameId varchar(20), gameDuration int, gameVersion varchar(20), summonerName varchar(50),
summonerLevel int, participantId int, championName varchar(20), champExperience int, teamPosition varchar(10), 
teamId int, win varchar(10), kills int, deaths int, assists int, totalDamageDealtToChampions int, totalDamageTaken int, 
wardsPlaced int, wardsKilled int, profileIcon int, firstChampion varchar(10), firstDragon varchar(10), firstTower varchar(10), 
g_5 int, g_6 int, g_7 int, g_8 int, g_9 int, g_10 int, g_11 int, g_12 int, g_13 int, g_14 int, g_15 int, g_16 int,
g_17 int, g_18 int, g_19 int, g_20 int, g_21 int, g_22 int, g_23 int, g_24 int, g_25 int,
CONSTRAINT LMT_PK_ID_PID PRIMARY KEY (gameId, participantId))
'''
mu.mysql_execute(sql_create, sql_conn)
sql_conn.close()

sql_conn = mu.connect_mysql('icia')
tqdm.pandas()
mt_df.progress_apply(lambda x: ai.insert(x, sql_conn), axis=1)
sql_conn.commit()
sql_conn.close()

ai.auto_insert(500)

raw_df['matches'][0]['info']['participants'][0]['teamId']
raw_df['matches'][0]['info']['teams'][0]['teamId']
raw_df['matches'][0]['info']['teams'][0]['objectives']['champion']['first']
raw_df['matches'][0]['info']['teams'][0]['objectives']['dragon']['first']
raw_df['matches'][0]['info']['teams'][0]['objectives']['tower']['first']
raw_df['matches'][8]['info']['teams'][1]['teamId']
raw_df['matches'][0]['info']['teams'][1]['objectives']['champion']['first']
raw_df['matches'][0]['info']['teams'][1]['objectives']['dragon']['f']
raw_df['matches'][0]['info']['teams'][1]['objectives']['tower']


