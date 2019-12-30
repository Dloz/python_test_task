import os
import api
from watchdog.events import RegexMatchingEventHandler
from BL.db_saver import DbSaver
from DAL.models import db

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
        db_saver = DbSaver(db)
        db_saver.save(file_path=filename)