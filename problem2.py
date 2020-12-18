import pandas as pd

def sort_by_name():
  data = pd.read_csv('file.csv', encoding="UTF - 8", sep=';')
  response = data.sort_values(by=["nome"], ascending=True)
  result = response.to_dict('records')

  return result


if __name__ == '__main__':
    print(sort_by_name())

