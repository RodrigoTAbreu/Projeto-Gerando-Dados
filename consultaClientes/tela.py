import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800,600)
janela.setWindowTitle("Primeira Janela do Programa")

btn = QPushButton("Botão 1", janela)
btn.setGeometry(100,100,150,80)
btn.setStyleSheet('background-color:blue;color:white')

label = QLabel("Texto", janela)
label.move(400,100)


#Mostra a tela criada digitada nas linhas anteriores
janela.show()


app.exec()