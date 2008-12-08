import pickle

class A:
  value = "value"
  
a = A()
b = []
b.append(a)

output = open("test.txt", "wb")
pickle.dump(b, output)
output.close()
