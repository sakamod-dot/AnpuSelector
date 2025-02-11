import serial
import time
import sounddevice as sd

# シリアルポートの設定
try:
    ser = serial.Serial('COM7', 9600)  # COMポートは適宜変更してください
except serial.SerialException as e:
    print(f"シリアルポートを開くことができませんでした: {e}")
    exit(1)

# 音声デバイスの情報を取得
try:
    default_device = sd.query_devices(kind='output')
    device_name = default_device['name']
except Exception as e:
    print(f"音声デバイスの情報を取得できませんでした: {e}")
    device_name = "Disconnected"

# デバイス名をシリアル通信で送信
ser.write(device_name.encode())

# シリアルポートを閉じる
ser.close()