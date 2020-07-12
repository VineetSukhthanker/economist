i=0
x = 2017
y = int(input("Type years\n"))
s = float(input("current GDP\n"))
g = float(input("average growth rate\n"))
r = s
while i<y:
    r += (r*g)/100
    i = i+1
    x = x+1
    print("%d : %f" %(x,r))


