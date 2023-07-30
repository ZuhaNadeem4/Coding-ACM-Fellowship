from cryptography.fernet import Fernet

def load_key():
   # write_key();
    file=open('key.key','rb');
    key=file.read();
    file.close();
    return key

'''def write_key():
    key=Fernet.generate_key();
    with open('key.key','wb') as key_file:
        key_file.write(key);'''

master_pwd=input('Enter your master password:');
key=load_key() + master_pwd.encode();
fer=Fernet(key);

def view():
    with open('passwords.txt','r') as f:
        for lines in f.readlines():
          data=lines.rstrip();
          user,password=data.split("|");
          print("User:",user," Password:", fer.decrypt(password.encode()).decode());

def add():
    name=input('Enter account name:');
    pwd=input('Enter password:');
    with open('passwords.txt','a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")

    
while True:
    mode=input('Would you like to view existing passwords or add new ones or enter q to quit? (view/add/q)').lower();
    if mode=='q':
        break
    if mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print("Invalid mode");
        continue
