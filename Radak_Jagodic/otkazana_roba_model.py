from PySide2 import QtCore

class OtkazanaRobaModel(QtCore.QAbstractTableModel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.otkazano = []
        
    def get_element(self, index):
        return self.otkazano[index.row()]

    def rowCount(self, index):
        return len(self.otkazano)

    def columnCount(self, index):
        return 3

    
    def data(self, index, role = QtCore.Qt.DisplayRole):
        roba = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return roba.naziv
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return roba.velicina
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return roba.broj_felera
        return None

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Velicina"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj felera"
        return None

    #Metode za editTable model
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        roba = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            roba.naziv = value
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            roba.velicina = value
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            roba.broj_felera = value
            return True
        return False


    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable
