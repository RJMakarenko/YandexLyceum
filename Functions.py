from PyQt5 import QtWidgets
import sqlite3
import random
from functools import lru_cache as lru

question_number= 0

def trajectory_error(self):
    QtWidgets.QMessageBox.critical(self, 'Ошибка в траектории расчёта',
        '''Введено неверное значение!\nТраектория вводится целыми числами через пробел!''',
        QtWidgets.QMessageBox.Ok)

def get_questions():
    con = sqlite3.connect('EGE23.db')
    cur = con.cursor()
    results = []
    rand_num = random.sample(range(1, 51), 10)
    for question in rand_num:
        cur.execute(f'''SELECT * FROM Exam WHERE Id = {question}''')
        results.append(list(cur.fetchone()))
    cur.close()
    return results


@lru()
def calculate(start, end, moves, blocked):
    if end < start or start > end or start in blocked:
        return 0
    if end == start:
        return 1
    first_rez = calculate(moves[0][0](start,moves[0][1]), end, moves, blocked) if moves[0][0] != 0 else 0
    second_rez = calculate(moves[1][0](start,moves[1][1]), end, moves, blocked) if moves[1][0] != 0 else 0
    third_rez =  calculate(moves[2][0](start, moves[2][1]), end, moves, blocked) if moves[2][0] != 0 else 0
    return first_rez + second_rez + third_rez
