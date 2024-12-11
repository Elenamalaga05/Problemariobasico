fun main() {
    // Solicita la primera nota
    print("Ingresa la primera nota: ")
    val nota1 = readLine()?.toDoubleOrNull() ?: -1.0

    // Solicita la segunda nota
    print("Ingresa la segunda nota: ")
    val nota2 = readLine()?.toDoubleOrNull() ?: -1.0

    // Solicita la tercera nota
    print("Ingresa la tercera nota: ")
    val nota3 = readLine()?.toDoubleOrNull() ?: -1.0

    // Verifica si las notas son válidas
    if (nota1 in 0.0..10.0 && nota2 in 0.0..10.0 && nota3 in 0.0..10.0) {
        // Calcula el promedio de las tres notas
        val promedio = (nota1 + nota2 + nota3) / 3

        // Muestra el promedio
        println("Tu promedio del trimestre es: %.2f".format(promedio))

        // Determina si aprobó o debe recuperar
        if (promedio >= 7.0) {
            println("¡Felicidades! Has aprobado el trimestre.")
        } else {
            println("Debes recuperar.")
        }
    } else {
        println("Una o más notas no son válidas. Por favor, ingresa notas entre 0 y 10.")
    }
}
