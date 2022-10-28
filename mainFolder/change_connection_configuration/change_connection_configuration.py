import mainFolder as func
import mysql.connector


def openConfWindow(self):
    self.newForm = func.change_connection_configuration_design.Ui_MainWindow()
    self.newForm.setupUi(self)
    self.setWindowTitle('MySqlManager')

    try:
        if self.ipDb is not None:
            self.newForm.backButton.clicked.connect(lambda: func.help_Methods.justGoBack(self))
    except Exception as e:
        self.newForm.backButton.clicked.connect(lambda: self.setupUi(self))

    self.newForm.Apply.clicked.connect(lambda: checkNewConnection(self))


def checkNewConnection(self):
    try:
        db = mysql.connector.connect(
            host=self.newForm.hostDb.text(),
            user=self.newForm.userDb.text(),
            password=self.newForm.password.text(),
            port=self.newForm.portDb.text()
        )

    except Exception as e:
        func.warnings.messageWarningShow(str(e))
        return

    self.ipDb = self.newForm.hostDb.text()
    self.userDb = self.newForm.userDb.text()
    self.passwordDb = self.newForm.password.text()
    self.portDb = int(self.newForm.portDb.text())

    func.help_Methods.justGoBack(self)
