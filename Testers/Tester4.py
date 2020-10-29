ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
twenties = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
other = ["", "hundred", "thousand"]

def num(N):
   
   n = str(N)
   length = len(n)
   output = ""

   ener = int(N % 10) # singles digit 
   tier = int(((N % 100) - ener) / 10) # tens digit 
   hundrer = int(((N % 1000) - (tier * 10) - ener) / 100) # hundreds digit 

   #Maks 1000
   if length >= 4:
      output += other[2]
      return output

   #Null
   if N == 0:
      output += "zero"
      return output

   #Hundrere
   if hundrer != 0 and tier == 0 and ener == 0:
      output += ones[hundrer] + " " + other[1]
      return output
   elif hundrer != 0:
      output += ones[hundrer] + " " + other[1] + " and "

   if tier <= 1:
      output += ones[N % 100]
   elif tier > 1:
      output += twenties[tier] + " " + ones[ener]

   return output

b = 1000
print(num(b))
print(len(num(b)))