from manim import *

class FirstScene(Scene):
    def construct(self):
        text = Text("First Scene")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))


# build the scene
scene = FirstScene()
scene.render()

