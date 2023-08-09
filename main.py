import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from src.Classes.ui_class_wrapper import uiDesignWrapper







if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = uiDesignWrapper()
    main_window.show()
    sys.exit(app.exec_())
