class Stats:
    """Статистика"""

    def __init__(self):
        """Иниц стат."""
        self.guns_left = None
        self.reset_stats()

    def reset_stats(self):
        """изм статы"""
        self.guns_left = 2
