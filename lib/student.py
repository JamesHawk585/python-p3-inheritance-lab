#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    def learn(self, new_knowledge):
        #  Treied cr4eating new instance variable. 
        # Append a new knowledge string to the end of an existing empty knowledge list. 
        self.knowledge.append(new_knowledge)

james_hawk = Student("James", "Hawk")

james_hawk.__dict__ 

