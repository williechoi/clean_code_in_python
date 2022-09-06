import datetime


class Post:
    def __init__(self, date, title, rst_text, tags):
        self.date = date            # 날짜
        self.title = title          # 제목
        self.rst_text = rst_text    # 텍스트
        self.tags = tags            # 태그

    def as_dict(self) -> dict:
        return dict(
            date=str(self.date),
            title=self.title,
            underline="-" * len(self.title),
            rst_text=self.rst_text,
            tag_text=" ".join(self.tags)
        )
