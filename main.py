#test
from PIL import Image
with Image.open("nebula.png") as image:
    message="message is hidden"
    message_bytes=message.encode()
    image=image.convert('RGBA')
    image.putdata([(r, g, b, message_bytes[i])
                   if i < len(message_bytes)
                   else (r, g, b, 255) for i,(r, g,b, a) in enumerate(image.getdata())])
    image.save('steg.png')
    image.show()

#### receiver to extract hidden message

with Image.open("steg.png") as image:

    image=image.convert('RGBA')
    message_bytes=[a for r, g, b, a in image.getdata() if a != 255]

    message = bytes(message_bytes).decode()
    print(message)

'''



# - - - - - - -  lect1
import hashlib as hh
hh.sha3_512
x = bytearray(5)
print(x.hex())
a=[1,2,3]
b=a
a.append(4)
print(b)


count=10
while (count < 5):
	print (count)
	count=count+1
else:
  print("count>5")
print("loop finihed")

all_kids = ["Eden", "Hayden", "Kenna"]
for kid in all_kids:
  print (kid)
print(type(all_kids))

def myEnc(plaintext, key):
  print("ciphertext")

myEnc("hello", "KeyError")

def funcc(a,b,c=10,d=100):
  print(a,b,c,d)


funcc(1,2)
funcc(1,2,3,4)
# - - - - --- - - - - - - - 
'''