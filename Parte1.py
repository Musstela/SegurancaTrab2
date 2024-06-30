import sympy
import secrets
from math import gcd as bltin_gcd

Ep = int("2E76A0094D4CEE0AC516CA162973C895",16)
Np = int("1985008F25A025097712D26B5A322982B6EBAFA5826B6EDA3B91F78B7BD63981382581218D33A9983E4E14D4B26113AA2A83BBCCFDE24310AEE3362B6100D06CC1EA429018A0FF3614C077F59DE55AADF449AF01E42ED6545127DC1A97954B89729249C6060BA4BD3A59490839072929C0304B2D7CBBA368AEBC4878A6F0DA3FE58CECDA638A506C723BDCBAB8C355F83C0839BF1457A3B6B89307D672BBF530C93F022E693116FE4A5703A665C6010B5192F6D1FAB64B5795876B2164C86ABD7650AEDAF5B6AFCAC0438437BB3BDF5399D80F8D9963B5414EAFBFA1AA2DD0D24988ACECA8D50047E5A78082295A987369A67D3E54FFB7996CBE2C5EAD794391",16)

def mdc_extendido(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = mdc_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverso_modular(Ea, L):
    gcd, x, y = mdc_extendido(Ea, L)
    if gcd != 1:
        raise ValueError(f"O inverso modular não existe para Ea = {Ea} e L = {L}")
    else:
        return x % L

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def encontrar_primo_relativo(L):
    candidato = 2
    while True:
        if mdc(candidato, L) == 1:
            return candidato
        candidato += 1

# Geração da Parte Assimetrica
p = sympy.randprime(2**1023, 2**1024)
q = sympy.randprime(2**1023, 2**1024)

print("\n p = "+hex(p)[2:])
print("\n q = "+hex(q)[2:])

modulo = p*q
funcaoEuler = (p-1)*(q-1)

print("\n modulo = "+hex(modulo)[2:])
print("\n funcaoEuler = "+hex(funcaoEuler)[2:])

inverso = encontrar_primo_relativo(funcaoEuler)
print("\n inverso = "+hex(inverso)[2:])

modInverso = inverso_modular(inverso,modulo)
print("\n modInverso = " + hex(modInverso)[2:])


# Gerar chave simétrica
inteiro128bits = 35966238280343333638208114881239354942

# Cifrar chave simétrica
x = pow(inteiro128bits,Ep,Np)
print("\n x = "+hex(x)[2:])

# Assinar	texto	cifrado
sigX = pow(x,modInverso,modulo)
print("\n sigX = "+hex(sigX)[2:])