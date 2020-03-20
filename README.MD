# Benthic Password Retriever

This is a tool that decrypts password stored for Benthic Golden software. 
It can be used to either remember a password you forgot but you have 
saved in Golden or to take a backup of the passwords before upgrading
your OS or moving to a different hard disk. 

*Note:* This requires python3, python2 is dead anyways why are you still 
using it?

Since the software runs on Windows, this tools is meant to be run on 
Windows only. So to run this tool just type 

```
C:\> python retrieve.py 
```

This goes through all your stored credentials and lists down the user, 
connection and decrypted password. 

If you somehow managed to get the hex value of a stored password and 
want to decrypt it you can also use this tool. 

```
C:\> python retrieve.py -p <hex value of the password>
```

