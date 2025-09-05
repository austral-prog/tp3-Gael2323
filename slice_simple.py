def slice_simple():
    texto = "Awesome"
<<<<<<< HEAD
    texto2 = texto.lower()
    print(texto2[0:3])
    print(texto2[2:5])
    print(f"{texto2[0:4]}{texto2[-3:]}")
=======
    print(texto[:3].lower())
    print(texto[2:5])
    print(texto[0:4].lower + texto [-3:])
>>>>>>> 27c65064ace6888c2a5142d89c1071808763e849
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
