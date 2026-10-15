import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class HabitTracker(QWidget):
    STAMP_FORMAT = "%Y-%m-%d %H:%M"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit Tracker")
        self.resize(520, 360)

        # --- Table: the data lives here ---
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Habit", "Date"])
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        # --- Input row ---
        self.habit_input = QLineEdit()
        add_button = QPushButton("Add")

        add_button.clicked.connect(self.add_habit)
        self.habit_input.returnPressed.connect(self.add_habit)  # Enter also adds

        input_row = QHBoxLayout()
        input_row.addWidget(QLabel("Habit:"))
        input_row.addWidget(self.habit_input)
        input_row.addWidget(add_button)

        # --- Assemble ---
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Habit List"))
        layout.addWidget(self.table)
        layout.addLayout(input_row)

    def add_habit(self):
        # Read the input, stamp the time, append a row, clear the field
        habit = self.habit_input.text().strip()
        if not habit:
            return  # ignore empty input

        stamp = datetime.now().strftime(self.STAMP_FORMAT)

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(habit))
        self.table.setItem(row, 1, QTableWidgetItem(stamp))

        self.habit_input.clear()
        self.habit_input.setFocus()


def main():
    app = QApplication(sys.argv)
    window = HabitTracker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()