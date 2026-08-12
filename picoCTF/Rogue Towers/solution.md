# Rogue Towers Writeup

So we are presented with a particular `.pcap` file that should be able to help us identify a unusual behavior in the network.
So to begin ,we can use our who...what questions

[1] what is happening? Normal traffic till we see many `POST` requests <br>
[2] why is it happening ? `exfiltration of base64 strings` <br>
[3] who is doing it ? `IP address: 10.100.55.55` <br>
[4] what is being exfiltration ? `encoded strings` <br>
derived questions: <br>
[5] Where is this server posting to ? '198.51.100.244'<br>
[6] Any suspicous request headers? `user agent anomaly detection.` <br>

Now we begin scraping exfiltration of the data taken out <br>
```bash
R1xbW3pnd
khFBV9BCm
xTAFtZZ0A
JRANBaAIB
BloEAQUAS
A==
```

*After a long search of answers i was stuck so i took a hint and i saw the decoding element was going to be a DERIVATIVE of the imsi * <br>
OK so, i made a code to automatically decode it 


```python3
import enum
import base64
import itertools


# CONFIGURATION!!!!!!!!!!!!!!!!!!!!!!!!
ciphertext = base64.b64decode("[ Your base64 code comes here  ]")
imsi = "310410275849303"
byteValue = imsi.encode()

storage = []
print("[*] Storing Values")
for j in range(1,len(imsi)):
    combinations  = itertools.combinations(imsi,j)
    for i in combinations:
        Cvalue = "".join(i)
        storage.append(Cvalue)
print(f"[*] Storage Length: {len(storage)}")

for i in storage:
    Ckey = i
    CEkey = i.encode()
    Bforce = bytes(c ^ CEkey[k % len(CEkey)] for k, c in enumerate(ciphertext))
    flag = b'picoCTF'
    if flag.lower() in Bforce.lower():
        print(f"[!] flag sniffed: {Bforce.decode(errors="ignore")}")
        print(f"[!] Key used: {i}")
print("================== Hopefully it worked ================")

```


and you will get the flag

Explanation of the code: 
[Used ai for this one:  make a temp list of posible combinations of imsi-> byte of current imsi_possible_combination then xor with byte of the flag -> then look for possible ones that produce picoCTF]

```txt
What the Code Does
Fetch inputs
You start with a Base64‑encoded ciphertext.
You also have an IMSI string ("xxxxxxxxxxxx").
Generate candidate keys
You build a list (storage) of possible key strings by taking combinations of digits from the IMSI.
Each combination is joined into a string, then stored.
Try each key
For each candidate key:
Convert it to bytes (CEkey).
Loop through the ciphertext with enumerate().
For each ciphertext byte c, pick the corresponding key byte using CEkey[k % len(CEkey)].
This cycles through the key repeatedly.
XOR the ciphertext byte with the key byte.
Collect the results into a new byte string (Bforce).
Check for flag
If the decrypted output contains "picoCTF", you print the result and the key that produced it.
```
