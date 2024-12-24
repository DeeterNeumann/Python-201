'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- One: Select all the actors with the first name of your choice

- Two: Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:PASSWORD@localhost/sakila")

connection = engine.connect()
metadata = sqlalchemy.MetaData()

actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload_with=engine)

# pprint(film)
# pprint(actor)

# # Select all the actors with the first name of your choice
query_one = sqlalchemy.select(actor).where(actor.columns.first_name == 'PENELOPE')
result_proxy_one = connection.execute(query_one)
result_set_one = result_proxy_one.fetchall()
pprint(result_set_one)

# Select all the actors and the films they have been in
join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id)
join_statement = join_actor_film_actor.join(film, film.columns.film_id == film_actor.columns.film_id)
query_two = sqlalchemy.select(film.columns.title, actor.columns.first_name).select_from(join_statement)
result_proxy_two = connection.execute(query_two)
result_set_two = result_proxy_two.fetchall()
pprint(result_set_two)

# # Select all the actors that have appeared in a category of a comedy of your choice
category_join_statement = join_actor_film_actor.join(film_category, film_category.columns.film_id == film_actor.columns.film_id)
query_three = sqlalchemy.select(film_category.columns.category_id, actor.columns.first_name, actor.columns.last_name)\
                        .select_from(category_join_statement).where(film_category.columns.category_id == 5)
result_proxy_three = connection.execute(query_three)
result_set_three = result_proxy_three.fetchall()
pprint(result_set_three)

# # Select all the comedic films and sort them by rental rate
join_film_film_category = film.join(film_category, film_category.columns.film_id == film.columns.film_id)
film_fc_cat_join_statement = join_film_film_category.join(category, category.columns.category_id == film_category.columns.category_id)
query_four = sqlalchemy.select(film.columns.title, film.columns.rental_rate).select_from(film_fc_cat_join_statement).where(film_category.columns.category_id == 5)
result_proxy_four = connection.execute(query_four)
result_set_four = result_proxy_four.fetchall()
pprint(result_set_four)

# # Using one of the statements above, add a GROUP BY statement of your choice
# category_join_statement = join_actor_film_actor.join(film_category, film_category.columns.film_id == film_actor.columns.film_id)
query_five = sqlalchemy.select(film_category.columns.category_id, actor.columns.first_name, actor.columns.last_name).select_from(category_join_statement).where(film_category.columns.category_id == 5).group_by(film_category.columns.category_id, actor.columns.first_name, actor.columns.last_name)
result_proxy_five = connection.execute(query_five)
result_set_five = result_proxy_five.fetchall()
pprint(result_set_five)


# # Using one of the statements above, add a ORDER BY statement of your choice
# film_fc_cat_join_statement = join_film_film_category.join(category, category.columns.category_id == film_category.columns.category_id)
query_six = sqlalchemy.select(film.columns.title, film.columns.rental_rate).select_from(film_fc_cat_join_statement).where(film_category.columns.category_id == 5).order_by(sqlalchemy.asc(film.columns.rental_rate))
result_proxy_six = connection.execute(query_six)
result_set_six = result_proxy_six.fetchall()
pprint(result_set_six)

# # # Select all the comedic films and sort them by rating
# join_film_film_category = film.join(film_category, film_category.columns.film_id == film.columns.film_id)
# film_fc_cat_join_statement = join_film_film_category.join(category, category.columns.category_id == film_category.columns.category_id)
# query_seven = sqlalchemy.select(film.columns.title, film.columns.rating).select_from(film_fc_cat_join_statement).where(film_category.columns.category_id == 5)
# result_proxy_seven = connection.execute(query_seven)
# result_set_seven = result_proxy_seven.fetchall()
# pprint(result_set_seven)
