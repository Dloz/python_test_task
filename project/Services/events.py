import os
from watchdog.events import RegexMatchingEventHandler

class FilesEventHandler(RegexMatchingEventHandler):
    JSON_FILES_REGEX = [r".*\.json$"]

    def __init__(self):
        super().__init__(self.JSON_FILES_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f"{filename}.json"
        print(filename)