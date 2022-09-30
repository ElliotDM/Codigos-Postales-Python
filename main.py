from os import mkdir, path


def make_dict():
    with open("CP.txt", 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    value_list = [lines[i].split('|') for i in range(len(lines))]

    key_list = ['d_codigo','d_asenta','d_tipo_asenta',
                'd_mnpio','d_estado','d_ciudad','d_CP',
                'c_estado','c_oficina','c_CP','c_tipo_asenta',
                'c_mnpio','id_asenta_cpcons','d_zona','c_cve_ciudad']
                
    return [dict(zip(key_list, value_list[i])) for i in range(len(lines))]


def get_data(cp:str, dict_list:list) -> dict:   
    for idx in range(len(dict_list)):
        aux : dict = dict_list[idx]
        if cp == aux.get('d_codigo'):
            break
       
    return dict_list[idx]


def make_file(name: str, cp: str, data: dict, directory: str):
    parent_dir = path.join(directory, cp)
    
    file_name = f'{parent_dir}\\{name}.txt'
    col = data.get('d_asenta')
    est = data.get('d_estado')
    mun = data.get('d_mnpio')
     
    with open(file_name, 'w', encoding='UTF-8') as f:
        f.write(f'Nombre: {name}\n')
        f.write(f'C.P.: {cp}\n')
        f.write(f'Colonia: {col}\n')
        f.write(f'Estado: {est}\n')
        f.write(f'Municipio: {mun}\n')
        
        if data.get('d_ciudad'):
            cd = data.get('d_ciudad')
            f.write(f'Ciudad: {cd}\n')


def check_directory(cp:str, parent_dir: str):
    directory = path.join(parent_dir, cp)
    message = ''

    try:
        mkdir(directory)
    except OSError:
        message = f"El directorio {cp} ya existe"

    return message 