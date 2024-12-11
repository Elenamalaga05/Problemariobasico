fun main() {
    // Crear una lista con los datos de los alumnos
    val alumnos = listOf(
        "Gómez, Juan" to 8,
        "Pérez, María" to 7,
        "López, Ana" to 9,
        "Martínez, Carlos" to 6,
        "Rodríguez, Laura" to 10,
        "Fernández, José" to 5,
        "Sánchez, Paula" to 8,
        "Díaz, Luis" to 7,
        "Vázquez, Marta" to 6,
        "García, Alberto" to 9,
        "Morales, Carmen" to 8,
        "Torres, Pablo" to 7,
        "Ruiz, Laura" to 10,
        "Jiménez, Javier" to 6,
        "Ramírez, Rosa" to 7,
        "Serrano, Andrés" to 9,
        "Hernández, Elena" to 8,
        "Gil, Pedro" to 6,
        "Álvarez, Susana" to 7,
        "Cordero, Raúl" to 10,
        "Luna, Teresa" to 8,
        "Mendoza, Luis" to 7,
        "Bermúdez, Isabel" to 9,
        "Vega, Javier" to 6
    )

    // Mostrar los datos de los alumnos
    for (alumno in alumnos) {
        val (nombre, nota) = alumno
        println("$nombre - Nota: $nota")
    }
}
