from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem, QHeaderView

import mainFolder as func


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.firstLayout = QtWidgets.QVBoxLayout()
        self.firstLayout.setObjectName("firstLayout")
        self.dbComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dbComboBox.setObjectName("dbComboBox")
        self.firstLayout.addWidget(self.dbComboBox)
        self.listTables = QtWidgets.QListWidget(self.centralwidget)
        self.listTables.setObjectName("listTables")
        self.firstLayout.addWidget(self.listTables)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.firstLayout)
        self.secondLoyout = QtWidgets.QHBoxLayout()
        self.secondLoyout.setObjectName("secondLoyout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.secondLoyout.addWidget(self.table)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.secondLoyout)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.labelForRoot = QtWidgets.QLabel(self.centralwidget)
        self.labelForRoot.setObjectName("labelForRoot")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelForRoot)
        self.downloadButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.downloadButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 22))
        self.menubar.setObjectName("menubar")
        self.menuActionsConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuActionsConfiguration.setObjectName('MenuConfiguration')
        self.actionAnnother_Connect = QtWidgets.QAction(MainWindow)
        self.actionAnnother_Connect.setObjectName("actionAnnother_Connect")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.makeChangesInSelectedDatabase = QtWidgets.QAction(MainWindow)
        self.makeChangesInSelectedDatabase.setObjectName("makeChangesInSelectedDatabase")
        self.actionAdd_database = QtWidgets.QAction(MainWindow)
        self.actionAdd_database.setObjectName("actionAdd_database")
        self.actionAdd_table = QtWidgets.QAction(MainWindow)
        self.actionAdd_table.setObjectName("actionAdd_table")
        self.actionAdd_Row = QtWidgets.QAction(MainWindow)
        self.actionAdd_Row.setObjectName("actionAdd_Row")
        self.actionRemove_Row = QtWidgets.QAction(MainWindow)
        self.actionRemove_Row.setObjectName("actionRemove_Row")
        self.actionDatabase_info_change = QtWidgets.QAction(MainWindow)
        self.actionDatabase_info_change.setObjectName("actionDatabase_info_change")
        self.actionchange_configuration = QtWidgets.QAction(MainWindow)
        self.actionchange_configuration.setObjectName("actionchange_configuration")
        self.actionDelete_selected_database = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected_database.setObjectName("actionDelete_selected_database")
        self.actionDelete_selected_table = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected_table.setObjectName("actionDelete_selected_table")
        self.menuActions.addAction(self.actionAdd_Row)
        self.menuActions.addAction(self.actionAdd_table)
        self.menuActions.addAction(self.actionAdd_database)
        self.menuActions.addAction(self.actionRemove_Row)
        self.menuActions.addAction(self.actionDelete_selected_table)
        self.menuActions.addAction(self.actionDelete_selected_database)
        self.menuActions.addAction(self.makeChangesInSelectedDatabase)
        self.menuActionsConfiguration.addAction(self.actionAnnother_Connect)
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuActionsConfiguration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.downloadButton.clicked.connect(lambda: func.download.downloadAction(self))
        self.dbComboBox.activated.connect(lambda: func.listTables_Actions.updateListTables(self))
        self.listTables.activated.connect(lambda: func.table_Actions.fillTable(self))
        self.actionAdd_database.triggered.connect(lambda: func.add_Database.createDatabase(self))
        self.password.textChanged.connect(lambda: func.help_Methods.passwordChange(self))
        self.table.itemChanged.connect(lambda: func.table_Actions.doChangesInTable(self))
        self.actionAdd_Row.triggered.connect(lambda: func.row_Actions.addRow_To_Table(self))
        self.actionRemove_Row.triggered.connect(lambda: func.row_Actions.remove_Selected_Row(self))
        self.actionAdd_table.triggered.connect(lambda: func.create_Table.createTableForm(self))
        self.actionDelete_selected_database.triggered.connect(lambda: func.delete_Table_Database.deleteDatabase(self))
        self.actionDelete_selected_table.triggered.connect(lambda: func.delete_Table_Database.deleteTable(self))
        self.actionAnnother_Connect.triggered.connect(lambda: func.change_connection_configuration.openConfWindow(self))
        self.makeChangesInSelectedDatabase.triggered.connect(lambda: func.change_TableName_ColumnName.makeChangesInSelectedDbForm(self))

        self.menuActions.setDisabled(True)
        self.downloadButton.setEnabled(False)
        self.actionAdd_Row.setEnabled(False)

        self.menuActions.setStyleSheet('background-color: #ADD8E6;')
        self.menuActionsConfiguration.setStyleSheet('background-color: #ADD8E6;')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelForRoot.setText(_translate("MainWindow", "Password for root"))
        self.downloadButton.setText(_translate("MainWindow", "Download mysql or check if download"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionAdd_database.setText(_translate("MainWindow", "CREATE DATABASE"))
        self.actionAdd_table.setText(_translate("MainWindow", "CREATE TABLE"))
        self.actionAdd_Row.setText(_translate("MainWindow", "ADD ROW"))
        self.actionRemove_Row.setText(_translate("MainWindow", "DELETE SELECTED ROW"))
        self.actionDelete_selected_database.setText(_translate("MainWindow", "DELETE SELECTED DATABASE"))
        self.actionDelete_selected_table.setText(_translate("MainWindow", "DELETE SELECTED TABLE"))
        self.actionAnnother_Connect.setText(_translate('MainWindow', 'Change connect configuration or connect without '
                                                                     'check download'))
        self.menuActionsConfiguration.setTitle(_translate('MainWindow', 'Configuration'))
        self.password.setPlaceholderText('Write root password here...')
        self.makeChangesInSelectedDatabase.setText(_translate('MainWindow', 'CHANGE DB NAME, TABLE, COLUMNS'))
        self.setWindowTitle('MySqlManager')
