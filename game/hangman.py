""" Main class for Hangman game """


def wait_for_user():
    letter = input()
    while len(letter) != 1:
        print('I need only one letter')
        letter = input()
    return letter


class Hangman:
    word_dictionary = [
        'zephyr',
        'gyrocopter',
        'bottle',
    ]

    def __init__(self, word=None):
        self.mistakes = 0
        self.word = word or self.choose_word()
        self.state = str.maketrans(self.word, '*' * len(self.word))
        self.mask = self.word.translate(self.state)
        self.incorrect = []

    def choose_word(self):
        from random import choice
        return choice(self.word_dictionary)

    def is_finished(self):
        return (self.mask == self.word) or (self.mistakes == 5)

    def check_guess(self, letter):
        if letter in self.word:
            self.state[ord(letter)] = ord(letter)
            self.mask = self.word.translate(self.state)
            return True
        self.incorrect.append(letter)
        return False

    def finish_game(self):
        if self.mistakes == 5:
            print('You lost!')
            return -1
        print('You won!')
        return 1

    def start(self):
        """Game cycle"""
        while not self.is_finished():
            print('Guess a letter')
            letter = wait_for_user()
            if letter in self.incorrect:
                print('You have already tried {}'.format(letter.upper()))
                continue
            guessed = self.check_guess(letter)
            if guessed:
                print('Hit\n')
            else:
                self.mistakes += 1
                print('Missed, mistakes {} out of 5'.format(self.mistakes))
            if self.incorrect:
                print('Incorrect: ', ','.join(self.incorrect))
            print('The word: ', self.mask, '\n')
        return self.finish_game()

    def test(self):
        print('### Test incorrect guessing')
        self.__init__('ark')
        for turn in 'fhtwe':
            guessed = self.check_guess(turn)
            assert not guessed, 'Check status is wrong'
            self.mistakes += 1
        assert self.mistakes == 5
        assert self.is_finished(), 'Game is in loop'
        assert self.finish_game() == -1, 'Incorrect finish criteria'
        print('### OK! ###\n')

        print('### Test correct guessing')
        self.__init__('ark')
        for turn in 'kar':
            guessed = self.check_guess(turn)
            assert guessed, 'Check status is wrong'
        assert self.is_finished(), 'Game is in loop'
        assert self.finish_game() == 1, 'Incorrect finish criteria'
        print('### OK! ###\n')
