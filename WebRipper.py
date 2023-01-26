print("Website Ripper 1.0")
from pywebcopy import save_website
import sys, urllib.robotparser
while True:
    try:
        save_website(
              url=input("What's the URL? "),
              project_folder=input("Please specify a path to save to: "),
              project_name="Download",
              bypass_robots=True,
              debug=True,
              open_in_browser=True,
              delay=None,
              threaded=False,
        )

    except Exception as e:
        print(e)
