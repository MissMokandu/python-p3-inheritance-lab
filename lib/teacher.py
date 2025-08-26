#!/usr/bin/env python
from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # give Teacher some knowledge (must not be empty)
        self.knowledge = ["Math", "Science", "History"]

    def teach(self):
        # return a random item from knowledge
        return random.choice(self.knowledge)
