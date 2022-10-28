import mainFolder as func


def createDatabase(self):
    self.newForm = func.add_Database_Design.Ui_AddDatabase()
    self.newForm.setupUi(self)
    self.setWindowTitle('MySqlManager')
    self.newForm.infoAboutEdit.setText('Enter a name for database')
    self.newForm.saveButton.clicked.connect(lambda: createDbAndGoBack(self))
    self.newForm.backButton.clicked.connect(lambda: func.help_Methods.justGoBack(self))


def createDbAndGoBack(self):
    db = func.help_Methods.makeConnect(self)
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE {0}'.format(str(self.newForm.inputEdit.text())))
    self.setupUi(self)
    func.comboBox_actions.connectAndFillComboBox(self)

    func.help_Methods.hideRootInput(self)
