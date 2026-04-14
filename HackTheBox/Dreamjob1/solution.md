# Solution for dreamjob 1
we can download the file and unzip using ```7z x <filename>``` with the password ```hacktheblue``` as always
we get an unzipped ```IOCs.txt```
contents:
```
cat IOCs.txt
1. 7bb93be636b332d0a142ff11aedb5bf0ff56deabba3aa02520c85bd99258406f
2. adce894e3ce69c9822da57196707c7a15acee11319ccc963b84d83c23c3ea802
3. 0160375e19e606d06f672be6e43f70fa70093d2a30031affd2929a5c446d07c1
```
the task essentialy wants us to be able to know how to use ```MITRE ATT$CK``` and ```VirusTotal``` and idenitfy who , when, how or what has been used during an attack 
We can begin with Virus total
<table>
  <thead>
    <tr>
      <th>MD5</th>
      <th>Name</th>
      </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        7bb93be636b332d0a142ff11aedb5bf0ff56deabba3aa02520c85bd99258406f
      </td>
      <td>
        IEXPLORE.EXE
      </td>
    </tr>
        <tr>
      <td>
        adce894e3ce69c9822da57196707c7a15acee11319ccc963b84d83c23c3ea802
      </td>
      <td>
        SumatraPDF.exe
      </td>
    </tr>
        <tr>
      <td>
        0160375e19e606d06f672be6e43f70fa70093d2a30031affd2929a5c446d07c1
      </td>
      <td>
        Salary_Lockheed_Martin_job_opportunities_confidential.doc
      </td>
    </tr>
  </tbody>
</table>

if you look at ```IEXPLORE.EXE``` and ```SumatraPDF.exe``` have one interesting hacking adversary ```lazarus```
Now to link them both using ```Mitre Att&ck```

There is a certain mentions of malwares that can be traced back to what names are listed in virus total.
<table>
  <thead>
    <tr>
      <th>
        Mitre Att&ck
      </th>
      <th>
        Virus Total
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
       DRATzarus 
      </td>
      <td>
      DRATzarus-1SI.exe
      </rd>
    </tr>
  <tr>
    <td>
      Sumarta
    </td>
    <td>
      SumatraPDF.exe
    </td>
  </tr>
  </tbody>
</table>

The doc most likely is used for Phishing and will be refered to drop other programs

Now to start answering question:
<h3> Question 1 </h3>

Who conducted Operation Dream Job?
Answer: ```Lazarus Group``` Source: ```Mitre Att&ck```
When was this operation first observed?
Answer: ```September 2019``` Source: ```Mitre Att&ck```
There are 2 campaigns associated with Operation Dream Job. One is Operation North Star, what is the other?
Answer: ```Operation Interception``` Source: ```Mitre Att&ck```
During Operation Dream Job, there were the two system binaries used for proxy execution. One was Regsvr32, what was the other?
Answer: ```Rundll32``` Source: ```Mitre Att&ck```
What lateral movement technique did the adversary use?
Answer: ```Internal Spearphishing``` Source:  ```Mitre Att&ck``` 
NB: This wasn't straight foward as i though password spraying was the technique used evidently ```Lazarus Group malware attempts to connect to Windows shares for lateral movement by using a generated list of usernames, which center around permutations of the username Administrator, and weak passwords.``` But had to resort to something that touches on sending the .doc to the victim.
What is the technique ID for the previous answer?
Answer: ```T1534```
What Remote Access Trojan did the Lazarus Group use in Operation Dream Job?
Answer: ```DRATzarus```
What technique did the malware use for execution?
Answer: ```Native API```

