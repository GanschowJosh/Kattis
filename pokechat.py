import re
encodingString = input()
indicesString = input()
indices = re.findall('...', indicesString)
for index in indices:
    print(encodingString[int(index) - 1], end="")