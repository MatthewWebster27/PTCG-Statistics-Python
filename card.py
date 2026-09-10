class Card:

    # typeOfCard parameter: "Pokemon", "Trainer" or "Energy"

    """
    The tags attribute is a list of strings, which indicate features of the card. 
    Some examples are: "ACE SPEC", "Basic", "Draw Supporter" etc
    """

    def __init__(self,typeOfCard):
        self.tags = [typeOfCard]
