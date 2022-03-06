import requests
from bs4 import BeautifulSoup


class Translator:

    languages = {"en": "english",
                 "fr": "french"}

    def __init__(self):
        self.source_language = ""
        self.target_language = ""
        self.text = ""
        self.page = ""
        self.soup = ""

    def translate(self):
        print(f'Type "en" if you want to translate from {self.languages["fr"].capitalize()} '
              f'into {self.languages["en"].capitalize()}, '
              f'or "fr" if you want to translate from {self.languages["en"].capitalize()} '
              f'into {self.languages["fr"].capitalize()}:')
        self.target_language = input()
        self.source_language = "fr" if self.target_language == "en" else "en"
        print("Type the word you want to translate:")
        self.text = input()
        print(f'You chose "{self.target_language}" as a language to translate "{self.text}".')
        self.request_translation()

    def request_translation(self):
        url = f'https://context.reverso.net/translation/' \
              f'{self.languages[self.source_language]}-{self.languages[self.target_language]}/{self.text}'
        user_agent = {'User-Agent': 'Chrome/98.0.4758.102'}
        self.page = requests.get(url, headers=user_agent)
        if self.page.status_code == 200:
            print("200 OK")
            self.soup = BeautifulSoup(self.page.content, "html.parser")
            print("Translations")
            # Word translations
            word_trans_container = self.soup.find('div', {"id": "translations-content"})
            word_trans_links = word_trans_container.find_all('a')
            word_trans = []
            for link in word_trans_links:
                word_trans.append(link.text.strip())
            print(word_trans)
            # Example translations
            example_trans_container = self.soup.find('section', {"id": "examples-content"})
            example_trans_spans = example_trans_container.find_all('span', {"class": "text"})
            example_trans = []
            for span in example_trans_spans:
                example_trans.append(span.text.strip())
            print(example_trans)
        else:
            print(self.page.status_code, "NOK")


translator = Translator()
translator.translate()
