# 🎁 amiguin

Código para realizar un sorteo de tipo amigo invisible entre varios participantes.
* Se envían emails personalizados.
* Posibilidad de excluir relaciones: las personas con el mismo número de "equipo" no pueden regalarse entre ellas.
  
## Tecnologías del proyecto
* 📚 **Random:** para realizar el sorteo aleatorio de los participantes.
* 📚 **smtplib:** permite la comunicación con servidores de correo electrónico mediante el protocolo SMTP. Se configura con              soporte SSL para garantizar conexiones seguras al servidor de correo.
* 📚 **email.mime:** se usa para crear correos electrónicos en formato MIME (Texto y HTML).
* 📚 **Gestión de archivos:** manejo de archivos de Python para guardar las asignaciones en un archivo de texto. Esto actúa como respaldo del sorteo.

  
## Tutorial para enviar los correos
Una vez definida la lista de participantes, antes de compilar el código, es necesario verificar:
1. Que la cuenta que definimos para enviar los correos tenga activado el doble factor de autenticación en google. [Activar la verificación en dos pasos](https://support.google.com/accounts/answer/185839?hl=es&co=GENIE.Platform%3DDesktop)
2. Que tenemos generada una contraseña de aplicación google.
[Iniciar sesión con contraseñas de aplicación](https://support.google.com/accounts/answer/185833?hl=es)  

Tanto la cuenta como la contraseña generada deben quedar definidas en el código.
 
