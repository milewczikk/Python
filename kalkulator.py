from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import math

class Kalkulator(QWidget): 
	def __init__(self, parent=None): 
		super().__init__(parent)
		self.interfejs()
	def interfejs(self):
		etykieta1 = QLabel("Liczba 1:", self)
		etykieta2 = QLabel("Liczba 2:", self)
		etykieta3 = QLabel("Wynik:", self)
		
		uklad = QGridLayout()
		uklad.addWidget(etykieta1, 0, 0)
		uklad.addWidget(etykieta2, 0, 1)
		uklad.addWidget(etykieta3, 0, 2)
		
		self.setLayout(uklad)
		self.setGeometry(20, 20, 300, 100)
		self.setWindowIcon(QIcon('kalkulator.png'))
		self.setWindowTitle ("Prosty kalkulator")
		
		self.liczba1Edt = QLineEdit()
		self.liczba2Edt = QLineEdit()
		self.wynikEdt = QLineEdit()
		self.wynikEdt.readonly = True
		self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
		
		uklad.addWidget(self.liczba1Edt, 1, 0)
		uklad.addWidget(self.liczba2Edt, 1, 1)
		uklad.addWidget(self.wynikEdt, 1, 2)
		
		dodajBtn = QPushButton("&Dodaj", self)
		odejmijBtn = QPushButton("&Odejmij", self)
		dzielBtn = QPushButton("&Mnóż", self)
		mnozBtn = QPushButton("&Dziel", self)
		pierBtn = QPushButton("&Pierwiastkuj", self)
		koniecBtn = QPushButton("&Koniec", self)
		koniecBtn.resize(koniecBtn.sizeHint())
		
		ukladH = QHBoxLayout()
		ukladH.addWidget(dodajBtn)
		ukladH.addWidget(odejmijBtn)
		ukladH.addWidget(dzielBtn)
		ukladH.addWidget(mnozBtn)
		ukladH.addWidget(pierBtn)
		uklad.addLayout(ukladH, 2, 0, 1, 3)
		uklad.addWidget(koniecBtn, 3, 0, 1, 3)
		
		self.resize(300, 100)
		self.setWindowTitle("Super Kalkulator")
		self.show()
		koniecBtn.clicked.connect(self.koniec)
		
		dodajBtn.clicked.connect(self.dzialanie)
		odejmijBtn.clicked.connect(self.dzialanie)
		mnozBtn.clicked.connect(self.dzialanie)
		dzielBtn.clicked.connect(self.dzialanie)
		pierBtn.clicked.connect(self.pierwiastek)
	
	def dzialanie(self):
		nadawca = self.sender()
		try:
			liczba1 = float(self.liczba1Edt.text())
			liczba2 = float(self.liczba2Edt.text())
			wynik = ""
			if nadawca.text() == "&Dodaj":
				wynik = liczba1 + liczba2
			elif nadawca.text() == "&Odejmij":
				wynik = liczba1 - liczba2
			elif nadawca.text() == "&Mnóż":
				wynik = liczba1 * liczba2
			elif nadawca.text() == "&Dziel":
				try:
					wynik = round(liczba1 / liczba2, 9)
				except ZeroDivisionError:
					QMessageBox.critical(self, "Błąd", "Nie można dzielić przez zero!")
					return
				else:
					pass
			self.wynikEdt.setText(str(wynik))
		except ValueError:
			QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
	def pierwiastek(self):
		nadawca = self.sender()
		try:
			liczba1 = float(self.liczba1Edt.text())
			wynik = math.sqrt(liczba1)
			if wynik <= 0:
				QMessageBox.critical(self, "Błąd", "Nie można pierwiastkować przez zero!")
				return

			self.wynikEdt.setText(str(wynik))
		except ValueError:
			QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
		
			
	def koniec(self):
			self.close()
	def keyPressEvent(self, e):
			if e.key() == Qt.Key_Escape:
				self.close()
	def closeEvent(self, event):
		odp = QMessageBox.question(self, 'Komunikat', "Czy na pewno koniec?",QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
if __name__ == '__main__':
		import sys
		app = QApplication(sys.argv) 
		okno = Kalkulator() 
		sys.exit(app.exec_())
