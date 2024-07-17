# BtReport.py
class BtReport:
    def __init__(self, title, subtitle, *sentences):
        self.title = title
        self.subtitle = subtitle
        self.sentences = list(sentences)

    def __str__(self):
        return f"{self.title}\n{self.subtitle}\n" + "\n".join(self.sentences)
