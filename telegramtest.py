# # 텔레그램 봇으로 알림
# import requests
#
#
# def send_telegram_message(token, chat_id, message):
#     base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
#     response = requests.get(base_url)
#     return response.json()
#
#
# # replace with your bot token and chat ID
# token = "6477170870:AAHz5BDApt1oBWI4yTV6siKnT-NTgAderXs"
# chat_id = "6324662357"
# message = "예약에 성공했습니다."
#
# response = send_telegram_message(token, chat_id, message)
# print(response)
# import wave
# import pyaudio as pyaudio
#
# with wave.open("alert.wav", 'rb') as wf:
#     p = pyaudio.PyAudio()
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
#
#     chunk = 1024
#     data = wf.readframes(chunk)
#
#     while data:
#         stream.write(data)
#         data = wf.readframes(chunk)
#
#     stream.stop_stream()
#     stream.close()
#
#     p.terminate()

# import requests
#
#
# def send_telegram_message(token, chat_id, message):
#     base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
#     response = requests.get(base_url)
#     return response.json()
#
#
# # replace with your bot token and chat ID(kangpu_bot)
# token = "6519072084:AAG16KvwOStQvnlFjPD3fWsOrIDHJXUqgNk"
# chat_id = "5209913866"
# message = "예약에 성공했습니다."
#
# response_check = send_telegram_message(token, chat_id, message)
# print("원하는 좌석이 선택되었습니다.")
# print(response_check)
