# Lets conquer this room

First and foremost we know that it is a web so we need to define our goal as early as possible. <br>
So we can start with looking into nmap and looking for open ports. <br>
# Network Scan
## Noblecrow:
```bash
--- Noble Crow Port Scanner ---
Use responsibly and only on authorized networks.
Enter target host (e.g., 127.0.0.1, google.com) [127.0.0.1]: 10.113.133.209
Enter port range (e.g., 1-1000) [1-65535]: 
Enter connection timeout in seconds [1]: 
Enter number of threads (e.g., 10, 50 for faster scan) [10]: 50

Scanning 10.113.133.209 from port 1 to 65535 with 50 threads and 1s timeout...
----------------------------------------
Port 8081: OPEN
Port 31331: OPEN
```

## Nmap
### TCP
```bash
PORT     STATE    SERVICE
21/tcp   open     ftp
22/tcp   open     ssh
| ssh-hostkey: 
|   3072 2c16bbd75c98fd2d46669d5af19ba07f (RSA)
|   256 25739e3cda8ee9758f0d4a18f519d133 (ECDSA)
|_  256 8bf9d4ebec7e1bda5c8e4ee1bacae4c0 (ED25519)
82/tcp   filtered xfer
8081/tcp open     blackice-icecap
```
### UDP
```bash
PORT      STATE         SERVICE
68/udp    open|filtered dhcpc
21383/udp open|filtered unknown
48761/udp open|filtered unknown
```

### Service scan & version:
```bash
10:20:16 kr0u@penguin ultratech1 → nmap -sV -p 21,22,82,8081,68,31331 $ip
Starting Nmap 7.93 ( https://nmap.org ) at 2026-03-08 22:21 EAT
Nmap scan report for 10.113.133.209
Host is up (0.25s latency).

PORT      STATE  SERVICE VERSION
21/tcp    open   ftp     vsftpd 3.0.5
22/tcp    open   ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
68/tcp    closed dhcpc
82/tcp    closed xfer
8081/tcp  open   http    Node.js Express framework
31331/tcp open   http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```



