from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_category""")
        categories = dict_fetchall(cursor)
    return categories


def get_author():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_authors""")
        authors = dict_fetchall(cursor)
        return authors


def get_category_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) as count from dashboard_category""")
        cat_count = dict_fetchone(cursor)
    return cat_count


def get_author_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(full_name) as count from dashboard_authors""")
        aut_count = dict_fetchone(cursor)
    return aut_count


def get_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) as count from dashboard_news""")
        new_count = dict_fetchone(cursor)
    return new_count


def get_ref():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) as count from dashboard_reference""")
        ref_count = dict_fetchone(cursor)
    return ref_count


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_news""")
        news = dict_fetchall(cursor)
    return news


def news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT name, COUNT(title) as news_count FROM dashboard_category left JOIN 
        dashboard_news ON dashboard_category.id=dashboard_news.category_id GROUP BY name """)
        count = dict_fetchall(cursor)
    return count


def get_view():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT name, SUM(views) as 
        count  FROM dashboard_category LEFT JOIN dashboard_news on dashboard_category.id=dashboard_news.category_id 
        GROUP BY name""")
        view = dict_fetchall(cursor)
    return view


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
