## Made by Zion Coding Incorporated

number = int(input("Enter a semiprime: ")) ## Setting permanent value for the number
n = number ## Main number
g = 8 ## Random number
r = 1 ## Exponent
m = 1 ## Only for coding purposes

acomplete = False

while acomplete == False:
    if (g**r)%n==1:
        x = ((g**(r/2))+1)
        y = ((g**(r/2))-1)
        acomplete = True
    else:
        r+=1
        
while n>0:
   m=x%n
   x=n
   n=m
   
m = 1
y = ((g**(r/2))-1)
n = number

while n>0:
   m=y%n
   y=n
   n=m
    
print(f'The lowest mN+1 number was {g**r} and the exponent was {r}')
print(f'First prime was {x} and second was {y}')
