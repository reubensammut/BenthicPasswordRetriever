import argparse
import codecs
import csv
import platform
import sys

def is_windows():
	return platform.system() == 'Windows'
	
if is_windows():
	import winreg

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

def fetch_from_registry():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Benthic\LoginList")
	print("Retrieved Credentials")
	print("=====================\n")
	for i in range(0, winreg.QueryInfoKey(key)[1]):
		v = winreg.EnumValue(key, i)[1]
		for row in csv.reader([v]):
			if row[1] == '':
				pw = "** NO PASSWORD STORED **"
			else:
				pw = decrypt_password(row[1])
			print(f"{row[3]}:{pw}")
	
def main():
	parser = argparse.ArgumentParser(description="""Benthic Password Decrypter:
Looks up stored credentials in the registry and decrypts them. This option only 
works on Windows. Also has the ability to decrypt a supplied password.""")
	parser.add_argument('-p', '--password', help='supply the hex of the password to decrypt')
	args = parser.parse_args()
	if args.password:
		print(decrypt_password(args.password))
	elif is_windows():
		fetch_from_registry()
	else:
		print("""Looking up credentials in registry is only supported on Windows. 
To use this application please supply the hex of the password using the `-p` option""")
		sys.exit(1)

if __name__ == "__main__":
	main()
