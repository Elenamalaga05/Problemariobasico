fun main() {
    var suma = 0

    // Ingresar 10 valores y acumular la sumatoria
    for (i in 1..10) {
        println("Ingrese el valor $i:")
        val valor = readLine()!!.toInt()
        suma += valor // Acumular el valor ingresado
    }

    // Imprimir el resultado final
    println("La sumatoria de los valores es: $suma")
}
