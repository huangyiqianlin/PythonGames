import pygame
import GameFunctions


class Loop:
    """ 主要循环，处理事件监听，更改游戏状态，刷新屏幕显示的功能 """

    def __init__(self):
        self.event_callbacks = []

    def register_events(self, event, call_back):
        """ 注册事件，让指定的事件映射到指定的回调方法 """
        event_callback = (event, call_back)
        self.event_callbacks.append(event_callback)

    def update_game_stats(self):
        pass

    def update_screen(self):
        pass

    def run(self):
        """ 运行事件监听，并且处理相应的事件 """
        for event in pygame.event.get():
            for event_name, callback in self.event_callbacks:
                if event.type == event_name:
                    callback()
