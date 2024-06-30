import sympy
import random
import sys

sys.setrecursionlimit(1500)

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
        return None
    else:
        return x % L

def gerar_primo_relativo_com_inverso_128_bits(L):
    while True:
        Ea = random.randint(2, L-1)
        Da = inverso_modular(Ea, L)
        if Da is not None and Da.bit_length() >= 128:
            return Ea, Da

# Gerar p e q como grandes números primos de 1024 bits
p = sympy.randprime(2**1023, 2**1024)
q = sympy.randprime(2**1023, 2**1024)

print("\n p = "+hex(p)[2:])
print("\n q = "+hex(q)[2:])

modulo = p*q
funcaoEuler_L = (p-1)*(q-1)

print("\n modulo = "+hex(modulo)[2:])
print("\n funcaoEuler_L = "+hex(funcaoEuler_L)[2:])

Ea,Da = gerar_primo_relativo_com_inverso_128_bits(funcaoEuler_L)

print("\n Ea = "+hex(Ea)[2:])
print("\n Da = " + hex(Da)[2:])


# Gerar chave simétrica
inteiro128bits = 35966238280343333638208114881239354942

# Cifrar chave simétrica
x = pow(inteiro128bits,Ep,Np)
print("\n x = "+hex(x)[2:])

# Assinar	texto	cifrado
sigX = pow(x,Da,modulo)
print("\n sigX = "+hex(sigX)[2:])