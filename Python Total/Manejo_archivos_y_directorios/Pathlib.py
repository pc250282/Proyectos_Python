from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/Pablo/Documents/ProyectosHTML/prueba.py')

#Parsear un ruta de windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

#Cambiar el nombre del archivo y/ubicacion
print(carpeta.rename('C:/Users/Pablo/Documents/ProyectosHTML/prueba.py'))

#Path lib permite abrir el archivo y no es necesario  cerrarlo
print(carpeta.read_text())

#Extraer nombre del archivo
print(carpeta.name)

#Extencion del archivo
print(carpeta.suffix)

#Sin la extencion
print(carpeta.stem)


#Validar existencia de un archivo
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('genial,existe')
