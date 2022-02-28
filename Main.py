import sys

import ExamWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import *
from Functions import *


class Main23EGE(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BtnCalculate.clicked.connect(self.calculation_prepare)
        self.spinStart.setValue(2)
        self.spinEnd.setValue(29)
        self.spinMove3.setValue(0)
        self.spinMove3.setHidden(True)
        self.move1.activated.connect(self.onActivated)
        self.move2.activated.connect(self.onActivated)
        self.move3.activated.connect(self.onActivated)
        self.BtnCalculate_2.clicked.connect(self.startExam)

    def onActivated(self):
        moves_with_spin = {self.move1: self.spinMove1, self.move2: self.spinMove2, self.move3: self.spinMove3}
        if self.sender().currentIndex() == 0 or self.sender().currentIndex() == 3:
            moves_with_spin[self.sender()].setHidden(True)
        else:
            moves_with_spin[self.sender()].setHidden(False)

    def calculation_prepare(self):
        if not any(x for x in [self.move1.currentIndex(), self.move2.currentIndex(), self.move3.currentIndex()]):
            QtWidgets.QMessageBox.critical(self, 'Ошибка в командах', 'Не определено ни одной команды!',
                            QtWidgets.QMessageBox.Ok)
        else:
            start = self.spinStart.value()
            end = self.spinEnd.value()
            symbol_to_function = {'+': lambda x, y: x + y,
                                    '*': lambda x, y: x * y,
                                    'sqr': lambda x, y: x ** 2,
                                     None: 0}
            if self.move1.currentIndex() == 1:
                move1 = (symbol_to_function['+'], self.spinMove1.value())
            elif self.move1.currentIndex() == 2:
                move1 = (symbol_to_function['*'], self.spinMove1.value())
            elif self.move1.currentIndex() == 3:
                move1 = (symbol_to_function['sqr'], self.spinMove1.value())
            else:
                move1 = (symbol_to_function[None], self.spinMove1.value())
            if self.move2.currentIndex() == 1:
                move2 = (symbol_to_function['+'], self.spinMove2.value())
            elif self.move2.currentIndex() == 2:
                move2 = (symbol_to_function['*'], self.spinMove2.value())
            elif self.move1.currentIndex() == 3:
                move2 = (symbol_to_function['sqr'], self.spinMove2.value())
            else:
                move2 = (symbol_to_function[None], self.spinMove2.value())
            if self.move3.currentIndex() == 1:
                move3 = (symbol_to_function['+'], self.spinMove3.value())
            elif self.move3.currentIndex() == 2:
                move3 = (symbol_to_function['*'], self.spinMove3.value())
            elif self.move3.currentIndex() == 3:
                move3 = (symbol_to_function['sqr'], self.spinMove3.value())
            else:
                move3 = (symbol_to_function[None], self.spinMove3.value())
            moves = (move1, move2, move3)
            self.result = {}
            required_points = []
            if self.lineEdit.text() != '':
                try:
                    required_points = list(x for x in map(int,self.lineEdit.text().split()))
                    required_points.sort()
                except:
                    self.lineEdit.setFocus()
                    trajectory_error(self)
                    return None
            required_tuple = tuple(required_points)
            blocked = ()
            if self.lineEdit_2.text() != '':
                block = self.lineEdit_2.text().split()
                for el in block:
                    try:
                        blocked += int(el),
                    except:
                        self.lineEdit_2.setFocus()
                        trajectory_error(self)
                        return None

            if not required_points:
                try:
                    for i in range(start, end + 1):
                        self.result[i] = (calculate(start, i, moves, blocked))
                except:
                    QtWidgets.QMessageBox.critical(self, 'Неверное выражение!',
                                                   'Неверно заданы команды, либо выражение бессмысленно!',
                                                   QtWidgets.QMessageBox.Ok)
                    return None
            else:
                intermediate_result = {}
                intermediate_coefficient = 1
                intermediate_point_start = start
                while len(required_points) != 0:
                    intermediate_point_end = required_points.pop(0)
                    try:
                        for i in range(intermediate_point_start, intermediate_point_end + 1):
                            if i not in intermediate_result.keys():
                                intermediate_result[i] = calculate(intermediate_point_start, i, moves, blocked) *\
                                    intermediate_coefficient
                            else:
                                intermediate_coefficient = intermediate_result[i]
                                intermediate_result[i] = calculate(intermediate_point_start, i, moves, blocked) *\
                                    intermediate_coefficient
                        intermediate_coefficient = i
                        intermediate_point_start = intermediate_point_end
                    except:
                        QtWidgets.QMessageBox.critical(self, 'Неверное выражение!',
                                                       'Неверно заданы команды, либо выражение бессмысленно!',
                                                       QtWidgets.QMessageBox.Ok)
                        return None
                for i in range(intermediate_point_start, end + 1):
                    if i not in intermediate_result.keys():
                        intermediate_result[i] = calculate(intermediate_point_start, i, moves, blocked) * \
                                                 intermediate_coefficient
                    else:
                        intermediate_coefficient = intermediate_result[i]
                        intermediate_result[i] = calculate(intermediate_point_start, i, moves, blocked) * \
                                                 intermediate_coefficient
                    intermediate_result[i] = calculate(intermediate_point_start, i, moves, blocked) *\
                        intermediate_coefficient
                self.result = intermediate_result
            self.AnswerLabel.setText(str(self.result[end]))
            self.item_list = []
            for i, j in self.result.items():
                if i in blocked:
                    value_for_listview = str(i) + ': ' + str(j) + '\tX'
                elif i in required_tuple:
                    value_for_listview = str(i) + ': ' + str(j) + '\t*'
                else:
                    value_for_listview = str(i) + ': ' + str(j)
                self.item_list.append(value_for_listview)
            self.listView.setAutoScroll(True)
            self.model_1 = QtCore.QStringListModel(self)
            self.model_1.setStringList(self.item_list)
            self.listView.setModel(self.model_1)
            self.listView.scrollToBottom()

    def startExam(self):
        window = Exam(self)
        window.show()


class Exam(QtWidgets.QWidget):
    def __init__(self, parent=Main23EGE):
        super().__init__(parent, QtCore.Qt.Window)
        self.exam_window = ExamWindow.Ui_Form()
        self.exam_window.setupUi(self)
        self.setWindowModality(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main23EGE()
    ex.show()
    sys.exit(app.exec_())