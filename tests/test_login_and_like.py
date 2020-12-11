from instapy import InstaPy, smart_run

comments = ['aMazing!', 'So cool!!', 'Nice!', 'wow looks nice!',
            'Just incredible :open_mouth:',
            'What camera did you use @{}?',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            'this is awesome!', 'hahah', 'WAHH']

# ig_name = 'wixjsuttles23017'
# ig_passwd = 'wix123.'
ig_name = 'zhejiang20'
ig_passwd = 'zhe123.'

# session = InstaPy(username=ig_name, password=ig_passwd)
session = InstaPy(username=ig_name, password=ig_passwd, proxy_address='172.15.104.201', proxy_port=33001)

with smart_run(session):
    """ Activity flow """
    # general settings
    # 设置不取关哪些好友
    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.join_pods(topic='cat', engagement_mode='no_comments')

    # activity
    session.like_by_tags(["huachenyu", "cat", "dog"], amount=10)

    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
