from collections import deque

def parse(tokens: tuple):
    queue = deque()

    for token in tokens:
        if token[0] == 'TAG_ABERTURA':
            queue.append(token[1])
        if token[0] == 'TAG_FECHA':
            if queue:
                top = queue[-1]
                if top != token[1]:
                    return False
                else:
                    queue.pop()
            else:
                return False
    
    if queue:
        return False

    return True