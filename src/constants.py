import os
from dotenv import load_dotenv
import configparser

load_dotenv()

config_obj = configparser.ConfigParser()
config_obj.read(os.path.expanduser('~/.linear-cli-ai-config.ini'))

LINEAR_GRAPHQL_ENDPOINT = "https://api.linear.app/graphql"
LINEAR_TOKEN = os.getenv("LINEAR_HEADER_AUTH") or config_obj.get("linear", "token") or ""
GPT_MODEL = os.getenv("GPT_MODEL") or config_obj.get("gpt", "model") or "gpt-3.5-turbo-0613"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or config_obj.get("gpt", "token") or ""