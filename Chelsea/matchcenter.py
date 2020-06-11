from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from pandas import DataFrame


def matchcenter(url):
    
    url = 'file:////content/drive/My Drive/Chelsea/html/' + url
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver',options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    if driver.find_element_by_css_selector('#qcCmpButtons > button:nth-child(2)').click():
      driver.find_element_by_css_selector('#qcCmpButtons > button:nth-child(2)').click()

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    
    #試合開催日取得
    date = soup.select_one('#match-header > table > tbody > tr:nth-child(2) > td:nth-child(2) > div:nth-child(3) > dl > dd:nth-child(4)').string
    
    #チーム名取得
    hometeam = soup.select_one('#match-header > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').string
    awayteam = soup.select_one('#match-header > table > tbody > tr:nth-child(1) > td:nth-child(3) > a').string
    
    #得点取得
    score = soup.select_one("#match-centre-header > div.match-centre-info > div > div.score").string
    score = score.replace(' ','')
    score = score.replace(':','')
    
    #Rating
    home_rate = soup.select_one("#match-centre-stats > ul > li.match-centre-stat.selected > div.match-centre-stat-values > span:nth-child(1)").string
    away_rate = soup.select_one("#match-centre-stats > ul > li.match-centre-stat.selected > div.match-centre-stat-values > span:nth-child(3)").string
    
    #シュート数
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(3) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_totalshot = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_woodwork = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    home_ontarget = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(1)').string
    home_offtarget = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(1)').string
    home_blocked = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(5) > div > span:nth-child(1)').string
    away_totalshot = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_woodwork = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    away_ontarget = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(3)').string
    away_offtarget = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(3)').string
    away_blocked = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(5) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #Posession
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(5) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_pos = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_touch = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    away_pos = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_touch = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #Pass
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(7) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_passuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_totalpas = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    home_accpas = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(1)').string
    home_keypas = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(1)').string
    away_passuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_totalpas = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    away_accpas = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(3)').string
    away_keypas = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #Dribble
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(9) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_dribwon = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_dribatt = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    home_dribpast = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(1)').string
    home_dribsuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(1)').string
    away_dribwon = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_dribatt = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    away_dribpast = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(3)').string
    away_dribsuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #Aerial
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(11) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_aerwon = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_aersuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    home_aeroff = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(1)').string
    home_aerdef = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(1)').string
    away_aerwon = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_aersuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    away_aeroff = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(3)').string
    away_aerdef = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #tackles
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(13) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_tackle = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_tacatt = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    home_wasdrib = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(1)').string
    home_tacsuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(1)').string
    home_clear = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(5) > div > span:nth-child(1)').string
    home_inter = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(6) > div > span:nth-child(1)').string
    away_tackle = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_tacatt = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    away_wasdrib = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(3)').string
    away_tacsuc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(3)').string
    away_clear = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(5) > div > span:nth-child(3)').string
    away_inter = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(6) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #corner
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(15) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_corner = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_coracc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    away_corner = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_coracc = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    #dispossessed
    driver.find_element_by_css_selector('#match-centre-stats > ul > li:nth-child(17) > div.toggle-stat-details.iconize.iconize-icon-right.ui-state-transparent-default > span').click()
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    home_dispos = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(1)').string
    home_error = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(1)').string
    home_foul = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(1)').string
    home_offside = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(1)').string
    away_dispos = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(1) > div > span:nth-child(3)').string
    away_error = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(2) > div > span:nth-child(3)').string
    away_foul = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(3) > div > span:nth-child(3)').string
    away_offside = soup.select_one('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.match-centre-stats > ul > li:nth-child(4) > div > span:nth-child(3)').string
    close = driver.find_element_by_css_selector('#match-centre-stats > ul > li.match-centre-stat-details.visible > div.close-stat-details')
    close.click()
    
    
    
     #リスト作成
    homelist = [date,hometeam,int(score[0]),home_rate,home_totalshot,home_woodwork,home_ontarget,home_offtarget,home_blocked,home_pos,home_touch,home_passuc,home_totalpas,home_accpas,home_keypas,
                home_dribwon,home_dribatt,home_dribpast,home_dribsuc,home_aerwon,home_aersuc,home_aeroff,home_aerdef,home_tackle,home_tacatt,home_wasdrib,home_tacsuc,home_clear,home_inter,
                home_corner,home_coracc,home_dispos,home_error,home_foul,home_offside]
    awaylist = [date,awayteam,int(score[1]),away_rate,away_totalshot,away_woodwork,away_ontarget,away_offtarget,away_blocked,away_pos,away_touch,away_passuc,away_totalpas,away_accpas,away_keypas,
                away_dribwon,away_dribatt,away_dribpast,away_dribsuc,away_aerwon,away_aersuc,away_aeroff,away_aerdef,away_tackle,away_tacatt,away_wasdrib,away_tacsuc,away_clear,away_inter,
                away_corner,home_coracc,away_dispos,away_error,away_foul,away_offside]
    matchlist = [homelist,awaylist]
    
    #データフレーム型
    column=['date','team', 'score','rating','totalshot','woodwork','ontarget','offtarget','blocked','pos%','touch','pass%','totalpass','accurate','keypass','dribwon','dribatt','dribpast','dribsuc%',\
            'aerwon','aersuc%','aeroff','aerdef','tackle','tacatt','wasdrib','tacsuc','clear','inter','corner','coracc%','dispos','error','foul','offside']
    frame = DataFrame(matchlist,index=['home','away'], columns=column)
    return(frame)

#試合url取得
import matches
a = matches.Matches

column=['date','team', 'score','rating','totalshot','woodwork','ontarget','offtarget','blocked','pos%','touch','pass%','totalpass','accurate','keypass','dribwon','dribatt','dribpast','dribsuc%',\
            'aerwon','aersuc%','aeroff','aerdef','tackle','tacatt','wasdrib','tacsuc','clear','inter','corner','coracc%','dispos','error','foul','offside']

#データ取得
for i,match in enumerate(a.pl):        
    frame = matchcenter(match)
    if i == 0:
        matchcenterframe = DataFrame(frame,index=['home','away'], columns= column)
    else:
        matchcenterframe = pd.concat([matchcenterframe, frame], axis=0)

matchcenterframe.to_csv('matchcenter.csv')

