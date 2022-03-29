#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql.cursors
from PyQt6.QtGui import QStandardItemModel,QStandardItem
from PyQt6.QtWidgets import QApplication,QTableView,QGridLayout,QPushButton,QWidget
from PyQt6.uic.properties import QtWidgets



class Table(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.model = QStandardItemModel()
        self.table = QTableView()
        self.table.setModel(self.model)
        self.btnLoad = QPushButton("load")
        self.btnLoad.clicked.connect(self.load_data)
        self.btnLoad2 = QPushButton("load2")
        self.btnLoad2.clicked.connect(self.vse)
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.table,0,0,4,4)
        self.grid.addWidget(self.btnLoad,4,0,1,1)
        self.grid.addWidget(self.btnLoad2,4,1,1,1)

    def load_data(self):
        l = [[i + j for i in range(3)] for j in range(4)]
        self.model.setRowCount(4)
        self.model.setColumnCount(3)
        for i in range(4):
            for j in range(3):
                item = QStandardItem(str(l[i][j]))
                self.model.setItem(i, j, item)

    def loadZ(self,rw1):
       # print('obana      '+str(rw1[0].keys()))
        self.model.setColumnCount(len(rw1[0]))
        self.model.setRowCount(len(rw1))

        k=1
        for i in range(len(rw1)):
            jj=0
            for j in rw1[0].keys():
                it=QStandardItem(rw1[i][j])
                self.model.setItem(i,jj,it)
                k+=1
                jj+=1

    def GetDat(self):
        con = pymysql.connect(host='217.25.94.235',
                              user='admin_sonalab',
                              password='Vgp@j918',
                              db='sonalab_db',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM nomenklatura")

            rows = cur.fetchall()

            # for i in rows:
            #     print(i.get('naimenovanie'),i.get('ostatok'))
        return rows

    def vse(self):
        return self.loadZ(self.GetDat())



app=QApplication([])


w = Table()
w.show()

#w.GetDat()

# model = QStandardItemModel()
# table = QTableView()
# table.setModel(model)
# btnLoad = QPushButton("load")
# btnLoad.clicked.connect(load_data)
# grid = QGridLayout()
# grid.addWidget(table, 0, 0, 4, 4)
# grid.addWidget(btnLoad, 4, 0, 1, 1)



app.exec()

