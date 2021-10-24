import time
import os
import argparse

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from profanity_filter import ProfanityFilter

# Text downloaded from 
# http://loremfuckingipsum.com/index.php

class Watcher:

    def __init__(self, directory, handler):
        self.observer = Observer()
        self.directory = directory
        self.handler = handler

    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    def __init__(self, callback):
        self.callback = callback
        super().__init__()

    def on_any_event(self, event):
        self.callback(event)


def callback(event):
    if event.is_directory:
        return None

    print(event)

    if event.event_type == "modified":

        # Check for temp file
        index = event.src_path.rfind("/")
        path = "" if index==-1 else event.src_path[:index+1]
        filename = event.src_path if index==-1 else event.src_path[index+1:]

        if filename == ".temp":
            return None

        pf = ProfanityFilter()

        # Check if file is clean
        with open(event.src_path, "r") as f:
            is_clean = pf.is_clean(f.read())

        if is_clean:
            return

        # Get stat from original file
        stat = os.stat(event.src_path)

        with open(event.src_path, "r") as original, open(f"{path}.temp", "w") as censored:
            for line in original:
                censored.write(pf.censor(line))     

        # Remove original file
        os.remove(event.src_path)

        # Set stat for censored file
        os.chown(f"{path}.temp", stat.st_uid, stat.st_gid)

        # Rename censored file
        os.rename(f"{path}.temp", event.src_path)

def parse_args():

    parser = argparse.ArgumentParser("Censor any files placed in specified directory")
    parser.add_argument("--directory", type=str, default="censor/directory", help="The directory to watch")
    return parser.parse_args()


def main():

    handler = Handler(callback)

    args = parse_args()
    directory = args.directory

    if not os.path.exists(directory):
        print(f"Unable to find directory '{directory}'")
        exit()

    watcher = Watcher(directory, handler)

    print(f"Watching directory '{directory}'")

    watcher.run()

if __name__ == "__main__":
    main()
