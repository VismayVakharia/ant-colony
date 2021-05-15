from .physical_object import PhysicalObject


class FoodParticle(PhysicalObject):
    def __init__(self, x: float, y: float):
        super().__init__(x=x, y=y)
