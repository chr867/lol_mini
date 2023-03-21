import time
import pandas as pd
import pymysql
import requests
from tqdm import tqdm

riot_api_key = 'RGAPI-85674ca5-e22d-4989-9f35-a106be25a318'

def connect_mysql(db):
    mysql_conn = pymysql.connect(host='localhost', user='root', password='1234', db=db, charset='utf8')
    return mysql_conn


def mysql_execute(query, mysql_conn):
    mysql_cursor = mysql_conn.cursor()
    mysql_cursor.execute(query)
    result = mysql_cursor.fetchall()
    return result


def mysql_execute_dict(query, mysql_conn):
    mysql_cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)
    mysql_cursor.execute(query)
    result = mysql_cursor.fetchall()
    return result


#  롤 데이터
def match_timeline(summoner_name=[], num=int):
    """
    :param summoner_name: 소환사 명(한글) list
    :param num: 명당 불러올 게임 수
    :return: 정제된 df
    """
    result = []

    def get_puuid(summoner_name_p):
        print('get_puuid')
        summoner_get_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_p}?api_key={riot_api_key}'
        summoner_get_res = requests.get(summoner_get_url).json()
        time.sleep(1)
        get_matches_id(summoner_get_res['puuid'])

    def get_matches_id(puuid):
        print('get_matches_id')
        get_matches_url = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count={num}&api_key={riot_api_key}'
        get_matches_res = requests.get(get_matches_url).json()
        time.sleep(1)
        get_match_info(get_matches_res)

    def get_match_info(match_ids):
        print('get_match_info')
        for match_id in match_ids:
            get_match_url = f'https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={riot_api_key}'
            get_match_res = requests.get(get_match_url).json()
            time.sleep(1)
            get_timeline_url = f'https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={riot_api_key}'
            get_timeline_res = requests.get(get_timeline_url).json()
            time.sleep(1)
            result.append([match_id, get_match_res, get_timeline_res])

    for n in tqdm(summoner_name):
        try:
            get_puuid(n)
        except Exception as e:
            print(n, f'{e} 예외 발생')
            continue
    print('match_timeline complete')
    return result
