from datetime import datetime

from blog import Blog
from mastering_object_oriented_programming.blog_rst_test import blog_template
from post import Post

travel = Blog("Travel")
travel.append(
    Post(date=datetime(2022, 8, 11, 17, 35, 00),
         title="Hard Aground",
         rst_text="""Some embrassing revelation. Including :) and f""",
         tags=("#RedRanger", "#Whitby42", "#ICW"),
    )
)

travel.append(
    Post(date=datetime(2022, 9, 5, 11, 22, 33),
         title="Anchor Follies",
         rst_text="""Some witty epigram. Including < & > characters.""",
         tags=("#RedRanger", "#Whitby42", "#Mistakes"),
    )
)

print(travel.as_dict())
print(blog_template.render(tags=travel.by_tag(), **travel.as_dict()))
