# Silent Stream

so we are presented by a `.pcap` and a `.py`.<br>For the `pcap` you can see data streams that are barely readable:
<img width="1920" height="1080" alt="Screenshot_2026-08-28_17-03-15" src="https://github.com/user-attachments/assets/7c93de22-e710-4b92-8ddd-3c8ec7f57c0e" />
but we can see from the other a file a particular code on how it was encrypted:
```python
import socket

def encode_byte(b, key):

    return (b + key) % 256

def simulate_flag_transfer(filename, key=42):
    print(f"[!] flag transfer for '{filename}' using encoding key = {key}")

    with open(filename, "rb") as f:
        data = f.read()

    print(f"[+] Encoding and sending {len(data)} bytes...")

    for b in data:
        encoded = encode_byte(b, key)
        pass

    print("Transfer complete")

if __name__ == "__main__":
    simulate_flag_transfer("flag.txt") 

```

### Map:<br>
<b> Encoding:
<li>Read `flag.txt` => encode using (b+key)%256 => send packet</li><br>
<b> Decoding:</b>
<li>Read flag.txt => decode using (b-key)%256 => retrieve packet</li><br>

so the decoding script would look like this:
```python
import socket

def decode_byte(b, key):

    return (b - key) % 256

def simulate_flag_transfer(filename, key=42):
    print(f"[!] flag transfer for '{filename}' using encoding key = {key}")

    with open(filename, "rb") as f:
        data = f.read()

    print(f"[+] Decoding and sending {len(data)} bytes...")
    storage=[]
    for b in data:
        decoded = decode_byte(b, key)
        storage.append(decoded)
        pass
    result = bytes(storage)
    with open("file",'wb') as f:
        f.write(result)

    print("Transfer complete")

if __name__ == "__main__":
    simulate_flag_transfer("flag.txt") 


```



Now we need to create flag.txt (raw traffic streams )

in here i will use `tshark => cyberchef (from hex)=> save file`

```bash
tshark -r packets.pcap -Y "tcp.len>0" -T fields -e data.data > traffic.txt
```

upload traffic.txt to cyberchef then use `from hex` to decode the hex data in `traffic.txt` save the output as a file and name it `flag.txt`
Now we have the item that was exfiltrated. 
now to recreate the file that was transmitted<br>Now run the decode program: 

```bash
kr0u@kr0u-Coral ~/W/B/C/R/SilentStream> file file 
file: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 800x500, components 3
```
Here is the file that we create from reading the decoded bytes from `flag.txt` to `file`.
This means that file is a image, we can view it from the file manager:
<img width="800" height="500" alt="file" src="https://github.com/user-attachments/assets/4248b8bf-e170-4239-bea5-a80431cb6a47" />

Now we have our image that contains the flag. 


# Solved


