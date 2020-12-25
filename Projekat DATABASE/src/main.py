import sys
from PySide2 import QtWidgets, QtGui, QtCore
from strukture_dock import StructureDock
from workspace import WorkspaceWidget
from data_generator import GenerickiModel
import json

'""Brisanje taba u app'''
def delete_tab(index):
    central_widget.removeTab(index)

""'Otvaranje fajla Struck docka u terminalu""'
def open_file(index):
    path = structure_dock.model.filePath(index)
    with open(path) as f:
        # TODO: proveriti da li postoji otvoren tab za ovaj fajl, da ne otvara vise puta jedan isti fajl, nego samo prebaci fokus
        #   - proci kroz tabove->workspace->model->source   #nisam nasao kako da iterisem kroz tabove, tj. kako da vidim koji su sve tabovi tu
        #       - ako postoji tab u kojem model.source == file_name: prebacimo fokus na njega
        #       - u suprotnom: kreiramo novi workspace i tab (kao ispod) i prebacimo fokus na njega
        # text = f.read()
        model = None  # izaberemo odgovarajuci model u zavisnosti od naziva file-a
        file_name = path.split("/")[-1]
        for m in models:                        #kako on ovde dohvati models kada je models definisano skroz dole?
            if m.source == file_name:
                model = m
                break
        if(model is not None):
            new_workspace = WorkspaceWidget(central_widget, model, models)
            central_widget.addTab(new_workspace, QtGui.QIcon("../picture/images.png"), model.name)  #ovde setujemo ime novog taba, tj. splitujemo putanju i uzmemo poslednji element
            central_widget.setCurrentWidget(new_workspace)    #sa ovim smo promenili fokus na novootvoreni tab
        # new_workspace.show_text(text)
        # print(f.read())

''' Metoda dza ocitavanje fajla structura *Djape file* '''
# def read_file(index):
#     path = structure_dock.model.filePath(index)
#     with open(path) as f:
#         text = (f.read())
#         new_workspace = WorkspaceWidget(central_widget)
#         central_widget.addTab(new_workspace, path.split("/")[-1])
#         new_workspace.show_text(text)



#TODO:

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(1500, 700)
    # Izgled prozora
    main_window.setWindowTitle("Prototype information resources")
    app.setWindowIcon(QtGui.QIcon("../picture/icons8-edit-file-64.png"))

    

    #Meni bar
    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File",menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)
    open_menu = QtWidgets.QMenu("Open", menu_bar)

    #Icon for menuAction
    fileIcon = QtGui.QIcon("../picture/icons8-edit-file-64.png")
    file_menu.addAction(fileIcon, "New file") # Akcija menija
    fileIcon = QtGui.QIcon("../picture/print.png")
    file_menu.addAction(fileIcon, "Print") # Akcija menija
    file_menu.setToolTip("Open")
    editIcon = QtGui.QIcon("../picture/textedit.png")
    edit_menu.addAction(editIcon, "Settings")# Akcija menija
    viewIcon = QtGui.QIcon("../picture/diplay.png")
    view_menu.addAction(viewIcon, "Window") # Akcija menija


    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)
    menu_bar.addMenu(open_menu)

    #ToolBar sa ikonicama
    tool_bar = QtWidgets.QToolBar(main_window)
    t1 = QtGui.QIcon("../picture/diplay.png")
    tool_bar.addAction(t1, "Display")
    t2 = QtGui.QIcon("../picture/mail.png")
    tool_bar.addAction(t2, "Inbox")
    t3 = QtGui.QIcon("../picture/telefon.png")
    tool_bar.addAction(t3, "Call")
    t4 = QtGui.QIcon("../picture/wifi.png")
    tool_bar.addAction(t4, "Wi-fi")

    text_editor_wgt = QtWidgets.QTextEdit("Unesite tekst", main_window)
    main_window.setCentralWidget(text_editor_wgt)
    
    status_bar = QtWidgets.QStatusBar(main_window)
    status_bar.showMessage("Status bar je prikazan...")




    # dock_wgt = QtWidgets.QDockWidget("Documents", main_window)
    # main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock_wgt)   #mora se importovati QtCOre!!!
    
    # obican_wgt = QtWidgets.QWidget(main_window)                         #napravimo obican (genericki) widget, setujemo layout i na kraju ga postavimo za centralni
    # layout = QtWidgets.QVBoxLayout()                                    #u konstruktru se odredjuje jel horizontalan ili vertikalan, u ovom slucaju H-horizontalan ili V-vertikalan
    # text_edit_wgt1 = QtWidgets.QTextEdit("Unesite tekst", main_window)
    # text_edit_wgt2 = QtWidgets.QTextEdit("Unesite tekst", main_window)
    # layout.addWidget(text_edit_wgt1)
    # layout.addWidget(text_edit_wgt2)
    # obican_wgt.setLayout(layout)                                        #obican widget, jer nije nam bitno koji je u ovom slucaju jer svaki moze da ima layout
    # main_window.setCentralWidget(obican_wgt)




    structure_dock = StructureDock("Strukture dokumenata", main_window)
    structure_dock.tree.clicked.connect(open_file)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)
    
    ###ucitavamo metadata
    metadata_file = open("metadata.json", encoding='utf-8')  #ENCODING se dodaje u citanju json-a jer nema podeseno po default-u UTF-8
    metadata = json.load(metadata_file)
    models = []
    for data in metadata:
        models.append(GenerickiModel(data))

    #WorkspaceWidget
    central_widget = QtWidgets.QTabWidget(main_window)
    # workspace = WorkspaceWidget(central_widget, None, models)
    # workspace.show_tabs()


    # central_widget.addTab(workspace, QtGui.QIcon("../slike/images.png"), "Dobro dosli")
    central_widget.setTabsClosable(True)
    #central_widget.removeTab(0)                                    #ako necu da imam pocetni tab, treba ga obrisati
    central_widget.tabCloseRequested.connect(delete_tab)
  
    main_window.setCentralWidget(central_widget)
    


    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)
    main_window.setCentralWidget(central_widget)
    main_window.setStatusBar(status_bar)

    # Kraj
    main_window.show()
    # menu_bar.setParent(main_window)
    sys.exit(app.exec_())
