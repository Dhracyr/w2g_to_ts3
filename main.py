import telnetlib

import requests
import pyperclip
import pyautogui
import time

from APIKeys_and_URLs import apiKey


# Step 1: Create a Watch2Gether lobby
def create_w2g_lobby():
    url = 'https://api.w2g.tv/rooms/create.json'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "w2g_api_key": "nkmz57lc6o5kz1k9eipzx1tjq3vti5wzbdbl4096klp5edo1y86t0k5babnhdp2y",
        "share": "https://www.youtube.com/watch?v=6Dh-RL__uN4",
        "bg_color": "#3a4759",
        "bg_opacity": "50"
    }

    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    return f"https://w2g.tv/rooms/{response_data['streamkey']}"


# Step 2: Paste the invite link into Teamspeak
def paste_into_teamspeak():
    # Assuming Teamspeak is already open and the chat box is focused
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")


# Function to connect to Teamspeak and send a message
def send_to_teamspeak(message, server='localhost', port=25639, apiKey=apiKey, target_mode=2, target=1):
    try:
        tn = telnetlib.Telnet(server, port)
        tn.read_until(b"TS3 Client")
        tn.write(f"auth apikey={apiKey}\n".encode('utf-8'))
        tn.read_until(b"msg=ok")

        tn.write(f"sendtextmessage targetmode={target_mode} target={target} msg={message}\n".encode('utf-8'))
        tn.read_until(b"msg=ok")

        tn.close()
    except Exception as e:
        print(f"An error occurred while connecting to Teamspeak: {e}")


def main():
    invite_link = create_w2g_lobby()
    pyperclip.copy(invite_link)
    time.sleep(5)  # Give some time to switch to Teamspeak chat window
    send_to_teamspeak(invite_link)
    open_dndbeyond(dndbeyond_url)


if __name__ == "__main__":
    main()
