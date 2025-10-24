from textx import metamodel_from_file
from textx.export import model_export
import os

# Carga la gramática
mm = metamodel_from_file('arch.tx')

# Carga el modelo (instancia)
model = mm.model_from_file('PPMS-model.tx')

print("Modelo cargado correctamente:", model)

#modelo a un archivo Graphviz (.dot)
output_dot = "modelo.dot"
model_export(model, output_dot)
print(f"Modelo exportado a '{output_dot}'")

# .dot a una imagen PNG usando Graphviz
output_png = "modelo.png"
os.system(f"dot -Tpng {output_dot} -o {output_png}")

if os.path.exists(output_png):
    print(f"Imagen generada: {output_png}")
    print(f"open {output_png}  # (en macOS)")
else:
    print("No se pudo generar la imagen. ¿Tienes Graphviz instalado?")
