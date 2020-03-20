import codecs

def decrypt_password(p):
	key = b"I1LOVE2SHARKS"
	pw = codecs.decode(p, "hex")
	
	k = pw[0]
	kp = 0
	
	res = bytearray()
	for i in range(1, len(pw)):
		x = key[kp] ^ pw[i]
		x = x - k
		if x < 0:
			x = x + 0xff
		res.append(x)
		k = pw[i]
	
		kp = kp + 1
		kp = kp % len(key)

	return bytes(res).decode()

print(decrypt_password("964189A25A9857FE3BE21221DF1734AA5F86A751F921CC0236EF0E"))
