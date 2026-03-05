# Wireshark doo dooo do doo...
Tools used to analyze this is:<br>
1. ```Wireshark```
2. ```www.dcode.fr (site)```
3. ```eyes```
4. ```Brain (Most importantly)```

### Wireshark
1. open Wireshark
2. ``` ctrl + o``` & open the file that you downloaded.

as we can see, We need to get some clear definitions of things.<br>
Main protocols are ```tcp``` and ```http```. <br> 
we can start by looking at basic things like text packets.<br>
there are only two text documents in which we find interesting things in the data section for:<br>

```Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}\n```
Doesn't that say something about this string ? possibly ceaser cipher <br>
we can use ```https://www.dcode.fr/caesar-cipher```
which is gonna be the best ceaser cipher site for things like this.<br>

scan through the results and you might see it. 

and we got out flag:
```bash
picoCTF{p33kab00_1_s33_u_deadbeef}
```
# 0xKr0u HAS PWNED THIS LAB
