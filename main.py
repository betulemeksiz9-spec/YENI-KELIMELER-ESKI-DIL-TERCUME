meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GHOSTİNG":"bir kişiyi görmezden gelmek",
            "LOVE BOMBİNG":"BİR KİŞİYİ ÇOK İLGİYE BOĞUP ARDINDAN İLGİ GÖSTERMEYİ BIRAKMAK",
            "ROFL":" bir şakaya karşılık cevap",
            "AGGRO":"agresifleşmek/sinirlenmek",
            "SHEESH":"onaylamamak",
            "CREEPY":" korkunç"
            
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    
else:
    print("doğru yazdığına emin misin")
