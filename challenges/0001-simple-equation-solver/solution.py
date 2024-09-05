from sys import stdin, stdout


for line in stdin:
    tokens = line.split()

    current_side = 'left'
    current_sign = '+'
    terms_sum = 0

    var = None
    var_sign = None
    var_side = None

    for token in line.split():
        if len(token) == 1 and token.isalpha():
            # Variable
            var = token
            var_side = current_side
            var_sign = current_sign
        elif len(token) == 2 and token[1].isalpha():
            # Signed variable
            var = token[1]
            var_side = current_side
            var_sign = '+' if token[0] == current_sign else '-'
        elif len(token) == 1 and (token == '+' or token == '-'):
            # Addition or substraction operator
            current_sign = token
        elif token == '=':
            # Eq symbol
            current_side = 'right'
            current_sign = '+'
        else:
            # Number
            if current_side == 'left':
                terms_sum += int(token) * (1 if current_sign == '+' else -1)
            else:
                terms_sum += int(token) * (-1 if current_sign == '+' else 1)

    if var_side == 'left':
        answer = -terms_sum if var_sign == '+' else terms_sum
    else:
        answer = -terms_sum if var_sign == '-' else terms_sum

    stdout.write(f'{var} = {answer}\n')
