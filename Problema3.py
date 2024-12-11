fun main() {
    // Solicita la nota del examen
    print("Ingresa la nota del examen de programación: ")
    val nota = readLine()?.toDoubleOrNull() ?: -1.0

    // Verifica si la nota es válida
    if (nota in 0.0..10.0) {
        // Comprueba si aprobó o debe recuperar
        if (nota >= 7.0) {
            println("¡Felicidades! Has aprobado el examen.")
        } else {
            println("Debes recuperar el examen.")
        }
    } else {
        println("Nota inválida. Por favor, ingresa una nota entre 0 y 10.")
    }
}
