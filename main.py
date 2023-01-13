import sys

CAMBRIDGE_DICTIONARY_WORD = "https://dictionary.cambridge.org/dictionary/english/"

def get_args():
    # Get file path from arguments.
    file_path = None

    try:
        file_path = sys.argv[1]
    except IndexError:
        print("File path isn't set!")
        exit(code=1)

    return file_path

def get_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.rstrip() for line in file]
    except OSError as exc:
        print("Can't open file for reading!")
        exit(code=1)

    return words

def process_words(index, word):
    word_link = CAMBRIDGE_DICTIONARY_WORD + word
    row = """
    <tr>
        <td>%s</td>
        <td><a href="%s" target="_blank">%s</a></td>
    </tr>
    """ % (index + 1, word_link, word)

    return row

def generate_data(words):
    result_data = """
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>5,000 of the most used English words</h1>
            <a href="https://studynow.ru/dicta/allwords" target="_blank">Источник</a></p>
            <table>
                <tr>
                    <th>№</th>
                    <th>Word</th>
                </tr>
    """
    for index, word in enumerate(words):
        result_data += process_words(index, word)
        
    result_data += """     </table>
        </body>
    </html>"""

    return result_data

def save_data(data):
    try:
        with open("result.html", 'w', encoding='utf-8') as file:
            file.write(data)
    except OSError as exc:
        print("Can't open file for writing!")
        exit(code=1)

def main():
    file_path = get_args()
    words = get_words(file_path)
    result_data = generate_data(words)
    save_data(result_data)

if __name__ == "__main__":
	main()