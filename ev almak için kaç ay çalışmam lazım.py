# 2. soru
maas=int(input('lütfen maaşınızı giriniz:'))
maasin_yuzdesi=int(input('maaşınınızın yüzde kaçını biirktirmek istersiniz:'))
ev_fiyati=400000
kac_ay_lazim = (500000//(maas*maasin_yuzdesi/100))
metin='evi almak için {} ay lazım'
print(metin.format(kac_ay_lazim))
#maaş ve maaşın yüzdesini integer olarak atadım. Evin fiyatını girdim ve 
#kaç ayda almamız gerektiğni söyleyen formülü yazdım. Daha sonrasında 
#yazdırmak istedğim metini girdim ve format kullanarak bunun çıkmasını 
#sağladım. Geriye sadece çalıştırmak kalıyor.
