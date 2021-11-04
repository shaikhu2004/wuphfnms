import pywhatkit
from datetime import datetime

def wuphf_whatsapp(msg):
    now = datetime.now()

    currenthr = now.strftime("%H")
    currentmin = now.strftime("%M")
    sendinghr = int(currenthr)
    sendingmin = int(currentmin) + 2

    if sendingmin > 55:
        sendinghr = sendinghr + 1
        sendingmin = 2
    else:
        None

    if 1 <= sendingmin <= 9:
        sendingmin = (f"{sendingmin:02}")
    else:
        None

    print(sendinghr, sendingmin)

    pywhatkit.sendwhatmsg('+971545996491', msg, sendinghr, sendingmin)


