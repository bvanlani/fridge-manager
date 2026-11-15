from arduino.app_utils import App
from arduino.app_bricks.web_ui import WebUI
from arduino.app_bricks.video_imageclassification import VideoImageClassification
from datetime import datetime, UTC
import json

ui = WebUI()
classification_stream = VideoImageClassification(confidence=0.5, debounce_sec=0.0)

ui.on_message("override_th", lambda sid, threshold: classification_stream.override_threshold(threshold))

def send_detections_to_ui(classifications: dict):
    if not classifications:
        return
    entries = [
        {"content": label, "confidence": conf, "timestamp": datetime.now(UTC).isoformat()}
        for label, conf in classifications.items()
    ]
    ui.send_message("classifications", message=json.dumps(entries))

classification_stream.on_detect_all(send_detections_to_ui)

App.run()