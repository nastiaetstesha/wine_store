import collections
import datetime as dt
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_age_since(establish_year=1920):
    # вычисление возраста с момента основания
    age = dt.date.today().year - establish_year

    # Определяем правильное склонение для слова "год"
    if 11 <= age % 100 <= 19:  # Проверка для чисел, оканчивающихся на 11-19
        years_name =  "лет"
    elif age % 10 == 1:  # Если заканчивается на 1
        years_name =  "год"
    elif 2 <= age % 10 <= 4:  # Если заканчивается на 2, 3, 4
        years_name =  "года"
    else:  # Во всех остальных случаях "лет"
        years_name = "лет"
    return f"{age} {years_name}"


def main():
    path_to_wines = "/Users/egorsemin/Practice/wine_store/wine2 (1).xlsx"

    path_to_wines = Path(path_to_wines)
    if not path_to_wines.exists():
        sys.exit("Файл с винами не существует")

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("template.html")

    wines = pandas.read_excel(
        path_to_wines, na_values=" ", keep_default_na=False
    ).to_dict(orient="records")

    wines_categorised = collections.defaultdict(list)
    for wine in wines:
        wines_categorised[wine["Категория"]].append(wine)

    sorted_categories = sorted(wines_categorised.keys())

    rendered_page = template.render(
    age=get_age_since(establish_year=1920),
    wines_categorised={category: wines_categorised[category] for category in sorted_categories})

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
