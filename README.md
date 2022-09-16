# encryption-decryption-app-
this program implements RSA public key encyption algorithm.
requirements are:
 1 Help user for public and private key selection
 2 Encrypt the given text
 3 Decrypt the given encrypted text
 
Help user for public and private key selection
  Get 2 prime numbers (p and q) from user
  Check whether they are prime or not
  Calculate n and z  (n should be grater than 127)
  Get e from user or determine automatically          (e<n, and e and z are relatively prime)
  Choose d automatically such that ed mod z  = 1 
  Write public key as {e, n}
  Write private key as {d, n}
  
Encrypt the given text
  Get public key as {e, n} from user
  Get text string from user
  Encrypt each character by using ASCII code of each character (convert to a number)
  Write the encrypted text in HEX encoding (4 characters output for each input- put 0 if it is less than 4 chars).For example:
  Dec: 326  => Hex: 146 => on screen: 0146

Decrypt the given text
  Get private key as {d, n} from user
  Get encrypted text string from user as HEX stream 
  Decrypt each character by using ASCII code of each character (convert to a number)
  Write the plaintext



