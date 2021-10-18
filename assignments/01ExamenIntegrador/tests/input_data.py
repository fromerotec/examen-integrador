# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
        (
            ["88", "41", "96", "0"],
            ["","","","","[88, 41, 96, 0]","El numero 1 es: 88","El numero 2 es: 41","El numero 3 es: 96","El numero 4 es: 0","[[88, 41, 96, 0], [88, 41, 96, 0]]"],
            "Revisa que estes imprimiendo la lista, la secuencua y la matriz correctamente."
        ),
    # Test case 2
        (
            ["20", "09", "88", "-1"],
            ["","","","","Error de captura"],
            "Revisa que estes validando el uso de números negativos."
        )
    ]
