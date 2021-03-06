from instapy import InstaPy
from instapy.util import smart_run

insta_username = 'username'
insta_password = 'pass'

#пример лайков по городу Балаково в России
#https://www.instagram.com/explore/locations/c1942833/balakovo-russia/
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True, disable_image_load=True)

with smart_run(session):
    """ Activity flow """
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)
    #лайкаем по тегу
    session.like_by_locations(['c1942833/balakovo-russia/'], amount=100)
    # or
    session.like_by_locations(['266526296'], amount=100)
    # or include media entities from top posts section

    session.like_by_locations(['266526296'], amount=5, skip_top_posts=False)
