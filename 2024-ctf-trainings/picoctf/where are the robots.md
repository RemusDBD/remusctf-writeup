where are the robots | 100 points
Tags: picoCTF 2019 Web Exploitation (59)
```
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u https://jupiter.challenges.picoctf.org/problem/60915/ -w /usr/share/wordlists/dirb/common.txt

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://jupiter.challenges.picoctf.org/problem/60915/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 431]
/robots.txt           (Status: 200) [Size: 36]
```

view-source:https://jupiter.challenges.picoctf.org/problem/60915/robots.txt

User-agent: *
Disallow: /8028f.html


view-source:https://jupiter.challenges.picoctf.org/problem/60915/8028f.html

<flag>picoCTF{ca1cu1at1ng_Mach1n3s_8028f}</flag></p>
