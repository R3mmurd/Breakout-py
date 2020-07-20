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


class BaseState:
    """
    This class represents an empty state. Any state machines
    will start in this state.

    It also is the base for any state. You should extend
    this class to implement any new state class.
    """
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

