import mainFolder as func


def addRow_To_Table(self):
    db = func.help_Methods.makeConnectWithDB(self)

    cursor = db.cursor()

    cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

    columnValues = []
    insertValues = []

    for item in cursor:
        columnValues.append(item[0])
        if str(item[1]).__contains__('int') or str(item[1]).__contains__('bigint'):
            insertValues.append('0')
        elif str(item[1]).__contains__('varchar'):
            insertValues.append('\'\'')

    columnValuesStr = ''
    insertValuesStr = ''
    for item in range(0, len(columnValues)):
        if item == (len(columnValues) - 1):
            columnValuesStr += columnValues.__getitem__(item)
            insertValuesStr += insertValues.__getitem__(item)
            break

        columnValuesStr += columnValues.__getitem__(item) + ', '
        insertValuesStr += insertValues.__getitem__(item) + ', '

    try:
        cursor.execute('INSERT INTO {0} ({1}) VALUES ({2});'.format(self.listTables.currentItem().text(),
                                                                    columnValuesStr, insertValuesStr))

        print('INSERT INTO {0} ({1}) VALUES ({2})'.format(self.listTables.currentItem().text(),
                                                          columnValuesStr, insertValuesStr))

        db.commit()

        func.help_Methods.reFillTable(self)
    except Exception as e:
        func.warnings.messageWarningShow(str(e))
        func.help_Methods.reFillTable(self)


def remove_Selected_Row(self):
    if self.table.currentItem() is None:
        func.warnings.messageWarningShow('Row in not selected')
        return

    db = func.help_Methods.makeConnectWithDB(self)

    cursor = db.cursor()

    cursor.execute(
        'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
        'from information_schema.columns  where table_schema =\'{0}\' and `table_name` = \'{1}\';'
        .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

    print(
        'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
        'from information_schema.columns  where table_schema =\'{0}\' and `table_name` = \'{1}\';'
        .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

    havePrimaryKey = False
    columnNamePrimary = ''
    for item in cursor:
        print(item)
        if str(item[1]) == 'Primary':
            havePrimaryKey = True
            columnNamePrimary = str(item[0])

    try:
        if havePrimaryKey:
            numberOfPrimaryColumn = 0
            headercount = self.table.columnCount()
            for x in range(headercount):
                columnName = self.table.horizontalHeaderItem(x).text()
                if columnNamePrimary == columnName:
                    numberOfPrimaryColumn = x

            if numberOfPrimaryColumn != self.table.currentColumn():
                change_value = self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()
            print('{0} {1}'.format(columnNamePrimary,
                                   self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()))

            cursor.execute('DELETE FROM {0} WHERE {1} = {2};'
                           .format(self.listTables.currentItem().text(),
                                   columnNamePrimary,
                                   self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()))

            print('DELETE FROM {0} WHERE \'{1}\' = \'{2}\';'
                  .format(self.listTables.currentItem().text(),
                          columnNamePrimary,
                          self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()))
        else:
            cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

            namesOfColumns = ''
            counter = 0
            for item in cursor:
                print(item)
                print(self.table.item(self.table.currentRow(), counter).text())

                if counter == self.table.columnCount() - 1:
                    namesOfColumns += '{0} = \'{1}\';'.format(item[0],
                                                              self.table.item(self.table.currentRow(),
                                                                              counter).text())
                else:
                    namesOfColumns += '{0} = \'{1}\' AND '.format(item[0],
                                                                  self.table.item(self.table.currentRow(),
                                                                                  counter).text())
                counter += 1

            cursor.execute('SELECT * FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                                namesOfColumns))
            counter = 0
            for item in cursor:
                counter += 1

            if counter > 1:
                func.warnings.messageWarningShow(
                    'Unexpected update count received (Actual: {0} Expected: 1). All changes will be rolled back.'
                    .format(str(counter)))
                return

            cursor.execute('DELETE FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                              namesOfColumns))

            print('DELETE FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                     namesOfColumns))
    except Exception as e:
        func.warnings.messageWarningShow(str(e))
        func.help_Methods.reFillTable(self)

    db.commit()
    func.help_Methods.reFillTable(self)
