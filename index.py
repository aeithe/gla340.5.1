new_list= ['apple', 'orange', 12, ['peanut', 'butter', 'jelly', 'time']]

print(new_list)
print(len(new_list))
print(type(new_list[2]))
num = new_list[2]
obj = new_list[1]

print(f"I have {num} {obj}'s")

print("I have ", new_list[2], new_list[1])


jell = new_list[3][2]
print(jell)
print(f"I like {jell} on my toast")


print(new_list[2])
print(new_list[-1])


print(new_list[:3])

for item in new_list[:3]:
  print(item)

new_list[0]= 'banana'
print(new_list)
