import thousandtext
import atbash
import cesar
import polibii
import tritemii
import belazo
import vizhener_1
import s_block_magma
import matrichnii
import playfer
# import vertical
import kardano
import shennon

import Diffie_Hellman

# 	ТЕРМИНАЛ
def terminal():
    print('\n\tДобро пожаловать в Терминал!\nНиже приведен список доступных программ шифрования:\n')
    print('1. Шифр АТБАШ\n2. Шифр Цезаря\n3. Шифр Полибия')
    print('4. Шифр Тритемия\n5. Шифр Белазо\n6. Шифр Виженера\n7. S-блок замены ГОСТ Р 34.12-2015')
    print('8. Матричный шифр\n9. Шифр Плэйфера')
    print('10. Вертикальная перестановка\n11. Решетка Кардано\n12. Сеть Фейстеля')
    print('13. Одноразовый блокнот К.Шеннона\n14. Гаммирование ГОСТ Р 34.13-2015')
    print('15. A5/1\n16. A5/2')
    print('17. МАГМА\n18. ГОСТ 28147-89\n19. AES\n20. КУЗНЕЧИК')
    print('21. RSA\n22. Elgamal\n23. ECC - с использованием абсциссы точки')
    print('24. Алгоритм ЦП RSA\n25. Алгоритм ЦП Elgamal')
    print('26. ГОСТ Р 34.10-94\n27. ГОСТ Р 34.10-2012')
    print('28. Diffie-Hellman')
    num_prog = int(input('\nВыберите программу шифрования и введите её номера: '))

    if num_prog == 1:
        print('\tШифр АТБАШ')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            thousandtext.format_text()
            atbash.atbash_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            atbash.atbash_decrypt()
            thousandtext.format_text_rev()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 2:
        print('\tШифр Цезаря')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            cesar.cesar_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            cesar.cesar_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 3:
        print('\tКвадрат Полибия')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 4:
        print('\tШифр Тритемия')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            tritemii.tritemii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            tritemii.tritemii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 5:
        print('\tШифр Белазо')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            belazo.belazo_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            belazo.belazo_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 6:
        print('\tШифр Виженера')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            vizhener_1.vizhener_1_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            vizhener_1.vizhener_1_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 7:
        print('\tS-блок замены ГОСТ Р 34.12-2015')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            s_block_magma.s_block_magma_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            s_block_magma.s_block_magma_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 8:
        print('\tМатричный шифр')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            matrichnii.matrichnii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            matrichnii.matrichnii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 9:
        print('\tШифр Плэйфера')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            playfer.playfer_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            playfer.playfer_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 10:
        print('\tВертикальная перестановка')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # vertical.vertical_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # vertical.vertical_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 11:
        print('\tРешетка Кардано')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            kardano.kardano_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            kardano.kardano_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 12:
        print('\tСеть Фейстеля')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # shennon.shennon_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # shennon.shennon_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 13:
        print('\tОдноразовый блокнот К.Шеннона')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            shennon.shennon_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            shennon.shennon_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 14:
        print('\tГаммирование ГОСТ Р 34.13-2015')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 15:
        print('\tA5/1')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 16:
        print('\tA5/2')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 17:
        print('\tМАГМА')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 18:
        print('\tГОСТ 28147-89')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 19:
        print('\tAES')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 20:
        print('\tКУЗНЕЧИК')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 21:
        print('\tRSA')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 22:
        print('\tElgamal')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 23:
        print('\tECC - с использованием абсциссы точки')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 24:
        print('\tАлгоритм ЦП RSA')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 25:
        print('\tАлгоритм ЦП Elgamal')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 26:
        print('\tГОСТ Р 34.10-94')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 27:
        print('\tГОСТ Р 34.10-2012')
        print('\nРежим работы программы:')
        print('1. Шифрование\n2. Расшифрование')
        choice = int(input('\nВведите число для выбора режима работы программы: '))
        if choice == 1:
            print('\tРежим шифрования')
            # polibii.polibii_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            # polibii.polibii_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit

    elif num_prog == 28:
        print('\tОбмен ключами по Diffie-Hellman')
        Diffie_Hellman.Diffie_Hellman_exchange()
        num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо введите любое другое число, чтобы завершить работу: '))
        if num_prog == 0:
            terminal()
        else:
            exit

terminal()