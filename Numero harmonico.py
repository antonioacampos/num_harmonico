num = int(input())
denominador = 1
H = 0
while denominador <= num :
    H += 1 / denominador
    denominador += 1
print(f"{H:.4f}")
