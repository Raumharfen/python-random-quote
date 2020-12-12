import random
def primary():
  print("Keep it logically awesome.")
  
  f = open("quotes.txt", "a")
  f.write("Bananen Wurst und Tee \n")
  f.close()
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  newQuote = input("Enter a quote:")
  
  quotes.append("Wer anderen eine Bratwurst brät.")
  quotes.append(newQuote)

  last = len(quotes)
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  
  for x in quotes:
    # quotes = quotes.rstrip("\n")
    print(x)
  print(quotes[rnd], quotes[rnd2], quotes[last - 1 ])

if __name__== "__main__":
  primary()
