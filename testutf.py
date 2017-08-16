#with open('data/small_vocab_fr', "r") as f:
import locale
print(locale.getpreferredencoding(False))
with open('zobi.utf', "rb") as f:
	print(f.read())
with open('zobi.utf', "r") as f:
	print(f.read())
	
with open('zobi.utf', "r", encoding="utf-8") as f:
	data = f.read()
	
print(data)