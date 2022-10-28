import mainFolder as func
import os


def downloadAction(self):
    func.warnings.messageInfromationShow('Download started, press \'OK\' and wait while MySQL will downloaded...\n'
                                         '( make sure that the password is entered correctly )')

    text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()

    if text.__contains__('mysql'):
        func.warnings.messageInfromationShow('Mysql is installed')
    else:
        command = './mysql {0}'.format(self.password.text())
        os.system(command)

        text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()
        if not text.__contains__('mysql'):
            func.warnings.messageWarningShow('Install failed, try again with another password')
            return

        func.warnings.messageInfromationShow('Mysql is installed')

    self.ipDb = 'localhost'
    self.userDb = 'root'
    self.passwordDb = 'mysqlManagerPassword1_'
    self.portDb = 3306

    func.comboBox_actions.connectAndFillComboBox(self)

    self.passwordForRoot = self.password.text()
    func.help_Methods.hideRootInput(self)

