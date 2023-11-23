from PyQt5 import QtWidgets, uic
import sys
import sympy as sp

x = sp.symbols('x')

class Ui(QtWidgets.QMainWindow):
    def __init__ (self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui',self)
        self.botonn.clicked.connect(self.factoreo)
        self.show()

    def factoreo(self):
            expresion = self.operacion.text()
            factores = sp.factor(expresion)
            self.imprimir_respuesta(factores)

    def imprimir_respuesta(self, respuesta):
        self.respuesta.setText(str(respuesta))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()