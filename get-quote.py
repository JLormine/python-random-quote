def maine():
   
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[3])

if __name__== "__maine__":
  maine()
