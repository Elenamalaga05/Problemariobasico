fun main() {
    // Solicita el primer número
    print("Ingresa el primer número: ")
    val numero1 = readLine()?.toDoubleOrNull() ?: 0.0

    // Solicita el segundo número
    print("Ingresa el segundo número: ")
    val numero2 = readLine()?.toDoubleOrNull() ?: 0.0

    // Suma los dos números
    val suma = numero1 + numero2

    // Muestra el resultado
    println("La suma de $numero1 y $numero2 es: $suma")
}
