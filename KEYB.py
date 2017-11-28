# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KEYB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip

class Ui_MainWindow(object):
    def __init__(self):
        self.pretext="";

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QPushButton(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(40, 130, 75, 23))
        self.tab.setObjectName("tab")
        self.pretext="";
        self.PQ = QtWidgets.QPushButton(self.centralwidget)
        self.PQ.setGeometry(QtCore.QRect(120, 130, 41, 21))
        self.PQ.setObjectName("PQ")
        self.PW = QtWidgets.QPushButton(self.centralwidget)
        self.PW.setGeometry(QtCore.QRect(160, 130, 41, 21))
        self.PW.setObjectName("PW")
        self.PE = QtWidgets.QPushButton(self.centralwidget)
        self.PE.setGeometry(QtCore.QRect(200, 130, 41, 21))
        self.PE.setObjectName("PE")
        self.PR = QtWidgets.QPushButton(self.centralwidget)
        self.PR.setGeometry(QtCore.QRect(240, 130, 41, 21))
        self.PR.setObjectName("PR")
        self.PT = QtWidgets.QPushButton(self.centralwidget)
        self.PT.setGeometry(QtCore.QRect(280, 130, 41, 21))
        self.PT.setObjectName("PT")
        self.PY = QtWidgets.QPushButton(self.centralwidget)
        self.PY.setGeometry(QtCore.QRect(320, 130, 41, 21))
        self.PY.setObjectName("PY")
        self.PU = QtWidgets.QPushButton(self.centralwidget)
        self.PU.setGeometry(QtCore.QRect(360, 130, 41, 21))
        self.PU.setObjectName("PU")
        self.PI = QtWidgets.QPushButton(self.centralwidget)
        self.PI.setGeometry(QtCore.QRect(400, 130, 41, 21))
        self.PI.setObjectName("PI")
        self.PO = QtWidgets.QPushButton(self.centralwidget)
        self.PO.setGeometry(QtCore.QRect(440, 130, 41, 21))
        self.PO.setObjectName("PO")
        self.PP = QtWidgets.QPushButton(self.centralwidget)
        self.PP.setGeometry(QtCore.QRect(480, 130, 41, 21))
        self.PP.setObjectName("PP")
        self.P7 = QtWidgets.QPushButton(self.centralwidget)
        self.P7.setGeometry(QtCore.QRect(560, 130, 41, 21))
        self.P7.setObjectName("P7")
        self.P8 = QtWidgets.QPushButton(self.centralwidget)
        self.P8.setGeometry(QtCore.QRect(600, 130, 41, 21))
        self.P8.setObjectName("P8")
        self.P9 = QtWidgets.QPushButton(self.centralwidget)
        self.P9.setGeometry(QtCore.QRect(640, 130, 41, 21))
        self.P9.setObjectName("P9")
        self.PS = QtWidgets.QPushButton(self.centralwidget)
        self.PS.setGeometry(QtCore.QRect(160, 160, 41, 21))
        self.PS.setObjectName("PS")
        self.P4 = QtWidgets.QPushButton(self.centralwidget)
        self.P4.setGeometry(QtCore.QRect(560, 160, 41, 21))
        self.P4.setObjectName("P4")
        self.P6 = QtWidgets.QPushButton(self.centralwidget)
        self.P6.setGeometry(QtCore.QRect(640, 160, 41, 21))
        self.P6.setObjectName("P6")
        self.PA = QtWidgets.QPushButton(self.centralwidget)
        self.PA.setGeometry(QtCore.QRect(120, 160, 41, 21))
        self.PA.setObjectName("PA")
        self.PH = QtWidgets.QPushButton(self.centralwidget)
        self.PH.setGeometry(QtCore.QRect(320, 160, 41, 21))
        self.PH.setObjectName("PH")
        self.PD = QtWidgets.QPushButton(self.centralwidget)
        self.PD.setGeometry(QtCore.QRect(200, 160, 41, 21))
        self.PD.setObjectName("PD")
        self.PK = QtWidgets.QPushButton(self.centralwidget)
        self.PK.setGeometry(QtCore.QRect(400, 160, 41, 21))
        self.PK.setObjectName("PK")
        self.PL = QtWidgets.QPushButton(self.centralwidget)
        self.PL.setGeometry(QtCore.QRect(440, 160, 41, 21))
        self.PL.setObjectName("PL")
        self.ENTER = QtWidgets.QPushButton(self.centralwidget)
        self.ENTER.setGeometry(QtCore.QRect(480, 160, 41, 31))
        self.ENTER.setObjectName("ENTER")
        self.P5 = QtWidgets.QPushButton(self.centralwidget)
        self.P5.setGeometry(QtCore.QRect(600, 160, 41, 21))
        self.P5.setObjectName("P5")
        self.PCAPS = QtWidgets.QPushButton(self.centralwidget)
        self.PCAPS.setGeometry(QtCore.QRect(40, 160, 75, 23))
        self.PCAPS.setObjectName("PCAPS")
        self.PG = QtWidgets.QPushButton(self.centralwidget)
        self.PG.setGeometry(QtCore.QRect(280, 160, 41, 21))
        self.PG.setObjectName("PG")
        self.PJ = QtWidgets.QPushButton(self.centralwidget)
        self.PJ.setGeometry(QtCore.QRect(360, 160, 41, 21))
        self.PJ.setObjectName("PJ")
        self.PF = QtWidgets.QPushButton(self.centralwidget)
        self.PF.setGeometry(QtCore.QRect(240, 160, 41, 21))
        self.PF.setObjectName("PF")
        self.PX = QtWidgets.QPushButton(self.centralwidget)
        self.PX.setGeometry(QtCore.QRect(160, 200, 41, 21))
        self.PX.setObjectName("PX")
        self.P1 = QtWidgets.QPushButton(self.centralwidget)
        self.P1.setGeometry(QtCore.QRect(560, 200, 41, 21))
        self.P1.setObjectName("P1")
        self.P3 = QtWidgets.QPushButton(self.centralwidget)
        self.P3.setGeometry(QtCore.QRect(640, 200, 41, 21))
        self.P3.setObjectName("P3")
        self.PZ = QtWidgets.QPushButton(self.centralwidget)
        self.PZ.setGeometry(QtCore.QRect(120, 200, 41, 21))
        self.PZ.setObjectName("PZ")
        self.PN = QtWidgets.QPushButton(self.centralwidget)
        self.PN.setGeometry(QtCore.QRect(320, 200, 41, 21))
        self.PN.setObjectName("PN")
        self.PC = QtWidgets.QPushButton(self.centralwidget)
        self.PC.setGeometry(QtCore.QRect(200, 200, 41, 21))
        self.PC.setObjectName("PC")
        self.PCOMMA = QtWidgets.QPushButton(self.centralwidget)
        self.PCOMMA.setGeometry(QtCore.QRect(400, 200, 41, 21))
        self.PCOMMA.setObjectName("PCOMMA")
        self.PSHIFTL = QtWidgets.QPushButton(self.centralwidget)
        self.PSHIFTL.setGeometry(QtCore.QRect(440, 200, 41, 21))
        self.PSHIFTL.setObjectName("Delete")
        self.PCONTROL = QtWidgets.QPushButton(self.centralwidget)
        self.PCONTROL.setGeometry(QtCore.QRect(480, 200, 41, 21))
        self.PCONTROL.setObjectName("PCONTROL")
        self.P2 = QtWidgets.QPushButton(self.centralwidget)
        self.P2.setGeometry(QtCore.QRect(600, 200, 41, 21))
        self.P2.setObjectName("P2")
        self.PSHIFT = QtWidgets.QPushButton(self.centralwidget)
        self.PSHIFT.setGeometry(QtCore.QRect(40, 200, 75, 23))
        self.PSHIFT.setObjectName("PSHIFT")
        self.PB = QtWidgets.QPushButton(self.centralwidget)
        self.PB.setGeometry(QtCore.QRect(280, 200, 41, 21))
        self.PB.setObjectName("PB")
        self.PM = QtWidgets.QPushButton(self.centralwidget)
        self.PM.setGeometry(QtCore.QRect(360, 200, 41, 21))
        self.PM.setObjectName("PM")
        self.PV = QtWidgets.QPushButton(self.centralwidget)
        self.PV.setGeometry(QtCore.QRect(240, 200, 41, 21))
        self.PV.setObjectName("PV")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 230, 41, 21))
        self.pushButton.setObjectName("pushButton")
        self.PSPACE = QtWidgets.QPushButton(self.centralwidget)
        self.PSPACE.setGeometry(QtCore.QRect(190, 230, 311, 31))
        self.PSPACE.setObjectName("PSPACE")
        self.plainTextEdit = QtWidgets.QLabel(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 50, 641, 71))
        self.plainTextEdit.setText("")

        self.cp = QtWidgets.QPushButton(self.centralwidget)
        self.cp.setGeometry(QtCore.QRect(40, 10, 181, 31))
        self.cp.setObjectName("cp")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.PA.clicked.connect(self.Pa)
        self.PB.clicked.connect(self.Pb)
        self.PC.clicked.connect(self.Pc)
        self.PD.clicked.connect(self.Pd)
        self.PE.clicked.connect(self.Pe)
        self.PF.clicked.connect(self.Pf)
        self.PG.clicked.connect(self.Pg)
        self.PH.clicked.connect(self.Ph)
        self.PI.clicked.connect(self.Pi)
        self.PJ.clicked.connect(self.Pj)
        self.PK.clicked.connect(self.Pk)
        self.PL.clicked.connect(self.Pl)
        self.PM.clicked.connect(self.Pm)
        self.PN.clicked.connect(self.Pn)
        self.PO.clicked.connect(self.Po)
        self.PP.clicked.connect(self.Pp)
        self.PQ.clicked.connect(self.Pq)
        self.PR.clicked.connect(self.Pr)
        self.PS.clicked.connect(self.Ps)
        self.PT.clicked.connect(self.Pt)
        self.PU.clicked.connect(self.Pu)
        self.PV.clicked.connect(self.Pv)
        self.PW.clicked.connect(self.Pw)
        self.PX.clicked.connect(self.Px)
        self.PY.clicked.connect(self.Py)
        self.PZ.clicked.connect(self.Pz)
        self.P1.clicked.connect(self.P1a)
        self.P2.clicked.connect(self.P2b)
        self.P3.clicked.connect(self.P3c)
        self.P4.clicked.connect(self.P4d)
        self.P5.clicked.connect(self.P5e)
        self.P6.clicked.connect(self.P6f)
        self.P7.clicked.connect(self.P7g)
        self.P8.clicked.connect(self.P8h)
        self.P9.clicked.connect(self.P9i)
        self.PSHIFTL.clicked.connect(self.dele)
        self.PSPACE.clicked.connect(self.spc)
        self.pushButton.clicked.connect(self.P0l)
        self.ENTER.clicked.connect(self.enter)
        self.cp.clicked.connect(self.copy)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab.setText(_translate("MainWindow", "TAB"))

        self.PQ.setText(_translate("MainWindow", "q"))
        self.PW.setText(_translate("MainWindow", "w"))
        self.PE.setText(_translate("MainWindow", "e"))
        self.PR.setText(_translate("MainWindow", "r"))
        self.PT.setText(_translate("MainWindow", "t"))
        self.PY.setText(_translate("MainWindow", "y"))
        self.PU.setText(_translate("MainWindow", "u"))
        self.PI.setText(_translate("MainWindow", "i"))
        self.PO.setText(_translate("MainWindow", "o"))
        self.PP.setText(_translate("MainWindow", "p"))
        self.P7.setText(_translate("MainWindow", "7"))
        self.P8.setText(_translate("MainWindow", "8"))
        self.P9.setText(_translate("MainWindow", "9"))
        self.PS.setText(_translate("MainWindow", "s"))
        self.P4.setText(_translate("MainWindow", "4"))
        self.P6.setText(_translate("MainWindow", "6"))
        self.PA.setText(_translate("MainWindow", "a"))
        self.PH.setText(_translate("MainWindow", "h"))
        self.PD.setText(_translate("MainWindow", "d"))
        self.PK.setText(_translate("MainWindow", "k"))
        self.PL.setText(_translate("MainWindow", "l"))
        self.ENTER.setText(_translate("MainWindow", "ENTER"))
        self.P5.setText(_translate("MainWindow", "5"))
        self.PCAPS.setText(_translate("MainWindow", "CAPS LK"))
        self.PG.setText(_translate("MainWindow", "g"))
        self.PJ.setText(_translate("MainWindow", "j"))
        self.PF.setText(_translate("MainWindow", "f"))
        self.PX.setText(_translate("MainWindow", "x"))
        self.P1.setText(_translate("MainWindow", "1"))
        self.P3.setText(_translate("MainWindow", "3"))
        self.PZ.setText(_translate("MainWindow", "z"))
        self.PN.setText(_translate("MainWindow", "n"))
        self.PC.setText(_translate("MainWindow", "c"))
        self.PCOMMA.setText(_translate("MainWindow", ","))
        self.PSHIFTL.setText(_translate("MainWindow", "DEl"))
        self.PCONTROL.setText(_translate("MainWindow", "control"))
        self.P2.setText(_translate("MainWindow", "2"))
        self.PSHIFT.setText(_translate("MainWindow", "SHIFT"))
        self.PB.setText(_translate("MainWindow", "b"))
        self.PM.setText(_translate("MainWindow", "m"))
        self.PV.setText(_translate("MainWindow", "v"))
        self.PSPACE.setText(_translate("MainWindow", "SPACE BAR"))
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.cp.setText(_translate("MainWindow", "copy to clipboard"))

    def Pa(self):

        i = self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"a");

    def Pb(self):

        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"b");
    def Pc(self):

        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"c");
    def Pd(self):

        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"d");
    def Pe(self):

        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"e");
    def Pf(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"f");
    def Pg(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"g");
    def Ph(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"h");
    def Pi(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"i");
    def Pj(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"j");
    def Pk(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"k");
    def Pl(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"l");
    def Pm(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"m");
    def Pn(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"n");
    def Po(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"o");
    def Pp(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"p");
    def Pq(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"q");
    def Pr(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"r");
    def Ps(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"s");
    def Pt(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"t");
    def Pu(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"u");
    def Pv(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"v");
    def Pw(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"w");
    def Px(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"x");
    def Py(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"y");
    def Pz(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"z");
    def P1a(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"1");
    def P2b(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"2");
    def P3c(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"3");
    def P4d(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"4");
    def P5e(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"5");
    def P6f(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"6");
    def P7g(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"7");
    def P8h(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"8");
    def P9i(self):
        i=self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"9");
    def enter(self):
        i-self.plainTextEdit.text();
        self.plainTextEdit.setText(i+"<-");

    def copy(self):
        y= self.plainTextEdit.text();
        pyperclip.copy(y)

    def dele(self):
        w="";
        x=self.plainTextEdit.text();
        m=list(x);
        r=len(m);
        if(r>0):
            m.pop(r-1);
        for i in m:
            w=(w+i)
        self.plainTextEdit.setText(w);
    def spc(self):
        i = self.plainTextEdit.text();
        self.plainTextEdit.setText(i + " ");
    def P0l(self):
        i = self.plainTextEdit.text();
        self.plainTextEdit.setText(i + "0");

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

