fun main() {
    var suma = 0
    var contador = 0

    // Ingresar 10 valores numéricos
    for (i in 1..10) {
        println("Ingrese el valor $i:")
        val valor = readLine()!!.toInt()

        // Verificar si el valor está entre 5 y 2500, ambos inclusive
        if (valor in 5..2500) {
            suma += valor  // Acumular la suma de los valores válidos
            contador++      // Contar cuántos valores están dentro del rango
        }
    }

    // Calcular y mostrar el promedio si hay valores válidos
    if (contador > 0) {
        val promedio = suma / contador.toDouble()
        println("El promedio de los valores entre 5 y 2500 es: $promedio")
    } else {
        println("No se ingresaron valores dentro del rango de 5 a 2500.")
    }
}
