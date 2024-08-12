import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_addtask import Ui_addtask

class Addtask(QMainWindow):
    def __init__(self, mainwindow, parent=None):
        super().__init__(parent)
        self.ui = Ui_addtask()
        self.ui.setupUi(self)

        # Se crea una instacia de mainwindow
        self.mainwindow = mainwindow

        # En caso de presionar el botón "Crear" se captura la información
        self.ui.createButton.clicked.connect(self.capturar_info)

    # Función para capturar la información
    def capturar_info(self):

        # Se obtiene el título
        title = self.ui.input_title.text()
        # Se obtiene la descripción
        description = self.ui.input_description.text()
        # Se obtiene la fecha
        date = self.ui.input_date.text()

        # Se usa la función addtask de mainwindow para llevar los datos a
        # la ventana principal
        self.mainwindow.add_task(title, description, date)

        # Se cierra la ventana de creación de tareas
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Addtask()
    print("Mostrando ventana")  # Mensaje de depuración
    widget.show()
    sys.exit(app.exec())
