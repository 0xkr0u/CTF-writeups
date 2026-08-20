# Trivial Flag Transfer Protocol
### Walkthough: 
<url>
<li> Cant lie, i was really confused in this one. </li>
<li> So we have a pcap file that has a network capture. </li><br>
<img width="1920" height="1080" alt="wireshark" src="https://github.com/user-attachments/assets/d2e8fecd-67b3-4482-9bf6-9e8037729ac6" />
<li>So as you can realize, we can see tftp which means there are some files being extracred. (protocol of FTP but for small unauthenticated/unencrypted traffic) </li>
<li> So i decided, why dont i just take all files being transfered and see whats going on.</li><br>
<img width="1920" height="1080" alt="tftp_capture" src="https://github.com/user-attachments/assets/0643aefd-233f-436f-a339-ebabb51378f1" />
<li>We extract all items using that and we see 3 pics, 1 program and some texts. Well, Spoilers (The encryption is a ceaser cipher)</li>
<li>So i thought, what if, i could see what the program.deb does and see if i can be able to understand wht the program did to the pictures. Below is the workflow of commands used </li>

```bash
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> ls
decodedText.txt  instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> cat *txt    
instructions.txt: TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
map.txt: IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> echo "Password: DUEDILIGENCE"
Password: DUEDILIGENCE
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> ls
decodedText.txt  instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> dpkg -x ./program.deb $(pwd)
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> ls
decodedText.txt  instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb  usr
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> cd usr  
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump/usr> ls
bin  share
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump/usr> cd bin
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump/usr/bin> ls
steghide
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump/usr/bin> echo "See steghide ? know what that means ? yes, there was a text or file inside this images"
See steghide ? know what that means ? yes, there was a text or file inside this images
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> ls
decodedText.txt  instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb  usr
PS /home/kr0u/Work/BlueTeam/Cylab/Forensics/TrivialFlagTransferProtocol/FileDump> steghide extract -sf ./picture3.bmp
Enter passphrase: 
wrote extracted data to "flag.txt".

```
<li> See where there is picture3.bmp, i was looking so hard at 1 and when i gave up i just started going rogue and looking at all the pictures and bruteforcing all pictures </li>
<li>gladly it worked</li>

you will get your flag once you you `cat flag.txt`

</ul>

# WAS A GOOD ONE!!!!
