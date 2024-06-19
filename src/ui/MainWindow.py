# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.gridLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.LoginPage = QtWidgets.QWidget()
        self.LoginPage.setObjectName("LoginPage")
        self.UsernameLineEdit = QtWidgets.QLineEdit(self.LoginPage)
        self.UsernameLineEdit.setGeometry(QtCore.QRect(68, 180, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UsernameLineEdit.setFont(font)
        self.UsernameLineEdit.setObjectName("UsernameLineEdit")
        self.UsernameLabel = QtWidgets.QLabel(self.LoginPage)
        self.UsernameLabel.setGeometry(QtCore.QRect(70, 140, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UsernameLabel.setFont(font)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.UsernameErrorLabel = QtWidgets.QLabel(self.LoginPage)
        self.UsernameErrorLabel.setGeometry(QtCore.QRect(70, 240, 511, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.UsernameErrorLabel.setFont(font)
        self.UsernameErrorLabel.setAutoFillBackground(False)
        self.UsernameErrorLabel.setStyleSheet("color: #C40000;")
        self.UsernameErrorLabel.setObjectName("UsernameErrorLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.LoginPage)
        self.PasswordLabel.setGeometry(QtCore.QRect(70, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.PasswordLineEdit = QtWidgets.QLineEdit(self.LoginPage)
        self.PasswordLineEdit.setGeometry(QtCore.QRect(68, 320, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PasswordLineEdit.setFont(font)
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.PasswordErrorLabel = QtWidgets.QLabel(self.LoginPage)
        self.PasswordErrorLabel.setGeometry(QtCore.QRect(70, 380, 551, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.PasswordErrorLabel.setFont(font)
        self.PasswordErrorLabel.setStyleSheet("color: #C40000;")
        self.PasswordErrorLabel.setObjectName("PasswordErrorLabel")
        self.SignInButton = QtWidgets.QPushButton(self.LoginPage)
        self.SignInButton.setGeometry(QtCore.QRect(70, 460, 631, 41))
        self.SignInButton.setStyleSheet("background-color: #FCD200;")
        self.SignInButton.setObjectName("SignInButton")
        self.LoginScreenHeaderImage = QtWidgets.QLabel(self.LoginPage)
        self.LoginScreenHeaderImage.setGeometry(QtCore.QRect(140, 40, 491, 51))
        self.LoginScreenHeaderImage.setText("")
        self.LoginScreenHeaderImage.setPixmap(QtGui.QPixmap("src/ui\\LoginScreenHeaderImage.PNG"))
        self.LoginScreenHeaderImage.setScaledContents(True)
        self.LoginScreenHeaderImage.setObjectName("LoginScreenHeaderImage")
        self.SignInButtonErrorLabel = QtWidgets.QLabel(self.LoginPage)
        self.SignInButtonErrorLabel.setGeometry(QtCore.QRect(130, 520, 551, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.SignInButtonErrorLabel.setFont(font)
        self.SignInButtonErrorLabel.setStyleSheet("color: #C40000;")
        self.SignInButtonErrorLabel.setObjectName("SignInButtonErrorLabel")
        self.LoadingIcon = QtWidgets.QLabel(self.LoginPage)
        self.LoadingIcon.setGeometry(QtCore.QRect(350, 540, 51, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.LoadingIcon.setFont(font)
        self.LoadingIcon.setStyleSheet("color: #C40000;")
        self.LoadingIcon.setObjectName("LoadingIcon")
        self.stackedWidget.addWidget(self.LoginPage)
        self.TitleSelectPage = QtWidgets.QWidget()
        self.TitleSelectPage.setObjectName("TitleSelectPage")
        self.SelectTitleHeader = QtWidgets.QLabel(self.TitleSelectPage)
        self.SelectTitleHeader.setGeometry(QtCore.QRect(200, 50, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SelectTitleHeader.setFont(font)
        self.SelectTitleHeader.setObjectName("SelectTitleHeader")
        self.TitleSelectLineEdit = QtWidgets.QLineEdit(self.TitleSelectPage)
        self.TitleSelectLineEdit.setGeometry(QtCore.QRect(200, 190, 361, 31))
        self.TitleSelectLineEdit.setObjectName("TitleSelectLineEdit")
        self.cinemaItemsComboBox = QtWidgets.QComboBox(self.TitleSelectPage)
        self.cinemaItemsComboBox.setGeometry(QtCore.QRect(200, 220, 361, 21))
        self.cinemaItemsComboBox.setObjectName("cinemaItemsComboBox")
        self.selectReviewTitleButton = QtWidgets.QPushButton(self.TitleSelectPage)
        self.selectReviewTitleButton.setGeometry(QtCore.QRect(320, 300, 121, 21))
        self.selectReviewTitleButton.setStyleSheet("background-color: #FCD200;")
        self.selectReviewTitleButton.setObjectName("selectReviewTitleButton")
        self.IMDBLogoImageSelectTitleScreen = QtWidgets.QLabel(self.TitleSelectPage)
        self.IMDBLogoImageSelectTitleScreen.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.IMDBLogoImageSelectTitleScreen.setText("")
        self.IMDBLogoImageSelectTitleScreen.setPixmap(QtGui.QPixmap("src/ui\\IMDb_Logo_Rectangle_Gold.png"))
        self.IMDBLogoImageSelectTitleScreen.setScaledContents(True)
        self.IMDBLogoImageSelectTitleScreen.setObjectName("IMDBLogoImageSelectTitleScreen")
        self.LoadingIconSelectTitleScreen = QtWidgets.QLabel(self.TitleSelectPage)
        self.LoadingIconSelectTitleScreen.setGeometry(QtCore.QRect(360, 350, 51, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.LoadingIconSelectTitleScreen.setFont(font)
        self.LoadingIconSelectTitleScreen.setStyleSheet("color: #C40000;")
        self.LoadingIconSelectTitleScreen.setObjectName("LoadingIconSelectTitleScreen")
        self.stackedWidget.addWidget(self.TitleSelectPage)
        self.SubmitReviewPage = QtWidgets.QWidget()
        self.SubmitReviewPage.setObjectName("SubmitReviewPage")
        self.ReviewTitleLabel = QtWidgets.QLabel(self.SubmitReviewPage)
        self.ReviewTitleLabel.setGeometry(QtCore.QRect(280, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ReviewTitleLabel.setFont(font)
        self.ReviewTitleLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ReviewTitleLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ReviewTitleLabel.setObjectName("ReviewTitleLabel")
        self.headlineLineEdit = QtWidgets.QLineEdit(self.SubmitReviewPage)
        self.headlineLineEdit.setGeometry(QtCore.QRect(80, 140, 651, 31))
        self.headlineLineEdit.setObjectName("headlineLineEdit")
        self.HeadlineLabel = QtWidgets.QLabel(self.SubmitReviewPage)
        self.HeadlineLabel.setGeometry(QtCore.QRect(80, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HeadlineLabel.setFont(font)
        self.HeadlineLabel.setObjectName("HeadlineLabel")
        self.ratingSpinBox = QtWidgets.QSpinBox(self.SubmitReviewPage)
        self.ratingSpinBox.setGeometry(QtCore.QRect(80, 220, 42, 22))
        self.ratingSpinBox.setObjectName("ratingSpinBox")
        self.ratingLabel = QtWidgets.QLabel(self.SubmitReviewPage)
        self.ratingLabel.setGeometry(QtCore.QRect(80, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ratingLabel.setFont(font)
        self.ratingLabel.setObjectName("ratingLabel")
        self.ReviewTitleNameLabel = QtWidgets.QLabel(self.SubmitReviewPage)
        self.ReviewTitleNameLabel.setGeometry(QtCore.QRect(180, 90, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ReviewTitleNameLabel.setFont(font)
        self.ReviewTitleNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ReviewTitleNameLabel.setWordWrap(True)
        self.ReviewTitleNameLabel.setObjectName("ReviewTitleNameLabel")
        self.reviewBodyPlainTextEdit = QtWidgets.QPlainTextEdit(self.SubmitReviewPage)
        self.reviewBodyPlainTextEdit.setGeometry(QtCore.QRect(80, 250, 651, 231))
        self.reviewBodyPlainTextEdit.setObjectName("reviewBodyPlainTextEdit")
        self.ErrorLabel = QtWidgets.QLabel(self.SubmitReviewPage)
        self.ErrorLabel.setGeometry(QtCore.QRect(80, 490, 401, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("color: #C40000;")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.isMovieCheckBox = QtWidgets.QCheckBox(self.SubmitReviewPage)
        self.isMovieCheckBox.setGeometry(QtCore.QRect(80, 510, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.isMovieCheckBox.setFont(font)
        self.isMovieCheckBox.setObjectName("isMovieCheckBox")
        self.isTvShowCheckBox = QtWidgets.QCheckBox(self.SubmitReviewPage)
        self.isTvShowCheckBox.setGeometry(QtCore.QRect(170, 510, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.isTvShowCheckBox.setFont(font)
        self.isTvShowCheckBox.setObjectName("isTvShowCheckBox")
        self.submitReviewButton = QtWidgets.QPushButton(self.SubmitReviewPage)
        self.submitReviewButton.setGeometry(QtCore.QRect(290, 540, 241, 21))
        self.submitReviewButton.setStyleSheet("background-color: #FCD200;")
        self.submitReviewButton.setObjectName("submitReviewButton")
        self.submitReviewErrorLabel = QtWidgets.QLabel(self.SubmitReviewPage)
        self.submitReviewErrorLabel.setGeometry(QtCore.QRect(240, 570, 351, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submitReviewErrorLabel.setFont(font)
        self.submitReviewErrorLabel.setStyleSheet("color: #C40000;\n"
"")
        self.submitReviewErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.submitReviewErrorLabel.setObjectName("submitReviewErrorLabel")
        self.IMDBLogoImageReviewTitleScreen = QtWidgets.QLabel(self.SubmitReviewPage)
        self.IMDBLogoImageReviewTitleScreen.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.IMDBLogoImageReviewTitleScreen.setText("")
        self.IMDBLogoImageReviewTitleScreen.setPixmap(QtGui.QPixmap("src/ui\\IMDb_Logo_Rectangle_Gold.png"))
        self.IMDBLogoImageReviewTitleScreen.setScaledContents(True)
        self.IMDBLogoImageReviewTitleScreen.setObjectName("IMDBLogoImageReviewTitleScreen")
        self.LoadingIconReviewTitleScreen = QtWidgets.QLabel(self.SubmitReviewPage)
        self.LoadingIconReviewTitleScreen.setGeometry(QtCore.QRect(380, 490, 51, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.LoadingIconReviewTitleScreen.setFont(font)
        self.LoadingIconReviewTitleScreen.setStyleSheet("color: #C40000;")
        self.LoadingIconReviewTitleScreen.setObjectName("LoadingIconReviewTitleScreen")
        self.stackedWidget.addWidget(self.SubmitReviewPage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UsernameLabel.setText(_translate("MainWindow", "Username"))
        self.UsernameErrorLabel.setText(_translate("MainWindow", "TextLabel"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.PasswordErrorLabel.setText(_translate("MainWindow", "TextLabel"))
        self.SignInButton.setText(_translate("MainWindow", "Sign In"))
        self.SignInButtonErrorLabel.setText(_translate("MainWindow", "TextLabel"))
        self.LoadingIcon.setText(_translate("MainWindow", "Loading Icon"))
        self.SelectTitleHeader.setText(_translate("MainWindow", "Select Title To Review"))
        self.selectReviewTitleButton.setText(_translate("MainWindow", "Select"))
        self.LoadingIconSelectTitleScreen.setText(_translate("MainWindow", "Loading Icon"))
        self.ReviewTitleLabel.setText(_translate("MainWindow", "Review Title"))
        self.HeadlineLabel.setText(_translate("MainWindow", "Headline"))
        self.ratingLabel.setText(_translate("MainWindow", "Rating"))
        self.ReviewTitleNameLabel.setText(_translate("MainWindow", "Planet of the Apes"))
        self.ErrorLabel.setText(_translate("MainWindow", "Error Placeholder"))
        self.isMovieCheckBox.setText(_translate("MainWindow", "Movie"))
        self.isTvShowCheckBox.setText(_translate("MainWindow", "TV Show"))
        self.submitReviewButton.setText(_translate("MainWindow", "SUBMIT"))
        self.submitReviewErrorLabel.setText(_translate("MainWindow", "Error Placeholder"))
        self.LoadingIconReviewTitleScreen.setText(_translate("MainWindow", "Loading Icon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
