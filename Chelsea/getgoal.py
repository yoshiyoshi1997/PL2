from bs4 import BeautifulSoup
import selenium
import pandas as pd
from pandas import DataFrame
from pandas import Series
import re

def goals(html):
    html = './html/' + html
    with open(html,encoding="utf-8") as f:
        soup = BeautifulSoup(f, 'html.parser')

    #チーム名取得
    hometeam = soup.select_one('#match-header > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').string
    awayteam = soup.select_one('#match-header > table > tbody > tr:nth-child(1) > td:nth-child(3) > a').string

    #得点取得
    score = soup.select_one("#match-centre-header > div.match-centre-info > div > div.score").string
    score = score.replace(' ','')
    score = score.replace(':','')

    #得点時間取得
    home = soup.select('#match-centre-header > div:nth-child(1) > ul > li')
    away = soup.select('#match-centre-header > div:nth-child(3) > ul > li')
    home_minute=[]
    for i in home:
        t = i.select_one('span').string
        t = str(t).replace('\'','')
        if '+' in t:
            t = t[0:2]
        home_minute.append(int(t))
    away_minute=[]
    for i in away:
        t = i.select_one('span').string
        t = str(t).replace('\'','')
        if '+' in t:
            t = t[0:2]
        away_minute.append(int(t))

    #得点者取得
    home_scorer=[]
    for x in home:
        t = x.text.replace('\'','')
        t = t.replace(' ','')
        t = t.replace('+','')
        t = re.sub(r'[1-9]','',t)
        home_scorer.append(t)
    away_scorer=[]
    for x in away:
        t = x.text.replace('\'','')
        t = t.replace(' ','')
        t = t.replace('+','')
        t = re.sub(r'[1-9]','',t)
        away_scorer.append(t)

    #試合開催日取得
    date = soup.select_one('#match-header > table > tbody > tr:nth-child(2) > td:nth-child(2) > div:nth-child(3) > dl > dd:nth-child(4)').string

    #リスト作成
    homelist = [date,hometeam,int(score[0]),home_minute,home_scorer]
    awaylist = [date,awayteam,int(score[1]),away_minute,away_scorer]
    matchlist = [homelist,awaylist]

    #データフレーム型
    frame = DataFrame(matchlist,index=['home','away'], columns=['date','team', 'score','minute','scorer'])
    return (frame)

#試合url取得
import matches
a = matches.Matches

#データ取得
for i,match in enumerate(a.pl):        
    frame = goals(match)
    if i == 0:
        goaldata = DataFrame(frame,index=['home','away'], columns=['date','team', 'score','minute','scorer'])
    else:
        goaldata = pd.concat([goaldata, frame], axis=0)

goaldata.to_csv('goals.csv')
