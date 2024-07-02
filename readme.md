
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

Open the `config.json` file in the same directory as the script which will show the following content:

```json
{
"teamspeak_apiKey": "YOUR_TEAMSPEAK_API_KEY",
"open_w2g_flag": true,
"w2g_apiKey": "YOUR_W2G_API_KEY",
"dnd_beyond_url": "YOUR_DND_BEYOND_URL",
"foundry_url": "YOUR_FOUNDRY_URL"
}
```

Replace the placeholder values with your actual API keys and URLs. If you don't want a feature from this json file, just leave it as is and it will skip it.
If you dont want to open the new Watch2Gether Lobby right away, change the open_w2g_flag to false:
```json
"open_w2g_flag": false,
```

## Usage

1. **Ensure Teamspeak Client Query Plugin is Enabled**:
    - Open Teamspeak.
    - Go to \`Tools -> Options -> Addons\` and enable the \`Client Query\` plugin.
    - Go to \`Tools -> Options -> Client Query\` and set up your API key or password.

2. **Get your W2G API Key**:
    - Open Watch2Gether, login and go to \`Profile -> Edit profile -> Tools / API\`
   
3. **Run the Setup Script**:
   Execute the \`setup.bat\` script to install the necessary packages:
   ```bash
   setup.bat
   ```

4. **Run the Script**:
   ```bash
   start.bat
   ```

The script will:
- Create a Watch2Gether lobby and copy the invite link to the clipboard.
- If the Teamspeak API key is set, it will post the invite link to Teamspeak. If not, it will paste the link into the chat after 5 seconds.
- Open the specified DnDBeyond and Foundry VTT URLs in the default web browser.

## Troubleshooting
- **Read any exceptions by adding 'pause' as last statement in the start.bat**
    - Edit the ``start.bat`` to look like this to read any exceptions that had been thrown:
```
@echo off
python main.py
pause
```

- **Connection Issues with Teamspeak**:
    - Ensure the Client Query plugin is enabled and configured correctly.
    - Check for any firewall or network issues that may block the connection.

- **Antivirus Interference**:
    - Temporarily disable your antivirus software if it blocks the script from running.
    - Add the script directory to the exclusion list of your antivirus software.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
