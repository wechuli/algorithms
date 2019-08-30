class AnimalNode:
    def __init__(self, question, yes_child, no_child):
        self.question = question
        self.yes_child = yes_child
        self.no_child = no_child

    def name(self):
        """
        Return the animal's name with an appropriate "a" or "an" in front.
        This only works for leaf nodes.
        """
        if self.question.lower()[0] in "aeiou":
            return f"an {self.question}"
        return f"a {self.question}"


class App:
    def __init__(self):
        """ Initialize the tree."""
        dog_node = AnimalNode("dog", None, None)
        fish_node = AnimalNode("fish", None, None)
        self.root = AnimalNode("Is it a mammal? ", dog_node, fish_node)

    def play_game(self):
        """ Play the animal game."""
        while True:
            # Play one round.
            self.play_round()

            # See if we should continue.
            response = input("\nPlay again? ").lower()
            if (len(response) == 0) or (response[0] != "y"):
                return

    def play_round(self):
        """ Play lone round of the animal game."""
        node = self.root
        while True:
            # See if this is an internal or leaf node.
            if node.yes_child == None:
                # It's a leaf node.
                self.process_leaf_node(node)
                return

            # It's an internal node.
            # Ask the node's question and move to the appropriate child node.
            response = input(node.question + " ").lower()
            if response[0] == "y":
                node = node.yes_child
            else:
                node = node.no_child

    def process_leaf_node(self, leaf):
        """ Process a leaf node."""
        # Guess the animal.
        prompt = f"Is your animal {leaf.name()}? "
        response = input(prompt).lower()
        if response[0] == "y":
            # We got it right. Gloat and exit.
            print("\n*** Victory is mine! ***")
            return
        else:
            # We got it wrong. Ask the user for the new animal.
            new_animal = input("What is your animal? ").lower()
            new_node = AnimalNode(new_animal, None, None)

            # Ask the user for a new question.
            prompt = \
                f"What question could I ask to differentiate between " + \
                f"{leaf.name()} and {new_node.name()}? "
            new_question = input(prompt)

            # See if the question's answer is true for the new animal.
            prompt = f"Is the answer to this question true for {new_node.name()}? "
            response = input(prompt).lower()

            # Update the knowledge tree.
            old_node = AnimalNode(leaf.question, None, None)
            leaf.question = new_question
            if response[0] == "y":
                leaf.yes_child = new_node
                leaf.no_child = old_node
            else:
                leaf.yes_child = old_node
                leaf.no_child = new_node


if __name__ == '__main__':
    app = App()
    app.play_game()

# app.root.destroy()
