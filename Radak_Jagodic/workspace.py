from PySide2 import QtWidgets, QtGui, QtCore
from kupac import Kupac
from porucena_roba import PorucenaRoba
from otkazana_roba import OtkazanaRoba
from kupac_model import KupacModel
from porucena_roba_model import PorucenaRobaModel
from otkazana_roba_model import OtkazanaRobaModel

class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        # self.main_text = QtWidgets.QTextEdit(self)
        # self.main_layout.addWidget(self.main_text)

        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.kupac_model = self.create_dummy_model()
        self.table1.setModel(self.kupac_model)

        self.table1.clicked.connect(self.kupac_selected)
        self.table1.clicked.connect(self.show_tabs) #veza za metodu show_tabs 

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)


    def kupac_selected(self, index):
        model = self.table1.model()
        selected_kupac = model.get_element(index)

        porucena_roba_model = PorucenaRobaModel()
        porucena_roba_model.poruceno= selected_kupac.porucena_roba

        otkazana_roba_model = OtkazanaRobaModel()
        otkazana_roba_model.otkazano = selected_kupac.otkazana_roba

        self.subtable1.setModel(porucena_roba_model)
        self.subtable2.setModel(otkazana_roba_model)
        
    def show_tabs(self):
        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("picture/tabela.png"), "Porucena roba")

        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("picture/tabela.png"), "Otkazana roba")

    def create_table(self, rows, columns):
        table_widget = QtWidgets.QTableWidget(rows, columns, self)

        for i in range(rows):
            for j in range(columns):
                table_widget.setItem(i, j, QtWidgets.QTableWidgetItem("Celija " + str(i) + str(j)))
        labels = []
        for i in range(columns):
            labels.append("Kolona" + str(i))
        table_widget.setHorizontalHeaderLabels(labels)
        return table_widget


    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)
        # self.show_tabs()

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    
    # def show_text(self, text):
    #     self.main_text.setText(text)

    def create_dummy_model(self):
        kupac_model = KupacModel()
        kupac_model.buyers = [
            Kupac("Predrag Radak", "Prvomajska 4, Pavlis", [
                PorucenaRoba("M.Majica", "M", 2000),
                PorucenaRoba("M.Jakna", "M", 17000)
            ],
            [
                OtkazanaRoba("Carape", "S", 2),
                OtkazanaRoba("M.Ves", "S", 1)
            ]),
            Kupac("Nikola Nikolic", "Partizanska 5, Valjevo", [
                PorucenaRoba("M.Duks", "XS", 7000),
                PorucenaRoba("M.Duks", "XS", 5000)
            ],
            [
                OtkazanaRoba("M.Trenerka", "L", 1),
                OtkazanaRoba("Jakna", "L", 2)
            ]),
            Kupac("Ivana Ivic", "Zarka Zrenjanina 1, Vrsac",  [
                PorucenaRoba("Carape", "M", 1300),
                PorucenaRoba("Kapa", "M", 1000)
            ],
            [
                OtkazanaRoba("Z.Haljina", "XL", 2),
                OtkazanaRoba("M.Majica", "XL", 2)
            ]),
            Kupac("Marta Maric", "Nemanjina 10, Kragujevac", [
                PorucenaRoba("Z.Bluza", "S", 2500),
                PorucenaRoba("Sorts", "S", 3000)
            ],
            [
                OtkazanaRoba("Z.Duks", "S", 2),
                OtkazanaRoba("Z.Jakna", "S", 1)
            ]),
            Kupac("Janko Janic", "Radakova 2, Pancevo", [
                PorucenaRoba("Dukser", "2XL", 6500),
                PorucenaRoba("M.Jakna", "2XL", 12000)
            ],
            [
                OtkazanaRoba("Patike", "L", 2),
                OtkazanaRoba("M.Majica", "L", 1)
            ]),
        ]
        return kupac_model

    