## Reverse Engineering 101
To crack this you may need the following tools:
```
ghidra
wine (if you are on linux)
```
so if you are ready with the tools, lets begin <br>
unzip the file using the password in <a href="../README.md"> README.md </a> 
We begin by importing our file to ghidra
<img width="1920" height="1039" alt="import_file" src="https://github.com/user-attachments/assets/b1d640d9-e7fe-4079-90e6-ce37dad4cdf8" />
<img width="1920" height="1039" alt="main_selection" src="https://github.com/user-attachments/assets/39c58cf3-a818-4b33-aa12-943acf50dbb0" />

so in ghidra we can go to the main seletion tab and view the guessed decompiled code <br>
<b>yes, ghidra will not be able to bring back the code as is so what it does is that it guesses wat the original code may have looked like before compiling </b><br>
so on the right tab we have what ghidra may be thinking is our code and we can paste the code on sublime text for easier track of the readability.<br>

{snippet of the code}
<img width="1922" height="1041" alt="code_preview" src="https://github.com/user-attachments/assets/0d94ad6f-7785-4586-a208-945a994f4386" />

now we can translate the readable words and process what is expected if it becomes easier:
{translation image}
<img width="1922" height="1041" alt="translarion_and_process" src="https://github.com/user-attachments/assets/8a834fa5-d903-40e4-9dce-20eeadee4e29" />

We can try the password from our verdict: ```password: 1234```
{succesful image}
<img width="914" height="627" alt="succesfull_output" src="https://github.com/user-attachments/assets/71ec5c41-49c0-47f9-ba08-05655cc3af0e" />

# PWNED
