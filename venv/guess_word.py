from utils import get_user_name, get_words, shuffle_letters, get_statistics, wright_statistics

WORDS_FILE = 'words.txt'
HISTORY_FILE = 'history.json'


def main():
    points = 0
    words = get_words(WORDS_FILE)
    user_name = get_user_name()

    for word in words:
        scrambled_word = shuffle_letters(word)

        print(f'Угадайте слово: {scrambled_word}')
        user_answer = input().lower().strip()

        if user_answer == word:
            print('Верно! Вы получаете 10 очков.')
            points += 10
        else:
            print(f'Неверно! Верный ответ – {word}')

    wright_statistics(user_name, points, HISTORY_FILE)

    games_count, max_points = get_statistics(HISTORY_FILE)
    print(f'\nВсего игр сыграно: {games_count}')
    print(f'Максимальный рекорд: {max_points}')


if __name__ == '__main__':
    main()
