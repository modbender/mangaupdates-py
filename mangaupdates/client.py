import requests


class MangaUpdates:
    def __init__(self):
        # URLs
        self.base_url = "https://api.mangaupdates.com/v1"

        # Endpoints

        # aboutus
        self.aboutus_url = self.base_url + "/aboutus"
        self.aboutus_users_url = self.base_url + "/aboutus/users"
        self.aboutus_category_url = self.base_url + "/aboutus/category"
        self.aboutus_category_id_url = self.base_url + "/aboutus/category/{}"
        self.aboutus_reorder_url = self.base_url + "/aboutus/reorder"
        self.aboutus_category_id_users_url = (
            self.base_url + "/aboutus/category/{}/users"
        )
        self.aboutus_category_id_user_id_url = (
            self.base_url + "/aboutus/category/{}/users/{}"
        )

        # account

        # genre
        self.genre_url = self.base_url + "/genres"
        self.genre_id_url = self.base_url + "/genres/{}"

        # groups
        self.groups_url = self.base_url + "/groups"
        self.groups_id_url = self.base_url + "/groups/{}"
        self.groups_id_reject_url = self.base_url + "/groups/{}/reject"
        self.groups_search_url = self.base_url + "/groups/search"
        self.groups_id_series_url = self.base_url + "/groups/{}/series"

        # lists
        self.lists_url = self.base_url + "/lists"
        self.lists_id_url = self.base_url + "/lists/{}"
        self.lists_public_user_id_url = self.base_url + "/lists/public/{}"
        self.lists_public_user_id_stats_url = self.base_url + "/lists/public/{}/stats"
        self.lists_public_user_id_search_id_url = (
            self.base_url + "/lists/public/{}/search/{}"
        )
        self.lists_id_search_url = self.base_url + "/lists/{}/search"
        self.lists_series_url = self.base_url + "/lists/series"
        self.lists_id_series_bulk_url = self.base_url + "/lists/{}/series/bulk"
        self.lists_series_delete_url = self.base_url + "/lists/series/delete"
        self.lists_series_id_url = self.base_url + "/lists/series/{}"
        self.lists_series_update_url = self.base_url + "/lists/series/update"
        self.lists_similar_list_name_series_id_url = (
            self.base_url + "/lists/similar/{}/series/{}"
        )

        # misc
        self.misc_time_url = self.base_url + "/misc/time"
        self.misc_online_url = self.base_url + "/misc/online"
        self.misc_slow_transaction_status_transaction_id_url = (
            self.base_url + "/misc/slow-transaction-status/{}"
        )
        self.misc_stats_url = self.base_url + "/misc/stats"

        # categories
        self.categories_url = self.base_url + "/categories/search"

        # Session
        self.session = requests.Session()
