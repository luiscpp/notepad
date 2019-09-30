from ventana_ui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.Qt import QApplication, QClipboard

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs) #Sobreescribiendo Constructor
        self.setupUi(self)
        self.route = ""
        
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionGuardar_como.triggered.connect(self.guardar_como)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionSalir.triggered.connect(self.salir)
        self.actionCopiar.triggered.connect(self.copiar)
        self.actionCortar.triggered.connect(self.cortar)
        self.actionPegar.triggered.connect(self.pegar)
        self.actionDeshacer.triggered.connect(self.deshacer)
        self.actionRehacer.triggered.connect(self.rehacer)
        self.actionAcercaDe.triggered.connect(self.acercaDe)
        
    def abrir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        ruta, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()")
        
        if ruta:
            self.route = ruta
            f = open(self.route)
            text = f.read()
            self.plainTextEdit.setPlainText(text)
            f.close()

    def guardar(self):
        if self.route:
            text = self.plainTextEdit.toPlainText()
            f = open(self.route,"w+")
            f.write(text)
            f.close()
        else:
            self.guardar_como()

    def guardar_como(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        ruta, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if ruta:
            self.route = ruta
            text = self.plainTextEdit.toPlainText()
            f = open(self.route,"w+")
            f.write(text)
            f.close()
    
    def copiar(self):
        self.plainTextEdit.copy()

    def cortar(self):
        self.plainTextEdit.cut()        
    
    def pegar(self):
        self.plainTextEdit.paste()

    def deshacer(self):
        self.plainTextEdit.undo()  

    def rehacer(self):
        self.plainTextEdit.redo()     

    def acercaDe(self):
        QMessageBox.about(self,"Información","Autor: Luis Fernando Ospino Ayala\nFecha: 20/09/2019\nSoftware: Bloc de Notas®")

    def salir(self):
        respuesta = QMessageBox.question(self,"Atención","¿Está seguro que quiere salir?")
        if respuesta == QMessageBox.Yes:
            QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
