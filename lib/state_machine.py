"""
This file contains the implementation of the class StateMachine.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020

Usage:
    States are instantiated when they are set to the attribute 'current'.
    They are passed to the constructor as a dictionary argument containing
    pairs either  (state_name, StateClass) or (state_name, function_to_build_state).

    It is expected that added states contain the methods: enter, exit,
    update, and render. It is recommended creating states by inheriting
    from BaseState in base_state module.

    Example:

    state_machine = StateMachine({
        'state_1': StartState,
        'state_2': lambda: return PlayState()
    })
    state_machine.change('state_1')
"""
from .base_state import BaseState


class StateMachine:
    def __init__(self, states={}):
        self.states = states
        self.current = BaseState(self)

    def change(self, state_name, *args, **kwargs):
        self.current.exit()
        self.current = self.states[state_name](self)
        self.current.enter(*args, **kwargs)
    
    def update(self, dt):
        self.current.update(dt)

    def render(self, surface):
        self.current.render(surface)

