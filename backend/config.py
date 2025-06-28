import os
from decouple import Config, RepositoryEnv, config as default_config_loader

# Construct the path to the .env file located in the same directory as this config.py
# __file__ is the path to config.py itself. os.path.dirname(__file__) is its directory.
_current_dir = os.path.dirname(os.path.abspath(__file__)) # Use abspath for robustness
_env_file_path = os.path.join(_current_dir, '.env')

# Create a specific config instance that loads from the .env file in this directory
if os.path.exists(_env_file_path):
    # If .env exists, prioritize it.
    _config_instance = Config(RepositoryEnv(_env_file_path))
else:
    # If .env file does not exist next to config.py, fall back to default python-decouple behavior
    # (which checks CWD, parent dirs for .env/.ini and then environment variables).
    _config_instance = default_config_loader

# Now use this specific config instance to load variables
try:
    GEMINI_API_KEY = _config_instance("GEMINI_API_KEY")
except Exception as e:
    # Optionally, log this error to a proper logging system instead of print
    # print(f"Error loading GEMINI_API_KEY: {e}")
    raise

# You can add other configurations here as needed, for example:
# DEBUG_MODE = _config_instance("DEBUG_MODE", default=False, cast=bool)

# To use in other modules:
# from backend.config import settings
# print(settings.GEMINI_API_KEY)

class Settings:
    def __init__(self):
        try:
            self.GEMINI_API_KEY = _config_instance("GEMINI_API_KEY")
        except Exception as e:
            # Optionally, log this error to a proper logging system instead of print
            # print(f"Error loading GEMINI_API_KEY into Settings class: {e}")
            self.GEMINI_API_KEY = None # Default to None or raise error

settings = Settings()
