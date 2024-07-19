n = 0
s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s = s + n
print(f'A soma entre os números digitados é {s}.')
