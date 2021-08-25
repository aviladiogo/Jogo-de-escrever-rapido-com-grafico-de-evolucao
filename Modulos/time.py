import time as t
t.localtime()
hora_agora = t.localtime()
print("programa rodado as:", str(hora_agora.tm_hour)+"h"+str(hora_agora.tm_min)+ "m")
t.time()
hora_agora = t.time()
Semana = hora_agora +(86400 * 7)
t.localtime(Semana)
t.sleep(5)