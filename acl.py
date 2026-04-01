
# PARTE 1 - Asignatura y alumnos
print("========================================")
print("  Asignatura : Implementación de Redes")
print("  Alumno     : Juan Pérez")
print("  Compañero  : María López")
print("========================================")
print()

# PARTE 2 - Solicitar datos
nombre   = input("Nombre   : ")
apellido = input("Apellido : ")
seccion  = input("Sección  : ")
sede     = input("Sede     : ")

print()
print("========================================")
print("  INFORMACIÓN INGRESADA")
print("========================================")
print("  Nombre   :", nombre)
print("  Apellido :", apellido)
print("  Sección  :", seccion)
print("  Sede     :", sede)
print("========================================")
print()

# PARTE 3 - Clasificar ACL
acl = int(input("Ingrese número ACL: "))
print()

if 1 <= acl <= 99:
    print("ACL", acl, "→ ACL ESTÁNDAR (rango 1-99)")
elif 100 <= acl <= 199:
    print("ACL", acl, "→ ACL EXTENDIDA (rango 100-199)")
elif 1300 <= acl <= 1399:
    print("ACL", acl, "→ ACL ESTÁNDAR (rango 1300-1399)")
elif 2000 <= acl <= 2699:
    print("ACL", acl, "→ ACL EXTENDIDA (rango 2000-2699)")
else:
    print("ACL", acl, "→ NÚMERO NO VÁLIDO (fuera de rango)")

print("========================================")
