from classes_base import Game, Player, Enemy, Hydra, DragonHydra

def main():
    player = Player('Zenek Błazenek', 20)
    enemies = [
        Enemy('Orc', 15),
        Enemy('Dwarf', 10),
        DragonHydra('Green hydra', 20, 2)
    ]
    game = Game(player, enemies)
    game.play(10)

if __name__ == "__main__":
    main()