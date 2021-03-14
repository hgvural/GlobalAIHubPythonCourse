#!/usr/bin/env python
# coding: utf-8

# In[13]:


soruListe = list()
soruListe.append({"soru":"Türkiye'nin başkenti neresidir?", "cevap":"ANKARA"})
soruListe.append({"soru":"İngiltere'nin başkenti neresidir?", "cevap":"LONDRA"})
soruListe.append({"soru":"Hollanda'nın başkenti neresidir?", "cevap":"AMSTERDAM"})
soruListe.append({"soru":"Danimarka'nın başkenti neresidir?", "cevap":"KOPENHAG"})
soruListe.append({"soru":"Çekya'nın başkenti neresidir?", "cevap":"PRAG"})
soruListe.append({"soru":"İtalya'nın başkenti neresidir?", "cevap":"ROMA"})
soruListe.append({"soru":"İran'ın başkenti neresidir?", "cevap":"TAHRAN"})
soruListe.append({"soru":"Rusya'nın başkenti neresidir?", "cevap":"MOSKOVA"})
soruListe.append({"soru":"Norveç'in başkenti neresidir?", "cevap":"OSLO"})
soruListe.append({"soru":"İsveç'in başkenti neresidir?", "cevap":"STOKHOLM"})
score = 0
for i in soruListe:
    if i["cevap"] == input(i["soru"]).upper():
        score += 10

print("Toplam puanınız:",score)
if score > 50:
    print("Yarışmayı BAŞARI ile tamamladınız. Tebrikler.")
else:
    print("Başarısız oldunuz. Katıldığınız için teşekkür ederiz.")

