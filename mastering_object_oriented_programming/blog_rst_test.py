from jinja2 import Template

blog_template = Template("""
{{title}}
{{underline}}

{% for e in entries %}
{{e.title}}
{{e.underline}}

{{e.rst_text}}

:date: {{e.date}}
:tags: {{e.tag_text}}

{% endfor %}

Tag Index
========
{% for t in tags %}

* {{t}}
  {% for post in tags[t] %}
  
  - `{{post.title}}`_
  {% endfor %}
{% endfor %}
""")

