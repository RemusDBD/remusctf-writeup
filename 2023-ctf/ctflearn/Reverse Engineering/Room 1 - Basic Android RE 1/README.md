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

Procedure :
1) Download the apk and check the soruce code.
2) Review directly into "com.example.secondapp" > "MainActivity"
3a) You will see Flag string at the bottom  (line 26)       ---   ((TextView) findViewById(R.id.textView)).setText("Success! CTFlearn{" + editText.getText().toString() + "_is_not_secure!}");
3b) in line 25 you will see hash code ---   if (DigestUtils.md5Hex(editText.getText().toString()).equalsIgnoreCase("b74dec4f39d35b6a2e6c48e637c8aedb")) {
4) use Tools [3] to identfy the hash and find out it is MD5
5) use Tools [4] to decrypt MD5 code in 3b)
6) You will get the password
7) use Tools [1] to open the apk
8) enter the password and you will get the flag
