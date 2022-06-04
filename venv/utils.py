import random
import json

def get_user_name() -> str:
    """
    Get a name consisting of only letters from user
    """
    while True:
        name = input('Введите ваше имя\n')
        if name.isalpha():
            break
        print('Имя должно содержать только буквы')
    return name


def get_words(filename: str) -> list[str]:
    """
    Get a shuffled list of words from file
    """
    with open(filename, encoding='utf8') as f:
        words = f.read().split()
    random.shuffle(words)
    return words


def shuffle_letters(word: str):
    """
    Shuffle characters from a string
    """
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)


def wright_statistics(name: str, points: int, filename: str):
    with open(filename, encoding='utf8') as f:
        stats = json.load(f)

    stats['games_count'] += 1
    if name not in stats['highscores'] or stats['highscores'][name] < points:
        stats['highscores'][name] = points

    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(stats))


def get_statistics(filename: str):
    """
    Get statistics information from a file
    """
    with open(filename, encoding='utf8') as f:
        stats = json.load(f)
        games_count = stats['games_count']
        max_points = max(stats["highscores"].values())
    return games_count, max_points
