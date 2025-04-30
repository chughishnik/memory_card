from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox,  QPushButton, QGroupBox, QButtonGroup 


class Question():
    def __init__(self, question,correct,wrong1,wrong2,wrong3):
        self.correct = correct
        self.question = question
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    




app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory card')
win.resize(500,300)

win.ttl = 0
win.score = 0
#БЛОК С ВОПРСОМ
#текст и кнопка
text = QLabel('вопрос')
btn = QPushButton('Ответить')
#варианты ответов
ans1 = QRadioButton('ответ 1')
ans2 = QRadioButton('ответ 2')
ans3 = QRadioButton('ответ 3')
ans4 = QRadioButton('ответ 4')
    
rgroup = QButtonGroup()
rgroup.addButton(ans1)
rgroup.addButton(ans2)
rgroup.addButton(ans3)
rgroup.addButton(ans4)

#лейауты
linev1 = QVBoxLayout()
linev2 = QVBoxLayout()
lineg = QHBoxLayout()

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
main_line = QVBoxLayout()
#создание группы ответов
linev1.addWidget(ans1, alignment = Qt.AlignCenter)
linev1.addWidget(ans2, alignment = Qt.AlignCenter)
linev2.addWidget(ans3, alignment = Qt.AlignCenter)
linev2.addWidget(ans4, alignment = Qt.AlignCenter)

lineg.addLayout(linev1)
lineg.addLayout(linev2)

group = QGroupBox('Варианты ответов')
group.setLayout(lineg)
#распределение виджетов


#БЛОК С ОТВЕТОМ
#кнопка и текст
group2 = QGroupBox('Результат теста')
res = QLabel('правильно/неправильно')
wer = QLabel('правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(res, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(wer, alignment=Qt.AlignHCenter, stretch=2)
group2.setLayout(layout_res)

line2.addWidget(group2)
group2.hide()

line1.addWidget(text, alignment = Qt.AlignCenter)
line2.addWidget(group)
line3.addStretch(1)
line3.addWidget(btn, stretch=2)
line3.addStretch(1)

main_line.addLayout(line1, stretch=2)
main_line.addStretch(1)
main_line.addLayout(line2,stretch=5)
main_line.addStretch(1)
main_line.addLayout(line3,stretch=2)



def answer():
    group.hide()
    group2.show()
    btn.setText('Следующий вопрос')

def ask(q):
    text.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.correct)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    wer.setText(q.correct)
    question1()


def question1():
    group.show()
    group2.hide()
    btn.setText('Ответить')
    rgroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    rgroup.setExclusive(True)

def test():
    if 'Ответить' == btn.text():
        check()
    else:
        next()

answers = [ans1,ans2,ans3,ans4]

pr1 = Question('какой жанр видеоигр задала игра по названием "metroid"?','метроидвания','мотрострой','градострой', 'выживание')
pr2 = Question('как вы оцените игру "content warning", играя с 4 друзьями?','не передать словами/10','7/10','10/10','5/10')
pr3 = Question('что нужно добыть в "Deep rock galactic", чтобы вызвать капсулу с боеприпасами?','нитру','селитру','золото','серебро')

questions = [pr1,pr2,pr3]

def next():
    cur_question = randint(0,len(questions)-1)
    problem = questions[cur_question]
    ask(problem)
    win.ttl +=1    
    print('всего вопросов',win.ttl)
    print('правильных ответов', win.score)
    print('рейтинг', win.score/win.ttl*100)

def check():
    if answers[0].isChecked():
        show_cor('Правильно!')
        win.score +=1
    else:
        show_cor('Неправильно!')


def show_cor(res1):
    res.setText(res1)
    answer()
ask(questions[0])
btn.clicked.connect(test)

main_line.setSpacing(2)
win.setLayout(main_line)

win.show()
app.exec_()