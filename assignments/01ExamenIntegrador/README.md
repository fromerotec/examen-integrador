![Tec de Monterrey](../../images/logotecmty.png)
# Examen Integrador
Examen Integrador


Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa (si, un solo programa) que contenga 3 funciones diferentes las cuales realicen las siguientes instrucciones:

/ 1. Crea una función llamada "vector" que permita guardar 4 números enteros positivos solicitados al usuario y que retorne una lista de números con los elementos ingresados. En caso de que el usuario capture un número negativo, se deberá desplegar en pantalla el mensaje "Error de captura" y el programa deberá terminar. Observa el ejemplo:

```
Entrada:
88
41
96
0


Salida:
[88, 41, 96, 0]
```

/ 2. Crea una función llamada "string" que, al utilizar un ciclo while o un ciclo for, permita escribir mensajes en pantalla con los números de la lista generada en el punto anterior, utilizando el formato "El numero" + número iterador + "es:" + número de la lista (omite la tilde en "numero"). La función no deberá retornar ningún valor. Observa el ejemplo:

```
Entrada:
[88, 41, 96, 0]


Salida:
El numero 1 es: 88
El numero 2 es: 41
El numero 3 es: 96
El numero 4 es: 0
```

/ 3. Crea una función llamada "matriz" que reciba como parámetro la lista generada en el punto 1 y que posteriormente la duplique, generando una matriz de 2x4. La función no deberá retornar ningún valor. Observa el ejemplo:

```
Entrada:
[88, 41, 96, 0]


Salida:
[[88, 41, 96, 0], [88, 41, 96, 0]]
```



Toma en cuenta que lo que se ha explicado hasta el momento es lo que se espera que haga tu programa.


__________


Ahora bien, a continuación se presentan tres ejemplos con las entradas y salidas FINALES que puede tener tu programa:


<b>Ejemplo 1:</b>

Entradas:
```
88
41
96
0
```

Salidas:
```
[88, 41, 96, 0]
El numero 1 es: 88
El numero 2 es: 41
El numero 3 es: 96
El numero 4 es: 0
[[88, 41, 96, 0], [88, 41, 96, 0]]
```


<b>Ejemplo 2:</b>

Entradas:
```
5
15
10
2020
```

Salidas:
```
[5, 15, 10, 2020]
El numero 1 es: 5
El numero 2 es: 15
El numero 3 es: 10
El numero 4 es: 2020
[[5, 15, 10, 2020], [5, 15, 10, 2020]]
```


<b>Ejemplo 3:</b>

Entradas:
```
20
09
88
-1
```

Salidas:
```
Error de captura
```

.



```
NOTA IMPORTANTE: Tu programa NO debe incluir algún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida (observa que la palabra "numero" no tiene tilde en las salidas).
```

.



No olvides incluir esta parte del código `if __name__ == '__main__':`.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
