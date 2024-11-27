import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos de los participantes: nombre, correo y equipo (numero)
# Dos personas del mismo equipo no pueden regalarse entre ellas
participantes = [
    {"nombre": "Maria", "correo": "maria@hotmail.com", "equipo": 1},
    {"nombre": "Juan", "correo": "juan@gmail.com", "equipo": 2}
]

# Función para realizar el sorteo sin conflictos de equipo
def realizar_sorteo(participantes):
    while True:
        random.shuffle(participantes)
        asignaciones = []
        conflicto = False
        for i, participante in enumerate(participantes):
            asignado = participantes[(i + 1) % len(participantes)]
            if participante["equipo"] == asignado["equipo"]:
                conflicto = True
                break
            asignaciones.append((participante, asignado))
        if not conflicto:
            return asignaciones

# Configuración de SMTP y envío de los correos
def enviar_correo(destinatario, receptor_asignado):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 465  # Puerto SSL
    smtp_user = 'a@gmail.com'  # Poner el correo que envía el resto
    smtp_pass = 'pass'         # Contraseña de la cuenta de correo: Importante tener la doble autenticación activada y generar contraseña de aplicación google
    
    mensaje = MIMEMultipart()
    mensaje["From"] = smtp_user
    mensaje["To"] = destinatario["correo"]
    mensaje["Subject"] = "Asunto"
    
    # Cuerpo del mensaje
    texto = (f"¡Hola {destinatario['nombre']}!\n\n"
             f"¡Bienvenid@ al amigo invisible! 🎁\n\n"
             f"Te ha tocado hacerle un regalo a: 🌟 {receptor_asignado['nombre']} 🌟 \n\n"
            )
    mensaje.attach(MIMEText(texto, "plain"))
    
    try:
        # Conexión segura con SSL
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, destinatario["correo"], mensaje.as_string())
            print(f"Correo enviado a {destinatario['nombre']}")
    except Exception as e:
        print(f"Error al enviar correo a {destinatario['nombre']}: {e}")

# Las asignaciones se guardan en un .txt en caso de tener que consultarlas
def guardar_asignaciones_en_archivo(asignaciones, nombre_archivo="secreto_asignaciones_amigo_invisible.txt"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Asignaciones de Amigo Invisible:\n\n")
        for participante, receptor_asignado in asignaciones:
            archivo.write(f"{participante['nombre']} le regala a  {receptor_asignado['nombre']} \n")
    print(f"Asignaciones guardadas en {nombre_archivo}")
    
# Ejecutar el sorteo y enviar correos
asignaciones = realizar_sorteo(participantes)
guardar_asignaciones_en_archivo(asignaciones)

for participante, receptor_asignado in asignaciones:
    enviar_correo(participante, receptor_asignado)
