import json

class StatisticsFile:
    encoding = 'utf8'

    def __init__(self, file):
        self.file = file

    def write(self, name, points):
        with open(self.file, encoding=self.encoding) as f:
            stats = json.load(f)

        stats['games_count'] += 1
        if name not in stats['highscores'] or stats['highscores'][name] < points:
            stats['highscores'][name] = points

        with open(self.file, 'w', encoding=self.encoding) as f:
            json.dump(stats, f)
    
    def get(self):
        with open(self.file, encoding=self.encoding) as f:
            stats = json.load(f)
            games_count = stats['games_count']
            max_points = max(stats["highscores"].values())
        return games_count, max_points
    
    @property
    def highscore(self):
        with open(self.file, encoding=self.encoding) as f:
            stats = json.load(f)
        return max(stats["highscores"].values())

    @property
    def games_count(self):
        with open(self.file, encoding=self.encoding) as f:
            stats = json.load(f)
        return stats['games_count']

    def clear(self):
        with open(self.file, 'w', encoding=self.encoding) as f:
            initial_stats = {"highscores": {}, "games_count": 0}
            json.dump(initial_stats, f)

    def __repr__(self):
        return f'StatisticsFile({self.file})'
    