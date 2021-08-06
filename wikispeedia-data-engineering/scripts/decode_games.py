import csv
import pandas as pd
import numpy as np

# def get_path_id(path_name, path_index, game_id):
#     for i in range(len(path_index)):
#         if game_id == path_index[i][1] and path_name == path_index[i][2]:
#             return path_index[i][0]

def get_article_id(article, article_list):
    for i in range(len(article_list)):
        if article == article_list[i][1]:
            return article_list[i][0]

# def create_path_step(path, game_id, path_list, path_index, path_start, path_end, continues_path, article_list):
#     index = path_index
#     for i in range(len(path)):
#         if path[i] == "<":
#             article = path[i - 2]
#             path_list.append((index, game_id, "<", i, get_article_id(article, article_list)))
#         else:
#             article = path[i]
#             path_list.append((index, game_id, article, i, get_article_id(article, article_list)))

#         # if i == 0:
#         #     path_start.append((game_id, index))
#         if i > 0:
#             continues_path.append((game_id, index - 1, index))
#         index += 1
#     # if finished:
#     #     path_end.append((game_id, index - 1))
#     return index

def path_steps(path , current_path, article_list, path_id, game_id):
    pid = path_id
    iteration = 0
    for step in current_path:
        path.append((pid, get_article_id(step, article_list), game_id, step, iteration))
        pid += 1
        iteration += 1
    return pid
    

def get_games():
    finished_games = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/decoded_csv/fixed_paths_finished_decoded.csv", delimiter=",").to_numpy()
    unfinished_games = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/decoded_csv/fixed_paths_unfinished_decoded.csv", delimiter=",").to_numpy()
    article_list = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/articles_iterated.csv", delimiter=",").to_numpy()
    game_id = 0
    games = []
    path = []
    path_id = 0
    for i in range(finished_games.shape[0]):
        game = finished_games[i]
        final_path = game[3].split(";")
        path_id = path_steps(path, final_path, article_list, path_id, game_id)
        games.append((game_id, game[0], game[1], True, game[2], game[4], None, final_path[0], final_path[-1], final_path[-1], len(final_path)))
        game_id += 1
        print("finished-running {}".format(game_id))
    for i in range(unfinished_games.shape[0]):
        game = unfinished_games[i]
        final_path = game[3].split(";")
        path_id = path_steps(path, final_path, article_list, path_id, game_id)
        games.append((game_id, game[0], game[1], False, game[2], None, game[5], final_path[0], final_path[-1], game[4], len(final_path)))
        game_id += 1
        print("unfinished_running: {}".format(game_id))
    pd.DataFrame(np.array(games)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/games.csv", header = ["Game ID", "HashedIP", "Timestamp", "Finished", "Duration", "Rating", "Unfinished Type", "Start Path", "End Path", "Target", "Steps"], index= None)
    pd.DataFrame(np.array(path)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/path_step.csv", header = ["Path ID", "Article ID", "Game ID", "Name", "Iteration"], index= None)


# def iterate_games():
#     finished_games = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/decoded_csv/paths_finished_decoded.csv", delimiter=",").to_numpy()
#     unfinished_games = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/decoded_csv/paths_unfinished_decoded.csv", delimiter=",").to_numpy()
#     article_list = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/articles_iterated.csv", delimiter=",").to_numpy()
#     games = []
#     game_index = 0
#     path_list = []
#     path_start = []
#     path_end = []
#     continues_path = []
#     path_index = 0
#     for i in range(finished_games.shape[0]):
#         path = finished_games[i][3].split(";")
#         path_index = create_path_step(path, game_index, path_list, path_index, path_start, path_end, continues_path, article_list)
#         games.append((game_index, True, finished_games[i][0], finished_games[i][1], finished_games[i][2], finished_games[i][4], path[-1],None))
#         game_index += 1
#         print("finished-running {}".format(game_index))
#     for i in range(unfinished_games.shape[0]):
#         path = unfinished_games[i][3].split(";")
#         path_index = create_path_step(path, game_index, path_list, path_index, path_start, path_end, continues_path, article_list)
#         games.append((game_index, False, unfinished_games[i][0], unfinished_games[i][1], unfinished_games[i][2], None, unfinished_games[i][4], unfinished_games[i][5]))
#         game_index += 1
#         print("unfinished_running: {}".format(game_index))
#     pd.DataFrame(np.array(games)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/games.csv", header = ["Game ID", "Finished", "Hashed IP", "Timestamp", "Duration", "Rating", "Target Name", "Unfinished Type"], index= None)
#     pd.DataFrame(np.array(path_list)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/path_step.csv", header = ["Path ID", "Game ID", "Path Name", "Iteration", "Article ID"], index= None)
#     #pd.DataFrame(np.array(path_start)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/path_start.csv", header = ["Game ID", "Path ID"], index= None)
#     #pd.DataFrame(np.array(path_end)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/path_end.csv", header = ["Game ID", "Path ID"], index= None)
#     pd.DataFrame(np.array(continues_path)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/continues_path.csv", header = ["Game ID", "Source Path ID", "Target Path ID"], index= None)

get_games()