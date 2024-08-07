import json
import telnetlib
import webbrowser

import requests
import pyperclip
import pyautogui
import time

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

w2g_apiKey = config.get('w2g_apiKey', '')
open_w2g_flag = config.get('open_w2g_flag', '')
teamspeak_apiKey = config.get('teamspeak_apiKey', '')
dnd_beyond_url = config.get('dnd_beyond_url', '')
foundry_url = config.get('foundry_url', '')
w2g_fixedUrl = config.get('w2g_fixedLink', '')


# Step 1: Create a Watch2Gether lobby
def create_w2g_lobby():
    url = 'https://api.w2g.tv/rooms/create.json'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "w2g_api_key": w2g_apiKey,
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
def send_to_teamspeak(message, server='localhost', port=25639, teamspeak_apiKey=teamspeak_apiKey, target_mode=2,
                      target=1):
    try:
        tn = telnetlib.Telnet(server, port)
        tn.read_until(b"TS3 Client")
        tn.write(f"auth apikey={teamspeak_apiKey}\n".encode('utf-8'))
        tn.read_until(b"msg=ok")

        tn.write(f"sendtextmessage targetmode={target_mode} target={target} msg={message}\n".encode('utf-8'))
        tn.read_until(b"msg=ok")

        tn.close()
    except Exception as e:
        print(f"An error occurred while connecting to Teamspeak: {e}")


def open_url_in_browser(link):
    webbrowser.open(link)


def main():
    if w2g_fixedUrl != 'YOUR_EXISTING_W2G_LOBBY_URL':
        pyperclip.copy(w2g_fixedUrl)
        if teamspeak_apiKey == 'YOUR_TEAMSPEAK_API_KEY':
            print("No Teamspeak API Key was set. The link will be pasted in 5 seconds...")
            time.sleep(5)
            paste_into_teamspeak()
        else:
            send_to_teamspeak(w2g_fixedUrl)
        if open_w2g_flag:
            open_url_in_browser(w2g_fixedUrl)
    else:
        if w2g_apiKey == 'YOUR_W2G_API_KEY':
            print("No Watch2Gether API Key was set. Skipping...")
        else:
            invite_link = create_w2g_lobby()
            pyperclip.copy(invite_link)
            if teamspeak_apiKey == 'YOUR_TEAMSPEAK_API_KEY':
                print("No Teamspeak API Key was set. The link will be pasted in 5 seconds...")
                time.sleep(5)
                paste_into_teamspeak()
            else:
                send_to_teamspeak(invite_link)
            if open_w2g_flag:
                open_url_in_browser(invite_link)
    if dnd_beyond_url == 'YOUR_DND_BEYOND_URL':
        print("No DnD-Beyond Character URL was set. Skipping...")
    else:
        open_url_in_browser(dnd_beyond_url)
    if foundry_url == 'YOUR_FOUNDRY_URL':
        print("No DnD-Lobby URL was set. Skipping...")
    else:
        open_url_in_browser(foundry_url)


if __name__ == "__main__":
    main()
