import json
from pathlib import Path
movies =[
	{"id":1,"title":"Terminator","year":1989},
	{"id":2, "title":"Kinder gardern cop","year":1983}
]

data = json.dumps(movies)
Path("movie.json").write_text(data)
print(data)