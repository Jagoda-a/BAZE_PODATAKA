import sys
from PySide2 import QtWidgets, QtGui, QtCore

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(640, 480)
    main_window.setWindowTitle('Editor Generickih Podataka')
    main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))
    
    #MENI BAR
    menu_bar=QtWidgets.QMenuBar(main_window)
    file_menu=QtWidgets.QMenu('File',menu_bar)
    menu_bar.addMenu(file_menu)
    edit_menu=QtWidgets.QMenu('Edit',menu_bar)
    menu_bar.addMenu(edit_menu)
    view_menu=QtWidgets.QMenu('View',menu_bar)
    menu_bar.addMenu(view_menu)
    help_menu=QtWidgets.QMenu('Help',menu_bar)
    menu_bar.addMenu(help_menu)

    #TOOLBAR
    tool_bar=QtWidgets.QToolBar(main_window)
    main_window.addToolBar(tool_bar)

    dock_widget=QtWidgets.QDockWidget('Dock Widget',main_window)

    #CENTRALNI VIDZET
    #central_widget=QtWidgets.QTextEdit(main_window)
    central_widget=QtWidgets.QWidget(main_window)
    central_widget.main_layout=QtWidgets.QVBoxLayout()
    central_widget.main_layout.addWidget(QtWidgets.QTextEdit(central_widget))
    central_widget.main_layout.addWidget(QtWidgets.QTextEdit(central_widget))
    central_widget.setLayout(central_widget.main_layout)
    main_window.setCentralWidget(central_widget)

    #dock_widget=QtWidgets.QDockQWidget('Dock Widget',main_window)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock_widget)

    #STATUS BAR
    status_bar=QtWidgets.QStatusBar(main_window)
    status_bar.showMessage('OVO JE STATUS BAR')
    main_window.setStatusBar(status_bar)


    
    main_window.setMenuBar(menu_bar)

    main_window.show()
    sys.exit(app.exec_())