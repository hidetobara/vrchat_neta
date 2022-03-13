from pydoc import cli
import sys, io, argparse, asyncio
from obniz import Obniz
from pythonosc import udp_client


client = None

async def onconnect(obniz):
    obniz.io4.drive("5v")
    obniz.io4.output(True)
    obniz.io6.output(False)

    lower = 5.0
    upper = 0.0
    obniz.ad5.start()
    await obniz.wait(1000)
    for _ in range(0, 60):
        v = obniz.ad5.value
        print("VOL=", v)
        if v > upper:
            upper = v
        if v < lower:
            lower = v
        await obniz.wait(500)
    print(f"READY: {lower} < voltage < {upper}" )

    while(True):
        v = obniz.ad5.value
        rate = max((v - lower)/(upper - lower), 0)
        print("VOL=", rate)
        client.send_message("/finger/index", rate)
        await obniz.wait(1000)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000, help="The port the OSC server is listening on")
    parser.add_argument("--id", type=str, default="0000-0000", help="obniz ID")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    obniz = Obniz(args.id)
    obniz.onconnect = onconnect
    asyncio.get_event_loop().run_forever()
