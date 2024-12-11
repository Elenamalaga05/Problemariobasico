fun main() {
    // Pedir al usuario que ingrese un número
    println("Ingrese un número:")
    val numero = readLine()!!.toInt()

    // Verificar si el número es positivo, negativo o igual a cero
    if (numero > 0) {
        println("El número es positivo.")
    } else if (numero < 0) {
        println("El número es negativo.")
    } else {
        println("El número es igual a cero.")
    }
}
