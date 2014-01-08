def print_html_header(title):
    html = """<!DOCTYPE html>
    <html>
      <head>
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link href="css/bootstrap.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </head>
  <body>
    <div class="container">
    <div class="page-header">
    <h1>{title}</h1>
    </div>

    """.format(title=title)

    print html

def print_selfpost_text(text):
    html = """<p>{text}</p>"""
    print html.format(text=text)

def print_panel_start(comment):
    html = """<div class="panel panel-default">
    <div class="panel-body">"""
    print html

def print_announcement(text):
    html = """<p><strong>Announcement from OP: </strong>{text}</p>"""
    print html.format(text=text)


def print_question_start(author, text):
    html = """<p><strong>Question ({user}): </strong> {text}</p>"""
    post = text.encode("utf-8").replace("\n", "<br>")
    print html.format(text=post, user=author)

def print_answer_start(text):
    post = text.encode("utf-8").replace("\n", "<br>")
    print """<p><strong>Answer: </strong> {text}</p>""".format(text=post)

def print_div_end():
    html = """</div>"""
    print html

def print_html_footer():
    html = """<div>
    </body>
    </html>"""

    print html
