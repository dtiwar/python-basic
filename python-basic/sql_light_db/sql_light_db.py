import sqlite3
import json
from pathlib import Path
movies= json.loads(Path("movie.json").read_text())

with sqlite3.connect('db.sqlite3') as conn:
	command = "insert into movies values (?, ?, ? )"
	for movie in movies:
		conn.execute(command,tuple(movie.values()))
	conn.commit()

print(movies)

