from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ListItemWidget(QWidget):
    def __init__(self, title, description, date, parent=None):
        super(ListItemWidget, self).__init__(parent)


        # Crear etiquetas para título, descripción y fecha
        self.titleLabel = QLabel(title)
        self.descriptionLabel = QLabel(description)
        self.dateLabel = QLabel(date)

        # Estilizar las etiquetas
        self.titleLabel.setStyleSheet("font-weight: bold; color: rgb(255, 208, 18);")
        self.descriptionLabel.setStyleSheet("color: white;")
        self.dateLabel.setStyleSheet("color: rgb(255, 249, 224);")

        # Layout para organizar las etiquetas y dar formato a cada tarea
        layout = QVBoxLayout()

        # Se añade el título
        layout.addWidget(self.titleLabel)

        # Se añade la descripción
        layout.addWidget(self.descriptionLabel)

        # Se añade la fecha
        layout.addWidget(self.dateLabel)
        layout.setContentsMargins(10, 5, 10, 5)

        # Establecer el layout para el widget personalizado
        self.setLayout(layout)

    def set_disable_styles(self):
        self.titleLabel.setStyleSheet("color:white;")
        self.descriptionLabel.setStyleSheet("color:white;")
        self.dateLabel.setStyleSheet("color:white;")
