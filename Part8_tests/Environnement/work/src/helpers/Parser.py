class Parser:

    def __init__(self, separator):
        self.separator = separator
        self.parsed_line = list

    def parse(self, sentence):
        """
            '9007'.isdigit() renvoie False
            '9007'.isdigit() renvoie True
        """
        return ' '.join([
            i.strip() for i in sentence.split(self.separator) if i.strip().isdigit()
        ])
