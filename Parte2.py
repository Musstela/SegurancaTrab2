import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad
from Variaveis import *

# Mensagem cifrada em hexadecimal (exemplo)
mensagem_cifrada_hex = Variaveis.c

# Converter a mensagem cifrada hexadecimal em bytes
mensagem_cifrada_bytes = bytes.fromhex(mensagem_cifrada_hex)

# Extrair os bytes do IV (primeiros 16 bytes)
iv = mensagem_cifrada_bytes[:16]

# Extrair a mensagem cifrada (a partir do 16º byte)
mensagem_cifrada_sem_iv = mensagem_cifrada_bytes[16:]

# Calcular o hash SHA-256 da mensagem cifrada sem o IV
hash_c = hashlib.sha256(mensagem_cifrada_bytes).hexdigest()
print("Hash SHA-256 da mensagem cifrada (sem IV):", hash_c)

# Assinatura SigC da mensagem em hexadecimal
sig_c_hex = Variaveis.SigC
sig_c = int(sig_c_hex, 16)  # Converter a assinatura de hexadecimal para inteiro

# Exponente
exponente_hex = Variaveis.Ep
exponente = int(exponente_hex, 16)

# Módulo N
modulo_n_hex = Variaveis.Np
modulo_n = int(modulo_n_hex, 16)

# Calcular assinatura
resultado = pow(sig_c, exponente, modulo_n)

# Calcular o HC
hc_int = int(hash_c, 16)

# Comparar com Hc
if hc_int == resultado:
    print("Hc é igual ao Calculo da assinatura")
    
    chave_s = Variaveis.s.to_bytes(16,byteorder='big')
    
    # Decifrar a mensagem cifrada usando AES no modo CBC com padding PKCS7
    cipher = AES.new(chave_s, AES.MODE_CBC, iv)
    
    # Unpad da mensagem
    mensagem_decifrada = unpad(cipher.decrypt(mensagem_cifrada_sem_iv), AES.block_size)
    print("Mensagem decifrada:", mensagem_decifrada.decode('utf-8'))

    # Mensagem Inversa
    mensagem_inversa = mensagem_decifrada[::-1]
    print(f"A mensagem inversa é {mensagem_inversa}")

    # Novo IV - que eu fiz invertendo o antigo
    novo_iv = (iv)[::-1]

    # Cifrar a mensagem invertida usando AES no modo CBC com padding PKCS7
    cipher = AES.new(chave_s, AES.MODE_CBC, novo_iv)
    mensagem_cifrada_inversa = cipher.encrypt(pad(mensagem_inversa, AES.block_size))

    # Concatenar o novo IV com a mensagem cifrada
    cinv = novo_iv + mensagem_cifrada_inversa

    # Converter para hexadecimal para visualização
    cinv_hex = cinv.hex()
    print("Cinv (IV + mensagem cifrada) em hexadecimal:", cinv_hex)

    # Calcular o Hc da nova mensagem
    h_inv = hashlib.sha256(cinv).hexdigest()

    # Definir as variaveis da exponenciação da assinatura
    sig_inv_expoente = int(Variaveis.Da,16)
    sig_inv_modulo = int(Variaveis.modulo,16)

    #Calcular a assinatura
    sig_inv = pow(int(h_inv,16),sig_inv_expoente,sig_inv_modulo)
    print("Sig inverso: ",hex(sig_inv)[2:])
else:
    print("Hc não é igual a assinatura")