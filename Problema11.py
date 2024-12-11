fun main() {
    // Repetir el proceso 10 veces
    repeat(10) {
        // Pedir al usuario que ingrese un número
        println("Ingrese un número:")
        val numero = readLine()!!.toInt()

        // Determinar y mostrar el resultado
        when {
            numero < 10 -> println("El número es menor que 10.")
            numero in 10..100 -> println("El número está entre 10 y 100.")
            else -> println("El número es mayor a 100.")
        }
    }
}
