import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def funcao1():
    label.setText("Mudando o Texto do Label - Botão 1 Pressionado")
    label.adjustSize()
    
def funcao2():
    label.setText("Mudando o Texto do Label - Botão 2 Pressionado")
    label.adjustSize()
    

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800,600) #tamanho da tela
janela.setWindowTitle("Primeira Janela do Programa") #titulo da tela

btn = QPushButton("Botão 1", janela) #Criando o Botão e o local(janela) onde será exibido
btn.setGeometry(100,100,150,80) #tamanho do botão
btn.setStyleSheet('background-color:blue;color:white') #cores de fundo e de texto do botão com CSS
btn.clicked.connect(funcao1)#evento de clic que chama a função1

btn2 = QPushButton("Botão 2", janela) #Criando o Botão e o local(janela) onde será exibido
btn2.setGeometry(100,300,150,80) #tamanho do botão
btn2.setStyleSheet('background-color:blue;color:white') #cores de fundo e de texto do botão com CSS
btn2.clicked.connect(funcao2) # evento de click que chama a função 2



label = QLabel("Texto", janela) #texto aleatorio na tela.
label.move(400,100) #posição do texto na tela
label.setStyleSheet("font-size: 30px")


#Mostra a tela criada digitada nas linhas anteriores
janela.show()


app.exec()