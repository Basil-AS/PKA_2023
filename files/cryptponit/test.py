import atbash
import cesar
import polibii

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
            atbash.atbash_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            atbash.atbash_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо любое другое число, чтобы завершить работу: '))
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
            atbash.atbash_crypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
        elif choice == 2:
            print('\tРежим расшифрования')
            atbash.atbash_decrypt()
            num_prog = int(input('\nВведите ноль, чтобы перезапустить терминал. Либо любое другое число, чтобы завершить работу: '))
            if num_prog == 0:
                terminal()
            else:
                exit
    elif num_prog == 3:
        import polibii
    elif num_prog == 4:
        import tritemii
    elif num_prog == 5:
        import belazo
    elif num_prog == 6:
        import vizhener_1
    elif num_prog == 7:
        import s_block_magma
    elif num_prog == 8:
        import matrichnii
    elif num_prog == 9:
        import playfer
    elif num_prog == 10:
        import vertical
    elif num_prog == 11:
        import kardano
    elif num_prog == 12:
        import feistel
    elif num_prog == 13:
        import shennon
    elif num_prog == 14:
        pass
    elif num_prog == 15:
        import a5_1
        # import a51
    elif num_prog == 16:
        import a5_2
    elif num_prog == 17:
        import MAGMA_исходник
        # import MAGMA(---)
    elif num_prog == 18:
        pass
    elif num_prog == 19:
        pass
    elif num_prog == 20:
        pass
    elif num_prog == 21:
        import RSA
    elif num_prog == 22:
        import Elgamal
    elif num_prog == 23:
        pass
    elif num_prog == 24:
        import cp_RSA
    elif num_prog == 25:
        import cp_Elgamal_
    elif num_prog == 26:
        import гост94
    elif num_prog == 27:
        pass
    elif num_prog == 28:
        import Diffie_Hellman

terminal()