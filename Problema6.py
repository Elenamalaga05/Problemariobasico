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

    // Determina el mayor de los tres números
    val mayor = maxOf(numero1, numero2, numero3)

    // Muestra el resultado
    println("El número mayor es: $mayor")
}
