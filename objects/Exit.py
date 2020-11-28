import pygame as pg

from functions import rect_collide
from models.LevelObject import LevelObject
from constants import Exit as Properties, Cell


class Exit(LevelObject):
    def __init__(self, scene, spawn_cell, *groups, width=Properties.WIDTH, height=Properties.HEIGHT):
        self.spawn = (spawn_cell[0] * Cell.WIDTH + (Cell.WIDTH - width) // 2,
                      spawn_cell[1] * Cell.HEIGHT + (Cell.HEIGHT - height))
        super().__init__(scene, *self.spawn, width, height, *groups)
        self.image = pg.image.load(Properties.IMAGE_PATH)
        self.rect = self.get_rect()

    def process_logic(self, events):
        if rect_collide(self.scene.groups['main_character'].sprite.get_rect(), self.get_rect()):
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_e:
                    self.scene.finish_level()
            
    def update(self, *args, **kwargs):
        if rect_collide(self.scene.groups['main_character'].sprite.get_rect(), self.get_rect()):
            self.scene.groups['to_exit_text'].sprite.show()
        else:
            self.scene.groups['to_exit_text'].sprite.hide()
        super().update(*args, **kwargs)