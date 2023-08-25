import re

def read_pgn_file(file_path):
    with open(file_path, 'r') as pgn_file:
        pgn_content = pgn_file.read()
        pgn_content_no_evals = re.sub(r'\{ \[%eval [^\]]+\] \}', '', pgn_content)
        pgn_content_cleaned = re.sub(r'\d+\.\.\.\s*', '', pgn_content_no_evals)
        print(pgn_content_cleaned)

if __name__ == "__main__":
    pgn_file_path = "game.pgn"  # Replace with the path to your .pgn file
    read_pgn_file(pgn_file_path)