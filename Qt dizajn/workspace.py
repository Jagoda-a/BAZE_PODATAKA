from PySide2 import QtWidgets, QtGui, QtCore
from student import Student
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet
from student_model import StudentModel
from polozeni_predmet_model import PolozeniPredmetModel
from nepolozeni_predmet_model import NepolozeniPredmetModel

import json
import csv

##TODO:

class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        # self.main_text = QtWidgets.QTextEdit()# *Djape file*
        # self.main_layout.addWidget(self.main_text)

        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) #Obelezava klikom ceo red
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.student_model = self.create_dummy_model()
        self.table1.setModel(self.student_model)

        self.table1.clicked.connect(self.student_selected)
        self.table1.clicked.connect(self.show_tabs) #veza za metodu show_tabs 

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)
    
    def student_selected(self, index):
        model = self.table1.model()
        selected_student = model.get_element(index)

        polozeni_predmeti_model = PolozeniPredmetModel()
        polozeni_predmeti_model.polozeni_predmeti = selected_student.polozeni_predmeti

        nepolozeni_predmeti_model = NepolozeniPredmetModel()
        nepolozeni_predmeti_model.nepolozeni_predmeti = selected_student.nepolozeni_predmeti

        self.subtable1.setModel(polozeni_predmeti_model)
        self.subtable2.setModel(nepolozeni_predmeti_model)

    def show_tabs(self):
        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("picture/tabela.png"), "Polozeni predmeti")

        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("picture/tabela.png"), "Nepolozeni predmeti")

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


    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    #funckija koja cita podatke iz csv filea i dodaje if u Student Model

    # def show_text(self, text): # * Djape file*
    #     self.main_text.setText(text)

    # def create_dummy_model(self):
    #     student_model = StudentModel()

    #     with open("student_data.csv", "r") as read_obj:
    #         csv_reader = csv.reader(read_obj)
    #         list_of_rows = list(csv_reader)
    #         for i in range(0, len(list_of_rows)):
    #             student_model.students.append(Student(list_of_rows[i][0], list_of_rows[i][1]))
    #     return student_model


    #funkcija koja deserializuje json filea i dodaje podatke u student mode objekat
    def create_dummy_model(self):
        student_model = StudentModel()

        with open("student_metadata.json", "r") as read_file:
            data = json.load(read_file)

        for x in data['student']:
            polozeni_ispiti = []
            nepolozeni_ispiti = []
            for y in x['polozeni_predmeti']:
                polozeni_ispiti.append(PolozeniPredmet(y['naziv'],"", y['ocena']))
            for y in x['nepolozeni_predmeti']:
                nepolozeni_ispiti.append(NepolozeniPredmet(y['naziv'],"", y['broj_polaganja']))

            student_model.students.append(
                Student(x['broj_indeksa'], x['ime_prezime'], polozeni_ispiti, nepolozeni_ispiti))
        return student_model


    