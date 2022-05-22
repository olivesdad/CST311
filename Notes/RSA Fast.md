# RSA in combination with symmetric key
## Session Key
- User chooses a session key denoted by $K_S$ which can be shared.
- The session key is then encrypted with the recievers public key
	- This uses the time consuming RSA process
- Reciever gets the symmetric key and decrypts it with their RSA key
- Now both sender and reciever have the symmetric key which can be used to encrypt and decrypt.

