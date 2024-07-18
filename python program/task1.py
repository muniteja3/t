#password genarator
import random
letters=['a','b','c','d','e','d','e','f','g','h','g','i','j','k','l','m','n','o','p','q','r','s','t','u','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*']
print('welcome to password generator')
n_letters=int(input('how many letters you wamt?\n'))
n_numbers=int(input('how many numberss you wamt?\n'))
n_symbols=int(input('how many symbols you wamt?\n'))
password=[]
for i in range(0,n_letters):
    char=random.choice(letters)
    
    password+=char
for j in range(0,n_numbers):
    num=random.choice(numbers) 
    password+=num  
for k in range(0,n_symbols):
    sym=random.choice(symbols) 
    password+=sym  
#password=char+num+sym
print(password)
random.shuffle(password)
print(password)
   
        
        
        