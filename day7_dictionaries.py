message=input(">")
words=message.split(' ')
emojis={":)":"☺️",
        ":(":"🙁",
        ":P":"😛",
        ">w<":"😖"}
output=""
for i in words:
    output+=emojis.get(i,i)+" "
print(output)
