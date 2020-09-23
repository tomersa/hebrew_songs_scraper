import string
import os
import pickle

from bs4 import BeautifulSoup

OUTPUT_FILE_PATH = "output.txt"
REPLACESABLES = {
    '_': ' '
}


def extract_text(filepath):
    html = None
    with open(filepath) as f:
        html = f.read()
    soup_mysite = BeautifulSoup(html, features='lxml')
    song_text = soup_mysite.find("span", {"class": "artist_lyrics_text"})

    if not song_text:
        print("Couldn\'t extract text. skipping")
        return ''

    text = song_text.text
    cleaned_text = text

    for char in string.ascii_letters + string.digits:
        if char in cleaned_text:
            print("Song is in latin alphabet. skipping")
            return ''

    for k, v in REPLACESABLES.items():
        cleaned_text = cleaned_text.replace(k, v)

    return cleaned_text


if __name__ == "__main__":
    song_text = []
    try:
        with open("song_list.lst") as song_list_file:
            song_text = song_list.lst
    except:
        pass

    if len(song_text) == 0:
        for html_path in os.listdir('shironet'):
            try:
                print(f"Processing file {html_path}")
                extracted_text = extract_text(os.path.join("shironet", html_path))
                if len(extracted_text) > 0:
                    song_text.append(extracted_text)
            except Exception as e:
                print(f"Error while processing file {html_path}:")
                print(e)

    song_lengths = [len(i) for i in song_text]
    avg = sum(song_lengths) / float(len(song_text))
    min_song = min(song_lengths)
    max_song = max(song_lengths)

    print(f"song_text.length: {len(song_text)}")
    print(f"avg: {avg}")
    print(f"min: {min_song}")
    print(f"max: {max_song}")


    print(f"Writing output file:{OUTPUT_FILE_PATH}")
    with open(OUTPUT_FILE_PATH, "w") as outFile:
        outFile.flush()
        outFile.writelines(song_text)

    print(f"Writing list file: song_list.lst")
    with open("song_list.lst", "wb") as song_list_file:
        song_list_file.flush()
        pickle.dump(song_text, song_list_file)

    print("Finished successfully")
