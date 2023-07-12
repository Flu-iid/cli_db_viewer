import os


class Showable():
    def __init__(self, att: list, rows: list, title_space: int = 20) -> None:
        self.width, self.height = os.get_terminal_size()
        self.att = att
        self.rows = rows
        self.space = title_space if self.width / \
            len(att) > title_space else self.width//len(att)

    def __str__(self):
        return "<Showable object>"

    def titler(self, title: str):
        ws = self.space - len(title) if self.space > len(title) else 0
        if ws % 2:  # if odd
            left_deli = ws//2 + 1
            right_deli = ws//2
            return left_deli*" "+title+right_deli*" "
        else:  # if even
            deli = ws//2
            return deli*" "+title+deli*" "

    def show(self):
        for i, title in enumerate(self.att):
            print(Showable.titler(title), end="")
            if i+1 == len(self.att):
                print()
            else:
                print("|", end="")
        print(self.width*"-")
        for j, row in enumerate(self.rows):
            for i, r in enumerate(row):
                print(Showable.titler(r), end="")
                if i+1 == len(row):
                    print()
                else:
                    print("|", end="")
            if j+1 != len(self.rows):
                print(self.width*"-")
