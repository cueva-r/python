from vpython import *

# Creamos la escena
scene = canvas(title="Boeing 777-300ER - KLM Livery", width=800, height=600)

# Dimensiones del avión (escala 1:1000)
length = 73.9  # Longitud del avión en metros
wing_span = 64.8  # Envergadura del ala en metros
height = 18.6  # Altura del avión en metros

# Dimensiones del modelo (escala 1:1000)
scale_factor = 0.001
length_model = length * scale_factor
wing_span_model = wing_span * scale_factor
height_model = height * scale_factor

# Creamos el fuselaje
fuselage = cylinder(pos=vector(0, 0, 0), axis=vector(length_model, 0, 0), radius=1, color=color.blue)

# Creamos las alas
wing = box(pos=vector(length_model * 0.25, 0, -1), size=vector(length_model * 0.5, wing_span_model, 2), color=color.white)

# Creamos la cola vertical
vertical_stabilizer = box(pos=vector(-length_model * 0.5, 0, -1), size=vector(2, 10, height_model), color=color.blue)

# Creamos la cola horizontal
horizontal_stabilizer = box(pos=vector(-length_model * 0.5, 0, -height_model), size=vector(2, wing_span_model, 10), color=color.blue)

# Creamos el motor
motor = cylinder(pos=vector(length_model * 0.75, wing_span_model * 0.5, -2), axis=vector(1, 0, 0), radius=3, color=color.gray(0.5))

# Creamos las ruedas
wheel1 = cylinder(pos=vector(length_model * 0.2, -wing_span_model * 0.5, -3), axis=vector(0, 0, -1), radius=1, color=color.black)
wheel2 = cylinder(pos=vector(length_model * 0.2, wing_span_model * 0.5, -3), axis=vector(0, 0, -1), radius=1, color=color.black)

# Agregamos la librea de KLM (KLM Livery)
klm_logo = text(text='KLM', pos=vector(-length_model * 0.1, 0, 3), align='center', depth=-0.3, color=color.blue, height=0.5)

# Configuramos la cámara
scene.camera.pos = vector(length_model * 2, 0, height_model * 0.5)
scene.camera.axis = vector(-length_model * 0.5, 0, height_model * 0.5)

# Mostramos la escena
scene.autoscale = False
