import json
from pathlib import Path

movie=Path('movie.json').read_text()
print(type(movie))

print("move_without_load",movie)
movie_json=json.loads(movie)
print(type(movie_json))
print("move_with_load_json",movie_json)

for i in movie_json:
	print(i.get('id'))

for i in movie:
	print(i.get('id'))