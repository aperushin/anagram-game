from utils import get_user_name, get_words, shuffle_letters, get_statistics, wright_statistics
from stats import StatisticsFile

WORDS_FILE = 'words.txt'
stats = StatisticsFile('history.json')


def main():
    points = 0
    words = get_words(WORDS_FILE)
    user_name = get_user_name()

    for word in words:
        scrambled_word = shuffle_letters(word)

        print(f'Guess word: {scrambled_word}')
        user_answer = input().lower().strip()

        if user_answer == word:
            print('Correct! You get 10 points')
            points += 10
        else:
            print(f'Nope. Correct answer — {word}')

    stats.write(user_name, points)

    games_count, max_points = stats.get()
    print(f'\nTotal games played: {games_count}')
    print(f'Record: {max_points}')


if __name__ == '__main__':
    main()
