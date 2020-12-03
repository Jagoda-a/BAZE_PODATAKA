import sys
from PySide2 import QtWidgets, QtGui, QtCore
from main_window import MainWindow

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    
    main_window=MainWindow()

    sys.exit(app.exec_())

