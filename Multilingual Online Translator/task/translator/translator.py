class Translator:

    languages = {"en": "English",
                 "fr": "French"}

    def __init__(self):
        self.target_language = ""
        self.text = ""

    def translate(self):
        print(f'Type "en" if you want to translate from {self.languages["fr"]} into {self.languages["en"]}, '
              f'or "fr" if you want to translate from {self.languages["en"]} into {self.languages["fr"]}:')
        self.target_language = input()
        print("Type the word you want to translate:")
        self.text = input()
        print(f'You chose "{self.target_language}" as the language to translate "{self.text}" to.')


translator = Translator()
translator.translate()
