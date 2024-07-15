COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}
def ukura(inn, search_value):
    found = False

    with open(inn, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 6:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]

            if search_value in dbirthdate:
                print(f'''{COLOR_CODE["GREEN"]}

        ,----,                        ,----,                             
      ,/   .`|     ,----..          ,/   .`|                      ____   
    ,`   .'  :    /   /   \       ,`   .'  :     ,---,.         ,'  , `. 
  ;    ;     /   /   .     :    ;    ;     /   ,'  .' |      ,-+-,.' _ | 
.'___,/    ,'   .   /   ;.  \ .'___,/    ,'  ,---.'   |   ,-+-. ;   , || 
|    :     |   .   ;   /  ` ; |    :     |   |   |   .'  ,--.'|'   |  ;| 
;    |.';  ;   ;   |  ; \ ; | ;    |.';  ;   :   :  |-, |   |  ,', |  ': 
`----'  |  |   |   :  | ; | ' `----'  |  |   :   |  ;/| |   | /  | |  || 
    '   :  ;   .   |  ' ' ' :     '   :  ;   |   :   .' '   | :  | :  |, 
    |   |  '   '   ;  \; /  |     |   |  '   |   |  |-, ;   . |  ; |--'  
    '   :  |    \   \  ',  /      '   :  |   '   :  ;/| |   : |  | ,     
    ;   |.'      ;   :    /       ;   |.'    |   |    \ |   : '  |/      
    '---'         \   \ .'        '---'      |   :   .' ;   | |`-'       
                   `---`                     |   | ,'   |   ;/           
                                             `----'     '---'        
╔═══════════════════════════════════════════════════════════════════             
║ Номер телефона: {icusid}    
║ Дата подключения: {ccusfullname}  
║ ФИО: {ccusinn}  
║ Адрес: {ccitizenship} 
║ Паспорт: {cgender}     
║ ИНН: {dbirthdate}                                    
╚═══════════════════════════════════════════════════════════════════ 
  ''')

                found = True 