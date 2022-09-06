from collections import defaultdict


class Blog:
    def __init__(self, title, posts=None):
        self.title = title
        self.entries = posts if posts is not None else []  # wrapping list

    def append(self, post):
        self.entries.append(post)

    def by_tag(self):
        tag_index = defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tag_index[tag].append(post.as_dict())
        return tag_index

    def as_dict(self):
        return dict(
            title=self.title,
            underline="=" * len(self.title),
            entries=[p.as_dict() for p in self.entries],
        )
