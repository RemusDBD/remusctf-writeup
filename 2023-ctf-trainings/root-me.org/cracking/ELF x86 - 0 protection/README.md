LF x86 - 0 protection
<br>
Link to the Room : https://www.root-me.org/en/Challenges/Cracking/ELF-x86-0-protection

Date Start : 7/12/2023 Date Finish : 7/12/2023

Reviewed any writeup : N/A

Tools :<br>
[1] Radare2 - Reversing elf<br>

OS : Ubuntu

Procedure :<br>
1) Download the room file ch1.zip (and all the Tools if you do not have)<br>
2) Extract the zip file and you will get ch1.bin<br>
3) Open the terminal and run the bin file with ./ch1.bin<br>
4) You are asked to enter to password<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/root-me.org/cracking/ELF%20x86%20-%200%20protection/0.jpg" width="50%" height="50%">
5) Run Radare2 on your terminal with : <br>
r2 -dA ch1.bin -> afl -> pdf@main<br>
You should successfully disassemble the code from a binary<br>
6. Now you can see the password already stored in plantext at the start in var_8h = str.xxxxxxxxx<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/root-me.org/cracking/ELF%20x86%20-%200%20protection/1.jpg" width="50%" height="50%">
7. Go back and run the bin file again and type the string value xxxxxxxxx<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/root-me.org/cracking/ELF%20x86%20-%200%20protection/2.jpg" width="50%" height="50%">
8. Profit<br>
