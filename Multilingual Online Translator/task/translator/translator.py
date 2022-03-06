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
            # Word translations
            print(f'\n{self.languages[self.target_language].capitalize()} Translations:')
            word_trans = self.get_word_translations()
            print('\n'.join(word_trans[:5]))  # print only up to first 5 translations
            # Example translations
            print(f'\n{self.languages[self.target_language].capitalize()} Examples:')
            example_trans = self.get_example_translations()
            for i in range(0, 10, 2):
                print('\n'.join(example_trans[i:i + 2]))
                print()
        else:
            print(self.page.status_code, "NOK")

    def get_word_translations(self):
        word_trans_container = self.soup.find('div', {"id": "translations-content"})
        word_trans_links = word_trans_container.find_all('a')
        word_trans = []
        for link in word_trans_links:
            word_trans.append(link.text.strip())
        return word_trans

    def get_example_translations(self):
        example_trans_container = self.soup.find('section', {"id": "examples-content"})
        example_trans_spans = example_trans_container.find_all('span', {"class": "text"})
        example_trans = []
        for span in example_trans_spans:
            example_trans.append(span.text.strip())
        return example_trans


translator = Translator()
translator.translate()
