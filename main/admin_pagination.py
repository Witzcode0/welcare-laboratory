from django.contrib import admin

def admin_pagination(per_page=50):
    """
    Decorator to apply pagination to a Django admin class.

    Args:
        per_page (int): The number of items to display per page. Default is 50.
    """
    def decorator(admin_class):
        class PaginatedAdmin(admin_class):
            list_per_page = per_page

        return PaginatedAdmin

    return decorator
