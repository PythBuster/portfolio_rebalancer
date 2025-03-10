# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 620)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_canvas = QFrame(self.centralwidget)
        self.frame_canvas.setObjectName(u"frame_canvas")
        self.frame_canvas.setMinimumSize(QSize(200, 200))
        self.frame_canvas.setMaximumSize(QSize(200, 200))
        self.frame_canvas.setStyleSheet(u"background-color: red;")
        self.frame_canvas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_canvas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_canvas)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_canvas)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_allocation_title = QLabel(self.centralwidget)
        self.label_allocation_title.setObjectName(u"label_allocation_title")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_allocation_title.setFont(font)

        self.verticalLayout.addWidget(self.label_allocation_title)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.monthly_savings_amount = QLabel(self.centralwidget)
        self.monthly_savings_amount.setObjectName(u"monthly_savings_amount")

        self.horizontalLayout_3.addWidget(self.monthly_savings_amount)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lineEdit_monthly_savings_amount = QLineEdit(self.centralwidget)
        self.lineEdit_monthly_savings_amount.setObjectName(u"lineEdit_monthly_savings_amount")
        self.lineEdit_monthly_savings_amount.setMinimumSize(QSize(100, 0))
        self.lineEdit_monthly_savings_amount.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_monthly_savings_amount.setStyleSheet(u"border: none; border-bottom: 1px solid black;")
        self.lineEdit_monthly_savings_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_monthly_savings_amount)

        self.label_currency = QLabel(self.centralwidget)
        self.label_currency.setObjectName(u"label_currency")

        self.horizontalLayout_3.addWidget(self.label_currency)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableView_portfolio_data = QTableView(self.centralwidget)
        self.tableView_portfolio_data.setObjectName(u"tableView_portfolio_data")
        self.tableView_portfolio_data.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tableView_portfolio_data.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout.addWidget(self.tableView_portfolio_data)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_save_portfolio_data = QPushButton(self.centralwidget)
        self.pushButton_save_portfolio_data.setObjectName(u"pushButton_save_portfolio_data")

        self.horizontalLayout_4.addWidget(self.pushButton_save_portfolio_data)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 818, 23))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.action_Exit)

        self.retranslateUi(MainWindow)
        self.action_Exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Portfolio Rebalancer", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.label_allocation_title.setText(QCoreApplication.translate("MainWindow", u"Verteilung - Bestrebung:", None))
        self.monthly_savings_amount.setText(QCoreApplication.translate("MainWindow", u"Monatliche Sparsumme:", None))
        self.lineEdit_monthly_savings_amount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_currency.setText(QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.pushButton_save_portfolio_data.setText(QCoreApplication.translate("MainWindow", u"&Speichern", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

