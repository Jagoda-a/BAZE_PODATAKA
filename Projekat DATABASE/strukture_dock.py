from PySide2 import QtWidgets, QtCore

class StructureDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str) # Atribut klase

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())

        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QtCore.QDir.currentPath()))
        self.tree.clicked.connect(self.file_clicked)
        self.setWidget(self.tree)
        # self.kliknut = QtCore.Signal(str)

    def file_clicked(self, index):
        print(self.model.filePath(index))
        path = self.model.filePath(index)
        
        self.kliknut.emit(path)


