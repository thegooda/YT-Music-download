import sys
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Qt, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI.ui_downloader_ver2 import Ui_MainWindow
from downloader.download import music_download

class worker_signals(QObject):
    set_total = Signal(int)
    progress = Signal(int)
    finished = Signal()
    error = Signal(str)

class DownloadWorker(QRunnable):
    def __init__(self, youtube_url, folder_path, file_type):
        super().__init__()
        self.youtube_url = youtube_url
        self.folder_path = folder_path
        self.file_type = file_type
        self.signals = worker_signals()

    @Slot()
    def run(self):
        try:
            # This runs in a background thread
            music_download(
                youtube_url=self.youtube_url,
                folder_path=self.folder_path,
                file_type=self.file_type,
                set_total_callback=self.signals.set_total.emit,
                progress_callback=self.signals.progress.emit
            )
            self.signals.finished.emit()
        except Exception as e:
            self.signals.error.emit(str(e))

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
    
    
    # def show_error(self, msg):
    #     # QMessageBox.critical(self, "Download Error", msg)
        
    
    def click_download(self):    
        worker = DownloadWorker(
            youtube_url=self.ui.youtube_link.text(),
            folder_path=self.ui.folder_path.text(), 
            file_type=self.ui.file_type.currentIndex()
        )
        
        worker.signals.set_total.connect(self.ui.progressBar.setMaximum)
        worker.signals.progress.connect(self.ui.progressBar.setValue)
        worker.signals.finished.connect(lambda: self.ui.status_label.setText("Status: Done"))
        # worker.signals.error.connect(self.show_error)
        
        self.ui.progressBar.setValue(0)
        
        self.threadpool.start(worker)
        
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()  
    window.show()
    sys.exit(app.exec())
