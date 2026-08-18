# Forensics Git 1 writeup 
<li> So we have disk.img.gz and we want to get the flag.</li> <br><ul><li> The first thing we have in mind is that its a Git challenge meaning you need some knowledge on how git works </li>
<li> We can decompress the file `disk.img.gz` </li>
  
  ```bash
  7z x disk.img.gz
  ```
</ul>   
Now we have a  fresh file that we need to work on.<br>But we can start by recon and seeing what the file is.<br>

```bash
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> file disk.img
disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x2,0,33), end-CHS (0x263,8,56), startsector 2048, 614400 sectors; partition 2 : ID=0x82, start-CHS (0x263,8,57), end-CHS (0x3ff,15,63), startsector 616448, 524288 sectors; partition 3 : ID=0x83, start-CHS (0x3ff,15,63), end-CHS (0x3ff,15,63), startsector 1140736, 956416 sectors
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000616447   0000614400   Linux (0x83)
003:  000:001   0000616448   0001140735   0000524288   Linux Swap / Solaris x86 (0x82)
004:  000:002   0001140736   0002097151   0000956416   Linux (0x83)
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> 

```
<li>from the code above, its sure to show that we have a different offset that may cause issues when tools try to parse the partitions.
so we can start curving/sculpting the two linux partitions.<br><li>
  
```bash
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> dd if=disk.img of=part1.img skip=2048 count=614400
614400+0 records in
614400+0 records out
314572800 bytes (315 MB, 300 MiB) copied, 2.845 s, 111 MB/s
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> dd if=disk.img of=part3.img skip=1140736 count=956416
956416+0 records in
956416+0 records out
489684992 bytes (490 MB, 467 MiB) copied, 5.23968 s, 93 MB/s
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> ls
disk.img  disk.img.gz  notes.txt  part1.img  part3.img
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> mkdir part1 part3 
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> ls
disk.img  disk.img.gz  notes.txt  part1/  part1.img  part3/  part3.img
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> mv part1.img part1 && mv part3.img part3
kr0u@kr0u-Coral ~/W/B/C/Forensics_Git_1_FORENSICS> ls
disk.img  disk.img.gz  notes.txt  part1/  part3/
```

<li>So now we have folders to work with, `part1` and `part3`</li>

```bash
kr0u@kr0u-Coral ~/W/B/C/F/part3> fls -r part3.img > part3.txt
kr0u@kr0u-Coral ~/W/B/C/F/part3> fls -m / -d -r part3.img > part3.txt
kr0u@kr0u-Coral ~/W/B/C/F/part3> mactime -b part3.txt -d > part3.csv
Old package separator "'" deprecated at /usr/bin/mactime line 154.
Old package separator "'" deprecated at /usr/bin/mactime line 167.
kr0u@kr0u-Coral ~/W/B/C/F/part3> 
```
<li> Now we have a CSV that is def supposed to help us find out the files compared with time</li>

```csv
Wed Nov 19 2025 12:20:05,160,m.cb,r/rr--r--r--,1000,1000,65709,"/home/ctf-player/Code/secrets/.git/objects/5f/b8194539c770a830b8ba089a50778c07072b03"
Wed Nov 19 2025 12:20:31,160,.a..,r/rr--r--r--,1000,1000,65709,"/home/ctf-player/Code/secrets/.git/objects/5f/b8194539c770a830b8ba089a50778c07072b03"
```

<li>Wasn't sure why this file came twice so i wondered what its contents are</li>
<li>We need a file system we can use right ? Command below should help.

```bash
kr0u@kr0u-Coral ~/W/B/C/F/part3> binwalk -e part3.img 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, blocks count: 478208, image size: 489684992, rev 1.0, ext4 filesystem data, UUID=7a00e9da-98f8-4f0f-b257-95edf422f422

kr0u@kr0u-Coral ~/W/B/C/F/part3> ls
_part3.img.extracted/  part3.csv  part3.img  part3.txt
kr0u@kr0u-Coral ~/W/B/C/F/part3> 

```
<li>We have `_part3.img.extracted` to work with. why dont we go back to the folder that made us curious. </li>

```bash
kr0u@kr0u-Coral ~/W/B/C/F/p/_/e/h/c/C/s/.g/o/5f (GIT_DIR!)> ls
b8194539c770a830b8ba089a50778c07072b03
kr0u@kr0u-Coral ~/W/B/C/F/p/_/e/h/c/C/s/.g/o/5f (GIT_DIR!)> git show b
fatal: ambiguous argument 'b': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
kr0u@kr0u-Coral ~/W/B/C/F/p/_/e/h/c/C/s/.g/o/5f (GIT_DIR!) [128]> git show b8194539c770a830b8ba089a50778c07072b03
kr0u@kr0u-Coral ~/W/B/C/F/p/_/e/h/c/C/s/.g/o/5f (GIT_DIR!)> git show 5fb8194539c770a830b8ba089a50778c07072b03
commit 5fb8194539c770a830b8ba089a50778c07072b03 (HEAD -> master)
Author: ctf-player <ctf-player@example.com>
Date:   Wed Nov 19 09:20:05 2025 +0000

    Remove flag

diff --git a/flag.txt b/flag.txt
deleted file mode 100644
index f150f47..0000000
--- a/flag.txt
+++ /dev/null
@@ -1 +0,0 @@
{You will get the flag here}
\ No newline at end of file
```

# And you got your flag.
