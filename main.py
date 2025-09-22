#### Fonction secondaire


def ispalindrome(p):

   # s = p.lower().replace(" ","").replace("'","").replace("é","e").replace("è","e").replace("ê","e").replace("ç","c").replace("ë","e").replace(":","").replace("!","").replace("?","").replace("-","").replace("à","a").replace(".","").replace("ô","o").replace(",","")
   # k = s[::-1]
   # return s==k
    table = str.maketrans("éèêëçàô","eeeeca o"," .,:;!?-'\"" )
    s = p.lower().translate(table)
    return s == s[::-1]
   
    
    

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()