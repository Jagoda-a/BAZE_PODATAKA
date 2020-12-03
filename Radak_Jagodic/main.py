import sys
from PySide2 import QtWidgets, QtGui
from PySide2 import QtWidgets, QtGui, QtCore
from strukture_dock import StructureDock
from workspace import WorkspaceWidget

'""Brisanje taba u app'''
def delete_tab(index):
    central_widget.removeTab(index)

''' Metoda dza ocitavanje fajla structura *Djape file* '''
def read_file(index):
    path = structure_dock.model.filePath(index)
    with open(path) as f:
        text = (f.read())
        new_workspace = WorkspaceWidget(central_widget)
        central_widget.addTab(new_workspace, path.split("/")[-1])
        new_workspace.show_text(text)

#TODO: Proveravaj kod!

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(700, 500)
    # Izgled prozora
    main_window.setWindowTitle("Editor generickih podataka")
    icon = QtGui.QIcon("picture/icons8-edit-file-64.png")
    main_window.setWindowIcon(icon)

    #Meni bar
    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File",menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)
    open_menu = QtWidgets.QMenu("Open", menu_bar)

    #Icon for menuAction
    fileIcon = QtGui.QIcon("picture/icons8-edit-file-64.png")
    file_menu.addAction(fileIcon, "New file") # Akcija menija
    fileIcon = QtGui.QIcon("picture/print.png")
    file_menu.addAction(fileIcon, "Print") # Akcija menija
    file_menu.setToolTip("Open")
    editIcon = QtGui.QIcon("picture/textedit.png")
    edit_menu.addAction(editIcon, "Settings")# Akcija menija
    edit_menu.setToolTip("Open")
    viewIcon = QtGui.QIcon("picture/diplay.png")
    view_menu.addAction(viewIcon, "Window") # Akcija menija


    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)
    menu_bar.addMenu(open_menu)

    tool_bar = QtWidgets.QToolBar(main_window)


    central_widget = QtWidgets.QTabWidget(main_window)
    text_edit = QtWidgets.QTextEdit(central_widget)
    central_widget.addTab(text_edit, QtGui.QIcon("picture/textedit.png"), "Tekstualni editor")
    # workspace = WorkspaceWidget(central_widget)
    # central_widget.addTab(workspace,QtGui.QIcon("picture/tabela.png"), "Prikaz tabele")
    central_widget.tabCloseRequested.connect(delete_tab) #Brisanje taba
    
    # structure_dock = QtWidgets.QDockWidget("Strukture dokumenata", main_window)
    structure_dock = StructureDock("Strukture dokumenata", main_window)
    structure_dock.tree.clicked.connect(read_file) # *Djape file*
    
    # Akcija za strukture
    toggle_structure_dock_action = structure_dock.toggleViewAction()
    view_menu.addAction(toggle_structure_dock_action)

    

    status_bar = QtWidgets.QStatusBar(main_window)
    status_bar.showMessage("Status bar je prikazan...")

    central_widget.setTabsClosable(True)

    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)
    main_window.setCentralWidget(central_widget)
    main_window.setStatusBar(status_bar)

    # Kraj
    main_window.show()
    # menu_bar.setParent(main_window)
    sys.exit(app.exec_())