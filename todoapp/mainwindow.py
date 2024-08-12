import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem, QListView
from list_item_widget import ListItemWidget
from ui_mainwindow import Ui_mainwindow
from routes import RouteManager

class Mainwindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)
        # Se crea una instancia de routes
        self.route_manager = RouteManager(self)
        self.count_complete_task = 0
        self.count_incomplete_task = 0

        # Cuando se presione el botón "Agregar" se abre una ventana para
        # agregar una tarea
        self.ui.addButton.clicked.connect(self.route_manager.go_to_addtask)

        # Cuando se presione el botón "Eliminar" se llama a la función
        # delete_task
        self.ui.deleteButton.clicked.connect(self.delete_task)

        # Cuando se presione el botón "Completar" se llama a la función
        # check_task
        self.ui.checkButton.clicked.connect(self.check_task)

    # Función para agregar tareas
    def add_task(self, title, description, date):

        # Se asignan los campos para crear la tarea
        self.title = title
        self.description = description
        self.date = date

        # Se verifica si no hay ningún campo vacío
        if self.title and self.description and self.date:
            # Se crea una instancia de la clase ListItemWidget del archivo
            # list_item_widgte (widget personalizado)
            item_widget = ListItemWidget(self.title, self.description, self.date)
            # Se crea un nuevo elemento (contenedor) de lista asociado
            # al QListWidget
            list_item = QListWidgetItem(self.ui.listWidget)
            # Se le asigna un tamaño predeterminado en función del tamaño del
            # item_widget
            list_item.setSizeHint(item_widget.sizeHint())
            # Se adjunta el widget personalizado a la lista para que se muestre
            # en pantalla
            self.ui.listWidget.setItemWidget(list_item, item_widget)

        # Se agrega una nueva tarea al contador de tareas pendientes
        self.count_incomplete_task += 1
        # El contador pasa a formato str y se utiliza otra variable para almacenar el valor
        self.count_incomplete_task_str = str(self.count_incomplete_task)
        # Se escribe en pantalla el número de tareas que existen sin completar
        self.ui.count_task.setText(self.count_incomplete_task_str)

    def check_task(self):
        # Se obtienen los items seleccionados
        selected_items = self.ui.listWidget.selectedItems()

        # Verifica si existe un item seleccionado
        if not selected_items:
            # Si no existe, se regresa
            return

        # Por cada item que esté seleccionado
        for item in selected_items:

            # Obtén el widget asociado al item (QWidget)
            item_widget = self.ui.listWidget.itemWidget(item)
            if item_widget:
                item_widget.set_disable_styles()
            # Deshabilita el ítem seleccionado
            item.setFlags(item.flags() & ~Qt.ItemIsEnabled)

        # Se agrega una tarea al contador de tareas completadas
        self.count_complete_task += 1
        # El contador pasa a formato str y se almacena en otra variable
        self.count_complete_task_str = str(self.count_complete_task)
        # Se escribe el contador en pantalla
        self.ui.count_complete.setText(self.count_complete_task_str)
        # En caso de que el contador de tareas incompletas sea 0
        if self.count_incomplete_task == 0:
            # Se pasa
            pass
        # En caso de no ser 0
        else:
            # Se le quita el valor de 1 al contador de tareas incompletas
            self.count_incomplete_task -= 1
            # El contador pasa a formato str y se almacena en otra variable
            self.count_incomplete_task_str = str(self.count_incomplete_task)
            # Se escribe el contador en pantalla
            self.ui.count_task.setText(self.count_incomplete_task_str)

    def delete_task(self):
        # Se obtienen los items seleccionados
        selected_items = self.ui.listWidget.selectedItems()
        # Verifica si existe un item
        if not selected_items:
            # Si no existe se regresa
            return

        # Por cada item que este seleccionado
        for item in selected_items:
            # Se obtiene la fila del item
            row = self.ui.listWidget.row(item)
            # Se elimina la fila del item seleccionado
            self.ui.listWidget.takeItem(row)
        # En caso de que el contador de tareas incompletas sea 0
        if self.count_incomplete_task == 0:
            # Se pasa
            pass
        # En caso de que no sea 0
        else:
            # Se le quita el valor de 1 al contador de tareas incompletas
            self.count_incomplete_task -= 1
            # El contador pasa a formato str y se almacena en otra variable
            self.count_incomplete_task_str = str(self.count_incomplete_task)
            # Se escribe el contador en pantalla
            self.ui.count_task.setText(self.count_incomplete_task_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Mainwindow()
    widget.show()
    sys.exit(app.exec())
