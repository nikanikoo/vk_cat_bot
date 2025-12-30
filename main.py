# ==========================================
# VK Cat Bot
#
# Author: Nika Falaleeva
# GitHub: https://github.com/nikanikoo
#
# Description:
# A simple VK bot that sends a random cat image
# in response to the /cat command.
#
# License: MIT
# ==========================================

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
import requests
from io import BytesIO

# --- CONFIGURATION ---
# Paste your VK user access token here
USER_TOKEN = "TOKEN" 

# List of chat or user IDs where the bot is allowed to respond
# To get the ID, send a message and check the console output
ALLOWED_CHATS = [2000000000] 
# --------------------

def get_random_cat_url():
    """ Fetches a direct URL to a random cat image using TheCatAPI. """
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        return data[0]['url']
    except Exception as e:
        print(f"Error while fetching cat image: {e}")
        return None

def upload_photo(upload, url):
    """ Downloads an image by URL and uploads it to VK messages without saving it to disk. """
    # Download image data
    img_data = requests.get(url).content
    # Store image in memory instead of a file
    image_file = BytesIO(img_data)

    # Upload image to VK message server
    photo = upload.photo_messages(photos=image_file)[0]
    
    # Build attachment string: photo{owner_id}_{photo_id}
    attachment = f"photo{photo['owner_id']}_{photo['id']}"
    return attachment

def main():
    """ Main bot loop. Listens for new messages and responds to /cat command. """
    # VK authorization
    vk_session = vk_api.VkApi(token=USER_TOKEN)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    longpoll = VkLongPoll(vk_session)

    print("Bot started! Waiting for /cat command...")

    # Listen for incoming events
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            
            # Debug output: shows chat ID and message text
            # print(f"Новое сообщение из ID: {event.peer_id} | Текст: {event.text}")

            # Check if this chat is allowed
            if event.peer_id in ALLOWED_CHATS:
                
                # Check command (case-insensitive)
                if event.text.lower() == '/cat':
                    print("Command received! Searching for a cat...")
                    
                    cat_url = get_random_cat_url()
                    
                    if cat_url:
                        attachment = upload_photo(upload, cat_url)
                        
                        # Send message with cat image
                        vk.messages.send(
                            peer_id=event.peer_id,
                            message="Here is your cat! 😺",
                            attachment=attachment,
                            random_id=0
                        )
                        print("Cat sent successfully!")
                    else:
                        vk.messages.send(
                            peer_id=event.peer_id,
                            message="Failed to find a cat :( Try again later.",
                            random_id=0
                        )

if __name__ == '__main__':
    main()