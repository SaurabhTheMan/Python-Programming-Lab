input_list = input('Enter Fruits(separated by space) ')
print("\n")
fruits = input_list.split()
print('list of fruits: ', fruits)
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
