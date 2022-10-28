import mainFolder as func
from PyQt5.QtWidgets import QListWidgetItem


def connectAndFillComboBox(self):
    self.dbComboBox.clear()
    self.listTables.clear()
    self.table.setRowCount(0)
    self.table.setColumnCount(0)

    try:
        db = func.help_Methods.makeConnect(self)
    except Exception as e:
        func.warnings.messageWarningShow(str(e))
        return

    cursor = db.cursor()

    cursor.execute('SHOW DATABASES')

    for database_name in cursor:
        print(database_name)
        self.dbComboBox.addItem(database_name[0])

    mydbWithDb = func.help_Methods.makeConnectWithDB(self)

    cursor = mydbWithDb.cursor()

    cursor.execute('SHOW TABLES')

    for table_name in cursor:
        print(table_name)
        self.listTables.addItem(QListWidgetItem(table_name[0]))

    self.menuActions.setDisabled(False)
