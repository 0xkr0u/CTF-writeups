# CRYPTOGRAPHY & CRACKING  
## Theory
So we start of with hashcrack that will touch on cryptography and cracking <br>
and before we start i would like to teach a bit about this task.<br>
lets create a scenario where a company has been breached and all you can see is some random strings like: ``` 482c811da5d5b4bc6d497ffa98491e38 ``` weird right ?<br>
we can have the liberty of cracking all of them or have a separate {hash algorithm} wordlist for your breached database (recommended). <br>

<br><br>
## Task
We have been tasked with connecting to the lab's instance.<br>
we should connect to the instance using the code provided: <br>
```bash
nc verbal-sleep.picoctf.net 61141
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash:
```

Tools that can be used in this scenario would be john and hashcat <br>
in this case i will be using hashcat <br>
the most basic hashcat command is <br>
```bash
hashcat -m <hash_type> -a <attack_mode> <hash_file> <wordlist>
```

in my case we can look for the -m for md5 and the -a for the attack mode <br>

-m:<br>
```bash
cat manual_hashcat.txt | grep -i md5
      0 | MD5                                                        | Raw Hash
            ....
```

-a: <br>
```bash
cat manual_hashcat.txt | grep -i "a 0"
  Wordlist         | $P$   | hashcat -a 0 -m 400 example400.hash example.dict
  Wordlist + Rules | MD5   | hashcat -a 0 -m 0 example0.hash example.dict -r rules/best64.rule
```

from the example we can also continue the hashcat command. (make sure you have your hash.txt and the dictionary in the comand)<br>
```bash
hashcat -a 0 -m 0 hash.txt ~/kr0u/Wordlists/SecLists-master/Passwords/Leaked-Databases/rockyou-75.txt
Dictionary cache built:
* Filename..: ~/kr0u/Wordlists/SecLists-master/Passwords/Leaked-Databases/rockyou-75.txt
* Passwords.: 59186
* Bytes.....: 478936
* Keyspace..: 59186
* Runtime...: 1 sec

482c811da5d5b4bc6d497ffa98491e38:password123
```
We have our cracked password: password123

```bash
We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!
```
Now we can continue with the next task with out knowledge on modes and attack modes <br>
And we can see just about the same result:

```bash
Dictionary cache hit:
* Filename..: ~/kr0u/Wordlists/SecLists-master/Passwords/Leaked-Databases/rockyou-75.txt
* Passwords.: 59186
* Bytes.....: 478936
* Keyspace..: 59186

b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3:letmein
```

one last:
```bash
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745:qwerty098
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1400 (SHA2-256)
Hash.Target......: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad...697745
Time.Started.....: Mon Mar  2 21:58:27 2026 (30 secs)
Time.Estimated...: Mon Mar  2 21:58:57 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   603.8 kH/s (0.28ms) @ Accel:256 Loops:1 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 596992/14344384 (4.16%)
Rejected.........: 0/596992 (0.00%)
Restore.Point....: 596480/14344384 (4.16%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: radom1 -> quehago
```
i had to use the full hashfile for this one.<br>
```bash
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found. 
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4de57566}
```

perfect!! <br>

# 0xkr0u Pwned the lab
