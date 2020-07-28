import sys
import pygame
from random import randint
from time import sleep

from p1_alien_invasion.project_1_exercises.pg_372_tiy_14_2.settings import Settings
from p1_alien_invasion.project_1_exercises.pg_372_tiy_14_2.ship import Ship
from p1_alien_invasion.project_1_exercises.pg_372_tiy_14_2.bullet import Bullet
from p1_alien_invasion.project_1_exercises.pg_372_tiy_14_2.rectancle import Target
from p1_alien_invasion.project_1_exercises.pg_372_tiy_14_2.game_stats import GameStats
from p1_alien_invasion.project_1_exercises.pg_372_tiy_14_2.button import Button


class ShootTheBlock:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways Shooter")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.targets = pygame.sprite.GroupSingle()

        self._create_target()

        # Make the Play button.
        self.play_button = Button(self, "Click or press 'p' to start!")

    def _create_target(self):
        target = Target(self)
        self.targets.add(target)

    def _check_target_edges(self):
        """Respond appropriately if any targets have reached an edge."""
        for target in self.targets.sprites():
            if target.check_edges():
                self._change_target_direction()

    def _change_target_direction(self):
        """Drop the entire target and change the target's direction."""
        for target in self.targets.sprites():
            target.rect.x -= self.settings.target_drop_speed
        self.settings.target_direction *= -1

    def _update_targets(self):
        """
        Check if the target is at an edge,
          then update the positions of all targets in the target.
        """
        self._check_target_edges()
        self.targets.update()

        # Check for targets hit ship
        if pygame.sprite.spritecollideany(self.ship, self.targets):
            self._ship_hit()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        self.check_if_bullets_hit_targets()

    def check_if_bullets_hit_targets(self):
        """Respond when bullets collide with targets"""

        # Check for bullets that has hit targets - delete bullet and target
        if pygame.sprite.groupcollide(self.bullets, self.targets, True, True):
            self.stats.game_active = False

        if not self.targets:
            self.bullets.empty()
            self._create_target()

        # Look if all bullets missed target and if third bullet hits right of screent
        self.bullets_finished()

    def bullets_finished(self):
        """Respond to the ship being hit by an target or an target hitting the bottom"""
        screen_rect = self.screen.get_rect()
        for bullet in self.bullets:
            if bullet.rect.left >= screen_rect.right:
                bullet.kill()
                self.settings.bullets_limit -= 1
                if self.settings.bullets_limit <= 0:
                    self.stats.game_active = False
                    break

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_targets()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.stats.game_active = True
        elif event.key == pygame.K_q or pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.targets.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    stb = ShootTheBlock()
    stb.run_game()
