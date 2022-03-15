from datetime import datetime
days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
d = datetime.now()
print(days[d.weekday()])
