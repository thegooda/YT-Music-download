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
    def __init__(self, youtube_url, folder_path, file_type, start_index):
        super().__init__()
        self.youtube_url = youtube_url
        self.folder_path = folder_path
        self.file_type = file_type
        self.start_index = start_index
        self.signals = worker_signals()

    @Slot()
    def run(self):
        try: 
            # This runs in a background thread
            music_download(
                youtube_url=self.youtube_url,
                folder_path=self.folder_path,
                file_type=self.file_type,
                start_index=self.start_index,
                set_total_callback=self.signals.set_total.emit,
                progress_callback=self.signals.progress.emit
            )
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()

class Mainwindow(QMainWindow):
    
    progress_signal = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
                        
        self.ui.Browse.clicked.connect(self.browse_folder)
        self.ui.download_button.clicked.connect(self.click_download)

        self.show()
        
    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        
        if folder_path:
            self.ui.folder_path.setText(folder_path)
        
    def click_download(self):    
        
        self.ui.status_label.setText("Status: Downloading...")
        
        
        try:
            start_index_test = max(1, int(self.ui.index_input.text()))
        except ValueError:
            start_index_test = 1
            self.ui.index_input.setText("1")
        
        
        worker = DownloadWorker(
            youtube_url=self.ui.youtube_link.text(),
            folder_path=self.ui.folder_path.text(), 
            file_type=self.ui.file_type.currentIndex(),
            start_index = start_index_test
        )
        
        worker.signals.set_total.connect(self.ui.progressBar.setMaximum)
        worker.signals.progress.connect(self.ui.progressBar.setValue)
        worker.signals.error.connect(lambda e: self.ui.status_label.setText(f"Status: Error"))
        worker.signals.finished.connect(lambda: self.ui.status_label.setText("Status: Done"))
        
        self.ui.progressBar.setValue(0)
        
        self.threadpool.start(worker)
        
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()  
    window.show()
    sys.exit(app.exec())
