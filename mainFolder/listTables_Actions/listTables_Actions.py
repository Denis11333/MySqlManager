import mainFolder as func
from PyQt5.QtWidgets import QListWidgetItem


def updateListTables(self):
    self.listTables.clear()

    db = func.help_Methods.makeConnectWithDB(self)

    cursor = db.cursor()

    cursor.execute('SHOW TABLES')

    for table_name in cursor:
        print(table_name)
        self.listTables.addItem(QListWidgetItem(table_name[0]))
