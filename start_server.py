import os

from app.main import create_app


def _get_words():
    result = []
    with open('words.txt') as file:
        for word in file:
            result.append(word.strip())
    return result


PORT = 5000
if __name__ == '__main__':
    port = int(os.environ.get('PORT', PORT))
    app = create_app(_get_words())
    app.run(host='0.0.0.0', port=port)
