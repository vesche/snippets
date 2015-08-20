n,c=input(),0;print n,
while n!=int(str(n)[::-1]):n,c=n+int(str(n)[::-1]),c+1
print"gets palindromic after %d steps: %d"%(c,n)
