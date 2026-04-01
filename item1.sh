DIRECTORIO="mi_directorio_ev1"

mkdir -p "$DIRECTORIO"
echo "Directorio '$DIRECTORIO' creado."

touch "$DIRECTORIO/ev1.txt"
echo "Archivo 'ev1.txt' creado dentro de '$DIRECTORIO'."

chmod 755 "$DIRECTORIO/ev1.txt"
echo "Permisos 755 asignados a 'ev1.txt'."

ls -l "$DIRECTORIO/"
