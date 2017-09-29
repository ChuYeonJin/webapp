# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/it/Desktop/ui_test.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainForm(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(400, 380)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("blog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setToolTip("")
        main.setAutoFillBackground(False)
        self.background = QtWidgets.QLabel(main)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(-110, -50, 621, 561))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.hyFont = font
        self.background.setFont(font)
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background3.png"))
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.gridLayoutWidget = QtWidgets.QWidget(main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 361, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.attr = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.attr.setContentsMargins(0, 0, 0, 0)
        self.attr.setObjectName("attr")
        self.html = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.html.setObjectName("html")
        self.attr.addWidget(self.html, 0, 0, 1, 1)
        self.current = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.current.setChecked(True)
        self.current.setObjectName("current")
        self.attr.addWidget(self.current, 1, 0, 1, 1)
        self.all = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.all.setObjectName("all")
        self.attr.addWidget(self.all, 1, 1, 1, 1)
        self.image = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.image.setObjectName("image")
        self.attr.addWidget(self.image, 0, 1, 1, 1)
        self.urlText = QtWidgets.QTextEdit(main)
        self.urlText.setGeometry(QtCore.QRect(20, 70, 361, 31))
        self.urlText.setStyleSheet("font: 12pt \"HY견고딕\";")
        self.urlText.setFont(font)
        self.urlText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.urlText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.urlText.setObjectName("urlText")

        self.urlLabel = QtWidgets.QLabel(main)
        self.urlLabel.setGeometry(QtCore.QRect(170, 40, 71, 20))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.urlLabel.setFont(font)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setObjectName("urlLabel")
        self.direction = QtWidgets.QComboBox(main)
        self.direction.setEnabled(True)
        self.direction.setGeometry(QtCore.QRect(20, 200, 76, 22))
        self.direction.setObjectName("direction")
        self.direction.addItem("")
        self.direction.addItem("")
        self.page = QtWidgets.QTextEdit(main)
        self.page.setEnabled(True)
        self.page.setGeometry(QtCore.QRect(110, 200, 31, 23))
        self.page.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.page.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.page.setObjectName("page")
        self.pageLabel = QtWidgets.QLabel(main)
        self.pageLabel.setGeometry(QtCore.QRect(150, 200, 41, 21))
        self.pageLabel.setObjectName("pageLabel")
        self.start = QtWidgets.QPushButton(main)
        self.start.setGeometry(QtCore.QRect(150, 260, 101, 41))
        self.start.setObjectName("start")
        self.login = QtWidgets.QPushButton(main)
        self.login.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.login.setObjectName("login")
        self.help = QtWidgets.QPushButton(main)
        self.help.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.help.setObjectName("help")
        self.pathButton = QtWidgets.QPushButton(main)
        self.pathButton.setGeometry(QtCore.QRect(330, 200, 51, 23))
        self.pathButton.setObjectName("pathButton")
        self.path = QtWidgets.QTextEdit(main)
        self.path.setEnabled(True)
        self.path.setGeometry(QtCore.QRect(220, 200, 101, 23))
        self.path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path.setObjectName("path")
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(310, 350, 81, 20))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "NaverBlogScraper"))
        self.html.setText(_translate("main", "HTML 추출"))
        self.current.setText(_translate("main", "현재 페이지"))
        self.all.setText(_translate("main", "카테고리 전체"))
        self.image.setText(_translate("main", "이미지 추출"))
        self.urlText.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'HY견고딕\'; font-size:12pt;\"><br /></p></body></html>"))
        self.urlLabel.setText(_translate("main", "URL 입력 :"))
        self.direction.setItemText(0, _translate("main", "앞으로"))
        self.direction.setItemText(1, _translate("main", "뒤로"))
        self.pageLabel.setText(_translate("main", "페이지"))
        self.start.setText(_translate("main", "추출"))
        self.login.setText(_translate("main", "로그인"))
        self.help.setText(_translate("main", "사용법"))
        self.pathButton.setText(_translate("main", "Path"))
        self.label.setText(_translate("main", "ver 0.1"))

    def getAppMain(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        main = QtWidgets.QDialog()
        return app, main
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     main = QtWidgets.QDialog()
#     ui = MainForm()
#     ui.setupUi(main)
#     main.show()
#     sys.exit(app.exec_())

