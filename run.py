# Import the application
from cryptomanager.app import app
# Import OS to access the env.py
import os
if os.path.exists("cryptomanager/app/env.py"):
    import cryptomanager.app.env

# Run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
