import sys

from part1 import create_annotation
from part2 import create_dataset_2, create_annotation_2
from part3 import create_dataset_3, create_annotation_3
from part5 import Iterator

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPixmap, QFont
from PyQt5.QtWidgets import  *
from PyQt5.QtWidgets import  QApplication,QWidget, QLabel


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initIterators()
        self.createActions()
        self.createMenuStr()
        self.setGeometry(0, 35, 1080, 720)
        self.setStyleSheet('background-color: grey;')



    def initUI(self) -> None:
        self.setWindowTitle('polarbear/brownbear')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        font = QFont('Georgia',14)

        polarbear_btn = QPushButton('The next polar bear', self)
        brownbear_btn = QPushButton('The next brown bear', self)
        polarbear_btn.setFont(font)
        brownbear_btn.setFont(font)
        polarbear_btn.setStyleSheet('background-color: black; color: white;')
        brownbear_btn.setStyleSheet('background-color: black; color: white;')

        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignRight)
        self.lbl.setFont(font)

        hbox = QHBoxLayout()
        hbox.addSpacing(0)
        hbox.addWidget(polarbear_btn)
        hbox.addWidget(brownbear_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(0)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)

        polarbear_btn.clicked.connect(self.nextpolarbear)
        brownbear_btn.clicked.connect(self.nextbrownbear)

        self.folderpath = ' '

        self.show()

    def initIterators(self) -> None:
        self.polarbear = Iterator('polarbear', 'dataset')
        self.brownbear = Iterator('brownbear', 'dataset')

    def nextpolarbear(self) -> None:
        lbl_size = self.lbl.size()
        next_image = next(self.polarbear)
        if next_image != None:
            img = QPixmap(next_image).scaled(lbl_size, Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            
            self.initIterators()
            self.nextpolarbear()

    def nextbrownbear(self) -> None:
        lbl_size = self.lbl.size()
        next_image = next(self.brownbear)
        if next_image != None:
            img = QPixmap(next_image).scaled(lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.initIterators()
            self.nextbrownbear()

    def createMenuStr(self) -> None:
        menuStr = self.menuBar()
        font = QFont('Georgia',14)
        self.setFont(font)

        self.fileMenu = menuStr.addMenu('&Menu')
        self.fileMenu.addAction(self.exitkey)
        self.fileMenu.addAction(self.changekey)


        self.annotationMenu = menuStr.addMenu('&Annotation')
        self.annotationMenu.addAction(self.createannotationkey)

        self.dataMenu = menuStr.addMenu('&Other Dataset')
        self.dataMenu.addAction(self.createData2key)
        self.dataMenu.addAction(self.createData3key)

    def createActions(self) -> None:
    
        self.exitkey = QAction('&Exit')
        self.exitkey.triggered.connect(qApp.quit)

        self.changekey = QAction('&Change dataset')
        self.changekey.triggered.connect(self.changeDataset)

        self.createannotationkey = QAction('&Create annotation')
        self.createannotationkey.triggered.connect(self.createAnnotation)

        self.createData2key = QAction('&dataset2')
        self.createData2key.triggered.connect(self.dataset2)

        self.createData3key = QAction('&dataset3')
        self.createData3key.triggered.connect(self.dataset3)
    
        
    def createAnnotation(self) -> None:
    
        if 'dataset' in str(self.folderpath):
            create_annotation()
        elif 'dataset_2' in str(self.folderpath):
            create_annotation_2()
        elif 'dataset_3' in str(self.folderpath):
            create_annotation_3()

    def changeDataset(self) -> None:
        reply = QMessageBox.question(self, 'Warning', f'Are you going to change current dataset. Confirm this?\nCurrent dataset: {str(self.folderpath)}', QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        else:
            pass
    
    def dataset2(self) -> None:
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        create_dataset_2(self.folderpath)
        

    def dataset3(self) -> None:
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        create_dataset_3(self.folderpath)


def closeEvent(self, event: QEvent) -> None:
        reply = QMessageBox.question(self, 'Message', 'Are you going to quit. Confirm this?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()
