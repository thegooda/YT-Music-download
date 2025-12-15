import sys
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI.ui_downloader_ver1 import Ui_MainWindow
from downloader.download import music_download

class DownloadWorker(QRunnable):
    def __init__(self, youtube_url, folder_path, file_type):
        super().__init__()
        self.youtube_url = youtube_url
        self.folder_path = folder_path
        self.file_type = file_type

    @Slot()
    def run(self):
        # This runs in a background thread
        music_download(
            youtube_url=self.youtube_url,
            folder_path=self.folder_path,
            file_type=self.file_type
        )

class Mainwindow(QMainWindow):
    
    progress_signal = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        
        #self.progress_signal.connect(self.update_display)
                
        self.ui.Browse.clicked.connect(self.browse_folder)
        self.ui.download_button.clicked.connect(self.click_download)

        self.show()
        
    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        
        if folder_path:
            self.ui.folder_path.setText(folder_path)
    
    #def update_display(self, new_num):
    
    def click_download(self):
        youtube_url_input = self.ui.youtube_link.text()
        folder_path_input = self.ui.folder_path.text()
        file_type_input = self.ui.file_type.currentIndex()
        
        worker = DownloadWorker(
            youtube_url=youtube_url_input, 
            folder_path=folder_path_input, 
            file_type=file_type_input)
        
        self.threadpool.start(worker)
        
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()  
    window.show()
    sys.exit(app.exec())
