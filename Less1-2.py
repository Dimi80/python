# ЧЧ:ММ:СС
sec = input('Введите количество секунд: ')
sec = float(sec)
sec = int(sec)
# часы
if int(sec / 60 / 60) < 10:
    hours = ('0' + str(int(sec / 60 / 60)))
else:
    hours = int(sec / 60 / 60)
# минуты
if int((sec - int(sec / 60 / 60) * 60 * 60) / 60) < 10:
    minutes = ('0' + str(int((sec - int(sec / 60 / 60) * 60 * 60) / 60)))
else:
    minutes = int((sec - int(sec / 60 / 60) * 60 * 60) / 60)
# секунды
if int(sec - int(sec / 60 / 60) * 60 * 60 - int((sec - int(sec / 60 / 60) * 60 * 60) / 60) * 60) < 10:
    seconds = ('0' + str(int(sec - int(sec / 60 / 60) * 60 * 60 - int((sec - int(sec / 60 / 60) * 60 * 60) / 60) * 60)))
else:
    seconds = int(sec - int(sec / 60 / 60) * 60 * 60 - int((sec - int(sec / 60 / 60) * 60 * 60) / 60) * 60)
print('Результат в формате "ЧЧ : ММ : СС":   ', hours, ':', minutes, ':', seconds)