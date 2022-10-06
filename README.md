# Buscador de códigos postales

El siguiente programa busca en el archivo `CP.txt` un determinado código postal y genera un archivo con el nombre y la dirección del usuario.

## Dependencias

Se recomienda tener Python actualizado a la versión 3.8 o 3.10 y verificar el correcto funcionamiento del módulo `Tkinter`.

## Como usar el programa

Para hacer más amigable el uso del buscador al usuario se creó una interfaz gráfica donde se le solicita su nombre y código postal.

Presionando el botón **Buscar** el usuario podrá elegir su colonia si es que hay más de una y se habilitará el botón **Aceptar** para generar una vista previa de cómo quedará el archivo.

Por último, presionando el botón **Guardar** el usuario podrá elegir donde guardar su archivo, el cual se creará dentro de un directorio con su código postal por nombre.

## To Do

- [ ] Implementar una base de datos en SQL para los códigos postales
- [ ] Modificar el código fuente para trabajar con la base de datos
