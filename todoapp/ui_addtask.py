# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addtask.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_addtask(object):
    def setupUi(self, addtask):
        if not addtask.objectName():
            addtask.setObjectName(u"addtask")
        addtask.resize(315, 344)
        addtask.setMinimumSize(QSize(315, 344))
        addtask.setMaximumSize(QSize(315, 344))
        addtask.setSizeIncrement(QSize(315, 344))
        self.centralwidget = QWidget(addtask)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 50, 20, 20)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.input_title = QLineEdit(self.centralwidget)
        self.input_title.setObjectName(u"input_title")

        self.verticalLayout.addWidget(self.input_title)

        self.input_description = QLineEdit(self.centralwidget)
        self.input_description.setObjectName(u"input_description")

        self.verticalLayout.addWidget(self.input_description)

        self.input_date = QDateEdit(self.centralwidget)
        self.input_date.setObjectName(u"input_date")

        self.verticalLayout.addWidget(self.input_date)

        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.createButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)
        addtask.setCentralWidget(self.centralwidget)

        self.retranslateUi(addtask)

        QMetaObject.connectSlotsByName(addtask)
    # setupUi

    def retranslateUi(self, addtask):
        addtask.setWindowTitle(QCoreApplication.translate("addtask", u"Agregar Tarea", None))
        self.label.setText(QCoreApplication.translate("addtask", u"Creador de tareas", None))
        self.input_title.setPlaceholderText(QCoreApplication.translate("addtask", u"T\u00edtulo", None))
        self.input_description.setPlaceholderText(QCoreApplication.translate("addtask", u"Descripci\u00f3n", None))
        self.createButton.setText(QCoreApplication.translate("addtask", u"Crear", None))
    # retranslateUi

