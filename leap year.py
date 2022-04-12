x = int(input("Enter a Year:"))
if (year%400 == 0) or (year%4==0 and year%100!=0):  
  print("This year is a Leap Year")
else:  
  print("This is Not a Leap Year")
