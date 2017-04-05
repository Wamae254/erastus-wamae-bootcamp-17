lower = 2
upper = 10**4
print("Here is a list of Prime numbers from:",lower,"and",upper)

for num in range(lower,upper):
   
   if num > 1:
       for z in range(2,num):
           if (num % z) == 0:
               break
       else:
           print(num)
