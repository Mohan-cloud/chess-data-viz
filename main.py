import pandas as pd
import chess.pgn
black_king_pos = []
white_king_pos = []
count = 1
with open('lichess_db.pgn') as file:  # database obtained from lichess
    while True:
        pgn = chess.pgn.read_game(file)
        if pgn is None:
            break
        if pgn.headers["Termination"] == "Abandoned":
            continue
        print(f'Processing game {count}...')
        if(pgn.headers["Result"] == "1-0"):  # white wins
            end_pos = pgn.end()
            end_pos_list = end_pos.board().pieces(chess.KING, chess.BLACK).tolist()
            if len(black_king_pos) == 0:
                black_king_pos = end_pos_list
            else:
                black_king_pos = [x+y for x,
                                  y in zip(black_king_pos, end_pos_list)]

        elif(pgn.headers["Result"] == "0-1"):  # black wins
            end_pos = pgn.end()
            end_pos_list = end_pos.board().pieces(chess.KING, chess.WHITE).tolist()
            if len(white_king_pos) == 0:
                white_king_pos = end_pos_list
            else:
                white_king_pos = [x+y for x,
                                  y in zip(white_king_pos, end_pos_list)]

        count += 1

df = pd.DataFrame()
df["Black King"] = black_king_pos
df["White King"] = white_king_pos
df.to_csv("chess.csv", index=False)
