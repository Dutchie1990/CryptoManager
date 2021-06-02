from cryptomanager.app import app
import os
if os.path.exists("cryptomanager/app/env.py"):
    import cryptomanager.app.env

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
