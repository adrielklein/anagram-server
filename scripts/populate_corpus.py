import requests as requests
import json

from scripts.start_server import PORT

if __name__ == '__main__':
    words = []
    with open('words.txt') as file:
        for word in file:
            words.append(word.strip())

    requests.post('http://localhost:{}/words.json'.format(PORT), data=json.dumps({"words": words}))
    print('Finished loading corpus successfully')
