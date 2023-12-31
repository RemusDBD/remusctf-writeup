Basic Android RE 1 
<br>
Link to the Room : https://ctflearn.com/challenge/962

Date Start : 5/11/2023
Date Finish : 5/11/2023

Reviewed any writeup : N/A

Tools : <br>
[1] BlueStacks - For opening apk <br>
[2] JADX-GUI - For reversing apk <br>
[3] https://hashes.com/en/tools/hash_identifier - For identifying the hash <br>
[4] https://hashes.com/en/decrypt/hash - For decrypting MD5

OS : Windows 10 

Procedure :<br>
1) Download the apk (and all the Tools if you do not have)<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/roomlayout.png" width="50%" height="50%">
2) Use Tool [2] and review source code directly into "com.example.secondapp" > "MainActivity"<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/jadxgui.png" width="50%" height="50%">
3a) You will see Flag string at the bottom  (line 26) <code>((TextView) findViewById(R.id.textView)).setText("Success! CTFlearn{" + editText.getText().toString() + "_is_not_secure!}");</code><br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/jadxgui-mainactivity-line26.png" width="50%" height="50%">
3b) in upper line you will see hash code (line 25) <code>if (DigestUtils.md5Hex(editText.getText().toString()).equalsIgnoreCase("b74dec4f39d35b6a2e6c48e637c8aedb")) {</code><br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/jadxgui-mainactivity-line25.png" width="50%" height="50%">
4) use Tools [3] to identfy the hash and find out it is MD5<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/hash-identify.png" width="50%" height="50%">
5) use Tools [4] to decrypt MD5 code in 3b)<br>
<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/hash-decrypt.png" width="50%" height="50%">
6) You will get the password<br>
7) use Tools [1] to open the apk<br>
8) enter the password and you will get the flag<br>

<img src="https://raw.githubusercontent.com/RemusDBD/remusctf-writeup/main/2023-ctf/ctflearn/Reverse%20Engineering/Room%201%20-%20Basic%20Android%20RE%201/flag.png" width="50%" height="50%">
