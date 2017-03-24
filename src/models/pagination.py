from models.post import Post
from math import ceil


class Pagination(object):
    posts_per_page = 4

    ITEMS_WANTED_BEFORE = 2
    ITEMS_WANTED_AFTER = 2
    nb_items_before = ITEMS_WANTED_BEFORE
    nb_items_after = ITEMS_WANTED_AFTER

    current_page = 1
    total_pages = 1
    total_posts = 0
    offset = 0

    def __init__(self, page_id, total_posts):
        if page_id:
            self.current_page = int(page_id)

        if total_posts:
            self.total_posts = total_posts

        self.offset = (self.current_page*self.posts_per_page)
        self.offset = self.offset - self.posts_per_page

        self.total_pages = int(ceil(float(self.total_posts) /
                                    float(self.posts_per_page)))

        self.init_nb_items()
        self.set_items_before()
        self.set_items_after()

    def init_nb_items(self):
        res = self.current_page - self.ITEMS_WANTED_BEFORE
        diff = 0
        if res < 1:
            diff = (res - 1) * -1

        res2 = self.current_page + self.ITEMS_WANTED_AFTER
        diff2 = 0
        if res2 > self.total_pages:
            diff2 = res2 - self.total_pages

        self.ITEMS_WANTED_AFTER += diff
        self.ITEMS_WANTED_BEFORE += diff2


    def set_items_before(self):
        if self.ITEMS_WANTED_BEFORE < 1:
            return 0

        minimum_page_id = 1

        first_item_id = self.current_page - self.ITEMS_WANTED_BEFORE
        self.nb_items_before = self.ITEMS_WANTED_BEFORE
        if first_item_id < minimum_page_id:
            diff = first_item_id - minimum_page_id
            self.nb_items_before = self.ITEMS_WANTED_BEFORE + diff

    def set_items_after(self):
        if self.ITEMS_WANTED_AFTER < 1:
            return 0

        maximum_page_id = self.total_pages
        last_item_id = self.current_page + self.ITEMS_WANTED_AFTER
        self.nb_items_after = self.ITEMS_WANTED_AFTER
        if last_item_id > maximum_page_id:
            diff = last_item_id - maximum_page_id
            self.nb_items_after = self.ITEMS_WANTED_AFTER - diff

    def validate(self):
        if self.current_page >= 1 and (self.current_page <= self.total_pages):
            return True
        return False
