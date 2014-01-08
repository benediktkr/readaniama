Read An IAmA
===

An IAmA on reddit with a person tends to be structured like an interview with questions and answers. One good example are the recent celebrity IAmA's. I don't think that the reddit comment system is always the best medium to read these in, so I made this!

Usage
----

Pass the link to the IAmA to `scraper.py` and pipe the output to a HTML file. Like this:

    $ python scraper.py [link-to-iama] > file.html


Reddit JSON
====

The reddit json structure is a little confusing. These are my notes for how it works. 

Listings
---

Retrieve a python "listing":

    >>> json = requests.get(thread + ".json").json()

The returned JSON works like this:
    
    >>> type(json) 
    list
    >>> len(json)
    2
    >>> type(json[0]) # The post itself
    dir
    >>> type(json[1]) # The comments for the thread
    dir

The selfpost/link
---

The first element of this list contains the original post, wrapped inside a kind-data structure:

    >>> json[0].keys()
    ['kind', 'data']
    >>> json[0]['kind']
    'Listing'
    >>> json[0]['data'].keys()
    ['modhash', 'children', 'after', 'before']

Since this is the post iself, there is only one child kind-data thing

    >>> len(json[0]['data']['children']) 
    1
    >>> json[0]['data']['children'][0].keys() 
    ['kind', 'data']
    >>> json[0]['data']['children'][0]['kind']
    't3'  # Link

Finding relevant things in it:

    >>> post = json[0]['data']['children'][0]['data']
    >>> post['is_self']
    True
    >>> post['permalink']
    u'/r/IAmA/comments/1ujvrg/jerry_seinfeld_here_i_will_give_you_an_answer/'
    >>> post['id']
    u'1ujvrg'
    >>> post['title']
    u'Jerry Seinfeld here. I will give you an answer.'
    >>> post['author']
    u'_Seinfeld'
    >>> post['name']
    u't3_1ujvrg'
    >>> post['num_comments']
    14521
    >>> post['selftext'] 
    ...   # Uses \n for newline
    >>> post['ups']-post['downs']
    3490    


Comments
---

    >>> comments = json[1]['data']['children']
    >>> # Check the number of Top-level comments available to us
    >>> len(comments)
    58
    >>> comments[0].keys()
    [u'kind', u'data']
    >>> comments[0]['kind']
    u't1'    # Comment

This works much the same as the selfpost. Too see avilable data:
     >>> top_comment = comments[0]['data']
     >>> top_comment.keys()
     ...

Some examples of Interesting data:
     >>> top_comment['ups'] - top_comment['downs']
     1298
     >>> top_comment['author']
     u'Thinking_is_Free'
     >>> top_comment['body']
     u'What is the most bizarre/surreal location that you have been to and been recognized? '
     >>> top_comment['id']
     u'ceiw01p'
     >>> top_comment['parent_id']
     u't3_1ujvrg'

Then find it's child comments:
     >>> len(top_comment['replies']['data']['children'])
     1
     >>> jerry_replies = top_comment['replies']['data']['children'][0]['data']
     >>> jerry_replies['author']
     u'_Seinfeld'


Notes:
----

Type prefixes

   t1_  Comment
   t2_  Account
   t3_  Link
   t4_  Message
   t5_  Subreddit
   t6_  Award
   t8_  PromoCampaign
