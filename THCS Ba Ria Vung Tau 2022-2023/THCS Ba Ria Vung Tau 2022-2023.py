#B1
fi = open("TENBAI.INP")
n =int( fi.readline())
m =int( fi.readline())
s=m+n

fo = open("TENBAI.OUT", "w")
fo.write(f'{s}')
fo.close()

