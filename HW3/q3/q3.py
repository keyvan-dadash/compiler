
import sys


class Q3DFA:

    def __init__(self, alphabet : list, start : str, end : list, transitions : dict):
        self._alphabet = alphabet
        self._start = start
        self._end = end
        self._transitions = transitions

    
    def isValid(self, text : str):
        start = self._start

        for char in text:
            if char not in self._alphabet:
                raise Exception("given text has some alphabet that cannot accept")
            list_transitions = self._transitions.get(start, None)

            if not list_transitions and char not in list_transitions:
                raise Exception("there is no transition to get to")
            
            start = list_transitions[char]
        
        if start not in self._end:
            return False
        
        return True



if __name__=='__main__':
    text = sys.argv[1]

    q3 = Q3DFA(['0', '1'], 0, [0, 1, 2, 3], {
        0: {'1' : 1, '0' : 0},
        1: {'1' : 2, '0' : 0},
        2: {'1' : 2, '0' : 3},
        3: {'1' : 4, '0' : 0},
        4: {'1' : 4, '0' : 4},
    })

    try:
        if q3.isValid(text):
            print("given text is valid")
        else:
            print("given text is not valid")
    except Exception as e:
        print(str(e))
            

            
