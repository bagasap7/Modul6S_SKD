
def egcd(a, b): #gcd berfungsi untuk mencari fpb
	x, y, u, v = 0, 1, 1, 0
	while a != 0:
		q, r = b//a, b % a
		m, n = x-u*q, y-v*q
		b, a, x, y, u, v = a, r, u, v, m, n
	gcd = b
	return gcd, x, y


def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None  
	else:
		return x % m


# Fungsi enskripsi
# mengembalikan ke chipher teks
def affine_encrypt(text, key):
	
	#C = (a*P + b) % 26 (rumus enskripsi dengan affine cipher)
	return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26)
                     + ord('A')) for t in text.upper().replace(' ', '')])


# fungsi dekripsi 
# mengembalikan ke teks asli
def affine_decrypt(cipher, key):
	
	#P = (a^-1 * (C - b)) % 26 (rumus enskripsi dengan affine cipher)
	
	return ''.join([chr(((modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                      % 26) + ord('A')) for c in cipher])



def main():
	# Deklaraasi plainteks dan key
	plaintext = 'BAGAS ADITYA PRAMUDANA'
	key = [7, 10] # kunci yang digunakan yaitu 7 kunci pertama dan 10 sebagai kunci kedua

	# memanggil fungsi enkripsi
	affine_encrypted_text = affine_encrypt(plaintext, key)

	print('Encrypted Text: {}'.format(affine_encrypted_text))

	# memanggil fungsi dekripsi
	print('Decrypted Text: {}'.format
            (affine_decrypt(affine_encrypted_text, key)))


if __name__ == '__main__':
	main()

