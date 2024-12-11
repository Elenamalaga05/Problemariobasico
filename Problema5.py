fun main() {
    // Solicita el sueldo base del empleado
    print("Ingresa el sueldo base del empleado: ")
    val sueldoBase = readLine()?.toDoubleOrNull() ?: -1.0

    // Solicita los años de antigüedad
    print("Ingresa los años de antigüedad del empleado: ")
    val aniosAntiguedad = readLine()?.toIntOrNull() ?: -1

    // Verifica si las entradas son válidas
    if (sueldoBase >= 0 && aniosAntiguedad >= 0) {
        // Determina el porcentaje según la antigüedad
        val porcentaje = if (aniosAntiguedad < 5) 0.30 else 0.50

        // Calcula el sueldo a cobrar
        val sueldoACobrar = sueldoBase + (sueldoBase * porcentaje)

        // Muestra el resultado
        println("El sueldo a cobrar es: $%.2f".format(sueldoACobrar))
    } else {
        println("Entrada inválida. Por favor, ingresa valores numéricos positivos.")
    }
}


#Caso con antigüedad menor a 5 años:

Ingresa el sueldo base del empleado: 1000
Ingresa los años de antigüedad del empleado: 3
El sueldo a cobrar es: $1300.00


#Caso con antigüedad de 5 años o más:

Ingresa el sueldo base del empleado: 1200
Ingresa los años de antigüedad del empleado: 7
El sueldo a cobrar es: $1800.00


#Entrada inválida:

Ingresa el sueldo base del empleado: abc
Ingresa los años de antigüedad del empleado: -3
Entrada inválida. Por favor, ingresa valores numéricos positivos.
