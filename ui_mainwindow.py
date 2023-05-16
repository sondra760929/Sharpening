# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.editContrast = QLineEdit(self.groupBox)
        self.editContrast.setObjectName(u"editContrast")

        self.gridLayout.addWidget(self.editContrast, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pbTone = QPushButton(self.groupBox)
        self.pbTone.setObjectName(u"pbTone")

        self.gridLayout.addWidget(self.pbTone, 6, 0, 1, 2)

        self.sliderContrast = QSlider(self.groupBox)
        self.sliderContrast.setObjectName(u"sliderContrast")
        self.sliderContrast.setMinimum(-127)
        self.sliderContrast.setMaximum(127)
        self.sliderContrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.sliderContrast, 5, 0, 1, 2)

        self.slideBrightness = QSlider(self.groupBox)
        self.slideBrightness.setObjectName(u"slideBrightness")
        self.slideBrightness.setMaximum(100)
        self.slideBrightness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slideBrightness, 2, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.editBrightness = QLineEdit(self.groupBox)
        self.editBrightness.setObjectName(u"editBrightness")

        self.gridLayout.addWidget(self.editBrightness, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.sliderSharpen = QSlider(self.groupBox_2)
        self.sliderSharpen.setObjectName(u"sliderSharpen")
        self.sliderSharpen.setMaximum(10)
        self.sliderSharpen.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderSharpen, 1, 0, 1, 2)

        self.pbSharpen = QPushButton(self.groupBox_2)
        self.pbSharpen.setObjectName(u"pbSharpen")

        self.gridLayout_2.addWidget(self.pbSharpen, 3, 0, 1, 2)

        self.editSharpen = QLineEdit(self.groupBox_2)
        self.editSharpen.setObjectName(u"editSharpen")

        self.gridLayout_2.addWidget(self.editSharpen, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cbTone = QCheckBox(self.groupBox_3)
        self.cbTone.setObjectName(u"cbTone")

        self.verticalLayout_4.addWidget(self.cbTone)

        self.cbSharpen = QCheckBox(self.groupBox_3)
        self.cbSharpen.setObjectName(u"cbSharpen")

        self.verticalLayout_4.addWidget(self.cbSharpen)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.editMax = QLineEdit(self.groupBox_3)
        self.editMax.setObjectName(u"editMax")

        self.verticalLayout_4.addWidget(self.editMax)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageLabel = QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.imageLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.scrollArea1 = QScrollArea(self.centralwidget)
        self.scrollArea1.setObjectName(u"scrollArea1")
        self.scrollArea1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 100, 100))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.imageLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.imageLabel1.setObjectName(u"imageLabel1")

        self.horizontalLayout_4.addWidget(self.imageLabel1)

        self.scrollArea1.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea1)

        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeView_2 = QTreeView(self.centralwidget)
        self.treeView_2.setObjectName(u"treeView_2")

        self.verticalLayout_2.addWidget(self.treeView_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 916, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sharpening Images", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tone", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Brightness: ", None))
        self.pbTone.setText(QCoreApplication.translate("MainWindow", u"미리보기", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contrast: ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Sharpen", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Value: ", None))
        self.pbSharpen.setText(QCoreApplication.translate("MainWindow", u"미리보기", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"변환", None))
        self.cbTone.setText(QCoreApplication.translate("MainWindow", u"Tone 적용", None))
        self.cbSharpen.setText(QCoreApplication.translate("MainWindow", u"Sharpen 적용", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"최대 허용 용량 (%)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"변환 >>", None))
        self.imageLabel.setText("")
        self.imageLabel1.setText("")
    # retranslateUi

