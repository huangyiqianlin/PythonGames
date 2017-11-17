class Settings:
    def __init__(self):
        self.colors = self.Colors()
        self.shapes = self.Shapes()
        self.fps = 120
        self.window_width = 640
        self.window_height = 480

        self.reveal_speed = 8  # 揭开方块的动画速度

        self.box_size = 40
        self.gap_size = 10

        self.board_width = 10  # 横向有多少个方块
        self.board_height = 7  # 纵向有多少个方块

        assert (self.board_width * self.board_height) % 2 == 0, \
            'Board needs to have an even number of boxes for pairs of matches.'

        self.x_margin = int((self.window_width - (self.board_width * (self.box_size + self.gap_size))) / 2)
        self.y_margin = int((self.window_height - (self.board_height * (self.box_size + self.gap_size))) / 2)

        self.bg_color = self.colors.navy_blue
        self.light_bg_color = self.colors.gray
        self.box_color = self.colors.blue
        self.high_light_color = self.colors.blue

        self.all_colors = (
            self.colors.red,
            self.colors.blue,
            self.colors.yellow,
            self.colors.orange,
            self.colors.cyan,
            self.colors.purple)

        self.all_shapes = (
            self.shapes.diamond,
            self.shapes.donut,
            self.shapes.lines,
            self.shapes.oval,
            self.shapes.square
        )

    class Colors:
        def __init__(self):
            #             R    G    B
            self.gray = (100, 100, 100)
            self.navy_blue = (60, 60, 100)
            self.white = (255, 255, 255)
            self.red = (255, 0, 0)
            self.green = (0, 255, 0)
            self.blue = (0, 0, 255)
            self.yellow = (255, 255, 0)
            self.orange = (255, 128, 0)
            self.purple = (255, 0, 255)
            self.cyan = (0, 255, 255)

    class Shapes:
        def __init__(self):
            self.donut = 'donut'
            self.square = 'square'
            self.diamond = 'diamond'
            self.lines = 'lines'
            self.oval = 'oval'
