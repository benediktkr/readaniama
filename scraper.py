import requests
import pprint
import sys

from html import *

def get_replies(comment):
    children = comment['replies']['data']['children']
    replies = [a['data'] for a in children if a['kind'] == "t1"]
    return replies

def iama(thread):
    json = requests.get(thread + ".json").json()
    selfpost = json[0]['data']['children'][0]['data']
    op = selfpost['author']
    children = json[1]['data']['children']
    comments = [a['data'] for a in children if a['kind']=="t1"]

    print_html_header(selfpost['title'])

    print_selfpost_text(selfpost['selftext'].encode("utf-8"))

    for top_comment in comments:
        print_panel_start(top_comment)
        search(top_comment, op)
        print_div_end()
        print_div_end()

    print_html_footer()
def search(comment, op, level=0):
    # onnur hugmynd: nota id og parent_id
    if 'replies' not in comment or not comment['replies']:
        return 

    replies = get_replies(comment)
    op_next = any(a['author'] == op for a in replies)

    smaller_set = [a for a in replies if a['author'] == op] 

    if comment['author'] == op:
        printed_something = True
        if level == 0:
            print_announcement(comment['body'])
        else:
            print_answer_start(comment['body'])
        
    elif op_next:
        printed_something = True
        print_question_start(comment['author'], comment['body'])

    for subcomment in replies:
        search(subcomment, op, level+1)

        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: python scraper.py [link]"
        sys.exit(1)
    
    if sys.argv[1] == "jerry":
        thread = "http://www.reddit.com/r/IAmA/comments/1ujvrg/jerry_seinfeld_here_i_will_give_you_an_answer/"
    else:
        thread = sys.argv[1]

    iama(thread)






