import sys
import sqlite3
import ebooklib
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.list = self.cur.execute('SELECT * FROM coffee').fetchall()
        for i in range(1, 8):
            idd = self.cur.execute(f'SELECT id from coffee WHERE id = {i}').fetchall()[0][0]
            sort = self.cur.execute(f'SELECT sort from coffee WHERE id = {i}').fetchall()[0][0]
            roast = self.cur.execute(f'SELECT roast from coffee WHERE id = {i}').fetchall()[0][0]
            v = self.cur.execute(f'SELECT viev from coffee WHERE id = {i}').fetchall()[0][0]
            flavor = self.cur.execute(f'SELECT flover from coffee WHERE id = {i}').fetchall()[0][0]
            price = self.cur.execute(f'SELECT price from coffee WHERE id = {i}').fetchall()[0][0]
            volume = self.cur.execute(f'SELECT volume from coffee WHERE id = {i}').fetchall()[0][0]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(idd)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(sort))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(roast)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(v))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(flavor))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(volume)))
            self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
