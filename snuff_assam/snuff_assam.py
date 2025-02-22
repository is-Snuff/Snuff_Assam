import requests

class TelegramBot:
    def init(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"

    def get_bot_name(self):
        """Fetches the bot's name using the token."""
        response = requests.get(f"{self.base_url}/getMe")
        if response.status_code == 200:
            return response.json().get("result", {}).get("first_name", "Unknown Bot")
        return "Invalid Token"

    def send_message(self, chat_id, text):
        """Sends a text message to a Telegram chat."""
        data = {"chat_id": chat_id, "text": text}
        response = requests.post(f"{self.base_url}/sendMessage", data=data)
        return response.json()

    def send_photo(self, chat_id, photo_url, caption=""):
        """Sends a photo to a Telegram chat."""
        data = {"chat_id": chat_id, "photo": photo_url, "caption": caption}
        response = requests.post(f"{self.base_url}/sendPhoto", data=data)
        return response.json()

    def send_video(self, chat_id, video_url, caption=""):
        """Sends a video to a Telegram chat."""
        data = {"chat_id": chat_id, "video": video_url, "caption": caption}
        response = requests.post(f"{self.base_url}/sendVideo", data=data)
        return response.json()
