## Introduction
This project explores simple encrypter and decrypter using the most widely known encryption technique, the Caesar's cipher.

## Encryption
To encrypt a given message, the function for encryption randomly determine a shift amount, then applying right-shift to all English characters containing in the given message. All characters other than English alphabets remain unchanged in the encrypted message.

## Decryption
To decrypt a given message, the function for decryption iterates through all 26 shift amounts to find the most possible decrypted message. A self-defined measure for evaluating the confidence of the decrypted result is defined as follow: <br /><br/>
<img src="https://i.imgur.com/YHV4HNK.png"> <br />
The decrypted message with highest degree of confidence is returned as the result of decryption.

## Required Packages
```
pip3 install pyenchant
```
Enchant is used to check the spelling of words and suggest corrections for words that are miss-spelled. In this project, the decrypter uses this package to create an dictionary of English words, so that it can tell whether the decrypted words are valid English vocabulary by referencing to this dictionary.

## Usage
To encrypt a message:
```
python3 caesar_ciper_encryptor.py 
```
To decrypt a message:
```
python3 caesar_ciper_decryptor.py 
```

## Examples
If the given message for encryption is perfectly legal in English, then the decrypter is able to decrypt the encrypted message with maximal confidence, which equals to 1.0.<br /><br />
<img src="https://i.imgur.com/q5VZpur.png"> <br /><br />
However, if there are typos or other non-English vocabulary in the given message, the decrypter is still able to decrypt the message correctly with slight losses in confidence. (The word "want" is mis-spelled as "watn" in this example) <br /><br />
<img src="https://i.imgur.com/2RRDsKS.png"> <br /><br />
