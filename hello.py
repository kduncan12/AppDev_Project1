import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class HelloWindow(QStackedWidget):
    # A stack of two pages; only one is visible at a time.

    FIRST_VIEW = 0
    SECOND_VIEW = 1

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")
        self.resize(360, 200)

        self.addWidget(self._build_first_view())
        self.addWidget(self._build_second_view())
        self.setCurrentIndex(self.FIRST_VIEW)

    def _build_first_view(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hello_button = QPushButton("Hello")
        hello_button.clicked.connect(self.show_second_view)
        layout.addWidget(hello_button)
        return page

    def _build_second_view(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hello_label = QLabel("Hello World")
        hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hello_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.show_first_view)
        layout.addWidget(ok_button)
        return page

    def show_second_view(self):
        self.setCurrentIndex(self.SECOND_VIEW)

    def show_first_view(self):
        self.setCurrentIndex(self.FIRST_VIEW)


def main():
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()