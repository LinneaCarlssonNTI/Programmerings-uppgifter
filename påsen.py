påse = []
max = 10

while True:
    print('[V] Visa innehållet i påsen')
    print('[S] Spara i påsen')
    print('[F] Leta i påsen')
    print('[Q] Avsluta')
    val = input('Vad vill du göra?').upper()

    if val == 'V':
        print(påse)

    elif val == 'S':
        if len(påse) < 10:
            sak = input('Vad vill du spara i påsen?')
            if sak in påse:
                sak_val = input('Men jag har ju redan en sån, ska jag verkligen ha fler?')
                while sak_val != 'ja' and sak_val != 'nej':
                    sak_val = input('Ska jag ha en till, ja eller nej?')
                if sak_val == 'ja':
                    påse.append(sak)
                    if len(påse) == 1:
                        print('Det finns nu', len(påse),'sak i din påse')
                    else:
                        print('Det finns nu', len(påse),'saker i din påse')
            else:
                påse.append(sak)
                if len(påse) == 1:
                        print('Det finns nu', len(påse),'sak i din påse')
                else:
                        print('Det finns nu', len(påse),'saker i din påse')

        else:
            print('Din påse är ju proppfull, det går inte att spara något mer i den. Den kommer spricka💥')
    
    elif val == 'F':
        leta = input('Vad vill du leta efter i påsen?')

        if leta in påse:
            print('Sedär,', leta,'fanns i påsen')
            bort = input('Vill du ta bort den ur påsen?').lower()
            while bort != 'ja' and bort != 'nej':
                bort = input('Vill du ta bort den ur påsen, ja eller nej?')
            if bort == 'ja':
                påse.remove(leta)
        else:
            print('Tyvärr fanns inte', leta,'i påsen😢')

    elif val == 'Q':
        val2 = input('Är du säker på att du vill avsluta programmet?').lower()
        while val2 != 'ja' and val2 != 'nej':
            val2 = input('Simpel ja eller nej fråga').lower()

        if val2 == 'ja':

            val3 = input('Är du riktigt riktigt säker på att du inte vill stanna?').lower()

            while val3 != 'ja' and val3 != 'nej':
                val3 = input('Jag vet att du vill säga nej, gör det bara. Ett simpelt nej är allt jag vill höra💕').lower()

            if val3 == 'ja':

                val4 = input('Seriöst, du tänker bara lämna mig???').lower()
                while val4 != 'ja' and val4 != 'nej':
                    val4 = input('JA ELLER NEJ! ÄR DET SÅ SVÅRT😡').lower()

                if val4 == 'ja':
                    print('Jag hatar dig.')
                    break

                elif val4 == 'nej':
                    print('Jag visste det, du skulle aldrig lämna mig💕💕💕')
                    print('Du borde inte ens tänka tanken👿👿👿')

            if val3 == 'nej':
                print('Yippie! Vi kommer vara bästa vänner för evigt. DU FÅR ALDRIG LÄMNA👹👹👹')
            
                
        if val2 == 'nej':
            print('Yippie! Vi kommer vara bästa vänner för evigt. DU FÅR ALDRIG LÄMNA👹👹👹')
            


    else:
        print('Du måste välja ett av alternativen')       
