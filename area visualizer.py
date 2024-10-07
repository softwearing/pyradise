replay = "y"
while (replay == "y"):
  L = int(input("Enter the length in ft²:"))
  W = int(input("Enter the width in ft²:"))
  MiddleL = round(L / 2)
  DisplayW = 2 if W == 1 else W
  MiddleW = round(DisplayW / 2)

  print(" " + "-" * L)

  for i in range(MiddleW):
    print("|" + " " * MiddleL + " " * round(L / 2) + "|")

  print(" " + "-" * L)

  print("area: " + str(L * W) + "ft²")
  print("perimeter: " + str(L * 2 + W * 2) + "ft²")
  replay = input("calculate again? (y/n):")
