#200312012 RIDVAN TUNA ALTUNTAŞ
def sayi(password):
    sayi_listesi=["0","1","2","3","4","5","6","7","8","9"]
    for sayi in password:
        for kontrol_sayi in sayi_listesi:
            if sayi==kontrol_sayi:
                return True
    return False
kullanicipassword=input("şifrenizi giriniz:")
def kontrol(password): 



    if len(password)==3:


        if int(password)%2 == 0 and password[2]!=password[1] and password[0]!=password[2] and password[1]!=password[0] and password[0]>password[1] and password[1]>password[2] :
            print ("şifreniz güçlü bir şifredir.")
        elif int(password)%2 == 0 and password[1]!=password[2] and password[0]!=password[2] and password[0]!=password[1]:
            print("orta düzey şifre")
        elif int(password)%2 == 0 and password[1]==password[2] or password[0]==password[2] or password[0]==password[1]:
            print("zayıf şifre")
        else:
            int(password)%2 != 0 and password[1]==password[2] or password[0]==password[2] or password[0]==password[1]
            print("bu şifre kullanılamaz")
    else: 

        print(" şifreniz geçeresiz")
kontrol(kullanicipassword)
             
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
               


            

    




