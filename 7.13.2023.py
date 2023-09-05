q = "How many fenestras does a synapsid animal have?"
answers = ("A) 1", "B) 2", "C) 3", "D) None")
def quest():
   print(q)
   print(" ".join (answers))
   a = input("Your answer: ")
   if a == "A":
      print("Correct!")
   else:
      print("Incorrect!")
quest()

