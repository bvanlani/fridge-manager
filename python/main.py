import time

from arduino.app_utils import App
from arduino.app_bricks.web_ui import WebUI

# Initialize the Web UI server
web_ui = WebUI()

# Add a simple REST API endpoint
web_ui.expose_api("GET", "/hello", lambda: {"message": "Hello, world!"})

# Send a welcome message over WebSocket to each client that connects
web_ui.on_connect(lambda sid: web_ui.send_message("hello", {"message": f"Hello, {sid}!"}))

App.run()
