import mainFolder as func


def deleteDatabase(self):
    db = func.help_Methods.makeConnect(self)

    cursor = db.cursor()

    try:
        cursor.execute('DROP DATABASE {0};'.format(self.dbComboBox.currentText()))
    except Exception as e:
        func.warnings.messageWarningShow(str(e))

    func.comboBox_actions.connectAndFillComboBox(self)


def deleteTable(self):
    if self.listTables.currentItem() is None:
        func.warnings.messageWarningShow('Table is not selected')
        return

    db = func.help_Methods.makeConnectWithDB(self)

    cursor = db.cursor()

    try:
        cursor.execute('DROP TABLE {0};'.format(self.listTables.currentItem().text()))
    except Exception as e:
        func.warnings.messageWarningShow(str(e))

    func.listTables_Actions.updateListTables(self)
    self.table.setRowCount(0)
    self.table.setColumnCount(0)
