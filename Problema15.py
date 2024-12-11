fun main() {
    // Inicializar contadores para cada condición
    var mayorAMenorA10 = 0
    var entre10y100 = 0
    var mayorA100 = 0
    var negativos = 0
    var igualesACero = 0

    // Ingresar 100 valores
    for (i in 1..100) {
        println("Ingrese el valor $i:")
        val valor = readLine()!!.toInt()

        // Verificar las condiciones y aumentar el contador correspondiente
        when {
            valor > 0 && valor < 10 -> mayorAMenorA10++
            valor in 10..100 -> entre10y100++
            valor > 100 -> mayorA100++
            valor < 0 -> negativos++
            valor == 0 -> igualesACero++
        }
    }

    // Imprimir los resultados
    println("Cantidad de valores mayores a 0 y menores a 10: $mayorAMenorA10")
    println("Cantidad de valores comprendidos entre 10 y 100: $entre10y100")
    println("Cantidad de valores mayores a 100: $mayorA100")
    println("Cantidad de valores negativos: $negativos")
    println("Cantidad de valores iguales a 0: $igualesACero")
}
