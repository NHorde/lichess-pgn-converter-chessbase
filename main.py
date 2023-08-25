import sys
import re

def read_pgn_file(file_name):
    file_path = f"{file_name}.pgn"
    with open(file_path, 'r') as pgn_file:
        pgn_content = pgn_file.read()
        pgn_content_no_evals = re.sub(r'\{ \[%eval [^\]]+\] \}', '', pgn_content)
        pgn_content_cleaned = re.sub(r'\d+\.\.\.\s*', '', pgn_content_no_evals)
        print(pgn_content_cleaned)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <name_of_the_game>")
    else:
        game_name = sys.argv[1]
        read_pgn_file(game_name)
