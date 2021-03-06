
import cv2
import aiohttp
import asyncio, sys
import cv2, base64
import numpy as np

async def get_data(arg='localhost'):
    while True:
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(f'http://{arg}:8080/') as resp:
                fromsrv =await resp.read()
                jpg_original = base64.b64decode(fromsrv)
                if jpg_original==None:
                    print("Nothing from server. Has the service been started?")
                    break
                nparr = np.frombuffer(jpg_original, np.uint8)
                if (nparr.size<5000):
                    print("Details:")
                    print(fromsrv)
                    print("Format Error: Could a proxy have blocked me?")
                    break
                img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                cv2.imshow('Output', img_np)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

def main(argv):
   inputfile = ''
   outputfile = ''
   # try:
   #    opts, args = getopt.getopt(argv) #,"hi:o:",["ifile=","ofile="])
   # except getopt.GetoptError:
   #    print( 'arg error') #'test.py -i <inputfile> -o <outputfile>'
      # sys.exit(2)
   # for opt, arg in opts:
   #    if opt == '-h':
   #       print 'test.py -i <inputfile> -o <outputfile>'
   #       sys.exit()
   #    elif opt in ("-i", "--ifile"):
   #       inputfile = arg
   #    elif opt in ("-o", "--ofile"):
   #       outputfile = arg
   loop = asyncio.get_event_loop()
   loop.run_until_complete(get_data(argv))


if __name__ == "__main__":
   if len(sys.argv) > 1:
       main(sys.argv[1])
   else:
       main('localhost')

