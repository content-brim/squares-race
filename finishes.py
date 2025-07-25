from interactables import Interactable
from surfaces import ImageSurfaceMixin, ImageMode


class Finish(Interactable, ImageSurfaceMixin):
    def __init__(self, position, size):
        image_path = "assets/finish.png"
        super().__init__(
            position,
            image_kwargs={
                "size": size,
                "image_path": image_path,
                "mode": ImageMode.REPEAT,
            },
        )

    def interact(self, other):
        other.kill()
