from PySide2 import QtWidgets, QtGui, QtCore
from data_generator import GenerickiModel
from forma_box import InputFormaBox

class WorkspaceWidget(QtWidgets.QWidget):               #predstavlja deo u main_window-u, tj. kao neki nas centralni wgt
    def __init__(self, parent, model, models):          #cemu sluzi model?
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()


        self.tabela = QtWidgets.QTableView(self.tab_widget)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)   #kada kliknem i vucem (dok je kliknut) po tabeli
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)    #sta da selektuje kad se klikne na red
        self.tabela.setModel(model)                                                 # main salje odgovarajuci model
        self.models = models                                                        # pamtimo sve postojece modele
        self.button = QtWidgets.QPushButton("Dodaj u glavnu tabelu.")
        self.forma = InputFormaBox(self, model)
        self.button.clicked.connect(self.button_clicked)

        self.tabela.clicked.connect(self.row_selected)         #na klik tabele se emituje odredjena metoda, treba postaviti i za ostale tabele

        self.main_layout.addWidget(self.tabela)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.tab_widget)
        
        self.setLayout(self.main_layout)

    def row_selected(self, index):                          #kada se klikne na red u tabeli
        model = self.tabela.model()                         #model glavne tabele (u kojoj smo nesto kliknuli), genericki model, koji smo joj prosledili
        selektovani_red = model.get_element(index)
        for child in self.models:           # prodjemo kroz sve modele
            for parent in child.parents:    # i medju njihovim parent-ima (ako ih ima)
                if parent["name"] == model.name:         # nadjemo sebe (tako znamo da nam je child)
                    
                    podtabela_model = child
                    for i in range(len(model.primary_key)):
                        filter_proxy_model = QtCore.QSortFilterProxyModel()
                        filter_proxy_model.setSourceModel(podtabela_model)
                        filter_proxy_model.setFilterKeyColumn(parent["columns"][i])  # u parent["columns"] pise u koje od nasih kolona se preslikava primary key kolone iz roditelja
                        filter_proxy_model.setFilterRegularExpression(selektovani_red[model.primary_key[i]]) #prolazimo krozk olone koje sacinjavaju primary_key od parent-a 
                        podtabela_model = filter_proxy_model

                    podtabela = QtWidgets.QTableView(self.tab_widget)
                    podtabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  #kada kliknem i vucem (dok je kliknut) po tabeli
                    podtabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)   #sta da selektuje kad se klikne na red
                    podtabela.setModel(podtabela_model)                      # postavljamo model koji sadrzi podskup redova iz generickog modela
                    podtabela.clicked.connect(self.row_selected)         #TODO: mozda? treba dodati clicked i ovde ali treba definisati kako da se ponasa, jer ovaj za gornju tabelu ne radi dobro
                    self.tab_widget.addTab(podtabela, QtGui.QIcon("../picture/tabela"), child.name)
                    
                    break # predjemo na naredni child 

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
        #TODO: obezbediti da za svaki model postoji samo jedan otvoreni tab (da se ne duplira prilikom otvaranja)

    def button_clicked(self):
        self.forma.show()




