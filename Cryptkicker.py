given = "the quick brown fox jumps over the lazy dog"
n = int(input("Enter no. of strings: "))
st_list = []
for i in range(n):
    s = input("Enter string " + str(i + 1) + " : ")
    st_list.append(s)

d = {}
for i in st_list:
    if len(given) == len(i):
        d.clear()  # Clear the dictionary for each new string
        for j in range(len(i)):
            d[i[j]] = given[j]

op_list = []
for i in st_list:
    st = ""
    for j in i:
        if j == " ":
            st += " "
        else:
            st += d.get(j, j)  # Use get method to handle characters not found in the dictionary
    op_list.append(st)

for i in op_list:
    print(i)
