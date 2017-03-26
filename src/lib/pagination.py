from math import ceil


class Pagination(object):
    posts_per_page = 4

    items_wanted_before = 2
    items_wanted_after = 2

    current_page = None
    offset = None
    total_posts = None
    total_pages = None

    def __init__(self, page_id, total_posts):
        try:
            self.set_current_page(page_id)
            self.set_total_posts(total_posts)
            self.calc_offset()
            self.calc_total_pages()

            self.init_nb_items()
            self.nb_items_before = self.calc_items_before()
            self.nb_items_after = self.calc_items_after()

        except TypeError, ValueError:
            return None

    def set_current_page(self, page_id):
        """ Set the current page

            :param page_id:
                Page number
        """
        if page_id:
            if page_id.isdigit():
                self.current_page = int(page_id)
            else:
                self.current_page = None
        else:
            self.current_page = 1

    def set_total_posts(self, nb_posts):
        """ Set the number total of posts

            :param nb_posts:
                Number of posts
        """
        if nb_posts:
            self.total_posts = int(nb_posts)
        else:
            self.total_posts = 0

    def calc_offset(self):
        """ Calculate the offset used to retrieve posts in DB
        """
        if (self.current_page and self.posts_per_page
                and self.posts_per_page > 0):
            self.offset = (self.current_page*self.posts_per_page)
            self.offset = self.offset - self.posts_per_page
        else:
            self.offset = None

    def calc_total_pages(self):
        """ Calculate the total of pages
        """
        if (self.total_posts and self.posts_per_page
                and self.total_posts > 0 and self.posts_per_page > 0):
            self.total_pages = int(ceil(float(self.total_posts) /
                                   float(self.posts_per_page)))
        else:
            self.total_pages = 1

    def init_nb_items(self):
        """ Add overflowed items to the other side

            For example:
            We want 2 items before and after the {current page}
                1 2 {3} 4 5

            If there is not enough elems on one side :
                1 {2} 3 4           5 6 {7}
            We add the diff to the other side:
                1 {2} 3 4 5         3 4 5 6 {7}
        """
        first_items_overflow = None
        last_items_overflow = None

        first_item_id = self.current_page - self.items_wanted_before
        if first_item_id < 1:
            first_items_overflow = 1 - first_item_id

        last_item_id = self.current_page + self.items_wanted_after
        if last_item_id > self.total_pages:
            last_items_overflow = last_item_id - self.total_pages

        if first_items_overflow:
            self.items_wanted_after += first_items_overflow

        if last_items_overflow:
            self.items_wanted_before += last_items_overflow

    def calc_items_before(self):
        c_page = self.current_page
        items_wanted = self.items_wanted_before

        items = 0
        while c_page > 1 and items_wanted > 0:
            items += 1
            c_page = c_page - 1
            items_wanted = items_wanted - 1

        return items

    def calc_items_after(self):
        c_page = self.current_page
        items_wanted = self.items_wanted_after

        items = 0
        while c_page < self.total_pages and items_wanted > 0:
            items += 1
            c_page = c_page + 1
            items_wanted = items_wanted - 1

        return items

    def is_valid(self):
        """ Check if pagination is valid
        """
        if (self.current_page is None or
                self.offset is None or
                self.total_posts is None or
                self.total_pages is None or
                self.nb_items_before is None or
                self.nb_items_after is None or
                self.current_page > self.total_pages):
            return False
        return True
