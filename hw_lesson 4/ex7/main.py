#! /usr/local/bin/python3

while 1:
    ''' 2-ой пункт я понял так, что нам надо заменить все символы строки стоящие 
        на четных позициях на введенный символ X взятый N раз.
        Постарался сделать без цикла, с ним наверное было бы проще во 2-ом п.
        '''
    s_str = input('Введите 3 параметра через пробел - строку, символ, число: ')
    s = s_str.split()
    print('Введенная строка:', s[0])
    odd_symbols = list(s[0])[0::2]  # Получил все символы стоящие на нечетных позициях
    n_x_str = s[1]*int(s[2])  # Строка из символов X взятых N раз
    print(n_x_str.join(odd_symbols), '!'*int(s[2]), sep='\n')
