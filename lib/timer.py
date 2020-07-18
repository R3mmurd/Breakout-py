"""
This file contains utility classes that perform as timers.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/13/2020
"""
class TimerItemBase:
    def __init__(self):
        self.to_remove = False

    def remove(self):
        self.to_remove = True


class Every(TimerItemBase):
    def __init__(self, time, function, limit=None):
        super(Every, self).__init__()
        self.timer = 0
        self.time = time
        self.function = function
        self.limit = limit

    def update(self, dt):
        self.timer += dt

        if self.timer >= self.time:
            self.timer %= self.time
            self.function()
            if self.limit:
                if self.limit == 1:
                    self.remove()
                else:
                    self.limit -= 1


class After(TimerItemBase):
    def __init__(self, time, function):
        super(After, self).__init__()
        self.timer = 0
        self.time = time
        self.function = function
    
    def update(self, dt):
        self.timer += dt
        if self.timer >= self.time:
            self.function()
            self.remove()


class Tween(TimerItemBase):
    def __init__(self, time, params, on_finish=lambda: None):
        super(Tween, self).__init__()
        self.timer = 0
        self.time = time
        self.objs = {}

        for obj, attrs in params.items():
            self.objs[obj] = {
                var: {
                    'target': val,
                    'velocity': (val - getattr(obj, var))/time
                }
                for var, val in attrs.items()
            }

        self.on_finish = on_finish

    def update(self, dt):
        self.timer += dt

        for obj, attrs in self.objs.items():    
            for var, val in attrs.items():
                setattr(
                    obj, var, getattr(obj, var) + val['velocity']*dt
                )

        if self.timer >= self.time:
            for obj, attrs in self.objs.items():    
                for var, val in attrs.items():
                    setattr(
                        obj, var, getattr(obj, var) + val['target']*dt
                    )

            self.on_finish()
            self.remove()


class Timer:
    items = []

    @classmethod
    def update(cls, dt):
        for item in cls.items:
            item.update(dt)
        
        cls.items = [item for item in cls.items if not item.to_remove]

    @classmethod
    def every(cls, time, function, limit=None):
        cls.items.append(
            Every(time, function, limit=limit)
        )
        return cls.items[-1]
    
    @classmethod
    def after(cls, time, function):
        cls.items.append(
            After(time, function)
        )
        return cls.items[-1]

    @classmethod
    def tween(cls, time, objs, on_finish):
        cls.items.append(Tween(time, objs, on_finish=on_finish))
        return cls.items[-1]
