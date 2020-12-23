import sys
from PySide2 import QtWidgets, QtGui, QtCore, QtPrintSupport
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from structure_dock import StructureDock
from workspace import WorkspaceWidget
from workspace import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window=QtWidgets.QMainWindow()
        self.main_window.setWindowTitle("RJP BASE")
        self.main_window.resize(880, 580)
        self.main_window.setWindowIcon(QIcon("RJP.png"))
        self.main_window.setStyleSheet('color:black')
        
        self.create_menu()

        self.main_window.show()
        

    def create_menu(self):
        self.menu_bar=QtWidgets.QMenuBar(self.main_window)

        #FILE MENU
        file_menu=QtWidgets.QMenu("File", self.menu_bar)
        self.menu_bar.addMenu(file_menu)

        new_action=QtWidgets.QAction(QIcon("./picture/new_file.png"), "New File", self)
        new_action.setShortcut('Ctrl+N')


        open_action=QtWidgets.QAction(QIcon("./picture/openfile.png"), "Open File", self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)

        open_folder=QtWidgets.QAction(QIcon("./picture/open.png"), "Open Folder", self)
        open_folder.setShortcut('Ctrl+K+O')

        save_action=QtWidgets.QAction(QIcon('./picture/save.png'), "Save", self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)

        print_action=QtWidgets.QAction(QIcon('./picture/pp.png'),"Print",self)
        print_action.setShortcut('Ctrl+P')
        print_action.triggered.connect(self.print_dialog)

        exit_action=QtWidgets.QAction(QIcon('./picture/xx.png'), "Exit", self)
        exit_action.triggered.connect(self.exit_app)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(open_folder)
        file_menu.addAction(save_action)
        file_menu.addAction(print_action)
        file_menu.addAction(exit_action)
        
        

        #EDIT MENU
        edit_menu=QtWidgets.QMenu('Edit',self.menu_bar)
        self.menu_bar.addMenu(edit_menu)

        undo_action=QtWidgets.QAction(QIcon('RJP.png'), "Undo", self)
        undo_action.setShortcut('Ctrl+Z')

        cut_action=QtWidgets.QAction(QIcon('RJP.png'),"Cut", self)
        cut_action.setShortcut('Ctrl+X')

        find_action=QtWidgets.QAction(QIcon('RJP.png'), "Find",self)
        find_action.setShortcut('Ctrl+F')

        copy_action=QtWidgets.QAction(QIcon('RJP.png'), "Copy",self)
        copy_action.setShortcut('Ctrl+C')

        paste_action=QtWidgets.QAction(QIcon('RJP.png'),"Paste", self)
        paste_action.setShortcut('Ctrl+V')
        
        edit_menu.addAction(undo_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(find_action)


        view_menu=QtWidgets.QMenu('View',self.menu_bar)
        self.menu_bar.addMenu(view_menu)

        window_menu=QtWidgets.QMenu('Window',self.menu_bar)
        self.menu_bar.addMenu(window_menu)

        help_menu=QtWidgets.QMenu('Help', self.menu_bar)
        self.menu_bar.addMenu(help_menu)

        self.main_window.setMenuBar(self.menu_bar)
        self.menu_bar.setStyleSheet('background-color:#222; color:white;')
        
        #STRUCTURE DOCK
        structure_dock=StructureDock("Strukture dokumenata", self.main_window)
        structure_dock.setStyleSheet("background-color:#222; color:white")

        #TOOLBAR
        self.toolbar=QtWidgets.QToolBar(self.main_window)
        self.main_window.addToolBar(self.toolbar)
        self.toolbar.addAction(new_action)
        self.toolbar.addAction(open_action)
        self.toolbar.addAction(save_action)
        self.toolbar.addAction(print_action)

        
        #CENTRALNI VIDZET
        
        central_widget=QtWidgets.QTabWidget(self.main_window)
        central_widget.setTabsClosable(True)

        def delete_tab(index):
            central_widget.removeTab(index)
        central_widget.tabCloseRequested.connect(delete_tab)
        
        #WORKSPACE
        workspace=WorkspaceWidget(central_widget)
        central_widget.addTab(workspace,QtGui.QIcon("picture/tabela.png"), "Prikaz tabele")
        central_widget.setStyleSheet("color:black")

        def read_file(index):
            path=structure_dock.model.filePath(index)
            with open(path) as f:
                text=(f.read())
                new_workspace=WorkspaceWidget(central_widget)
                central_widget.addTab(new_workspace, path.split("/")[-1])
                new_workspace.show_text(text)

        structure_dock.tree.clicked.connect(read_file)
        self.main_window.setCentralWidget(central_widget)
        self.main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)

    def save_file(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Save File", None, "PDF files (.pdf); All files")

        if fn != '':

            if QFileInfo(fn).suffix() == "": fn += '.pdf'

            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
        self.workspace.document().print_(self.printer)
    
    def print_dialog(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)

        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def exit_app(self):
        self.main_window.close()

    def open_file(self):
            path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load File"), self.tr("~/Desktop/"), self.tr("PDF (.pdf)"))

            self.file_viewer = self.FileViewer(path_to_file)
            self.file_viewer.show()

        

    