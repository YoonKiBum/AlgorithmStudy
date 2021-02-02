word = input()
word += " "
count = 0
for i in range(len(word)-1):
    if word[i] != " " and word[i+1] == " ":
        count += 1

print(count)
