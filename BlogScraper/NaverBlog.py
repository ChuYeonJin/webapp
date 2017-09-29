# coding: UTF-8

from NaverLogin import NaverSession
from Ui_main import MainForm
from bs4 import *
import sys

nl = NaverSession()
ui = MainForm()
app,main = ui.getAppMain()
# nl.login(user_id = "dydlcl4037", user_pw = "")
# r = nl.get("http://www.naver.com")
# print(r.text)
def setEvent():
    ui.start.clicked.connect(getPasingData)

def getPasingData():
    text = ui.urlText.toPlainText()
    try:
        try:
            id = text.split("//")[1].split(".blog")[0]
            logNo = text.split("blog.me/")[1]
        except IndexError as ie:
            id = text.split("naver.com/")[1].split("/")[0]
            logNo = text.split(id + "/")[1]

        url = "http://blog.naver.com/PostView.nhn?blogId=" + id + "&logNo="+ logNo
        r = nl.get(url)
        tag = BeautifulSoup(r.text)
        title = tag.find('div', attrs={'class': 'se_editView se_title'})

        if(title != None):
            contents = tag.find('div', attrs={'class': 'se_component_wrap sect_dsc __se_component_area'})
            img = contents.find_all('img', attrs={'class': 'se_mediaImage'})
            # a = contents.find_all('a', attrs={'class': 'se_mediaArea'})
        else:
            title = tag.find('meta',attrs={'property' : 'og:title'})
            contents = tag.find('div', attrs={'id': 'postViewArea'})
            # print(title.attrs.get('content'))

        if(contents != None):
            file = open("./"+title.text.replace("\n", "").replace(" ", "_")+".txt", "w+")
            contents.encode("UTF-8")

            text = contents.text.replace(u'\xa0', u' ')
            file.write(text)
            print(contents.text)

    except Exception as e:
        print(type(e))
        print(e)


try:

    ui.setupUi(main)

    ui.urlText.setText("http://blog.naver.com/makestream/221046256640")

    setEvent()
    main.show()
    sys.exit(app.exec_())
except:
    print("except")




