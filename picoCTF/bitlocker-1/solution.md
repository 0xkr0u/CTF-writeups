# Bitlocker-1 

Greetings r34d3r, so we are brought up with an disk image file `.dd` and we need to get the file contents inside it. You may need the following knowledge to be able to operate through this lab
<li>bitcracker - finds bitlock password hash entries that will be used later during decryption</li>
<li>Cracking hashes - cracking hashes using bitlocker mode and a wordlist</li>
<li>Dislocker - create a dislocker-file that will be used to be mounted in the local fs </li>
<li>Mounting filesystems - obv from above </li>

Ok, to get started, 
### Instalation:

BitCracker: <a href="https://github.com/e-ago/bitcracker"> Bitcracker GitHub Link </a>
Hashcat: `sudo apt install -y hashcat`
dislocker: `sudo apt install -y dislocker`
<br>
Now that we have the tools setuip we can start by running Bitcracker on the `.dd` file:
### bitcracker
```bash 
$bitcracker -i bitlocker-1.dd 
```
Now we have the below as our files.
```txt
hash_recv_pass.txt  hash_user_pass.txt
hash_recv_pass.txt: $bitlocker$2$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
hash_user_pass.txt: $bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
```
so now we can get straight on to hashcat
### Hashcat
```bash
Command:  hashcat -m 22100 -a 0 hash_user_pass.txt /usr/share/wordlists/SecLists-master/Passwords/Leaked-Databases/rockyou.txt
~/W/B/C/F/Bitlocker1> hashcat -m 22100 -a 0 hash_user_pass.txt /usr/share/wordlists/SecLists-master/Passwords/Leaked-Databases/rockyou.txt --show
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d: {password will be here}
```

### Dislocker&Mount:
```bash
sudo mkdir -p /media/Bitlocker-1/Dislocker-location/
sudo mkdir -p /media/Bitlocker-1/mount-location/
sudo dislocker -V bitlocker-1.dd -u{password here and no space from -u} -- /media/Bitlocker-1/Dislocker-location/
sudo mount -o loop /media/Bitlocker-1/Dislocker-location/dislocker-file /media/Bitlocker-1/mount-location/
```

We have finally mounted the file and we can see our flag print out:

```bash
kr0u@kr0u-Coral ~/W/B/C/F/Bitlocker1> ls /media/bitlocker-mount/
 '$RECYCLE.BIN'/   'System Volume Information'/   flag.txt*
kr0u@kr0u-Coral ~/W/B/C/F/Bitlocker1> cat  /media/bitlocker-mount/flag.txt
{You will get your flag here}⏎
```

# SOLVED
