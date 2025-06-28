from decouple import config

# Load the Gemini API Key from .env file or environment variables
# The config function will raise an UndefinedValueError if the variable is not found.
GEMINI_API_KEY = config("GEMINI_API_KEY")

# You can add other configurations here as needed, for example:
# DEBUG_MODE = config("DEBUG_MODE", default=False, cast=bool)

# To use in other modules:
# from .config import GEMINI_API_KEY
# print(GEMINI_API_KEY)
