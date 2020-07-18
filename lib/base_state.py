"""
This file contains a base class to define states for a State Machine.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""

class BaseState:
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def enter(self, *args, **kwargs):
        """
        Method to be executed when the state machine enters in the state.
        """
        pass

    def exit(self):
        """
        Method to be executed when the state machine exits from the state.
        """
        pass

    def update(self, dt):
        pass

    def render(self, surface):
        pass
