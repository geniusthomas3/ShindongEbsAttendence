from selenium import webdriver
import datetime
import time
import sys, os
if __name__ == "__main__":

  if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
  else:
    driver = webdriver.Chrome('C:/Users/honsa/chromedriver.exe')

def nameXpath(a):
    return '//*[@id="bbsArticleCmtList_66010"]/ul/li[' + str(a) + ']/div/p'

name = '김도연'#str(input("이름: "))
username = 'geniusthomas'#str(input("아이디: "))
password = 'rlaehdus3'#str(input("비밀번호: "))
Class = 8
CLASS8 = 'https://oc31.ebssw.kr/shindong308/hmpg/hmpgAlctcrDetailView.do?menuSn=376452&alctcrSn=178674'
num = 30803 #int(input("학번: "))

#로그인
driver.get('https://oc31.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=01125&schCssTyp=online_mid')
driver.get('https://oc31.ebssw.kr/sso/loginView.do?loginType=onlineClass')
driver.find_element_by_name('j_username').send_keys(username)
driver.find_element_by_name('j_password').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginViewForm"]/div/div[1]/fieldset/div/button').click()
#출석게시판 들어가기(가장 처음에 있는것)
driver.implicitly_wait(5)
driver.get('https://oc31.ebssw.kr/sso/loginView.do?loginType=onlineClass')
while True:
    #while True:
        #now = datetime.datetime.now().timetuple().tm_min +   datetime.datetime.now().timetuple().tm_hour* 60
        #if (530 <= now <= 630) or (900 <= now <= 960):
            #break
    driver.get(CLASS8)
    elem = driver.find_element_by_xpath('//*[@id="record01"]/ul/li[2]/div/a').text
    siteNum = elem.split("'")[1]
    url = ' '+siteNum
    driver.get(url)
    #댓글 입력
    flag = 0
    allComment = driver.find_elements_by_class_name('reply_text')
    for i in allComment:
        if name in i.text:
            flag = 1
            print('지금은 이미 출책을 완료하였습니다.')
    if flag == 0:
        title = driver.find_element_by_xpath('//*[@id="cntntsDiv"]/div[1]/strong').text
        if '조회' in title:
            comment = str(num) + ' ' + name + ' 건강상태는 양호합니다.'
        else:
            comment = str(num) + ' ' + name + ' 수업 잘 들었습니다.'
        driver.find_element_by_xpath('//*[@id="dscsnCn"] ').send_keys(comment)
        driver.find_element_by_xpath('//*[@id="cntntsDiv"]/div[2]/ul/li/div[2]/div/div/a').click()
        alert = driver.switch_to.alert
        alert.accept()
    else:
        time.sleep(120)