import sympy
import secrets
from math import gcd as bltin_gcd

def cifrar(valor,potencia,mod):
    valorCifrado = pow(valor,potencia) % mod
    return valorCifrado

Ep = int("2E76A0094D4CEE0AC516CA162973C895",16)
Np = int("1985008F25A025097712D26B5A322982B6EBAFA5826B6EDA3B91F78B7BD63981382581218D33A9983E4E14D4B26113AA2A83BBCCFDE24310AEE3362B6100D06CC1EA429018A0FF3614C077F59DE55AADF449AF01E42ED6545127DC1A97954B89729249C6060BA4BD3A59490839072929C0304B2D7CBBA368AEBC4878A6F0DA3FE58CECDA638A506C723BDCBAB8C355F83C0839BF1457A3B6B89307D672BBF530C93F022E693116FE4A5703A665C6010B5192F6D1FAB64B5795876B2164C86ABD7650AEDAF5B6AFCAC0438437BB3BDF5399D80F8D9963B5414EAFBFA1AA2DD0D24988ACECA8D50047E5A78082295A987369A67D3E54FFB7996CBE2C5EAD794391",16)

print("Geração da Parte Assimetrica \n")
p = sympy.randprime(2**1023, 2**1024)
q = sympy.randprime(2**1023, 2**1024)

print("p = "+str(p))
print("\nq = "+str(q))

modulo = p*q
funcaoEuler = (p-1)*(q-1)

print("\nmodulo = "+str(modulo))
print("\nfuncaoEuler = "+str(funcaoEuler))

inverso = 11111222223333334444445555556666661111188887

primoRelativo = bltin_gcd(funcaoEuler, inverso) == 1
print("\n" + str(primoRelativo))


print("Geração da Parte Assimetrica \n")

inteiro128bits = 35966238280343333638208114881239354942
#int.from_bytes(secrets.token_bytes(16), byteorder='big') #transforma em inteiro

x = cifrar(inteiro128bits,Ep,Np)
sigX = cifrar(x,inverso,modulo)

print(sigX)
print("aham")
