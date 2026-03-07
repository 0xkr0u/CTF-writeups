# Documentation for the wireshark network forensics.

protocols used <br>
ip, arp, tcp, http, TLS, dns <br>
```Encapsulation:``` arp, ip, tcp, tls, http, dns <br>


## top 10 outputs from the protocols
### ARP
```bash
sudo tshark -r shark2.pcapng -Y "arp" | head -n 10

3318  17.530380 02:fb:68:4c:e9:41 → Broadcast    ARP 56 Who has 192.168.38.104? Tell 192.168.38.1
3319  17.530392 MS-NLB-PhysServer-32_1b:c6:1a:ae:f5 → 02:fb:68:4c:e9:41 ARP 42 192.168.38.104 is at 02:3b:c6:1a:ae:f5
```
IP : Mac
192.168.38.1: 02:fb:68:4c:e9:41
192.168.38.104 :MS-NLB-PhysServer-32_1b:c6:1a:ae:f5

### IP

```bash
sudo tshark -r shark2.pcapng -Y "ip" | grep -ioE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" | sort | uniq
169.254.169.254
18.217.1.57
192.168.38.103
192.168.38.104
192.168.38.105
216.58.194.196
8.8.8.8
```

### TCP
```bash
sudo tshark -r shark2.pcapng -Y "tcp" |   head -n 10

    1   0.000000 192.168.38.104 → 192.168.38.105 TCP 54 63631 → 8412 [FIN, ACK] Seq=1 Ack=1 Win=8394 Len=0
    2   0.000380 192.168.38.105 → 192.168.38.104 TLSv1.2 78 Application Data
    3   0.000430 192.168.38.104 → 192.168.38.105 TCP 54 63631 → 8412 [RST, ACK] Seq=2 Ack=25 Win=0 Len=0
    4   0.000458 192.168.38.105 → 192.168.38.104 TCP 54 8412 → 63631 [FIN, ACK] Seq=25 Ack=2 Win=227 Len=0
    5   0.003036 192.168.38.104 → 192.168.38.105 TCP 66 63633 → 8412 [SYN] Seq=0 Win=62727 Len=0 MSS=8961 WS=256 SACK_PERM
    6   0.003348 192.168.38.105 → 192.168.38.104 TCP 66 8412 → 63633 [SYN, ACK] Seq=0 Ack=1 Win=26883 Len=0 MSS=8961 SACK_PERM WS=128
    7   0.003403 192.168.38.104 → 192.168.38.105 TCP 54 63633 → 8412 [ACK] Seq=1 Ack=1 Win=2150400 Len=0
    8   0.004374 192.168.38.104 → 192.168.38.105 TLSv1 571 Client Hello
    9   0.004602 192.168.38.105 → 192.168.38.104 TCP 54 8412 → 63633 [ACK] Seq=1 Ack=518 Win=28032 Len=0
   10   0.007436 192.168.38.105 → 192.168.38.104 TLSv1.3 1420 Server Hello, Change Cipher Spec, Application Data, Application 
```



### TLS

```bash
sudo tshark -r shark2.pcapng -Y "tls" |   head -n 10
    2   0.000380 192.168.38.105 → 192.168.38.104 TLSv1.2 78 Application Data
    8   0.004374 192.168.38.104 → 192.168.38.105 TLSv1 571 Client Hello
   10   0.007436 192.168.38.105 → 192.168.38.104 TLSv1.3 1420 Server Hello, Change Cipher Spec, Application Data, Application Data, Application Data, Application Data, Application Data
   11   0.008274 192.168.38.104 → 192.168.38.105 TLSv1.3 118 Change Cipher Spec, Application Data
   13   0.049431 192.168.38.104 → 192.168.38.105 TLSv1.3 495 Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data
   15   0.053117 192.168.38.105 → 192.168.38.104 TLSv1.3 219 Application Data
  178   2.398279 192.168.38.104 → 216.58.194.196 TLSv1 634 Client Hello
  180   2.399809 216.58.194.196 → 192.168.38.104 TLSv1.3 266 Server Hello, Change Cipher Spec, Application Data
  181   2.401254 192.168.38.104 → 216.58.194.196 TLSv1.3 118 Change Cipher Spec, Application Data
  182   2.401491 192.168.38.104 → 216.58.194.196 TLSv1.3 146 Application Data
```


### HTTP

```bash
08:26:26 kr0u@penguin investigation → sudo tshark -r shark2.pcapng -Y "http" | grep -i "text" | head -n 10
Running as user "root" and group "root". This could be dangerous.
   57   1.541467  18.217.1.57 → 192.168.38.104 HTTP 289 HTTP/1.0 200 OK  (text/html)
  744   4.819777  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 1550   8.579695  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 1624   9.262103  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 1688   9.791664  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 1770  10.294677  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 1905  10.786051  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 1963  11.290115  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 2025  11.741040  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
 2067  12.156371  18.217.1.57 → 192.168.38.104 HTTP 263 HTTP/1.0 200 OK  (text/html)
```

the text responses may contain something so we can be able to open this in wireshark specifically.<br>

### DNS
```bash
08:30:35 kr0u@penguin investigation → sudo tshark -r shark2.pcapng -Y "dns"| head -n 10
Running as user "root" and group "root". This could be dangerous.
  791   7.931626 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x76aa A lDqoR16q.reddshrimpandherring.com
  792   7.943025      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x76aa No such name A lDqoR16q.reddshrimpandherring.com SOA a.gtld-servers.net
  793   7.947216 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcdd5 A lDqoR16q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  794   7.957680      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xcdd5 No such name A lDqoR16q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
  795   7.958549 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5d2d A lDqoR16q.reddshrimpandherring.com.windomain.local
  796   7.967998      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5d2d No such name A lDqoR16q.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
  797   7.968981 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc847 A 1Th0dQuT.reddshrimpandherring.com
  798   8.049550      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc847 No such name A 1Th0dQuT.reddshrimpandherring.com SOA a.gtld-servers.net
  799   8.050527 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x21a5 A 1Th0dQuT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  800   8.061483      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x21a5 No such name A 1Th0dQuT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
  ```
  We can collect all domians from this:
``` 
  Domains → Subdomians → any files
```
Domains:
```bash
08:35:58 kr0u@penguin investigation → sudo tshark -r shark2.pcapng -Y "dns" | grep -iEo "reddshrimpandherring.com" | sort | un
iq
Running as user "root" and group "root". This could be dangerous.
reddshrimpandherring.com
```
subdomains:

```bash
08:40:54 kr0u@penguin investigation → sudo tshark -r shark2.pcapng -Y "dns" | grep -iEo "reddshrimpandherring.com[0-9a-zA-Z.-]
+" | sort | uniq

reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
reddshrimpandherring.com.windomain.local
```
compiled:

```bash
reddshrimpandherring.com
reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
reddshrimpandherring.com.windomain.local
```

subdomians: reddshrimpandherring.com
```bash

05lusaWy.reddshrimpandherring.com
0bLbK94Z.reddshrimpandherring.com
0gHMI0EI.reddshrimpandherring.com
1FjuRiR8.reddshrimpandherring.com
1.reddshrimpandherring.com
1Th0dQuT.reddshrimpandherring.com
282DOxFJ.reddshrimpandherring.com
2a3XH03l.reddshrimpandherring.com
2DA0w7Jt.reddshrimpandherring.com
2fHPxt2H.reddshrimpandherring.com
2Gu7zRXL.reddshrimpandherring.com
2VPCMWzB.reddshrimpandherring.com
2vy.reddshrimpandherring.com
30d1RFWu.reddshrimpandherring.com
32eplH1b.reddshrimpandherring.com
3dTlY7.reddshrimpandherring.com
3Dz6rCU.reddshrimpandherring.com
3gEtiL6U.reddshrimpandherring.com
3.reddshrimpandherring.com
3U.reddshrimpandherring.com
44ujVBuF.reddshrimpandherring.com
48b4iU01.reddshrimpandherring.com
5FALrYGV.reddshrimpandherring.com
5ga9YWjo.reddshrimpandherring.com
5HyMGCS6.reddshrimpandherring.com
5lZkiKa3.reddshrimpandherring.com
5r2f.reddshrimpandherring.com
5ShcZekS.reddshrimpandherring.com
5yYuuf.reddshrimpandherring.com
60aidRgy.reddshrimpandherring.com
6iKi0zDD.reddshrimpandherring.com
6tNHEBtX.reddshrimpandherring.com
		...
YQoNqdqR.reddshrimpandherring.com
YQuKySPc.reddshrimpandherring.com
ysnuBebx.reddshrimpandherring.com
YuvBSCsM.reddshrimpandherring.com
YWRiZWVm.reddshrimpandherring.com
yXzo0cCL.reddshrimpandherring.com
Yz2l3aBW.reddshrimpandherring.com
Z5hJZHyn.reddshrimpandherring.com
zEBnIu8y.reddshrimpandherring.com
Zf688UTz.reddshrimpandherring.com
ZLRLdSKq.reddshrimpandherring.com
Zn2Gq.reddshrimpandherring.com
ZnR3X2Rl.reddshrimpandherring.com
zpt1YuKN.reddshrimpandherring.com
ZSdLCe14.reddshrimpandherring.com
```
















## RESEARCHED QUESTIONS DURING THE INVESTIGATION
```

#What does a tcp do, why is it important and what information is really needed for a forenics aspect and network security engineer aspect.  
#who configures the tcp
#if a network engineer should be able to configure a tcp then where should someone learn it 
#when someone is investigating a tcp file what should he look for 
#why is there an occurence of using two versions to get the Application data"
15   0.053117 192.168.38.105 → 192.168.38.104 TLSv1.3 219 Application Data
and 
2   0.000380 192.168.38.105 → 192.168.38.104 TLSv1.2 78 Application Data"


```
