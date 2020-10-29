def add_time(start, time, day = None):
    tiempo_start_1 = start.split()

    #Adecuacion Start
    tiempo_start = []
    if len(tiempo_start_1[0]) == 5:
        tiempo_start.append(int(tiempo_start_1[0][0:2]))
        tiempo_start.append(int(tiempo_start_1[0][3:]))
        tiempo_start.append(tiempo_start_1[1].upper())
        #print('Tiempo Start: ', tiempo_start)
    elif len(tiempo_start_1[0]) == 4:
        tiempo_start.append(int(tiempo_start_1[0][0]))
        tiempo_start.append(int(tiempo_start_1[0][2:]))
        tiempo_start.append(tiempo_start_1[1].upper())
        #print('Tiempo Start: ', tiempo_start)
    else:
        print("Hora introducida erroneamente")
        return None

    #Adecuacion Time
    tiempo_add = []
    tiempo_add.append(int(time[:-3]))
    tiempo_add.append(int(time[-2:]))
    if int(tiempo_add[1]) > 60:
        print("Los minutos no pueden ser mayores de 60")
        return None
    #print('Tiempo add: ', tiempo_add)

    # Suma
    final_time = []
    am_pm = tiempo_start[2]
    n_dias = 0
    n = int(tiempo_add[0]/12)
    #print(n)
    modo = None
    if tiempo_add[0]>11:
        modo = 0
        final_time.append(tiempo_start[0]+(tiempo_add[0]-12*n))
        if (n/2-int(n/2))>0.0001: #impar
            if am_pm=='AM':
                am_pm = 'PM'
                if n>=2:
                    n_dias = int(n/2)
            elif am_pm=='PM':
                am_pm = 'AM'
                if n>=1:
                    n_dias = 1+int(n/2)
        elif (n/2-int(n/2))<0.0001:
            if am_pm=='AM':
                if n>=2:
                    n_dias = int(n/2)
            elif am_pm=='PM':
                if n>=1:
                    n_dias = 1+int(n/2)

    elif tiempo_add[0] <= 11:
        modo = 1
        final_time.append(tiempo_start[0] + (tiempo_add[0]))


    añade_horas = int((tiempo_start[1] + tiempo_add[1]) / 60)
    añade_minutos = ((tiempo_start[1] + tiempo_add[1]) - 60 * int((tiempo_start[1] + tiempo_add[1]) / 60))
    if añade_minutos < 10:
        añade_minutos = '0' + str(añade_minutos)
    final_time[0]+=añade_horas
    final_time.append(añade_minutos)

    if modo==1:
        if final_time[0]>12:
            final_time[0]-=12
            if am_pm=='AM':
                am_pm = 'PM'
            elif am_pm=='PM':
                am_pm = 'AM'
                n_dias +=1
        elif añade_horas == 1 and tiempo_start[0]==11:
            if am_pm=='AM':
                am_pm = 'PM'
            elif am_pm=='PM':
                am_pm = 'AM'
                n_dias +=1

    elif modo==0:
        if final_time[0]>12:
            final_time[0]-=12
            if am_pm =='PM':
                am_pm = 'AM'
            if final_time[0]==12 and am_pm=='PM':
                am_pm = 'AM'
                n_dias +=1
        elif añade_horas == 1 and tiempo_start[0]==11:
            if am_pm=='AM':
                am_pm = 'PM'
            elif am_pm=='PM':
                am_pm = 'AM'


    final_time.append(am_pm)
    final_time.append(n_dias)


    if day != None:
        dias_dic = {'1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday','7':'Sunday'}
        dia = 0
        if day.lower() == 'monday':
            dia = 1
        elif day.lower() == 'tuesday':
            dia = 2
        elif day.lower() == 'wednesday':
            dia = 3
        elif day.lower() == 'thursday':
            dia = 4
        elif day.lower() == 'friday':
            dia = 5
        elif day.lower() == 'saturday':
            dia = 6
        elif day.lower() == 'sunday':
            dia = 7

        t_dias = dia + n_dias

        n_dia_final = t_dias-7*int(t_dias/7)
        if n_dia_final == 0:
            n_dia_final = 7

        dia_final = dias_dic.get(str(n_dia_final))

        final_time.append(dia_final)

    #print(final_time)

    new_time = str(final_time[0]) + ':' + str(final_time[1]) + ' ' + final_time[2]
    if day!= None:
        new_time +=', ' + final_time[4]
    if final_time[3] == 1:
        new_time += ' (next day)'
    elif final_time[3] > 1:
        new_time += ' (' + str(final_time[3]) + ' days later)'

    #print(new_time)
    return new_time
