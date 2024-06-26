
# Watch2Gether to Teamspeak Integration

This script creates a Watch2Gether lobby, generates an invite link, and posts it into a Teamspeak chat. Additionally, it can open specified URLs for DnDBeyond and Foundry VTT.

## Features

- **Watch2Gether Lobby Creation**: Automatically creates a Watch2Gether lobby and generates an invite link.
- **Teamspeak Integration**: Posts the Watch2Gether invite link into Teamspeak.
- **DnDBeyond URL Opener**: Opens a specified DnDBeyond URL in the default web browser.
- **Foundry VTT URL Opener**: Opens a specified Foundry VTT URL in the default web browser.

## Prerequisites

- Python 3.6 or higher
- The following Python packages, specified in `requirements.txt`:
    - `requests`
    - `pyperclip`
    - `pyautogui`

You can install these packages using the provided `setup.bat` script:
```bash
pip install -r requirements.txt -v
```

## Configuration

Create a `config.json` file in the same directory as the script with the following content:

```json
{
"teamspeak_apiKey": "YOUR_TEAMSPEAK_API_KEY",
"w2g_apiKey": "YOUR_W2G_API_KEY",
"dnd_beyond_url": "https://www.dndbeyond.com/characters/your_character_id",
"foundry_url": "https://foundryvtt.yourserver.com/game"
}
```

Replace the placeholder values with your actual API keys and URLs.

## Usage

1. **Ensure Teamspeak Client Query Plugin is Enabled**:
    - Open Teamspeak.
    - Go to \`Tools -> Options -> Addons\` and enable the \`Client Query\` plugin.
    - Go to \`Tools -> Options -> Client Query\` and set up your API key or password.

2. **Run the Setup Script**:
   Execute the \`setup.bat\` script to install the necessary packages:
   ```bash
   setup.bat
   ```

3. **Run the Script**:
   ```bash
   python script.py
   ```

The script will:
- Create a Watch2Gether lobby and copy the invite link to the clipboard.
- If the Teamspeak API key is set, it will post the invite link to Teamspeak. If not, it will paste the link into the chat after 5 seconds.
- Open the specified DnDBeyond and Foundry VTT URLs in the default web browser.

## Script Overview

### create_w2g_lobby
Creates a Watch2Gether lobby and returns the invite link.

### paste_into_teamspeak
Simulates the paste and enter keys to post the invite link into Teamspeak chat.

### send_to_teamspeak
Connects to the Teamspeak Client Query plugin via telnet and sends the invite link.

### open_dndbeyond
Opens the specified DnDBeyond URL in the default web browser.

### open_foundry
Opens the specified Foundry VTT URL in the default web browser.

### main
Coordinates the creation of the Watch2Gether lobby, posting the invite link to Teamspeak, and opening the DnDBeyond and Foundry VTT URLs.

## Troubleshooting

- **Connection Issues with Teamspeak**:
    - Ensure the Client Query plugin is enabled and configured correctly.
    - Check for any firewall or network issues that may block the connection.

- **Antivirus Interference**:
    - Temporarily disable your antivirus software if it blocks the script from running.
    - Add the script directory to the exclusion list of your antivirus software.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
