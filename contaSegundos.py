total_segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))


dias = total_segundos // 86400
segundos_restantes = total_segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
min = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(f"{dias} dias, {horas} horas, {min} minutos e {segundos_restantes_final} segundos.")