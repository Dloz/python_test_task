import os
import api
from watchdog.events import RegexMatchingEventHandler
from DAL.models import db, db_saver

class FilesEventHandler(RegexMatchingEventHandler):
    '''
    When new file appears, event handler will process the file found.
    '''
    JSON_FILES_REGEX = [r".*\.json$"]

    def __init__(self):
        super().__init__(self.JSON_FILES_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f"{filename}.json"
        result = db_saver.save(file_path=filename)
        if result == 'OK':
            os.remove(filename)
            print('File', filename, 'deleted')