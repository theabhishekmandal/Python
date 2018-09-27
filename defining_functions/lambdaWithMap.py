rupees = [10, 20, 100]

dollars = map(lambda x : x / 64, rupees)

print(" ".join(str(i) for i in dollars))
print(str(dollars))
print(repr(dollars))
