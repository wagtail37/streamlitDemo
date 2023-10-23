import streamlit as st
import serial

# Arduinoとのシリアル通信を開始
ser = serial.Serial('COM5', 9600)  # 'COM5'はArduinoが接続されているポート名です

# streamlitアプリケーションの設定
st.title("Arduinoデータ受信アプリ")

try:
    while True:
        # Arduinoからデータを読み取り、デコードして表示
        data = ser.readline().decode('utf-8').strip()
        st.write("受信したデータ:", data)
except KeyboardInterrupt:
    # キーボードでCtrl+Cが押された場合にクリーンアップ
    ser.close()

#streamlit run arduino_streamlit.py
