alphabet = 'ABCDEFGHIJKLEMNOPQRSTUVWXYZ'

def encrypt(text,k):
	result = ""

	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + ord(k) - 65) % 26 + 65)
		else:
			result += chr((ord(char) + ord(k) - 97) % 26 + 97)
	return result

def decrypt(text,k):
	result = ""

	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) - ord(k) - 65) % 26 + 65)
		else:
			result += chr((ord(char) - ord(k) - 97) % 26 + 97)
	return result

#second step
def cipher(letter):
	if 'E' in letter:
		k = input("Type the key('A'-'Z') you want to choose: " )
		text = input("Please enter input text: " )
		print ("Output text: " + encrypt(text,k))
	elif 'D' in letter:
		k = input("Type the key('A'-'Z') you want to choose: " )
		text = input("Please enter input text: " )
		print ("Output text: " + decrypt(text,k))
	else:
		print('Error')

dict = {'E': encrypt, 'D': decrypt}

#first step
letter = input("Type 'E' or 'D' to choose encryption mode or decryption mode: ")
cipher(letter)
