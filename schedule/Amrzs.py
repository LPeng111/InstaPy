import random
import traceback

from instapy import InstaPy, smart_run, set_workspace


class Amrzs:
    allowed_pod_topics = [
        "general",
        "fashion",
        "food",
        "travel",
        "sports",
        "entertainment"
    ]
    hashtags = ['travelcouples', 'travelcommunity', 'passionpassport',
                'travelingcouple',
                'backpackerlife', 'travelguide', 'travelbloggers',
                'travelblog', 'letsgoeverywhere',
                'travelislife', 'stayandwander', 'beautifuldestinations',
                'moodygrams',
                'ourplanetdaily', 'travelyoga', 'travelgram', 'sunsetporn',
                'lonelyplanet',
                'igtravel', 'instapassport', 'travelling', 'instatraveling',
                'travelingram',
                'mytravelgram', 'skyporn', 'traveler', 'sunrise',
                'sunsetlovers', 'travelblog',
                'sunset_pics', 'visiting', 'ilovetravel',
                'photographyoftheday', 'sunsetphotography',
                'explorenature', 'landscapeporn', 'exploring_shotz',
                'landscapehunter', 'colors_of_day',
                'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                'thegreatoutdoors']
    comments = ['Amazing! Just followed you, if you could follow back so we can stay connected',
                'So cool!! Just followed you, if you could follow back so we can stay connected',
                'Nice! Just followed you, if you could follow back so we can stay connected',
                'wow looks nice! Just followed you, if you could follow back so we can stay connected',
                'Just incredible :open_mouth: Just followed you, if you could follow back so we can stay connected',
                'Love your posts @{}, Just followed you, if you could follow back so we can stay connected',
                'Looks awesome @{}, Just followed you, if you could follow back so we can stay connected',
                'Getting inspired by you @{}, Just followed you, if you could follow back so we can stay connected',
                'this is awesome! Just followed you, if you could follow back so we can stay connected',
                'Nice shot! @{}, Just followed you, if you could follow back so we can stay connected',
                'I love your profile! @{}, Just followed you, if you could follow back so we can stay connected',
                '@{} Love it! Just followed you, if you could follow back so we can stay connected',
                '@{} :heart::heart: , Just followed you, if you could follow back so we can stay connected',
                'Love your posts @{}, Just followed you, if you could follow back so we can stay connected',
                'Looks awesome @{}, Just followed you, if you could follow back so we can stay connected',
                'Getting inspired by you @{}, Just followed you, if you could follow back so we can stay connected',
                ':raised_hands: Yes! Just followed you, if you could follow back so we can stay connected',
                'Love your posts, 好漂亮啊 @{}, Just followed you, if you could follow back so we can stay connected',
                'Love your posts, 好美啊 @{}, Just followed you, if you could follow back so we can stay connected',
                '我感觉我看到了天使, Just followed you, if you could follow back so we can stay connected',
                '这张照片拍的真好 @{}, Just followed you, if you could follow back so we can stay connected',
                '哇哇哇，好看 @{}, Just followed you, if you could follow back so we can stay connected',
                '@{}:revolving_hearts::revolving_hearts: , Just followed you, if you could follow back so we can stay connected',
                '@{}:fire::fire::fire: , Just followed you, if you could follow back so we can stay connected']

    def __init__(
            self,
            ig_name: str = None,
            ig_passwd: str = None,
            proxy_ip: str = None,
            proxy_port: str = None,
            proxy_name: str = None,
            proxy_passwd: str = None,
            workspace: str = None,
            headless: bool = False
    ):
        self.ig_name = ig_name
        self.ig_passwd = ig_passwd
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.proxy_name = proxy_name
        self.proxy_passwd = proxy_passwd
        self.headless = headless
        set_workspace(workspace)

    def get_session(self):
        session = InstaPy(username=self.ig_name, password=self.ig_passwd, proxy_address=self.proxy_ip,
                          proxy_port=self.proxy_port, proxy_username=self.proxy_name, proxy_password=self.proxy_passwd,
                          disable_image_load=False, headless_browser=self.headless, multi_logs=False)
        return session

    def daily_maintenance(self):
        # 打乱hash标签
        random.shuffle(self.hashtags)
        # 随机选择6个标签
        my_hashtags = self.hashtags[:6]

        session = self.get_session()

        with smart_run(session, threaded=True):
            print(session.browser.get_cookies())
            # general settings
            session.set_dont_like(['sad', 'rain', 'depression'])
            session.set_do_follow(enabled=True, percentage=20, times=1)
            session.set_do_comment(enabled=True, percentage=80)
            session.set_comments(self.comments)
            session.set_do_like(True, percentage=70)
            session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
            session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
            session.set_relationship_bounds(enabled=True,
                                            potency_ratio=None,
                                            delimit_by_numbers=True,
                                            max_followers=9999,
                                            max_following=9999,
                                            min_followers=10,
                                            min_following=50)

            session.set_quota_supervisor(enabled=True,
                                         sleep_after=["likes", "follows"],
                                         sleepyhead=True, stochastic_flow=True,
                                         notify_me=True,
                                         peak_likes_hourly=30,
                                         peak_likes_daily=60,
                                         peak_comments_hourly=10,
                                         peak_comments_daily=30,
                                         peak_follows_hourly=20,
                                         peak_follows_daily=None,
                                         peak_unfollows_hourly=5,
                                         peak_unfollows_daily=10,
                                         peak_server_calls_hourly=None,
                                         peak_server_calls_daily=4700)

            session.set_user_interact(amount=10, randomize=True, percentage=80)

            # let's go! :>
            session.unfollow_users(amount=100, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                                   style="FIFO",
                                   unfollow_after=12 * 60 * 60, sleep_delay=501)
            # session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
            #                        style="FIFO", unfollow_after=24 * 60 * 60,
            #                        sleep_delay=501)
            session.like_by_tags(my_hashtags, amount=90, media=None)
            # session.follow_user_followers(['ironman.official', 'jjlin', 'danielkordan'], amount=20, randomize=True, interact=True, sleep_delay=120)
            """ Joining Engagement Pods...
            """
            random.shuffle(self.allowed_pod_topics)
            session.join_pods(topic=self.allowed_pod_topics[0], engagement_mode='no_comments')

    def follow_and_like(self):
        session = self.get_session()
        print(session.browser.get_cookies())
        # let's go! :>
        with smart_run(session):
            counter = 0

            while counter < 1:
                counter += 1
                try:
                    # settings
                    session.set_relationship_bounds(enabled=False,
                                                    potency_ratio=-1.21,
                                                    delimit_by_numbers=True,
                                                    max_followers=4590,
                                                    max_following=5555,
                                                    min_followers=45,
                                                    min_following=77)

                    session.set_do_comment(True, percentage=45)
                    session.set_comments(self.comments)

                    # activity
                    session.follow_by_tags(['cat', 'dog'], amount=5)
                    session.follow_user_followers(['lajixi', 'jaychou'], amount=5, randomize=False)
                    session.like_by_tags(
                        ['cat', 'ironman'],
                        amount=8, skip_top_posts=True)

                    """ Joining Engagement Pods...
                        """
                    session.join_pods(topic='entertainment', engagement_mode='light')
                except:
                    print(traceback.format_exc())
