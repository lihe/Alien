class Settings:
    # 存储《入侵外星人》的所有设置的类

    def __init__(self):
        # 初始化游戏的设置

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 1

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # 外星人点数的提高速度
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        # 初始化随游戏而变化的设置
        self.ship_speed_factor = 1.5
        self.bullets_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

    def increase_speed(self):
        # 提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullets_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


