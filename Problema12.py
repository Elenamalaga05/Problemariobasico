fun main() {
    var suma = 0

    // Continuar pidiendo valores hasta que la suma sea mayor que 78500
    while (suma <= 78500) {
        println("Ingrese un valor:")
        val valor = readLine()!!.toInt()

        suma += valor // Acumular el valor ingresado
    }

    // Imprimir el resultado final
    println("La suma final es: $suma")
}
