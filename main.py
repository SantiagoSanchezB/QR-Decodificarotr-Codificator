import qrcode

data = 'Hola, la verdad hice este proyecto porque queria probar unas cosas de mi conocimiento y hacerte algo a ti, te hice un codigo QR solo para ti, Te amo chica hermosa que esta leyendo esto, y te tengo siempre en mi cabeza'

img = qrcode.make(data)

img.save('/home/santiago/Documentos/Python/QR Decodificator/IMGQR/myqrcode.png')