n=int(input("rows:"))
print("right angled pyramid with triangle")
for i in range(n):
    for j in range(i+1):
        letter=chr(65+j)
        print(letter,end="")

    print()
