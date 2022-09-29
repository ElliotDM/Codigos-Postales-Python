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


def print_data(name:str, cp:str, dict_list:list):   
    for idx in range(len(dict_list)):
        aux : dict = dict_list[idx]
        if cp == aux.get('d_codigo'):
            break
    
    data:dict = dict_list[idx]
    
    print('Nombre: ', name)
    print('C.P.: ', cp)    
    print('Colonia: ', data.get('d_asenta'))
    print('Estado: ', data.get('d_estado'))
    print('Municipio: ', data.get('d_mnpio'))
    
    if data.get('d_ciudad'):
        print('Ciudad: ', data.get('d_ciudad'))
    
    return (data, name, cp)


def make_file(info):
    data, name, cp = info
    
    parent_dir = r'C:\\Users\\ellio\\OneDrive\\Documentos\\Visual Studio Code\\Codigos_postales' 
    directory = path.join(parent_dir, cp)
    
    try:
        mkdir(directory)
    except OSError:
        print(f"\nEl directorio {cp} ya existe\n")
    
    file_name = f'{directory}\\{name}.txt'
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
    

def main():
    name = input("Ingrese su nombre: ")
    cp = input("Ingrese su codigo postal: ")

    info = print_data(name, cp, make_dict())
    make_file(info)


if __name__ == '__main__':
    main()
