import psycopg2


def popular_author():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select name, count(log.id) as num "
              "from articles, authors, log "
              "where authors.id = articles.author and "
              "log.path = concat('/article/', articles.slug) "
              "group by name order by num desc;")
    authors_info = c.fetchall()
    db.close()
    return authors_info


def popular_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select slug, count(log.id) as num "
              "from articles, log "
              "where log.path = concat('/article/', articles.slug) "
              "group by slug order by num desc limit 3;")
    articles_info = c.fetchall()
    db.close()
    return articles_info


def error_stats():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select ar.request_date, "
              "round("
              "er.err_requests_cnt*100/ar.requests_count, 2"
              ") as err_rate "
              "from all_requests_stats ar "
              "join err_requests_stats as er "
              "on ar.request_date = er.request_date "
              "where er.err_requests_cnt > ar.requests_count / 100;")
    err_info = c.fetchall()
    db.close()
    return err_info


if __name__ == "__main__":

    print("The most popular article authors of all time are:")
    for key, value in popular_author():
        print(key, "-", value, "views")
    print('\n')

    print("The most popular three articles of all time are:")
    for key, value in popular_articles():
        print(key, "-", value, "views")
    print('\n')

    print("On these days more than 1% of requests led to errors:")
    for key, value in error_stats():
        print(key, "-", value, "%", "errors")
