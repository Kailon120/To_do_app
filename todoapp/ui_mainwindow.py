# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(901, 451)
        mainwindow.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(mainwindow)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(mainwindow)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(50,50,50);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_task = QLabel(self.frame)
        self.text_task.setObjectName(u"text_task")
        sizePolicy.setHeightForWidth(self.text_task.sizePolicy().hasHeightForWidth())
        self.text_task.setSizePolicy(sizePolicy)
        self.text_task.setMaximumSize(QSize(50, 30))
        self.text_task.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.text_task)

        self.count_task = QLabel(self.frame)
        self.count_task.setObjectName(u"count_task")
        sizePolicy.setHeightForWidth(self.count_task.sizePolicy().hasHeightForWidth())
        self.count_task.setSizePolicy(sizePolicy)
        self.count_task.setMaximumSize(QSize(20, 16777215))
        self.count_task.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.count_task)

        self.text_complete = QLabel(self.frame)
        self.text_complete.setObjectName(u"text_complete")
        sizePolicy.setHeightForWidth(self.text_complete.sizePolicy().hasHeightForWidth())
        self.text_complete.setSizePolicy(sizePolicy)
        self.text_complete.setMaximumSize(QSize(90, 30))
        self.text_complete.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.text_complete)

        self.count_complete = QLabel(self.frame)
        self.count_complete.setObjectName(u"count_complete")
        sizePolicy.setHeightForWidth(self.count_complete.sizePolicy().hasHeightForWidth())
        self.count_complete.setSizePolicy(sizePolicy)
        self.count_complete.setMaximumSize(QSize(20, 16777215))
        self.count_complete.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.count_complete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.gridLayout_5.addWidget(self.frame, 0, 1, 1, 1)

        self.listWidget = QListWidget(mainwindow)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget.setStyleSheet(u"/* Estilos para QListWidget */\n"
"QListWidget {\n"
"    background-color: rgb(66,66,66);\n"
"    border: none;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Estilos para los \u00edtems de QListWidget */\n"
"QListWidget::item {\n"
"    background-color: rgb(94,94,94);\n"
"    border-radius: 10px;\n"
"    margin: 4px;\n"
"    min-width: 150px;\n"
"    min-height: 100px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Efecto hover para los \u00edtems */\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(130,130,130);\n"
"}\n"
"\n"
"/* \u00cdtem seleccionado */\n"
"QListWidget::item:selected {\n"
"    background-color: #a0a0a0;\n"
"    border: 1px solid #909090;\n"
"}")

        self.gridLayout_5.addWidget(self.listWidget, 1, 1, 1, 1)

        self.frame_2 = QFrame(mainwindow)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35,35,35);\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(35)
        self.gridLayout_2.setContentsMargins(12, 12, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.addButton = QPushButton(self.frame_2)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy1)
        self.addButton.setMinimumSize(QSize(0, 0))
        self.addButton.setMaximumSize(QSize(16777215, 120))
        self.addButton.setSizeIncrement(QSize(0, 0))
        self.addButton.setBaseSize(QSize(0, 0))
        self.addButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(240,240,240);\n"
"	background-color: rgb(86,86,86);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(130,130,130);\n"
"}")

        self.gridLayout_2.addWidget(self.addButton, 1, 0, 1, 1)

        self.checkButton = QPushButton(self.frame_2)
        self.checkButton.setObjectName(u"checkButton")
        sizePolicy1.setHeightForWidth(self.checkButton.sizePolicy().hasHeightForWidth())
        self.checkButton.setSizePolicy(sizePolicy1)
        self.checkButton.setMaximumSize(QSize(16777215, 120))
        self.checkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(240,240,240);\n"
"	background-color: rgb(86,86,86);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(130,130,130);\n"
"}")

        self.gridLayout_2.addWidget(self.checkButton, 2, 0, 1, 1)

        self.deleteButton = QPushButton(self.frame_2)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy1.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy1)
        self.deleteButton.setMaximumSize(QSize(16777215, 120))
        self.deleteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(240,240,240);\n"
"	background-color: rgb(86,86,86);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(130,130,130);\n"
"}")

        self.gridLayout_2.addWidget(self.deleteButton, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 2, 1)

        self.gridLayout_5.setRowStretch(1, 2)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 4)

        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 2, 1)


        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"to_do_app", None))
        self.text_task.setText(QCoreApplication.translate("mainwindow", u"Tareas:", None))
        self.count_task.setText(QCoreApplication.translate("mainwindow", u"0", None))
        self.text_complete.setText(QCoreApplication.translate("mainwindow", u"Completadas:", None))
        self.count_complete.setText(QCoreApplication.translate("mainwindow", u"0", None))
        self.addButton.setText(QCoreApplication.translate("mainwindow", u"Agregar", None))
        self.checkButton.setText(QCoreApplication.translate("mainwindow", u"Completar", None))
        self.deleteButton.setText(QCoreApplication.translate("mainwindow", u"Eliminar", None))
    # retranslateUi

