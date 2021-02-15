from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import webbrowser

html = urlopen(
    "https://www.nytimes.com/puzzles/sudoku/hard")

soup = BeautifulSoup(html, 'html.parser')

board = soup.find(class_="pz-game-screen")
s = board.find("script")
i = s.string.find("{")
subD = s.string[i:]
obj = json.loads(subD)
puzzle = obj['hard']['puzzle_data']['puzzle']

nums = ','.join(str(n) for n in puzzle)

webbrowser.open("https://sudokuexchange.com/play/?s=" + nums)
