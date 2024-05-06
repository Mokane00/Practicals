def myst(L):
 return 0 if not L else L[0] + myst(L[1:]) # Use ternary expression



print(myst("Tsolo"))