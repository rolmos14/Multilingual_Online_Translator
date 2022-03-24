import requests
from bs4 import BeautifulSoup


class Translator:

    languages = {1: "Arabic",
                 2: "German",
                 3: "English",
                 4: "Spanish",
                 5: "French",
                 6: "Hebrew",
                 7: "Japanese",
                 8: "Dutch",
                 9: "Polish",
                 10: "Portuguese",
                 11: "Romanian",
                 12: "Russian",
                 13: "Turkish"}

    def __init__(self):
        self.source_language = ""
        self.target_language = ""
        self.text = ""
        self.page = ""
        self.soup = ""

    def run(self):
        print("Hello, you're welcome to the translator. Translator supports:")
        for num, language in self.languages.items():
            print(f'{num}. {language}')
        print("Type the number of your language:")
        self.source_language = self.languages[int(input())]
        print("Type the number of a language you want to translate to or '0' to translate to all languages:")
        selected_language = input()
        if selected_language != '0':
            self.target_language = self.languages[int(selected_language)]
        print("Type the word you want to translate:")
        self.text = input()
        # Translate only to one language
        if self.target_language:
            self.request_translation()
        else:
            # Translate to all languages except to source_language
            for tar_lang in self.languages.values():
                self.target_language = tar_lang
                if self.source_language != self.target_language:
                    self.request_translation()

    def request_translation(self):
        url = f'https://context.reverso.net/translation/' \
              f'{self.source_language.lower()}-{self.target_language.lower()}/{self.text}'
        user_agent = {'User-Agent': 'Chrome/98.0.4758.102'}
        self.page = requests.get(url, headers=user_agent)
        if self.page.status_code == 200:
            # print("200 OK")
            self.soup = BeautifulSoup(self.page.content, "html.parser")
            with open(f'{self.text}.txt', 'a', encoding='UTF-8') as f:
                # Word translations
                print(f'\n{self.target_language} Translations:')
                print(f'\n{self.target_language} Translations:', file=f)
                word_trans = self.get_word_translations()
                print('\n'.join(word_trans[:5]))  # print only up to first 5 translations
                print('\n'.join(word_trans[:5]), file=f)  # print only up to first 5 translations
                # Example translations
                print(f'\n{self.target_language} Examples:')
                print(f'\n{self.target_language} Examples:', file=f)
                example_trans = self.get_example_translations()
                for i in range(0, 10, 2):  # print only up to first 5 translations
                    print('\n'.join(example_trans[i:i + 2]), end="\n\n")
                    print('\n'.join(example_trans[i:i + 2]), end="\n\n", file=f)
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
translator.run()
