def count_calls():
    global count
    count += 1

def string_info( string):
    str_inf = [len(string),string.upper(),string.lower()]
    count_calls()
    return str_inf

def is_contains(string,list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        flg_s = False
        string = string.lower()
        list_to_search[i] =list_to_search[i].lower()
        if (list_to_search[i] == string):
            flg_s = True
            break
    return flg_s

count = 0
print(string_info('Fortification'))
print(string_info('Sidney Sheldon'))
print(is_contains('Guest', ['est', 'GueGu', 'GuEst']))
print(is_contains('ход', ['ухо', 'поднос']))
print(is_contains('ход', ['ход', 'поднос']))
print(count)