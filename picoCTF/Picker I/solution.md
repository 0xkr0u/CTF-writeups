# Picker I
So you download a file and you just need to think of how to get the flag by exploiting a flaw in the code.<br>
Now when you see the code, you can start by looking for any logic that fetches the flag. <br>
In the file you realize win() is the only one that has it, which makes me wonder, how can we run the function.
Later down there you can see a eval() = > processing the input which is our flaw here.
We need to ensure the function win() is our  input <br>

### Python code:
``` python
def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
  
```

### User interaction section of the code:
```python
while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
  except Exception as e:
    print(e)
    break

```

you then enter win() in the netcat connection, and you will get a flag in hex code.

place it in a payload.txt, install this:<a href="https://github.com/0xkr0u/CTF-writeups/blob/main/picoCTF/ASCII_Numbers/HexConversion.py"> HexConversion.py </a>then change the path of the file location of the `payload.txt` and you will get your flag.


## Thank you!!!
