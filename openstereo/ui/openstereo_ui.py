# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\openstereo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 572)
        MainWindow.setAcceptDrops(False)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(600, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.projectionTab = QtWidgets.QWidget()
        self.projectionTab.setObjectName("projectionTab")
        self.tabWidget.addTab(self.projectionTab, "")
        self.roseTab = QtWidgets.QWidget()
        self.roseTab.setObjectName("roseTab")
        self.tabWidget.addTab(self.roseTab, "")
        self.classificationTab = QtWidgets.QWidget()
        self.classificationTab.setObjectName("classificationTab")
        self.tabWidget.addTab(self.classificationTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plotButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.plotButton.setObjectName("plotButton")
        self.horizontalLayout.addWidget(self.plotButton)
        self.clearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.settingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout.addWidget(self.settingsButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport_Fault_Data = QtWidgets.QMenu(self.menuFile)
        self.menuImport_Fault_Data.setObjectName("menuImport_Fault_Data")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionImport_Plane_Data_DD = QtWidgets.QAction(MainWindow)
        self.actionImport_Plane_Data_DD.setObjectName("actionImport_Plane_Data_DD")
        self.actionImport_Plane_Data_Dir = QtWidgets.QAction(MainWindow)
        self.actionImport_Plane_Data_Dir.setObjectName("actionImport_Plane_Data_Dir")
        self.actionImport_Line_Data_Trend = QtWidgets.QAction(MainWindow)
        self.actionImport_Line_Data_Trend.setObjectName("actionImport_Line_Data_Trend")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionEqual_Area = QtWidgets.QAction(MainWindow)
        self.actionEqual_Area.setCheckable(True)
        self.actionEqual_Area.setChecked(True)
        self.actionEqual_Area.setObjectName("actionEqual_Area")
        self.actionEqual_Angle = QtWidgets.QAction(MainWindow)
        self.actionEqual_Angle.setCheckable(True)
        self.actionEqual_Angle.setObjectName("actionEqual_Angle")
        self.actionMerge_Data = QtWidgets.QAction(MainWindow)
        self.actionMerge_Data.setObjectName("actionMerge_Data")
        self.actionRotate_Data = QtWidgets.QAction(MainWindow)
        self.actionRotate_Data.setObjectName("actionRotate_Data")
        self.actionSave_as_Packed_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_as_Packed_Project.setObjectName("actionSave_as_Packed_Project")
        self.actionBla = QtWidgets.QAction(MainWindow)
        self.actionBla.setObjectName("actionBla")
        self.actionBlabla = QtWidgets.QAction(MainWindow)
        self.actionBlabla.setObjectName("actionBlabla")
        self.actionReopen_Last_File = QtWidgets.QAction(MainWindow)
        self.actionReopen_Last_File.setObjectName("actionReopen_Last_File")
        self.actionUnpack_Project_to = QtWidgets.QAction(MainWindow)
        self.actionUnpack_Project_to.setObjectName("actionUnpack_Project_to")
        self.actionPlot_on_Apply = QtWidgets.QAction(MainWindow)
        self.actionPlot_on_Apply.setCheckable(True)
        self.actionPlot_on_Apply.setChecked(True)
        self.actionPlot_on_Apply.setObjectName("actionPlot_on_Apply")
        self.actionImport_Circular_Data_Trend = QtWidgets.QAction(MainWindow)
        self.actionImport_Circular_Data_Trend.setObjectName("actionImport_Circular_Data_Trend")
        self.actionImport_Fault_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Fault_Data.setObjectName("actionImport_Fault_Data")
        self.actionPlot_on_Accept = QtWidgets.QAction(MainWindow)
        self.actionPlot_on_Accept.setCheckable(True)
        self.actionPlot_on_Accept.setChecked(True)
        self.actionPlot_on_Accept.setObjectName("actionPlot_on_Accept")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionImport_Small_Circle_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Small_Circle_Data.setObjectName("actionImport_Small_Circle_Data")
        self.actionConvert_Shapefile_to_Azimuth_data = QtWidgets.QAction(MainWindow)
        self.actionConvert_Shapefile_to_Azimuth_data.setObjectName("actionConvert_Shapefile_to_Azimuth_data")
        self.actionConvert_Mesh_to_Plane_Data = QtWidgets.QAction(MainWindow)
        self.actionConvert_Mesh_to_Plane_Data.setObjectName("actionConvert_Mesh_to_Plane_Data")
        self.actionSubmit_Issue = QtWidgets.QAction(MainWindow)
        self.actionSubmit_Issue.setObjectName("actionSubmit_Issue")
        self.actionPlot_on_Update_Table = QtWidgets.QAction(MainWindow)
        self.actionPlot_on_Update_Table.setCheckable(True)
        self.actionPlot_on_Update_Table.setChecked(True)
        self.actionPlot_on_Update_Table.setObjectName("actionPlot_on_Update_Table")
        self.actionAdd_Plane = QtWidgets.QAction(MainWindow)
        self.actionAdd_Plane.setObjectName("actionAdd_Plane")
        self.actionAdd_Line = QtWidgets.QAction(MainWindow)
        self.actionAdd_Line.setObjectName("actionAdd_Line")
        self.actionAdd_Small_Circle = QtWidgets.QAction(MainWindow)
        self.actionAdd_Small_Circle.setObjectName("actionAdd_Small_Circle")
        self.actionAdd_Slope = QtWidgets.QAction(MainWindow)
        self.actionAdd_Slope.setObjectName("actionAdd_Slope")
        self.actionAssemble_Fault = QtWidgets.QAction(MainWindow)
        self.actionAssemble_Fault.setObjectName("actionAssemble_Fault")
        self.actionChange_Language = QtWidgets.QAction(MainWindow)
        self.actionChange_Language.setObjectName("actionChange_Language")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionRecent_Projects = QtWidgets.QAction(MainWindow)
        self.actionRecent_Projects.setObjectName("actionRecent_Projects")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionCalculate_difference_vectors = QtWidgets.QAction(MainWindow)
        self.actionCalculate_difference_vectors.setObjectName("actionCalculate_difference_vectors")
        self.actionOpen_fault_data_Plane_Line_Sense = QtWidgets.QAction(MainWindow)
        self.actionOpen_fault_data_Plane_Line_Sense.setObjectName("actionOpen_fault_data_Plane_Line_Sense")
        self.actionOpen_TectonicsFP_Fault_Data = QtWidgets.QAction(MainWindow)
        self.actionOpen_TectonicsFP_Fault_Data.setObjectName("actionOpen_TectonicsFP_Fault_Data")
        self.actionOpen_T_TECTO_Fault_Data = QtWidgets.QAction(MainWindow)
        self.actionOpen_T_TECTO_Fault_Data.setObjectName("actionOpen_T_TECTO_Fault_Data")
        self.actionAdd_Arc = QtWidgets.QAction(MainWindow)
        self.actionAdd_Arc.setObjectName("actionAdd_Arc")
        self.actionRotate_on_Drag = QtWidgets.QAction(MainWindow)
        self.actionRotate_on_Drag.setCheckable(True)
        self.actionRotate_on_Drag.setObjectName("actionRotate_on_Drag")
        self.actionOpen_fault_data_PlaneDir_Line_Sense = QtWidgets.QAction(MainWindow)
        self.actionOpen_fault_data_PlaneDir_Line_Sense.setObjectName("actionOpen_fault_data_PlaneDir_Line_Sense")
        self.actionAdd_Group = QtWidgets.QAction(MainWindow)
        self.actionAdd_Group.setObjectName("actionAdd_Group")
        self.actionConvert_Shapefile_to_Azimuth_Data_UTM = QtWidgets.QAction(MainWindow)
        self.actionConvert_Shapefile_to_Azimuth_Data_UTM.setObjectName("actionConvert_Shapefile_to_Azimuth_Data_UTM")
        self.menuImport_Fault_Data.addAction(self.actionOpen_fault_data_Plane_Line_Sense)
        self.menuImport_Fault_Data.addAction(self.actionOpen_fault_data_PlaneDir_Line_Sense)
        self.menuImport_Fault_Data.addAction(self.actionOpen_TectonicsFP_Fault_Data)
        self.menuImport_Fault_Data.addAction(self.actionOpen_T_TECTO_Fault_Data)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_as_Packed_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Plane_Data_DD)
        self.menuFile.addAction(self.actionImport_Plane_Data_Dir)
        self.menuFile.addAction(self.actionImport_Line_Data_Trend)
        self.menuFile.addAction(self.actionImport_Small_Circle_Data)
        self.menuFile.addAction(self.actionImport_Circular_Data_Trend)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.menuImport_Fault_Data.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionPlot_on_Apply)
        self.menuSettings.addAction(self.actionPlot_on_Accept)
        self.menuSettings.addAction(self.actionPlot_on_Update_Table)
        self.menuSettings.addAction(self.actionRotate_on_Drag)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionChange_Language)
        self.menuTools.addAction(self.actionUnpack_Project_to)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionMerge_Data)
        self.menuTools.addAction(self.actionRotate_Data)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionConvert_Shapefile_to_Azimuth_data)
        self.menuTools.addAction(self.actionConvert_Shapefile_to_Azimuth_Data_UTM)
        self.menuTools.addAction(self.actionConvert_Mesh_to_Plane_Data)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionCalculate_difference_vectors)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionSubmit_Issue)
        self.menuData.addAction(self.actionAdd_Plane)
        self.menuData.addAction(self.actionAdd_Line)
        self.menuData.addAction(self.actionAdd_Small_Circle)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionAdd_Slope)
        self.menuData.addAction(self.actionAdd_Arc)
        self.menuData.addAction(self.actionAssemble_Fault)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionAdd_Group)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenStereo - Open-source, Multiplatform Stereonet Analysis"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.projectionTab), _translate("MainWindow", "Projection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.roseTab), _translate("MainWindow", "Rose diagram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.classificationTab), _translate("MainWindow", "Classification"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImport_Fault_Data.setTitle(_translate("MainWindow", "Import Fault Data"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionImport_Plane_Data_DD.setText(_translate("MainWindow", "Import Plane Data (DD)"))
        self.actionImport_Plane_Data_Dir.setText(_translate("MainWindow", "Import Plane Data (Dir)"))
        self.actionImport_Line_Data_Trend.setText(_translate("MainWindow", "Import Line Data (Trend)"))
        self.actionImport.setText(_translate("MainWindow", "Import..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSettings.setText(_translate("MainWindow", "Project Settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionEqual_Area.setText(_translate("MainWindow", "Equal Area"))
        self.actionEqual_Angle.setText(_translate("MainWindow", "Equal Angle"))
        self.actionMerge_Data.setText(_translate("MainWindow", "Merge Data"))
        self.actionRotate_Data.setText(_translate("MainWindow", "Rotate Data"))
        self.actionSave_as_Packed_Project.setText(_translate("MainWindow", "Save as Packed Project..."))
        self.actionBla.setText(_translate("MainWindow", "Reopen Last File"))
        self.actionBlabla.setText(_translate("MainWindow", "blabla"))
        self.actionReopen_Last_File.setText(_translate("MainWindow", "Reopen Last File"))
        self.actionUnpack_Project_to.setText(_translate("MainWindow", "Unpack Project to..."))
        self.actionPlot_on_Apply.setText(_translate("MainWindow", "Plot on Apply"))
        self.actionImport_Circular_Data_Trend.setText(_translate("MainWindow", "Import Azimuth Data"))
        self.actionImport_Fault_Data.setText(_translate("MainWindow", "Import Fault Data"))
        self.actionPlot_on_Accept.setText(_translate("MainWindow", "Plot on Accept"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionImport_Small_Circle_Data.setText(_translate("MainWindow", "Import Small Circle Data"))
        self.actionConvert_Shapefile_to_Azimuth_data.setText(_translate("MainWindow", "Convert Shapefile to Azimuth Data (geographic)"))
        self.actionConvert_Mesh_to_Plane_Data.setText(_translate("MainWindow", "Convert Mesh to Plane Data"))
        self.actionSubmit_Issue.setText(_translate("MainWindow", "Submit Issue"))
        self.actionPlot_on_Update_Table.setText(_translate("MainWindow", "Plot on Update Table"))
        self.actionAdd_Plane.setText(_translate("MainWindow", "Add Plane"))
        self.actionAdd_Line.setText(_translate("MainWindow", "Add Line"))
        self.actionAdd_Small_Circle.setText(_translate("MainWindow", "Add Small Circle"))
        self.actionAdd_Slope.setText(_translate("MainWindow", "Add Slope"))
        self.actionAssemble_Fault.setText(_translate("MainWindow", "Assemble Fault"))
        self.actionChange_Language.setText(_translate("MainWindow", "Change Language"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionRecent_Projects.setText(_translate("MainWindow", "Recent Projects"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
        self.actionCalculate_difference_vectors.setText(_translate("MainWindow", "Calculate difference vectors"))
        self.actionOpen_fault_data_Plane_Line_Sense.setText(_translate("MainWindow", "Open fault data (Dipdir/Dip // Trend/Plunge // Sense)"))
        self.actionOpen_TectonicsFP_Fault_Data.setText(_translate("MainWindow", "Open TectonicsFP Fault Data"))
        self.actionOpen_T_TECTO_Fault_Data.setText(_translate("MainWindow", "Open T-TECTO Fault Data"))
        self.actionAdd_Arc.setText(_translate("MainWindow", "Add Arc"))
        self.actionRotate_on_Drag.setText(_translate("MainWindow", "Rotate on Drag"))
        self.actionOpen_fault_data_PlaneDir_Line_Sense.setText(_translate("MainWindow", "Open fault data (Dir/Dip // Trend/Plunge // Sense)"))
        self.actionAdd_Group.setText(_translate("MainWindow", "Add Group"))
        self.actionConvert_Shapefile_to_Azimuth_Data_UTM.setText(_translate("MainWindow", "Convert Shapefile to Azimuth Data (UTM)"))

