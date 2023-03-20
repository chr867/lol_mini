import my_utils_PJ as mu

sql_conn = mu.connect_mysql('lol_icia')
sql_create = '''
CREATE TABLE 
LOL_MINI ( match_id varchar(20), gameDuration int, gameVersion varchar(20), summonerName varchar(20),
summonerLevel int, participantId int, championName varchar(20), champExperience int, teamPosition varchar(10), 
teamId int, win varchar(10), kills int, deaths int, assists int, totalDamageDealtToChampions int, totalDamageTaken int, 
g_5 int, g_6 int, g_7 int, g_8 int, g_9 int, g_10 int, g_11 int, g_12 int, g_13 int, g_14 int, g_15 int, g_16 int,
g_17 int, g_18 int, g_19 int, g_20 int, g_21 int, g_22 int, g_23 int, g_24 int, g_25 int,
CONSTRAINT LMT_PK_ID_PID PRIMARY KEY (match_id, participantId))
'''
mu.mysql_execute(sql_create, sql_conn)
sql_conn.close()
