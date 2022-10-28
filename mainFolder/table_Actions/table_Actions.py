import mainFolder as func
from PyQt5.QtWidgets import QTableWidgetItem


def fillTable(self):
    self.actionAdd_Row.setEnabled(True)

    db = func.help_Methods.makeConnectWithDB(self)

    cursor = db.cursor()

    cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

    count_of_columns = 0
    for column in cursor:
        count_of_columns += 1

    self.table.setColumnCount(count_of_columns)

    cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

    column_id = 0
    for column in cursor:
        self.table.setHorizontalHeaderItem(column_id, QTableWidgetItem(column[0]))
        column_id += 1

    cursor.execute('SELECT COUNT(*) FROM {0}'.format(self.listTables.currentItem().text()))

    row_of_count = cursor.fetchall()
    self.table.setRowCount(row_of_count[0][0])

    cursor.execute('SELECT * FROM {0}'.format(self.listTables.currentItem().text()))

    items_count = 0
    for items in cursor:
        print(items)
        columns_index = 0
        for item in items:
            self.table.setItem(items_count, columns_index, QTableWidgetItem(str(item)))
            columns_index += 1
        items_count += 1


def doChangesInTable(self):
    if self.table.currentItem() is not None:
        db = func.help_Methods.makeConnectWithDB(self)

        cursor = db.cursor(buffered=True)

        cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

        column_to_change = ''

        column_id = 0
        for column in cursor:
            if self.table.currentColumn() is column_id:
                column_to_change = column[0]
                break

            column_id += 1

        cursor.execute('SELECT * FROM {0}'.format(self.listTables.currentItem().text()))

        change_value = ''
        change_value_All = []

        row_id = 0
        arrayValues = []
        for item in cursor:
            if row_id is self.table.currentRow():
                change_value = item[self.table.currentColumn()]
                change_value_All = item
            arrayValues.append(item)
            row_id += 1

        if str(change_value) == str(self.table.currentItem().text()):
            return None

        if arrayValues.count(change_value_All) > 1:
            func.warnings.messageWarningShow(
                'Unexpected update count received (Actual: {0} Expected: 1). All changes will be rolled back.'
                .format(arrayValues.count(change_value_All)))

            func.help_Methods.reFillTable(self)
            return

        cursor.execute(
            'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
            'from information_schema.columns  where table_schema = \'{0}\' and `table_name` = \'{1}\';'
            .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

        print(
            'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
            'from information_schema.columns  where table_schema = \'{0}\' and `table_name` = \'{1}\';'
            .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

        havePrimaryKey = False
        columnNamePrimary = ''
        for item in cursor:
            if str(item[1]) == 'Primary':
                havePrimaryKey = True
                columnNamePrimary = str(item[0])

        if havePrimaryKey:
            numberOfPrimaryColumn = 0
            headercount = self.table.columnCount()
            for x in range(headercount):
                columnName = self.table.horizontalHeaderItem(x).text()
                if columnNamePrimary == columnName:
                    numberOfPrimaryColumn = x

            if numberOfPrimaryColumn != self.table.currentColumn():
                change_value = self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()
        else:
            cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

            change_value = ''
            counter = 0
            for item in cursor:

                if counter == self.table.columnCount() - 1:
                    change_value += '{0} = \'{1}\''.format(item[0],
                                                           self.table.item(self.table.currentRow(),
                                                                           counter).text() if item[
                                                                                                  0] != column_to_change else
                                                           change_value_All[self.table.currentColumn()])
                else:
                    change_value += '{0} = \'{1}\' AND '.format(item[0],
                                                                self.table.item(self.table.currentRow(),
                                                                                counter).text() if item[
                                                                                                       0] != column_to_change else
                                                                change_value_All[self.table.currentColumn()])
                counter += 1

        try:
            if not havePrimaryKey:
                query = 'UPDATE {0} SET {1} = \'{2}\' WHERE {3};'.format(
                    self.listTables.currentItem().text(),
                    str(column_to_change),
                    self.table.currentItem().text(),
                    str(change_value))
                print(query)
                cursor.execute(query)
            else:
                query = 'UPDATE {0} SET {1} = \'{2}\' WHERE {3} = \'{4}\';'.format(
                    self.listTables.currentItem().text(),
                    str(column_to_change),
                    self.table.currentItem().text(),
                    str(columnNamePrimary),
                    str(change_value))
                print(query)
                cursor.execute(query)
        except Exception as e:
            func.warnings.messageWarningShow(str(e))
            func.help_Methods.reFillTable(self)

        db.commit()

        self.table.setCurrentItem(None)
