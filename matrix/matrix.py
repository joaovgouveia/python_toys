#@author JotaV-0 | 2023

from curses import wrapper
import curses
import time
from random import randint

def handle_lines(lines, screen):
    for i in range(len(lines) -1, -1, -1):
        line = lines[i]
        if not line['finished']: draw_line(line, screen)
        else: 
            erease_line(line, screen)
            lines.pop(i)
            
def erease_line(line, screen):
    for lin in range(0, line['finish_lin'] +1):
        screen.addstr(lin, line['col'], ' ')

def draw_line(line, screen):
    char_list = ['0', '1']

    char = char_list[randint(0, 1)]
    screen.addstr(line['current_lin'], line['col'], char)

    if line['current_lin'] != line['finish_lin']: 
        line['current_lin'] += 1
    else: line['finished'] = True

    screen.refresh()

def create_line(max_lins, max_cols, lines_list):
    while True:
        selected_col = randint(0, max_cols -1)
        found = False
        for e in lines_list:
            if selected_col == e['col']: found = True

        if not found: break

    if max_lins <= 8: min_lin = 0
    else: min_lin = 8

    line = {
        "finish_lin": randint(min_lin, max_lins -1),
        "col": selected_col,
        "current_lin": 0,
        "finished": False }

    lines_list.append(line)

def main(screen):
    curses.curs_set(0)
    lins, cols = screen.getmaxyx()

    lines = []
    while True:
        for _ in range(2):
            create_line(lins, cols, lines)
        handle_lines(lines, screen)
        time.sleep(0.075)

wrapper(main)
