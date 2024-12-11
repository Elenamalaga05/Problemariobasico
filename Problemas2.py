fun main() {
    // Solicita el primer número
    print("Ingresa el primer número: ")
    val numero1 = readLine()?.toDoubleOrNull() ?: 0.0

    // Solicita el segundo número
    print("Ingresa el segundo número: ")
    val numero2 = readLine()?.toDoubleOrNull() ?: 0.0

    // Solicita el tercer número
    print("Ingresa el tercer número: ")
    val numero3 = readLine()?.toDoubleOrNull() ?: 0.0

    // Calcula el promedio
    val promedio = (numero1 + numero2 + numero3) / 3

    // Muestra el resultado
    println("El promedio de $numero1, $numero2 y $numero3 es: $promedio")
}
