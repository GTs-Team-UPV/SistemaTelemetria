# GT's Team UPV

![logo](https://i.ibb.co/zm9bxz3/logo2.png)

Aplicación para visualizar datos sobre el coche de competición para el grupo de Generación Espontánea 'GT's Team UPV' de
la Universidad Politécnica de Valencia

# Preparación del entorno de desarrollo

Para empezar con el desarrollo del proyecto, se deben instalar unos prerequisitos en el sistema.

## Python

Se requiere de una instalación de Python con una versión igual o mayor a `3.8`. Se puede descargar el instalador para el
sistema operativo de tu elección en [la web oficial de Python][python-web].

Los binarios deben ser accesibles des de cualquier parte del sistema, para facilitar los siguientes pasos. Se puede ver
una guía para realizar esto en sistemas Windows [aquí][tuto-vars]. Para comprobar si los binarios son accesibles des de
cualquier parte del sistema podemos abrir un terminal y ejecutar:

```shell
python -V
```

Lo que nos debería dar una respuesta parecida a:

```
Python #.#.##
```

De lo contario, se deberá configurar correctamente.

## Pip

Pip es el administrador de paquetes que se usa en el proyecto. Normalmente viene preinstalado en Python, pero nos
podemos asegurar ejecutando el siguiente comando en el terminal:

```shell
python -m ensurepip
```

# Dependencias

El proyecto requiere que se instalen algunos paquetes de Python. Usaremos Pip, y el
archivo [`requirements.txt`](./requirements.txt) con el siguiente comando:

```shell
python -m pip install -r requirements.txt
```

Una vez se tengan instaladas todas las dependencias, se podrá proceder con el desarrollo o ejecución del proyecto.


[python-web]: https://www.python.org/

[tuto-vars]: https://www.javatpoint.com/how-to-set-python-path