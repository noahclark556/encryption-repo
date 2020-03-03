# encryption-repo
<h1>Python and mysql based encryption algorithm</h1> 

To run the full program as python, execute the main.py.
To run as executable (exe), execute DoubleEncrypt.exe.

<h2>IMPORTANT!</h2><br/>A row with a static id of 1 must be inserted into database as well as a placeholder
string value for crypto collumn or this application will fail!
<br/>
<b>SETUP:</b><br/>
BEFORE USING:
Edit parseUpload.py and tables.py and input your own database information based on the information provided in the code
comments. You can either have a database set up on your own system with applications like XAMPP/WAMP, or you can use an
online host. 
<br/>

<b>COMMANDS:</b><br/>
c - create and upload a new key/crypto<br/>
e - encrypt using currently uploaded crypto<br/>
d - decrypt using currently uploaded crypto<br/>
clear - clear screen<br/>
exit - exit terminal<br/>

<b>REMARKS:</b>
If you plan on decrypting a message, DO NOT forget<br/>
the seed and double encryption key you used to create the crypto.<br/>
Because if new crypto is uploaded to database, there is no going back <br/>unless you have Seed and DE. <br/>
When encrypting and decrypting with a key, remember that the code reads for spaces. If you do not copy <br/>
white space when placing encrypted code into the decrypter, the outcome will be wrong.
