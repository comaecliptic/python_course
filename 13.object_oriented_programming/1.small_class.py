class Dinosaur:
    """A class to make 2D dinosaurs. Dinosaur has a name and can run
    and roar.
    """

    def __init__(self, name, length, height, catchphrase=None):
        self.name = name
        self.length = length
        self.height = height
        self.x_coord = 0
        self.catchphrase = catchphrase

    def run(self, direction, steps):
        """Run in a chosen direction.

        Parameters
        ----------
        direction : str from {'left', 'right'}
            The direction of running, left of right.
        steps : int
            How long to move in chosen direction.
        """
        if direction == 'left':
            self.x_coord -= steps
        elif direction == 'right':
            self.x_coord += steps
        else:
            print('Wrong direction!')

    def roar(self):
        if self.catchphrase:
            print(self.catchphrase)
        else:
            print('RRAAAAAWWWRRRRRRRR!')


if __name__ == '__main__':
    dino = Dinosaur(
        name='Littlefoot',
        length=3,
        height=2,
        catchphrase="Hello! I'm Littlefoot!"
    )
    print(f'Position before running: {dino.x_coord}')
    dino.run('right', 10)
    print(f'Position after running: {dino.x_coord}')
    dino.roar()
