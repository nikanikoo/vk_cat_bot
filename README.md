# VK Cat Bot 😺
A simple user bot for VKontakte that sends a random picture of a cat on command.

The user bot works through LongPoll, receives messages in authorized chats, and in response sends a photo of the cat uploaded directly to VK messages.

## 📌Features
- 📩 Handles incoming VK messages
- 😺 /cat command — sends a random cat image
- 🌐 Uses the public TheCatAPI
- 🖼 Uploads images without saving them to disk
- 🔒 Restricts access by chat / user ID

## 🛠 Technologies Used
- Python 3.8+
- vk_api
- requests
- TheCatAPI

## ⚙️ Installation & Setup
##### 1. Clone the repository
```bash
git clone https://github.com/nikanikoo/vk-cat-bot.git
cd vk-cat-bot
```
##### 2. Install dependencies
```bash
pip install vk_api requests
```
##### 3. Configuration
Open **main.py** and set:
```python
USER_TOKEN = "YOUR_VK_TOKEN" ## (we get the token here - https://vkhost.github.io/)
ALLOWED_CHATS = [2000000009]
```
- USER_TOKEN — VK user access token
- ALLOWED_CHATS — list of chat or user IDs where the bot is allowed to respond
> 💡 To get a peer_id, send any message — the bot will print the ID to the console.

##### 4. Running
```bash
python main.py
```
After launching, the bot will start listening to messages.

## 💬 Usage
Send the following command in an allowed chat:
```bash
/cat
```
We get the chat ID from the Debug output. Add it to ALLOWED_CHATS, and then the bot will send a random cat in response to the command.

## 📜 License - MIT
