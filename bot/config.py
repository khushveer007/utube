import os


class Config:

    BOT_TOKEN = os.environ.get("5848537364:AAEwt5ED7zOcTYOHBJdn1jMmJ1GJ8po3rv4")

    SESSION_NAME = os.environ.get("Ictuploadbot", ":memory:")

    API_ID = int(os.environ.get("26367674"))

    API_HASH = os.environ.get("9758292b691b82c5915900c506fcbe83")

    CLIENT_ID = os.environ.get("1066294001498-ne4ajfmj9vs2ufbb23qmm7oek0mdho5t.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("5697445137"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
