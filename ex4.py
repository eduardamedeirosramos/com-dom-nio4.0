
horario1=int(input("digite o primeiro horario: "))
minuto1=int(input("digite o primeiro minuto: "))
horario2=int(input("digite o segundo horario: "))
minuto2=int(input("digite o segundo minuto: "))

horario=horario1+horario2#somando
minuto=minuto1+minuto2

minutotal= minuto%60 #sobra do resto da divisao
horatotal=horario%12#resto da divisao horas
horadicional= horatotal+1 #se os numeros forem maiores que 60

if minuto>60:#se os minutos sao maiores que 60
     print(f"o horário final é {horadicional}:0{minutotal}")
else:
    print(f"{horatotal}:0 {minutotal}")

