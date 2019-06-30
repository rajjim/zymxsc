import sys
from controler import uison
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':

    app = QApplication(sys.argv)
    uif= uison.uison()
    uif.show()
    sys.exit(app.exec_())

