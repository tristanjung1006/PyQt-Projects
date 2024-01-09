from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl, QEventLoop
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import PySide2
print(PySide2.__version__)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI
        loader = QUiLoader()
        file = QFile("coin_test.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        self.resize(800, 600)

        # Create QWebEngineView
        self.webview = QWebEngineView()

        # Replace placeholder widget
        self.ui.widget.setParent(None)
        self.ui.verticalLayout.addWidget(self.webview)

        # Load webpage
        self.webview.load(QUrl("https://www.naver.com"))

        # Create an event loop
        loop = QEventLoop()

        def load_finished(success):
            if success:
                print("The page was loaded successfully.")
            else:
                print("An error occurred while loading the page.")

        self.webview.loadFinished.connect(load_finished)

        # Connect the loadFinished signal to quit the loop
        self.webview.loadFinished.connect(loop.quit)

        # Start the loop
        loop.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
