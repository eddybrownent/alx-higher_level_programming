#!/usr/bin/python3
# Script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

if __name__ == "__main__":
    # Use a with statement to open the URL
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as html:
        content = html.read()

        # Print a header for the info
        print("Body response:")

        # print the type of the contents
        print("     - type: {}".format(type(content)))

        # print the content of the response
        print("     - content: {}".format(content))

        # decodes the content "UTF-8" and print it
        print("     - utf8 content: {}".format(content.decode("utf-8")))
