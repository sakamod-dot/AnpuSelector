import serial
from tqdm import tqdm
import platform

# OSに応じたポートの設定
if platform.system() == 'Windows':
    PORT = 'COM7'  # Windows の場合、適切なCOMポートを指定してください
elif platform.system() == 'Darwin':
    PORT = '/dev/cu.usbmodem*'  # Mac の場合
else:
    raise EnvironmentError("Unsupported platform")

BAUD = 9600

try:
    ser = serial.Serial(
        port=PORT,
        baudrate=BAUD,
        timeout=1,
        write_timeout=1,
        exclusive=True,
    )
except serial.SerialException as e:
    print(f"シリアルポートを開くことができませんでした: {e}")
    exit(1)

# 任意のテキストデータをserial_strに代入
serial_str = "a"

try:
    send_bytes = bytes(serial_str + '\r\n', 'utf-8')
    ser.write(send_bytes)
    ser.flush()

    receive_bytes = ser.read_all()
    receive = receive_bytes.decode('utf-8').splitlines()

    if len(receive) > 0:
        print(f"Received: {receive}")

except serial.SerialTimeoutException as e:
    print(f"シリアルポートへの書き込みがタイムアウトしました: {e}")
finally:
    ser.close()