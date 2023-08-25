import sys
import re
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger()

def read_pgn_file(file_name):
    input_file_path = os.path.join("games", f"{file_name}.pgn")
    output_file_path = os.path.join("games", f"{file_name}_cleaned.pgn")

    if not os.path.exists(input_file_path):
        logging.error(f"File '{input_file_path}' does not exist.")
        return

    with open(input_file_path, 'r') as pgn_file:
        pgn_content = pgn_file.read()
        pgn_content_no_evals = re.sub(r'\{ \[%eval [^\]]+\] \}', '', pgn_content)
        pgn_content_cleaned = re.sub(r'\d+\.\.\.\s*', '', pgn_content_no_evals)

    with open(output_file_path, 'w') as cleaned_file:
        cleaned_file.write(pgn_content_cleaned)
        logging.info(f"Cleaned PGN content saved to '{output_file_path}'")

    logging.info(f"Successfully read '{input_file_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.info("Usage: python main.py <name_of_the_game>")
    else:
        game_name = sys.argv[1]
        read_pgn_file(game_name)
