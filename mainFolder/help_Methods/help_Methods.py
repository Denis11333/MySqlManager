import mainFolder as func
import mysql.connector


def makeConnect(self):
    return mysql.connector.connect(
        host=self.ipDb,
        user=self.userDb,
        password=self.passwordDb,
        port=self.portDb
    )


def makeConnectWithDB(self):
    return mysql.connector.connect(
        host=self.ipDb,
        user=self.userDb,
        password=self.passwordDb,
        database=self.dbComboBox.currentText(),
        port=self.portDb
    )


def passwordChange(self):
    self.downloadButton.setEnabled(True)


def reFillTable(self):
    self.table.setRowCount(0)
    self.table.setColumnCount(0)
    func.table_Actions.fillTable(self)


def justGoBack(self):
    self.setupUi(self)
    func.comboBox_actions.connectAndFillComboBox(self)

    hideRootInput(self)


def hideRootInput(self):
    self.downloadButton.setParent(None)
    self.labelForRoot.setParent(None)
    self.password.setParent(None)
