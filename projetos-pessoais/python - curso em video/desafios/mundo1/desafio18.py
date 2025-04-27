import math
angulo=int(input("digite um angulo:"))
rad=math.radians(angulo)
seno=math.sin(rad)
consseno=math.cos(rad)
tangente=math.tan(rad)
print("o seno desse angulo é:{:.3f},\no cosseno desse angulo é:{:.3f}\n a tangente desse angulo é:{:.3f}"
      .format(seno,consseno,tangente))
