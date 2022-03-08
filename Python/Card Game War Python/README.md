# 4.2 - Loops

Let's play a game!

The card game War is a two-player game played with a standard poker deck with Aces high (values from least to most: 2-10, Jack, Queen, King, Ace).

For this exercise, you can use the numeric equivalents 2-14.

The cards are dealt equally to each player and each round is played by both players laying down their top card. This means you will need to make sure you are drawing from the beginning of the list and adding to the end of it. (This is known as "First In, First Out," or FIFO.)

Highest card wins the round and takes the cards, adding them to their pile.

In the event of a tie, three cards from each are played face down and a fourth is played face up (for the purpose of this exercise, "face up" vs "face down" doesn't really matter, what does matter is the 3+1 format). The winner takes the full stack. If a tie happens again, then this tie-breaker round happens again, and repeats until the tie is broken. The winner gets all of the cards.

The first player to run out of cards loses.

The standard poker deck has 4 suits, for a total of 52 cards, though for this game, only the face value of the cards matter.

Your task is to simulate the game and fill in the log as a record. As in previous exercises, functions are provided for you to fill in.

**Do not submit this assignment with the functions just filled in with the string or number literals. You will get a zero for this assignment if you do, even if the tests pass.** At this point, there is no reason for you to be copying strings and numbers around.

## Usual Info

Like before, the tests will fail initially. Your task is to make the source code changes required to get them working. The source file will provide more information on how to do that via notes and/or pre-existing code, and the tests themselves will also provide you information for what's expected.

As always, **do not change the tests!** Your assignment submission will be considered invalid until your tests are reverted to their original state.

## Submitting Your Assignment

You are welcome and encouraged to commit and push your code as often as you like. 

If you want to submit an assignment for grading that does not have all its tests passing, then send me a message to let me know that you're submitting the attempt as-is.
