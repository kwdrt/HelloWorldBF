#Text to Brainfuck
#

text = input()
print(text)
res =""
for i in range(len(text)):
    res = res + (ord(text[i])*'+')
    res = res + (".>")

print(res)
