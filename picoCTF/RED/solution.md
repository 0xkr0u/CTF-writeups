Before we begin, i would really love to  start by saying that this was a hard but terrible ctf <br>
but we can still proceed anyways. <br>

so we have a our file red.png<br>
As always, we can use binwalk, file and exiftool to check for any interesting info<br>

### Binwalk: <br>
```bash
 binwalk red.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 128 x 128, 8-bit/color RGBA, non-interlaced
284           0x11C           Zlib compressed data, default compression
```
### File:
```bash
file red.png
red.png: PNG image data, 128 x 128, 8-bit/color RGBA, non-interlaced
```

### exiftool: <br>
```bash
exiftool red.png
ExifTool Version Number         : 12.57
File Name                       : red.png
Directory                       : .
File Size                       : 796 bytes
File Modification Date/Time     : 2026:03:03 15:43:32+03:00
File Access Date/Time           : 2026:03:03 00:00:00+03:00
File Inode Change Date/Time     : 2026:03:03 15:43:34+03:00
File Permissions                : -rwxr-xr-x
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 128
Image Height                    : 128
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
Image Size                      : 128x128
Megapixels                      : 0.016
```

So i tried taking my first outcome as my decision maker.<br>
and i tried to unzip the document using the following command from dd since steghide doesnt accept png i think. <br>
```bash
dd if=red.png of=red.zlib skip=284 bs=1 
512+0 records in
512+0 records out
512 bytes copied, 0.496899 s, 1.0 kB/s
```
so i thought that the document was holding important information and decided to print some of it:
```bash
strings red.zlib
IEND
```

Holding the string can be so important after <br>
