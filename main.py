import os
from app import app
from dotenv import load_dotenv

if __name__ == "__main__":
    
    load_dotenv()
    debug = os.getenv('DEBUG', 'False').lower() in (
        'true', '1', 't', 'y', 'yes')
    app.run(port=6233, debug=debug)