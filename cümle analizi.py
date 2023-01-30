#RIDVAN TUNA ALTUNTAŞ 200312012
metin=str("Karşında ziya yoksa, sağından ya solundan Tek bir ışık olsun buluver, kalma yolundan.")
sayac=0
while sayac < len(metin.split()):
  print(metin.split()[sayac])
  sayac =sayac+ 1
i=0
sesli = "aeıioöuüAEIİOÖUÜ"
for x in metin:
    if x in sesli:
        i =i+1
print (i,"sesli harf vardır")
print (metin[::-1])

