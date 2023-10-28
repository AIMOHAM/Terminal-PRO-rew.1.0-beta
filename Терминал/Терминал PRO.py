import platform
import psutil


loop = True
print("Терминал PRO")
print("Версия 1.0")
print("Русифицированное исполнение")
print("Запускать только от имени администратора!")
print('Чтобы узнать все возможные команды, введите "Команды"')

ram = psutil.virtual_memory()
total_ram = ram.total
available_ram = ram.available
used_ram = ram.used
percent_ram = ram.percent
system_info = platform.uname()

while loop:
    command = input("Ваша команда: ")

    if command.lower() == "команды":
        print("Список доступных команд:")
        print("Стандартная информация") #
        print("Информация о ОЗУ")       #
        print("Информация о видеокарте")#
        print("Информация о процессоре")#
        print("Информация о накопителях")#
        print("Связь с разработчиком")#


    elif command.lower() == "выход":
        loop = False

    elif command.lower() == "стандартная информация":
        print("Операционная система:", system_info.system)
        print("Имя узла:", system_info.node)
        print("Версия системы:", system_info.release)
        print("Версия системы (подробно):", system_info.version)
        print("Архитектура процессора:", system_info.machine)
        print("Тип процессора:", system_info.processor)

    elif command.lower() == "информация о озу":
        print("Всего ОЗУ:", total_ram, "байт")
        print("Доступно ОЗУ:", available_ram, "байт")
        print("Используется ОЗУ:", used_ram, "байт")
        print("Загрузка ОЗУ (%):", percent_ram, "байт")

        # Дополнительная информация о ОЗУ, если доступна
        try:
            ram_info = psutil.virtual_memory()
            print("Частота ОЗУ:", ram_info.freq)
            print("Тайминги ОЗУ:", ram_info.timing)
        except AttributeError:
            print("Дополнительная информация о ОЗУ недоступна. Доступ о получении подробной информации отклонён.")

    elif command.lower() == "информация о видеокарте":
        try:
            gpu_info = psutil.virtual_memory()
            print("Модель видеокарты:", gpu_info.model)
            print("Количество видеопамяти:", gpu_info.vram)
            print("Частота видеокарты:", gpu_info.freq)
            print("Вольтаж видеокарты:", gpu_info.voltage)
        except AttributeError:
            print("Дополнительная информация о видеокарте недоступна. Доступ к подробной информации отклонён.")

    elif command.lower() == "информация о процессоре":
        print("Информация о процессоре:")
        print("Архитектура:", platform.processor())
        print("Количество ядер:", psutil.cpu_count(logical=False))
        print("Количество потоков:", psutil.cpu_count(logical=True))
        print("Частота процессора:", psutil.cpu_freq().current)
        print("Максимальная частота процессора:", psutil.cpu_freq().max)
        print("Минимальная частота процессора:", psutil.cpu_freq().min)
        print("Загрузка процессора (%):", psutil.cpu_percent())

    elif command.lower() == "связь с разработчиком":
        print("Контакты для связи с разработчиком:")
        print("telegram: zqseqz")

    elif command.lower() == "информация о накопителях":    
        drives = psutil.disk_partitions()
        for drive in drives:
            print("Накопитель:", drive.device)
            print("Тип файловой системы:", drive.fstype)
            print("Метка тома:", drive.mountpoint)
            print("Доступно места (байт):", psutil.disk_usage(drive.mountpoint).free)
            print("Используется места (байт):", psutil.disk_usage(drive.mountpoint).used)
            print("Всего места (байт):", psutil.disk_usage(drive.mountpoint).total)
            print("")



    else:
        print("Неверная команда. Пожалуйста, попробуйте еще раз.")