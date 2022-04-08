import qrcode

data = 'Si todo ello era verdadero, aunque muchas cosas que haga no tenga su retribucion o una ganancia motenaria o algo siempre ganare una sinria tuya y con eso es el mayor pago que puedo tener de ti'

img = qrcode.make(data)

img.save('/home/santiago/Documentos/Python/QR Decodificator/IMGQR/MiVida.png')