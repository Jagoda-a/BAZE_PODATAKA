from PySide2 import QtCore

class KupacModel(QtCore.QAbstractTableModel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.buyers = []

        #Pomocna metoda
    def get_element(self, index):
        return self.buyers[index.row()]

    def rowCount(self, index):
        return len(self.buyers)

    def columnCount(self, index):
        return 3

    def data(self, index, role = QtCore.Qt.DisplayRole):
        kupac = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return kupac.ime_prezime
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return kupac.adresa
        return None

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ime i prezime"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Adresa"
        return None

    #Metode za editTable model
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        kupac = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            kupac.ime_prezime = value
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            kupac.adresa = value
            return True
        return False


    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable
