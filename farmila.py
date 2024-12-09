import os
import wget
import requests
from colorama import init, Fore

init(autoreset=True)

# URL с версией на сервере (измените ссылку на ваш URL)
VERSION_URL = "https://kead.top/version.txt"
# Текущая версия программы
CURRENT_VERSION = "6.9.3"

# Функция проверки обновлений
def check_for_updates():
    try:
        # Получаем текущую версию с сервера
        response = requests.get(VERSION_URL)
        response.raise_for_status()  # Проверка на успешный запрос
        server_version = response.text.strip()

        # Сравниваем версии
        if server_version != CURRENT_VERSION:
            print(Fore.GREEN + f"☼ Доступно обновление: {server_version}.")
            return True
        else:
            return False
    except Exception as e:
        print(Fore.RED + f"☼ Проверка обновления не удалась!\n")
        return False

# Очистка экрана
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.GREEN + '♥ Здравия желаю, сотрудник! Я Artem_Nikolskiy #3. Введи соответствующую цифру, чтобы выбрать свою структуру.')

print(Fore.YELLOW + '\n1 - ГИБДД')
print(Fore.YELLOW + '\n2 - УВД')

frak = input(Fore.YELLOW + '\nЯ работаю в ')

if frak == "2":

    clear_console()

    # Функция для записи результатов в файл
    def save_results_to_file(results, total_score):
        with open("Баллы.txt", "w", encoding="utf-8") as file:
            file.write("Результаты:\n\n")
            # Нумерация начинается с 1
            idx = 1
            for task_name, input_value, task_score in results:
                if task_score > 0:  # Записываем только если балл больше 0
                    file.write(f"{idx}. {task_name} [{input_value}]: {task_score} | Доказательства: *тык*\n")
                    idx += 1  # Увеличиваем номер для следующего результата
            file.write(f"\nОбщий балл: {total_score}")

    # Проверяем обновления перед выполнением программы
    if __name__ == "__main__":
        if check_for_updates():
            input(Fore.YELLOW + "\n♦ Нажмите 'Enter' для обновления программы.")
            clear_console()
            wget.download("https://kead.top/farmila.exe", out=str(f"farmila {CURRENT_VERSION}.exe"))
            print(Fore.GREEN + "\n\n♦ Загрузка завершена, нажмите 'Enter' для выхода."), input()
        else:
            print(Fore.GREEN + '★ Выбрано "УВД". Ты можешь нажать "Enter", чтобы пропустить невыполненную работу.')
            
            print(Fore.YELLOW + "\n╔════════════════════════ ♦ Инструкция ♦ ══════════════════════════╗")
            print(Fore.YELLOW + "║                                                                  ║")
            print(Fore.YELLOW + "║ 1) Ввести количество выполненной работы                          ║")
            print(Fore.YELLOW + "║ " + Fore.GREEN + "Пример: Введите количество штрафов: 6"  + Fore.YELLOW + "                            ║")
            print(Fore.YELLOW + "║ 2) Зайти в файл 'Баллы.txt' - там будет готовая форма для отчета ║")
            print(Fore.YELLOW + "║                                                                  ║")
            input(Fore.YELLOW + "╚══════════════ ♦ Чтобы продолжить нажмите 'Enter' ♦ ══════════════╝")
            
            clear_console()
            
            print(Fore.GREEN + '♥ Здравия желаю, сотрудник ГИБДД! Я Artem_Nikolskiy #3. Ты можешь нажать "Enter", чтобы пропустить невыполненную работу.')
            # Ввод данных
            prk = int(input(Fore.YELLOW + "\n┏ Введите количество практик/тренировок: ") or 0) * 7
            mpr = int(input(Fore.YELLOW + "┃ Введите количество мероприятий: ") or 0) * 7
            akt = int(input(Fore.YELLOW + "┃ Введите количество активных вызовов: ") or 0) * 10
            loj = int(input(Fore.YELLOW + "┃ Введите количество ложных вызовов: ") or 0) * 4
            rey = int(input(Fore.YELLOW + "┃ Введите количество участий в рейде: ") or 0) * 10
            sht = int(input(Fore.YELLOW + "┃ Введите количество штрафов: ") or 0) * 6
            pr3 = int(input(Fore.YELLOW + "┃ Задержание преступников (1-3 звезды): ") or 0) * 5
            pr5 = int(input(Fore.YELLOW + "┃ Задержание преступников (4-6 звезд): ") or 0) * 10
            gmp = int(input(Fore.YELLOW + "┃ Введите количество участий в ГМП: ") or 0) * 15
            smp = int(input(Fore.YELLOW + "┃ Введите количество участий в совместных МП: ") or 0) * 7
            ink = int(input(Fore.YELLOW + "┃ Сопровождение инкассации на протяжении 10 минут: ") or 0) * 5
            rpz = int(input(Fore.YELLOW + "┃ Введите количество выполненных РП заданий: ") or 0) * 7
            sob = int(input(Fore.YELLOW + "┃ Помощь в проведении собеседования: ") or 0) * 7
            ohr = int(input(Fore.YELLOW + "┗ Охрана общественного порядка на собеседовании других организаций: ") or 0) * 10

            clear_console()

            # Создаем список для хранения результатов
            results = [
                ("Практики/тренировки", prk // 7, prk),
                ("Мероприятия", mpr // 7, mpr),
                ("Активные вызовы", akt // 10, akt),
                ("Ложные вызовы", loj // 4, loj),
                ("Участие в рейде", rey // 10, rey),
                ("Штрафы", sht // 6, sht),
                ("Задержание преступников (1-3 звезды)", pr3 // 5, pr3),
                ("Задержание преступников (4-6 звезд)", pr5 // 10, pr5),
                ("Участия в ГМП", gmp // 15, gmp),
                ("Участия в совместных МП", smp // 7, smp),
                ("Сопровождение инкассации на протяжении 10 минут", ink // 5, ink),
                ("Выполнения РП заданий", rpz // 7, rpz),
                ("Помощь в проведении собеседования", sob // 7, sob),
                ("Охрана общественного порядка на собеседовании других организаций", ohr // 10, ohr),
            ]

            # Отфильтровываем результаты, где баллы больше 0
            filtered_results = [(task_name, input_value, task_score) for task_name, input_value, task_score in results if task_score > 0]

            # Выводим результаты с правильной нумерацией
            print(Fore.GREEN + "☼ Итак, ваши баллы:\n")
            for idx, (task_name, input_value, task_score) in enumerate(filtered_results, 1):
                print(Fore.YELLOW + f"○ {idx}. {task_name}:" + Fore.WHITE + f" {task_score}")

            # Считаем и выводим общий балл
            total_score = sum(task_score for _, _, task_score in filtered_results)
            if total_score == 0:
                print(Fore.YELLOW + "░ А их нет, что-то вы филоните, товарищ сотрудник...")
                input(Fore.RED + "\n♦ Лучше работайте! Нажмите 'Enter' для выхода.")
            else:
                print(Fore.YELLOW + "\n☺ Ура, закончили! Ваш общий бал составляет: ", total_score)

                # Сохраняем результаты в файл
                save_results_to_file(results, total_score)

                input(Fore.RED + "\n♦ Результаты успешно записаны в 'Баллы.txt'! Нажмите 'Enter' для выхода.")

else:

    clear_console()

    # Функция для записи результатов в файл
    def save_results_to_file(results, total_score):
        with open("Баллы.txt", "w", encoding="utf-8") as file:
            file.write("Результаты:\n\n")
            # Нумерация начинается с 1
            idx = 1
            for task_name, input_value, task_score in results:
                if task_score > 0:  # Записываем только если балл больше 0
                    file.write(f"{idx}. {task_name} [{input_value}]: {task_score} | Доказательства: *тык*\n")
                    idx += 1  # Увеличиваем номер для следующего результата
            file.write(f"\nОбщий балл: {total_score}")

    # Проверяем обновления перед выполнением программы
    if __name__ == "__main__":
        if check_for_updates():
            input(Fore.YELLOW + "\n♦ Нажмите 'Enter' для обновления программы.")
            clear_console()
            wget.download("https://kead.top/farmila.exe", out=str(f"farmila {CURRENT_VERSION}.exe"))
            print(Fore.GREEN + "\n\n♦ Загрузка завершена, нажмите 'Enter' для выхода."), input()
        else:
            print(Fore.GREEN + '♥ Здравия желаю, сотрудник ГИБДД! Я Artem_Nikolskiy #3. Ты можешь нажать "Enter", чтобы пропустить невыполненную работу.')
            
            print(Fore.YELLOW + "\n╔════════════════════════ ♦ Инструкция ♦ ══════════════════════════╗")
            print(Fore.YELLOW + "║                                                                  ║")
            print(Fore.YELLOW + "║ 1) Ввести количество выполненной работы                          ║")
            print(Fore.YELLOW + "║ " + Fore.GREEN + "Пример: Введите количество штрафов: 6"  + Fore.YELLOW + "                            ║")
            print(Fore.YELLOW + "║ 2) Зайти в файл 'Баллы.txt' - там будет готовая форма для отчета ║")
            print(Fore.YELLOW + "║                                                                  ║")
            input(Fore.YELLOW + "╚══════════════ ♦ Чтобы продолжить нажмите 'Enter' ♦ ══════════════╝")
            
            clear_console()
            
            print(Fore.GREEN + '★ Выбрано "УВД". Ты можешь нажать "Enter", чтобы пропустить невыполненную работу.')
            # Ввод данных
            prk = int(input(Fore.YELLOW + "\n┏ Введите количество практик/тренировок: ") or 0) * 7
            mpr = int(input(Fore.YELLOW + "┃ Введите количество мероприятий: ") or 0) * 7
            akt = int(input(Fore.YELLOW + "┃ Введите количество активных вызовов: ") or 0) * 10
            loj = int(input(Fore.YELLOW + "┃ Введите количество ложных вызовов: ") or 0) * 4
            rey = int(input(Fore.YELLOW + "┃ Введите количество участий в рейде: ") or 0) * 10
            sht = int(input(Fore.YELLOW + "┃ Введите количество штрафов: ") or 0) * 6
            vu = int(input(Fore.YELLOW + "┃ Введите количество лишений ВУ: ") or 0) * 7
            dtp = int(input(Fore.YELLOW + "┃ Введите количество оформленных ДТП: ") or 0) * 10
            gmp = int(input(Fore.YELLOW + "┃ Введите количество участий в ГМП: ") or 0) * 15
            smp = int(input(Fore.YELLOW + "┃ Введите количество участий в совместных МП: ") or 0) * 7
            rpz = int(input(Fore.YELLOW + "┃ Введите количество выполненных РП заданий: ") or 0) * 7
            sob = int(input(Fore.YELLOW + "┃ Помощь в проведении собеседования: ") or 0) * 7
            reg = int(input(Fore.YELLOW + "┗ Регулировка на протяжении 30 минут на труднопроходимых перекрестках, c чрезвычайной необходимостью урегулирования пробок: ") or 0) * 10

            clear_console()

            # Создаем список для хранения результатов
            results = [
                ("Практики/тренировки", prk // 7, prk),
                ("Мероприятия", mpr // 7, mpr),
                ("Активные вызовы", akt // 10, akt),
                ("Ложные вызовы", loj // 4, loj),
                ("Участие в рейде", rey // 10, rey),
                ("Штрафы", sht // 6, sht),
                ("Лишения ВУ", vu // 7, vu),
                ("Оформление ДТП", dtp // 10, dtp),
                ("Участия в ГМП", gmp // 15, gmp),
                ("Участия в совместных МП", smp // 7, smp),
                ("Выполнения РП заданий", rpz // 7, rpz),
                ("Помощь в проведении собеседования", sob // 7, sob),
                ("Регулировка на протяжении 30 минут на труднопроходимых перекрестках, c чрезвычайной необходимостью урегулирования пробок", reg // 10, reg)
            ]

            # Отфильтровываем результаты, где баллы больше 0
            filtered_results = [(task_name, input_value, task_score) for task_name, input_value, task_score in results if task_score > 0]

            # Выводим результаты с правильной нумерацией
            print(Fore.GREEN + "☼ Итак, ваши баллы:\n")
            for idx, (task_name, input_value, task_score) in enumerate(filtered_results, 1):
                print(Fore.YELLOW + f"○ {idx}. {task_name}:" + Fore.WHITE + f" {task_score}")

            # Считаем и выводим общий балл
            total_score = sum(task_score for _, _, task_score in filtered_results)
            if total_score == 0:
                print(Fore.YELLOW + "░ А их нет, что-то вы филоните, товарищ сотрудник...")
                input(Fore.RED + "\n♦ Лучше работайте! Нажмите 'Enter' для выхода.")
            else:
                print(Fore.YELLOW + "\n☺ Ура, закончили! Ваш общий бал составляет: ", total_score)

                # Сохраняем результаты в файл
                save_results_to_file(results, total_score)

                input(Fore.RED + "\n♦ Результаты успешно записаны в 'Баллы.txt'! Нажмите 'Enter' для выхода.")