import pyqrcode
from pyqrcode import QRCode
//Give URL
s="https://youtube.com/channel/UCdto6jnxyQR2tjRt2DtnfXw"
url=pyqrcode.create(s)
url.svg("YouTubeQR.svg",scale=10)
