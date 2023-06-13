def elimina_lineas(entrada, salida, linea_eliminar):
    
    with open(entrada, "rt") as arch_in:
        with open(salida, "wt") as arch_out:
            nro_linea = 1
            for linea_in in arch_in:
                if nro_linea != linea_eliminar:
                    arch_out.write(linea_in)
                nro_linea += 1
