import mainFolder as func
from PyQt5 import QtWidgets
import mysql.connector


def createTableForm(self):
    self.newForm = func.create_Table_design.Ui_createTable()
    self.newForm.setupUi(self)
    self.newForm.databaseName = self.dbComboBox.currentText()
    self.setWindowTitle('MySqlManager')

    self.newForm.go_Back.clicked.connect(lambda: func.help_Methods.justGoBack(self))
    self.newForm.addColumn.clicked.connect(lambda: addColumnToNewTable(self))
    self.newForm.deleteColumn.clicked.connect(lambda: deleteColumn(self))
    self.newForm.create_Table.clicked.connect(lambda: createTable(self))


def createTable(self):
    if len(self.newForm.array) == 0:
        func.warnings.messageWarningShow('Table can not have 0 columns')
        return

    if self.newForm.tableName.text() == '':
        func.warnings.messageWarningShow('Table name can not be empty')
        return

    AllColumnsArray = []
    columnArray = []
    counterForArraysColumns = 0

    for item in self.newForm.array:
        if isinstance(item, QtWidgets.QLineEdit):
            columnArray.append('param' if item.text() == '' else item.text())
            print('param' if item.text() == '' else item.text())
            if item.placeholderText() == 'Column name':
                if item.text() == '':
                    func.warnings.messageWarningShow('Column name can not be empty')
                    return

        if isinstance(item, QtWidgets.QComboBox):
            columnArray.append(item.currentText())
            print(item.currentText())

        counterForArraysColumns += 1
        print(counterForArraysColumns)
        if counterForArraysColumns % 5 == 0 and counterForArraysColumns > 4:
            print(columnArray)
            AllColumnsArray.append(columnArray.copy())
            columnArray.clear()

    print(AllColumnsArray)

    print(self.newForm.databaseName)

    db = mysql.connector.connect(
        host=self.ipDb,
        user=self.userDb,
        password=self.passwordDb,
        database=self.newForm.databaseName
    )

    cursor = db.cursor()

    createString = ''

    try:
        for array in AllColumnsArray:
            if array[1].__contains__('varchar'):
                if array[3] != 'param' and array[3].isnumeric():
                    array[1] = array[1].replace('30', array[3])

            if array[1].__contains__('int'):
                array[3] = ''

            createString += '{0} {1}'.format(array[0], array[1])

            if array[2] == 'Primary key auto_increment':
                createString += ' primary key auto_increment'

            if array[2] == 'Primary key':
                createString += ' primary key'

            createString += ', '

        print('CREATE TABLE {0} ({1});'.format(self.newForm.tableName.text(), createString[:-2]))
        cursor.execute('CREATE TABLE {0} ({1});'.format(self.newForm.tableName.text(), createString[:-2]))

        func.help_Methods.justGoBack(self)
    except Exception as e:
        func.warnings.messageWarningShow(str(e))


def addColumnToNewTable(self):
    columnName = QtWidgets.QLineEdit(self.newForm.scrollAreaWidgetContents)
    columnName.setPlaceholderText('Column name')

    type_of_column = QtWidgets.QComboBox(self.newForm.scrollAreaWidgetContents)
    type_of_column.setEditable(True)
    type_of_column.addItem('varchar(30)')
    type_of_column.addItem('int')

    primary_key = QtWidgets.QComboBox(self.newForm.scrollAreaWidgetContents)
    primary_key.setEditable(True)
    primary_key.addItem('Not a primary key')
    primary_key.addItem('Primary key')
    primary_key.addItem('Primary key auto_increment')

    additionalText = QtWidgets.QLineEdit(self.newForm.scrollAreaWidgetContents)
    additionalText.setPlaceholderText('Parameters for example varchar( your param )')

    line = QtWidgets.QFrame(self.newForm.scrollAreaWidgetContents)
    line.setFrameShape(QtWidgets.QFrame.HLine)
    line.setFrameShadow(QtWidgets.QFrame.Sunken)

    self.newForm.tableLayout.addWidget(columnName)
    self.newForm.tableLayout.addWidget(type_of_column)
    self.newForm.tableLayout.addWidget(primary_key)
    self.newForm.tableLayout.addWidget(additionalText)
    self.newForm.tableLayout.addWidget(line)

    self.newForm.array.append(columnName)
    self.newForm.array.append(type_of_column)
    self.newForm.array.append(primary_key)
    self.newForm.array.append(additionalText)
    self.newForm.array.append(line)


def deleteColumn(self):
    count = len(self.newForm.array)

    if count == 0:
        return

    tempArray = []

    for itemId in range(count - 5, count):
        self.newForm.array.__getitem__(itemId).setParent(None)
        tempArray.append(self.newForm.array.__getitem__(itemId))

    for item in tempArray:
        self.newForm.array.remove(item)
