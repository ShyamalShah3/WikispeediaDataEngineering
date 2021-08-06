import pandas as pd

def fix_path(path_string: str):
  path = path_string.split(";")
  real_path = []
  final_path = []
  for article in path:
    if article == "<":
      real_path.pop()
    else:
      real_path.append(article)
    final_path.append(real_path[-1])
  return ";".join(final_path)

csv_files = [
  "decoded_csv/paths_finished_decoded.csv",
  "decoded_csv/paths_unfinished_decoded.csv"
]

for csv_file in csv_files:
  df = pd.read_csv(csv_file)
  try:
    df['rating'] = df['rating'].astype('Int64')
  except KeyError:
    pass
  df['path'] = df['path'].map(fix_path)
  df.to_csv(csv_file.split('/')[0] + "/fixed_" + csv_file.split("/")[1], index=False)
