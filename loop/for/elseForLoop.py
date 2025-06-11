for x in range(6):
  print(x)
else:
  print("Finally finished!")

# output:
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  

# output:
# 0
# 1
# 2