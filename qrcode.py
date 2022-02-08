#QR CODE GENERATOR
import pyqrcode
from pyqrcode import QRCode
s="https://youtube.com/channel/UCdto6jnxyQR2tjRt2DtnfXw"
url=pyqrcode.create(s)
url.svg("YouTubeQR.svg",scale=10)
