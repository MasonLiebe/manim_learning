from manim import *
import os

class ShuffleCards(Scene):
    def construct(self):
        # Create 10 squares (cards) with initial colors
        card_colors = [RED] * 3 + [GREY] * 7
        cards = VGroup(*[Square(side_length=1.0).set_fill(color, opacity=1) for color in card_colors])

        # Arrange the cards in a straight line
        cards.arrange(RIGHT, buff=0.5)

        # Add cards to the scene
        self.add(cards)

        # Function to shuffle the positions of the cards
        def shuffle_cards(cards):
            positions = [card.get_center() for card in cards]
            np.random.shuffle(positions)
            return positions

        # Animate shuffling the card    s three times
        for _ in range(3):
            shuffled_positions = shuffle_cards(cards)
            self.play(AnimationGroup(*[
                card.animate.move_to(pos) for card, pos in zip(cards, shuffled_positions)
            ]))
            self.wait(0.5)

        self.wait(2)  # Wait to view the final state
# Run the scene
if __name__ == "__main__":
    os.system("manim -pql firstFile.py ShuffleCards")
