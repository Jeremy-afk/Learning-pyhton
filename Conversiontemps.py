import sys

T = 0
T = int(input('Temps a convertir '))

A = 0
J = 0
H = 0
M = 0
S = 0
R = 0

A = T // 31557600 # 1 an = 365,25 jours
R = T % 31557600

J = R // 86400 # 1 jour = 24*60*60 secondes
R = R % 86400

H = R // 3600
R = R % 3600

M = R // 60
S = R % 60

print (A," ans ",J, "jours ",H," heures ",M,"minutes ","et ",S," secondes.")