# -*- coding: utf-8 -*-

'''

Calculates depletion of funds
Tested on opensuse 11.1 linux only
2009-November-12  Version 0.5

Use at your own peril or improve it

Free

'''
import sys,math
try:
   import locale
except:
   pass

from PyQt4 import QtCore, QtGui
#from deplgui import Ui_Dialog


# show some color in the terminal
def printgreen(s):
        print '\033[1;42m%s\033[1;m'  % s

def printred(s):
        print '\033[1;48m%s\033[1;m' % s

def printcyan(s):
        print '\033[1;46m%s\033[1;m' % s
 
def printblue(s):
        print '\033[1;44m%s\033[1;m' % s
        
def printbrown(s):
        print '\033[1;43m%s\033[1;m' % s


# how much can I withdraw give pv,r,y per year
def MYdepl(pv,r,y):
  try:
     wdy=pv * r *(((1+r)**(y-1))/((1+r)**y-1))
     return wdy
  except:
     return -1
     
# how much can I withdraw give pv,r,y per month 
def MYdeplm(pv,r,y):
  try:
     r=r/12
     y=y*12
     wdym=pv * r *(((1+r)**(y-1))/((1+r)**y-1))
     return wdym
  except:
     return -1     


# how many years do funds last at rate r 
# input : pv ,r, wd
def MYydepl(pv,r,wd):
    try:
       y=math.log((wd-((pv*r)/(r+1)))/wd)/math.log(r+1)
       return abs(y)
    except:
       
       return -1

       
    
# what pv is required at rate r and yearly withdrawal wd for y years
def MYpdepl(r,wd,y):
    try:
      p=wd*((r+1)**(1-y)*((r+1)**y-1))/r
     
      return p
    except:
      return -1


# Ui_Dialog class created using qt-designer and copied here

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(571, 542)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 571, 531))
        self.groupBox.setStyleSheet("background-color: rgb(139, 142, 142);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 55, 16))
        self.label_4.setObjectName("label_4")
        self.pvedit = QtGui.QLineEdit(self.groupBox)
        self.pvedit.setGeometry(QtCore.QRect(140, 50, 113, 26))
        self.pvedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pvedit.setObjectName("pvedit")
        self.rateedit = QtGui.QLineEdit(self.groupBox)
        self.rateedit.setGeometry(QtCore.QRect(140, 80, 113, 26))
        self.rateedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rateedit.setObjectName("rateedit")
        self.wdedit = QtGui.QLineEdit(self.groupBox)
        self.wdedit.setGeometry(QtCore.QRect(140, 110, 113, 26))
        self.wdedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wdedit.setObjectName("wdedit")
        self.yearsedit = QtGui.QLineEdit(self.groupBox)
        self.yearsedit.setGeometry(QtCore.QRect(140, 140, 41, 26))
        self.yearsedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.yearsedit.setObjectName("yearsedit")
        self.wdbutton = QtGui.QPushButton(self.groupBox)
        self.wdbutton.setGeometry(QtCore.QRect(20, 190, 100, 25))
        self.wdbutton.setStyleSheet("background-color: rgb(64, 200, 62);")
        self.wdbutton.setObjectName("wdbutton")
        self.pvbutton = QtGui.QPushButton(self.groupBox)
        self.pvbutton.setGeometry(QtCore.QRect(130, 190, 100, 25))
        self.pvbutton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pvbutton.setObjectName("pvbutton")
        self.yearsbutton = QtGui.QPushButton(self.groupBox)
        self.yearsbutton.setGeometry(QtCore.QRect(240, 190, 100, 25))
        self.yearsbutton.setStyleSheet("background-color: rgb(254, 220, 255);")
        self.yearsbutton.setObjectName("yearsbutton")
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 460, 100, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 230, 531, 131))
        self.textEdit.setStyleSheet("""background-color: rgb(238, 238, 238);
font: 15pt \"Adobe Courier\";""")
        self.textEdit.setObjectName("textEdit")
        self.clearbutton = QtGui.QPushButton(self.groupBox)
        self.clearbutton.setGeometry(QtCore.QRect(350, 190, 100, 25))
        self.clearbutton.setStyleSheet("background-color: rgb(172, 172, 0);")
        self.clearbutton.setObjectName("clearbutton")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 380, 241, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", " Depletion  Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "PV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Rate % p.a.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Withdrawal p.a.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Years", None, QtGui.QApplication.UnicodeUTF8))
        self.wdbutton.setText(QtGui.QApplication.translate("Dialog", "Withdrawal", None, QtGui.QApplication.UnicodeUTF8))
        self.pvbutton.setText(QtGui.QApplication.translate("Dialog", "PV", None, QtGui.QApplication.UnicodeUTF8))
        self.yearsbutton.setText(QtGui.QApplication.translate("Dialog", "Years", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: rgb(255, 88, 38);", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Dialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.clearbutton.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Based on 1 withdrawal p.a. end of year", None, QtGui.QApplication.UnicodeUTF8))


        
class DE(QtGui.QDialog): 
  from datetime import datetime
  def __init__(self):
         
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)      
        self.connect(self.ui.pvbutton, QtCore.SIGNAL("clicked()"), self.pdepl)
        self.connect(self.ui.wdbutton, QtCore.SIGNAL("clicked()"), self.depl)
        self.connect(self.ui.yearsbutton, QtCore.SIGNAL("clicked()"), self.ydepl)
        self.connect(self.ui.clearbutton, QtCore.SIGNAL("clicked()"), self.clearit)
        self.clearit()


  def depl(self):
    pv=float(self.ui.pvedit.text())
    r=float(self.ui.rateedit.text())/100
    y=float(self.ui.yearsedit.text())
    self.ui.wdedit.setStyleSheet("background-color: rgb(139, 142, 142);")
    self.ui.pvedit.setStyleSheet("background-color: rgb(255, 255, 255);")
    self.ui.yearsedit.setStyleSheet("background-color: rgb(255, 255, 255);")
       
    wd=MYdepl(pv,r,y)
    
    wdm=MYdeplm(pv,r,y)
    
    anote='PV : %s   Rate : %s p.a.  Years : %s  ' % (str(pv),str(r),str(y)) 
    self.ui.textEdit.setText(anote)
    self.ui.textEdit.append('')
    if wd ==-1:
       if r==0:
           self.ui.textEdit.append('Rate can not be 0. Try 0.000001')
           self.ui.textEdit.append('Error ! Check Data and try again !')
       else:
           self.ui.textEdit.append('Error ! Check Data and try again !')
    else:
      
       try:
          
           aresult='Yearly Withdrawal Amount  : %s' % locale.currency( wd, grouping=True )
           self.ui.textEdit.append(aresult)
           self.ui.textEdit.append('')
           aresult='Monthly Withdrawal Amount : %s' % locale.currency( wdm, grouping=True )
           self.ui.textEdit.append(aresult)
           
           
       except: 
      
          aresult='Yearly Withdrawal Amount  : %s' % str(wd)
          self.ui.textEdit.append(aresult)
          self.ui.textEdit.append('')
          aresult='Monthly Withdrawal Amount : %s' % str(wdm)
          self.ui.textEdit.append(aresult)
          # for quick testing put the result back
          #self.ui.wdedit.setText(str(wd)) 

  # how many years do funds last at rate r 
  # input : pv ,r, wd
  def ydepl(self):
      pv=float(self.ui.pvedit.text())
      r=float(self.ui.rateedit.text())/100
      wd=float(self.ui.wdedit.text())
      self.ui.yearsedit.setStyleSheet("background-color: rgb(139, 142, 142);")
      self.ui.pvedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      self.ui.wdedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      anote='PV : %s    Rate : %s p.a.  Withdrawal/year : %s  ' % (str(pv),str(r),str(wd)) 
      self.ui.textEdit.setText(anote)
      y = MYydepl(pv,r,wd)
      if y == -1 :
         if r==0:
             self.ui.textEdit.append('Rate can not be 0. Try 0.000001')
             self.ui.textEdit.append('Error ! Check Data and try again !')
         else:
            self.ui.textEdit.append('')
            self.ui.textEdit.append('')
            self.ui.textEdit.append('Forever !')
      else:   
         aresult='Years until depleted : %s' % str(y)
         self.ui.textEdit.append('')
         self.ui.textEdit.append(aresult)


  def pdepl(self):
      wd=float(self.ui.wdedit.text())
      r=float(self.ui.rateedit.text())/100
      y=float(self.ui.yearsedit.text()) 
      # change color to dark as this field is not used as datainput
      self.ui.pvedit.setStyleSheet("background-color: rgb(139, 142, 142);")
      self.ui.yearsedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      self.ui.wdedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      p=MYpdepl(r,wd,y)
      anote=  'Withdrawal/year : %s   Rate : %s p.a. Years : %s  ' % (str(wd),str(r),str(y)) 
      self.ui.textEdit.setText(anote)
      self.ui.textEdit.append('')
      if p==-1:
         if r==0:
             self.ui.textEdit.append('Rate can not be 0. Try 0.000001')
             self.ui.textEdit.append('Error ! Check Data and try again !')
         else:
             self.ui.textEdit.append('Error ! Check Data and try again !')
      else:  
         try:
           aresult='Pv required  : %s' % locale.currency( p, grouping=True )
         except:
           aresult='Pv required  : %s' % str(p)

         self.ui.textEdit.append(aresult)


  def clearit(self):
      # some test data to start
      self.ui.pvedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      self.ui.yearsedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      self.ui.rateedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      self.ui.wdedit.setStyleSheet("background-color: rgb(255, 255, 255);")
      self.ui.pvedit.setText('100000.00')
      self.ui.wdedit.setText('50000')
      self.ui.rateedit.setText('5.0')
      self.ui.yearsedit.setText('15')



if __name__ == "__main__":
      
    printgreen('Hello from pydeplete') 
    printgreen ("Qt Version  : '%s'"  % str(QtCore.QT_VERSION_STR)) 
    printgreen ("PyQt Version: '%s'"  % str(QtCore.PYQT_VERSION_STR))
    app = QtGui.QApplication(sys.argv)
    myapp = DE()
    myapp.show()
    sys.exit(app.exec_())
    
    
