<<<<<<< HEAD
#QR Code Generator
=======
#QR CODE GENERATOR
>>>>>>> 15dcad882313666c09cbe25a9ddf4a4f1a5af683
import pyqrcode
from pyqrcode import QRCode
s="https://youtube.com/channel/UCdto6jnxyQR2tjRt2DtnfXw"
url=pyqrcode.create(s)
url.svg("YouTubeQR.svg",scale=10)
