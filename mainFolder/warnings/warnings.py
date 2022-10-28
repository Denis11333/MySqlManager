from PyQt5.QtWidgets import QMessageBox


def messageInfromationShow(message):
    msg = QMessageBox()
    msg.setStyleSheet("background-color: #1E5162;")
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle('Information')
    msg.setText(message)
    msg.exec_()


def messageWarningShow(message):
    msg = QMessageBox()
    msg.setStyleSheet("background-color: #1E5162;")
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Warning')
    msg.setText(message)
    msg.exec_()
