
#==========================================
# tela gulosa
import turtle
import random
import time

tela = turtle.Screen()
tela.title("Jogo da Cobrona - Nokia 3310")
tela.setup(width=600, height=600)

# imagem de fundo
tela.bgpic(r"C:\Users\integral\Desktop\nicole\caio.rossi.gif")

pontos = 0
tela.tracer(0)

#============================================
# cobra gulosa
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("violet")
cobra.penup() # impede a cobrona maligna fique desenhando enquanto se movimenta
cobra.goto(0, 0)
cobra.direction = 'stop'

#===============================================================================
# fruta golosona
fruta = turtle.Turtle()
fruta.speed(0)
fruta.shape("circle")
fruta.color("green")
fruta.penup()
fruta.goto(0, 100)

corpo = []

#================================================================================
# direção

def cima():
    if cobra.direction != "down":
        cobra.direction = "up"

def baixo():
    if cobra.direction != "up":
        cobra.direction = "down"

def direita():
    if cobra.direction != "left":
        cobra.direction = "right"

def esquerda():
    if cobra.direction != "right":
        cobra.direction = "left"

#=================================================================================
# fazer a cobra obedecer safadonaa obedece pau mandado os comando
tela.listen()
tela.onkeypress(cima, "Up")
tela.onkeypress(baixo, "Down")
tela.onkeypress(direita, "Right")
tela.onkeypress(esquerda, "Left")

#==================================================================================
# nao paraaaa safada

while True:
    tela.update()

    if cobra.distance(fruta) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        fruta.goto(x, y)
        pontos += 10

        novo_pedaco = turtle.Turtle()
        novo_pedaco.speed(0)
        novo_pedaco.shape("square")
        novo_pedaco.color("purple")
        novo_pedaco.penup()
        corpo.append(novo_pedaco)

        tela.title(f"Jogo da Cobrona | Pontos: {pontos}")

    time.sleep(0.08)

    # movimentação da cobra
    if cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)

    elif cobra.direction == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)

    elif cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)

    elif cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)

    #================================================================
    # movimentação dos pedaços do corpo

    for i in range(len(corpo) - 1, 0, -1):
        x = corpo[i - 1].xcor()
        y = corpo[i - 1].ycor()
        corpo[i].goto(x, y)

    if len(corpo) > 0:
        x = cobra.xcor()
        y = cobra.ycor()
        corpo[0].goto(x, y)

    #================================================================
    # colisão com as paredes

    if (cobra.xcor() > 290 or cobra.xcor() < -290
            or cobra.ycor() > 290 or cobra.ycor() < -290):
        tela.title(f"GAME OVER! Pontuação Final: {pontos}")
        break

    #================================================================
    # colisão com o próprio corpo

    for pedaco in corpo:
        if pedaco.distance(cobra) < 10:
            tela.title(f"GAME OVER! Pontuação Final: {pontos}")
            break
    else:
        continue

    break

#================================================================
# fim de jogo

tela.mainloop()
