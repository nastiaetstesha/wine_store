import datetime


def get_age():
    current_year = datetime.datetime.now().year
    start_year = 1920
    return current_year - start_year

def get_year_word(age):
  if 11 <= age % 100 <= 19:  # Проверка для чисел, оканчивающихся на 11-19
      return "лет"
  elif age % 10 == 1:  # Если заканчивается на 1
      return "год"
  elif 2 <= age % 10 <= 4:  # Если заканчивается на 2, 3, 4
      return "года"
  else:  # Во всех остальных случаях "лет"
      return "лет"

