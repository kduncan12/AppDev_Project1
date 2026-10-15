import sys

print("executable :", sys.executable)
print("python     :", sys.version.split()[0])

try:
    import PySide6
    from PySide6.QtCore import qVersion
    from PySide6.QtWidgets import QApplication, QLabel
except ModuleNotFoundError as err:
    print("RESULT     : FAIL -", err)
    print("Fix        : pip install -r requirements.txt")
    sys.exit(1)

print("PySide6    :", PySide6.__version__)
print("Qt runtime :", qVersion())

app = QApplication(sys.argv)
print("platform   :", app.platformName())

label = QLabel("PySide6 OK\nClose this window to finish.")
label.setWindowTitle("PySide6 OK")
label.setMargin(24)
label.show()

print("RESULT     : PASS - window opened")
sys.exit(app.exec())