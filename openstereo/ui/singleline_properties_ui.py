# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\singleline_properties.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 428)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.prop_data_attitude = QtWidgets.QLineEdit(self.groupBox_3)
        self.prop_data_attitude.setObjectName("prop_data_attitude")
        self.verticalLayout_2.addWidget(self.prop_data_attitude)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.prop_color_point_c = QtWidgets.QPushButton(self.groupBox)
        self.prop_color_point_c.setText("")
        self.prop_color_point_c.setObjectName("prop_color_point_c")
        self.gridLayout.addWidget(self.prop_color_point_c, 1, 0, 1, 1)
        self.prop_point_marker = QtWidgets.QComboBox(self.groupBox)
        self.prop_point_marker.setObjectName("prop_point_marker")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.prop_point_marker.addItem("")
        self.gridLayout.addWidget(self.prop_point_marker, 1, 1, 1, 1)
        self.prop_point_ms = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.prop_point_ms.setObjectName("prop_point_ms")
        self.gridLayout.addWidget(self.prop_point_ms, 1, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.groupBox_8 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.prop_legend_point = QtWidgets.QLineEdit(self.groupBox_8)
        self.prop_legend_point.setObjectName("prop_legend_point")
        self.gridLayout_11.addWidget(self.prop_legend_point, 0, 1, 1, 1)
        self.prop_checklegend_point = QtWidgets.QCheckBox(self.groupBox_8)
        self.prop_checklegend_point.setObjectName("prop_checklegend_point")
        self.gridLayout_11.addWidget(self.prop_checklegend_point, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_8)
        spacerItem = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setObjectName("apply")
        self.horizontalLayout.addWidget(self.apply)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox_3.raise_()
        self.groupBox_8.raise_()

        self.retranslateUi(Dialog)
        self.ok_button.clicked.connect(Dialog.accept)
        self.cancel_button.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.prop_color_point_c, self.prop_point_marker)
        Dialog.setTabOrder(self.prop_point_marker, self.prop_point_ms)
        Dialog.setTabOrder(self.prop_point_ms, self.cancel_button)
        Dialog.setTabOrder(self.cancel_button, self.apply)
        Dialog.setTabOrder(self.apply, self.ok_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_3.setTitle(_translate("Dialog", "Attitude"))
        self.groupBox.setTitle(_translate("Dialog", "Pole"))
        self.label_2.setText(_translate("Dialog", "Symbol"))
        self.label_3.setText(_translate("Dialog", "Size"))
        self.label.setText(_translate("Dialog", "Color"))
        self.prop_point_marker.setItemText(0, _translate("Dialog", "o"))
        self.prop_point_marker.setItemText(1, _translate("Dialog", "^"))
        self.prop_point_marker.setItemText(2, _translate("Dialog", "v"))
        self.prop_point_marker.setItemText(3, _translate("Dialog", "<"))
        self.prop_point_marker.setItemText(4, _translate("Dialog", ">"))
        self.prop_point_marker.setItemText(5, _translate("Dialog", "s"))
        self.prop_point_marker.setItemText(6, _translate("Dialog", "+"))
        self.prop_point_marker.setItemText(7, _translate("Dialog", "x"))
        self.prop_point_marker.setItemText(8, _translate("Dialog", "D"))
        self.prop_point_marker.setItemText(9, _translate("Dialog", "d"))
        self.prop_point_marker.setItemText(10, _translate("Dialog", "h"))
        self.prop_point_marker.setItemText(11, _translate("Dialog", "H"))
        self.prop_point_marker.setItemText(12, _translate("Dialog", "p"))
        self.prop_point_marker.setItemText(13, _translate("Dialog", "|"))
        self.prop_point_marker.setItemText(14, _translate("Dialog", "_"))
        self.prop_point_marker.setItemText(15, _translate("Dialog", "*"))
        self.prop_point_marker.setItemText(16, _translate("Dialog", "1"))
        self.prop_point_marker.setItemText(17, _translate("Dialog", "2"))
        self.prop_point_marker.setItemText(18, _translate("Dialog", "3"))
        self.prop_point_marker.setItemText(19, _translate("Dialog", "4"))
        self.groupBox_8.setTitle(_translate("Dialog", "Data Legend"))
        self.prop_checklegend_point.setText(_translate("Dialog", "Line"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.apply.setText(_translate("Dialog", "Apply"))

