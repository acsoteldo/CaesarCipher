message = 'SORUHIUSKHYJOFHEJUSJIJXUTQJQ' #encrypted message
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

length = int(input("Please input shift: "))

for k in range(length):
   result = ''
   for i in message:
      if i in alphabet:
         num = alphabet.find(i)
         num = num - k
         if num < 0:
            num = num + len(alphabet)
         result += alphabet[num]
      else:
         result += i
    
print('Key #%s: %s' % (k, result))
