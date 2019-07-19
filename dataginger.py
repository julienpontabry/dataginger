import sys

from PySide2.QtWidgets import QApplication

from gui import DataGingerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = DataGingerWindow()
    main_window.show()
    sys.exit(app.exec_())
