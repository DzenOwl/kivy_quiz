from .const import *
from time import time
from random import randint


class User:
    def __init__(self, username, questions=QS):
        self.username = username
        self.start_time = None
        self.qs = questions
        self.total = len(questions)
        self.current = 0
        self.right = 0
        self.answered = 0
        self.end_time = 0
        self.best_res = (0, 0)
        self.best_time = 0 
    
    def start_test(self):
        self.start_time = time()
        self.current = randint(0, self.total-1)
        self.right = 0
        self.answered = 0
        self.end_time = 0
    
    # TODO: add statistics for each question set
    def check_best(self):
        if self.right > self.best_res[0]:
            self.best_res = (self.right, self.total)
            self.best_time = round(self.end_time - self.start_time, 2)
    
    def next_question(self):
        self.answered += 1
        if self.answered == self.total:
            self.current = -1
            self.end_time = time()
            return
        if self.current < self.total - 1:
            self.current += 1
        else:
            self.current = 0

        