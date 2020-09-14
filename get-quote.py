def maine():
   
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
   last = 13
   rnd = random.randit(0,last)
  print(quotes[rnd])

if __name__== "__maine__":
  maine()
