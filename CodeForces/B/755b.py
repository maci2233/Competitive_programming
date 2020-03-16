#Hago un set con los numeros de la primer persona
#luego para cada palabra de la segunda persona checo
#si intersecta con los de la primer persona y cuento cuantas intersectan
# si hay 0 o un numero impar de intersecciones, sera el turno del jugador 1 despues
# si hay un numero impar de intersecciones, sera el turno del jugaror 2 despues
n, m = map(int, input().split())
n_set = set()
inters = 0
for _ in range(n):
    n_set.add(input())
for _ in range(m):
    if input() in n_set:
        inters += 1
if inters == 0 or inters % 2 == 0:
    print("YES" if n > m else "NO")
else:
    print("YES" if n >= m else "NO")
