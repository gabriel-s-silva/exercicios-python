X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

resultado = [[0,0,0],
            [0,0,0],
            [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       resultado[i][j] = X[i][j] + Y[i][j]

for r in resultado:
   print(r)
def CamelCase(frase):
   frase = frase.title()
   frase = frase.replace(' ', '')
   return frase

