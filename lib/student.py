#!/usr/bin/env python

from user import User   # assuming your User class is in user.py

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []   # start with empty list

    def learn(self, info):
        self.knowledge.append(info)
