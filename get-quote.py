def maine():
   #print("Keep it logically awesome.")
   
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__maine__":
  main()
