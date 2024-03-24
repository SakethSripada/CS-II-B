from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

with open("random.txt","rb") as myFile:
  text = myFile.read()

encrypted_text = f.encrypt(text)

with open("random_encrypted.txt", "wb") as encrypted_file:
  encrypted_file.write(encrypted_text)
