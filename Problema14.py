fun main() {
    var suma = 0

    // Ingresar 10 valores y acumular la suma
    for (i in 1..10) {
        println("Ingrese el valor $i:")
        val valor = readLine()!!.toInt()
        suma += valor // Acumular el valor ingresado
    }

    // Calcular el promedio
    val promedio = suma / 10.0

    // Imprimir la suma y el promedio con sus respectivas leyendas
    println("La suma de los valores es: $suma")
    println("El promedio de los valores es: $promedio")
}
