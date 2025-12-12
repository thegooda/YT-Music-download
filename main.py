import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI.ui_downloader_ver1 import Ui_MainWindow
# import downloader.download

class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.Browse.clicked.connect(self.browse_folder)

        self.show()
        
    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        
        if folder_path:
            self.ui.folder_path.setText(folder_path)
        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()  
    window.show()
    sys.exit(app.exec())
