file = "/home/kr0u/Workstation/Cylab/BinExploit/HexList.txt"
with open(file,'r') as f:
    word = f.readlines()

wordList = list(word)
storage = []
for i in range(0,len(wordList[0]),5):
    storage.append(f"{wordList[0][i]}{wordList[0][i+1]}{wordList[0][i+2]}{wordList[0][i+3]}")

flag = []
for i in storage:
    value = int(i,16)
    flag.append(chr(value))

print("".join(flag))