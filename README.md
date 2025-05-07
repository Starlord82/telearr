# TeleArr

This uses a Telegram bot to update you on the status of movies and series from Radarr and Sonarr.  
You can use it alongside the same bot used for Addarr — they work well together.

---

## 🔧 How to Set Up Your Telegram Bot

1. **Create a Telegram Bot:**
   - Open Telegram and search for [@BotFather](https://t.me/BotFather)
   - Type `/newbot` and follow the prompts:
     - Choose a name (e.g., `TeleArrBot`)
     - Choose a username (must end in `bot`, e.g., `telearr_notifier_bot`)
   - BotFather will give you a **bot token** (looks like: `123456789:ABCdefGhIJKlmnoPQrstuvWXyz`)

2. **Get Your Chat ID:**
   - Start a conversation with your bot by clicking its Telegram link and sending any message
   - Visit this URL in your browser (replace `<TOKEN>` with your bot token):
     ```
     https://api.telegram.org/bot<TOKEN>/getUpdates
     ```
   - Look for `"chat":{"id":123456789,...}` — that number is your **Chat ID**

---

## 🛠️ Configuration

Once you have your `BOT_TOKEN` and `CHAT_ID`, set them as environment variables or in a `.env` file:

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmnoPQrstuvWXyz
TELEGRAM_CHAT_ID=123456789
```
---

## 🔔 Webhook Integration with Radarr and Sonarr

TeleArr listens for webhook events from Radarr and Sonarr and forwards them as Telegram messages.

### ⚙️ Steps to Integrate:

1. Open **Radarr** or **Sonarr**
2. Go to:  
   `Settings` → `Connect` → `+ Add` → choose **Webhook**
3. Fill in the following fields:

| Field        | Value                                   |
|--------------|-----------------------------------------|
| **Method**   | `POST`                                  |
| **URL**      | `http://your-server-ip:5000/webhook`    |
| **Name**     | `TeleArr` (or any name you prefer)      |
| **Triggers** | Choose the events you'd like to monitor |

4. Click **Test** to verify. You should receive a Telegram message.

Your bot should now send updates when the selected events occur.

---




