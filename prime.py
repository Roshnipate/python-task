x = int(input("Enter a number: "))
if x > 1:    
  for i in range(2, (x // 2) + 1):        
    if (x % i == 0):            
      print(x, "is not a Prime number")            
      break    
  else:        
      print(x, "is a Prime number")
else:    
  print(x, "is not a Prime number")
