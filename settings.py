import os

TOKEN = os.environ.get("SLACK_TOKEN")
channel = os.environ.get("SLACK_CHANNEL")

SLACK_BASE_URL = "https://slack.com/api"
DEFAULT_CHANNEL = channel or "general"