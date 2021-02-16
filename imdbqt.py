import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,QVBoxLayout,QPushButton
from PyQt5.QtGui import *
class SecWindow(QWidget):
    def __init__(self):
        super(SecWindow, self).__init__()
        self.init_ui2()
    def init_ui2(self):
        v_box2=QVBoxLayout(self)
        self.setGeometry(500,300,400,300)
        self.setWindowTitle("IMDB 250 second window")
        self.setStyleSheet("background-color:gray;")
        self.setWindowIcon(QIcon("download.png"))
        self.output=QLabel("",self)
        self.output.setStyleSheet("font-size:15px;")

        self.setLayout(v_box2)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.secondWindow = SecWindow()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(500,300,400,300)
        self.setFixedSize(400,600)
        self.setWindowTitle("IMDB 250")
        self.setStyleSheet("background-color:gray;")
        self.setWindowIcon(QIcon("download.png"))

        self.create_labels()
        self.create_lines()
        self.create_buttons()
        self.mystr=""

        v_box=QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addStretch()
        v_box.addWidget(self.label2)
        v_box.addWidget(self.line1)
        v_box.addStretch()
        v_box.addWidget(self.button1)
        self.setLayout(v_box)

        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        self.titles = soup.find_all("td", {"class": "titleColumn"})
        self.ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

    def create_labels(self):
        self.label = QLabel(self)
        self.label2 = QLabel(self)

        self.label.setText("Welcome To The IMDB 250 Program")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label2.setText("SORT BY IMDB RATING")
        self.label2.setStyleSheet("font-size:20px;")
        self.label2.setAlignment(Qt.AlignCenter)

    def create_lines(self):
        self.line1 = QLineEdit(self)
        self.line1.setStyleSheet("border: 3px solid yellow;")
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setFont(QFont("Arial",16))
        self.line1.setStyleSheet("background-color:white;")
    def create_buttons(self):
        self.button1=QPushButton(self)
        self.button1.setText("ENTER")
        self.button1.setStyleSheet("background-color:yellow;")
        self.button1.setShortcut("Enter")
        self.button1.clicked.connect(self.passingInfo)
        self.button1.clicked.connect(self.close)

    def passingInfo(self):
        get=self.line1.text()
        a=float(get)
        for title, rating in zip(self.titles, self.ratings):
            title = title.text
            rating = rating.text
            title = title.strip()
            title = title.replace("\n", "")
            rating = rating.strip()
            rating = rating.replace("\n", "")
            if (float(rating) > a):
                self.mystr+="title: {} rating: {}".format(title, rating)+"\n"
                self.secondWindow.output.setText(self.mystr)
            self.update()
        self.secondWindow.show()
    def update(self):
        self.secondWindow.output.adjustSize()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






