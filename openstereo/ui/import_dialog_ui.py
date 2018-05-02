# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/import_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(287, 499)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fname = QtWidgets.QLineEdit(Dialog)
        self.fname.setReadOnly(False)
        self.fname.setObjectName("fname")
        self.horizontalLayout_2.addWidget(self.fname)
        self.browse = QtWidgets.QPushButton(Dialog)
        self.browse.setObjectName("browse")
        self.horizontalLayout_2.addWidget(self.browse)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lines = QtWidgets.QRadioButton(self.groupBox)
        self.lines.setObjectName("lines")
        self.verticalLayout.addWidget(self.lines)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.planes = QtWidgets.QRadioButton(self.groupBox)
        self.planes.setChecked(True)
        self.planes.setObjectName("planes")
        self.horizontalLayout_3.addWidget(self.planes)
        self.planetype = QtWidgets.QComboBox(self.groupBox)
        self.planetype.setObjectName("planetype")
        self.planetype.addItem("")
        self.planetype.addItem("")
        self.horizontalLayout_3.addWidget(self.planetype)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.small_circle = QtWidgets.QRadioButton(self.groupBox)
        self.small_circle.setObjectName("small_circle")
        self.verticalLayout.addWidget(self.small_circle)
        self.circular = QtWidgets.QRadioButton(self.groupBox)
        self.circular.setObjectName("circular")
        self.verticalLayout.addWidget(self.circular)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.do_skip = QtWidgets.QCheckBox(self.groupBox_3)
        self.do_skip.setObjectName("do_skip")
        self.gridLayout_2.addWidget(self.do_skip, 4, 0, 1, 1)
        self.has_header = QtWidgets.QCheckBox(self.groupBox_3)
        self.has_header.setChecked(True)
        self.has_header.setObjectName("has_header")
        self.gridLayout_2.addWidget(self.has_header, 3, 0, 1, 1)
        self.skip_rows = QtWidgets.QSpinBox(self.groupBox_3)
        self.skip_rows.setObjectName("skip_rows")
        self.gridLayout_2.addWidget(self.skip_rows, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.delimiter = QtWidgets.QLineEdit(self.groupBox_3)
        self.delimiter.setObjectName("delimiter")
        self.gridLayout_2.addWidget(self.delimiter, 0, 1, 1, 1)
        self.header_row = QtWidgets.QSpinBox(self.groupBox_3)
        self.header_row.setObjectName("header_row")
        self.gridLayout_2.addWidget(self.header_row, 3, 1, 1, 1)
        self.worksheet = QtWidgets.QComboBox(self.groupBox_3)
        self.worksheet.setObjectName("worksheet")
        self.gridLayout_2.addWidget(self.worksheet, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.comment_marker = QtWidgets.QLineEdit(self.groupBox_3)
        self.comment_marker.setObjectName("comment_marker")
        self.gridLayout_2.addWidget(self.comment_marker, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.longitude_label = QtWidgets.QLabel(self.groupBox_2)
        self.longitude_label.setObjectName("longitude_label")
        self.gridLayout.addWidget(self.longitude_label, 0, 0, 1, 1)
        self.longitude = QtWidgets.QComboBox(self.groupBox_2)
        self.longitude.setObjectName("longitude")
        self.gridLayout.addWidget(self.longitude, 0, 1, 1, 1)
        self.colatitude_label = QtWidgets.QLabel(self.groupBox_2)
        self.colatitude_label.setObjectName("colatitude_label")
        self.gridLayout.addWidget(self.colatitude_label, 1, 0, 1, 1)
        self.colatitude = QtWidgets.QComboBox(self.groupBox_2)
        self.colatitude.setObjectName("colatitude")
        self.gridLayout.addWidget(self.colatitude, 1, 1, 1, 1)
        self.alpha_label = QtWidgets.QLabel(self.groupBox_2)
        self.alpha_label.setObjectName("alpha_label")
        self.gridLayout.addWidget(self.alpha_label, 2, 0, 1, 1)
        self.alpha = QtWidgets.QComboBox(self.groupBox_2)
        self.alpha.setObjectName("alpha")
        self.gridLayout.addWidget(self.alpha, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.ok_button.clicked.connect(Dialog.accept)
        self.cancel_button.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Import Data"))
        self.browse.setText(_translate("Dialog", "Browse..."))
        self.groupBox.setTitle(_translate("Dialog", "Data Type"))
        self.lines.setText(_translate("Dialog", "Lines"))
        self.planes.setText(_translate("Dialog", "Planes"))
        self.planetype.setItemText(0, _translate("Dialog", "Dip Direction"))
        self.planetype.setItemText(1, _translate("Dialog", "Direction"))
        self.small_circle.setText(_translate("Dialog", "Small Circles"))
        self.circular.setText(_translate("Dialog", "Azimuth Data"))
        self.groupBox_3.setTitle(_translate("Dialog", "File Settings"))
        self.do_skip.setText(_translate("Dialog", "Skip Rows"))
        self.has_header.setText(_translate("Dialog", "Header Row"))
        self.label.setText(_translate("Dialog", "Delimiter"))
        self.label_5.setText(_translate("Dialog", "Worksheet"))
        self.label_2.setText(_translate("Dialog", "Comment"))
        self.groupBox_2.setTitle(_translate("Dialog", "Attitude Columns"))
        self.longitude_label.setText(_translate("Dialog", "Dip Direction"))
        self.colatitude_label.setText(_translate("Dialog", "Dip"))
        self.alpha_label.setText(_translate("Dialog", "Alpha"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))

