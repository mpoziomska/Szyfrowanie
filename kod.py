import sys

def szyfruj(szyfr, tekst):

    szyfr = szyfry[szyfr]
    
    dic = {k[0]: k[1].lower() for k in szyfr.split('-')}
    
    
    tekst_szyfr = tekst.upper()
    
    for k, v in dic.items():
        tekst_szyfr = tekst_szyfr.replace(k, v)
        

    inv_dic = {v.upper(): k for k, v in dic.items()}
    
    for k, v in inv_dic.items():
        tekst_szyfr = tekst_szyfr.replace(k, v)
    
    return tekst_szyfr.upper()

def spr(szyfr, tekst):
    
    return szyfruj(szyfr, szyfruj(szyfr, tekst)).lower() == tekst.lower()

szyfry = {'a': 'GA-DE-RY-PO-LU-KI', 'b': 'PO-LI-TY-KA-RE-NU'}
              
while True:
    szyfr = input(f'''Wybierz rodzaj szyfru:
                  a: {szyfry['a']},
                  b: {szyfry['b']}
                  ''')
    if szyfr in szyfry.keys():
        break
    else:
        print("Niepoprawne! Podaj 'a' lub 'b'.")



tekst = input("Podaj tekst do zaszyfrowania: ")

#print(spr(szyfr, tekst))

