class font:
    def __init__(self, txt = False, style = False, text = False, back = False):
        self.txt = txt
        self.style = style
        self.text = text
        self.back = back

    def color_txt(self, color_front = 0, front = False, back = False):
        self.text = True
