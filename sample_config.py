import os

api_id = 26330942
api_hash = os.environ.get("API_HASH", "5de9fd033aa828dfd3bf0c28adeee660)
bot_token = os.environ.get("7999358042:AAGXpAPxJkftNoUVKtzq4aQsmbs32wBEmf0")
auth_users = os.environ.get("AUTH_USERS", "6883471516)
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6883471516)
owner_users = [int(num) for num in osowner_users.split(",")]
