from container import *


def banana_verify(source, goal, container, moves):
    '''

    '''
    original_word = source
    new_word = ''
    i = 0
    illegal_move = False

    try:

        while (i < len(moves) and illegal_move is False):
            # put
            if (moves[i] == 'P'):
                # makes sure the source isn't empty
                if source != '':
                    # getting the letter from the source
                    letter = source[0]
                    # updating the source word
                    source = source[1:]
                    # placing the letter into the container
                    container.put(letter)
                else:
                    illegal_move = True
            elif (moves[i] == 'M'):
                if source != '':
                    # getting the letter from the source
                    letter = source[0]
                    # updating the source word
                    source = source[1:]
                    # placing the letter into the goal word
                    new_word += letter
                else:
                    illegal_move = True
            elif (moves[i] == 'G'):
                if not container.is_empty():
                    letter = container.get()
                    new_word += letter
                else:
                    illegal_move = True
            i += 1

        if (new_word == goal):
            output = True
        elif (new_word != goal):
            output = False

    except:
        output = False

    return output
