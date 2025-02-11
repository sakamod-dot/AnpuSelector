import serial,time

PORT = 'COM7'  # Windows の場合COM*

ser = serial.Serial(port=PORT,baudrate=115200,timeout=1)

command = 'Hello!'
send_bytes = bytes(command+'\r\n','utf-8')
ser.write(send_bytes)
buf = ser.readlines()
print(buf,type(buf))

command = 'name?'
send_bytes = bytes(command+'\r\n','utf-8')
ser.write(send_bytes)
buf = ser.readlines()
buf = [i.decode().strip() for i in buf]
print(buf)
ser.close()

try:
    while True:
        ser.open()
        command = 'temp?'
        send_bytes = (command+'\r\n').encode('utf-8')
        ser.write(send_bytes)
        buf = ser.readlines()
        buf = [i.decode().strip() for i in buf]
        print(buf)
        ser.close()
        time.sleep(1)

except KeyboardInterrupt:
    print('stop')
    pass
