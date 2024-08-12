# Esta clase administra las ventanas
class RouteManager:

    # Metodo constructor de un nuevo atributo que va a contener
    # la ventana que quiero abrir
    def __init__(self, mainwindow):
        self.current_window = None
        # Se consigue la ventana principal
        self.mainwindow = mainwindow

    def go_to_addtask(self):
        from addtask import Addtask
        # Se crea una instancia de Addtask y se manda la ventana principal
        self.addtask_window = Addtask(self.mainwindow)
        # A traves de la instancia se muestra la ventana para crear tareas
        self.addtask_window.show()
