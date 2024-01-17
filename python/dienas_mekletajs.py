def dienas_mekletajs (sis_gads, sis_menesis, sis_datums, si_diena, dz_gads, dz_menesis, dz_datums):
    menesu_dienu_skaits = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #Skaitām, cik dienas ir pagājušas
    #Pārbaude, vai šogad jau ir bijusi dzimšanas diena
    

    pagajusas_dienas = 0
    pagajusie_gadi = sis_gads-dz_gads

    if vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums) == False:
        pagajusie_gadi -=1

    pagajusas_dienas += 365*pagajusie_gadi

    garie_gadi = 0
    sakuma_gads = dz_gads
    if vai_datums_pagajis(dz_menesis, dz_datums, 2, 29):
        sakuma_gads +=1

    beigu_gads = sis_gads
    if vai_datums_pagajis(sis_menesis, sis_datums, 2, 29) == False:
        beigu_gads -=1


    for gads in range (sakuma_gads, beigu_gads+1):
        if gads % 4 == 0:
            garie_gadi +=1
        if gads % 100 == 0 and gads % 400 != 0:
            garie_gadi -=1

    pagajusas_dienas += garie_gadi

    # cik pilni mēneši ir pagājuši?
    if sis_menesis>=dz_menesis:
       pilni_menesi = sis_menesis-dz_menesis
    else:
      pilni_menesi = sis_menesis+12-dz_menesis
    if vai_datums_pagajis(1, sis_datums, 1, dz_datums):
        pilni_menesi = pilni_menesi - 1
    
    dienas_menesos = 0


    for i in range(dz_menesis, sis_menesis):
        menesis=dz_menesis
    while menesis != sis_menesis:
        if menesis  == 13:
            menesis=1
        dienas_menesos += menesu_dienu_skaits[menesis]
        menesis +=1

    pagajusas_dienas += dienas_menesos

    if sis_datums>=dz_datums:
        pagajusas_dienas += sis_datums-dz_datums
    else:
        pagajusas_dienas += sis_datums + menesu_dienu_skaits[sis_menesis-1] - dz_datums
        print("Pagajušas")
    # cik dienas ir kopā pa tiem mēnešiem?
        

    # cik dienas ir pagājušas nepilnajā mēnesī?
    dienu_atlikums = pagajusas_dienas % 7 

    dz_diena = si_diena-dienu_atlikums
    if dz_diena <=0:
        dz-diena +=7
    return "OK"


def vai_datums_pagajis(tagad_menesis, tagad_datums, salidzinamais_menesis, salidzinamais_datums):
    if tagad_menesis>salidzinamais_menesis:
        return True
    if tagad_menesis<salidzinamais_menesis:
        return False
    if tagad_datums>salidzinamais_datums:
        return True
    return False
    
dz_d = int(input("Lūdzu ievadiet savu dzimšanas dienu!:"))

