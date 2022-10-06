from os import makedirs, path


def make_dict() -> list:
    with open("CP.txt", 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    value_list = [lines[i].split('|') for i in range(len(lines))]

    key_list = ['d_codigo','d_asenta','d_tipo_asenta',
                'd_mnpio','d_estado','d_ciudad','d_CP',
                'c_estado','c_oficina','c_CP','c_tipo_asenta',
                'c_mnpio','id_asenta_cpcons','d_zona','c_cve_ciudad']
                
    return [dict(zip(key_list, value_list[i])) for i in range(len(lines))]


def get_data(cp:str, dict_list:list) -> list:   
    similarly = []

    for idx in range(len(dict_list)):
        aux : dict = dict_list[idx]
        if cp == aux.get('d_codigo'):
            similarly.append(aux)
        else:
            continue

    return similarly


def make_file(name: str, cp: str, data: str, parent_dir: str):
    directory = path.join(parent_dir, cp)

    if not path.exists(directory):
        makedirs(cp)
     
    with open(f'{directory}\\{name}.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{data}')
