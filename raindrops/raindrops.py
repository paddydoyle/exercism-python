def raindrops(number):
    # Dict of test divisors to output strings
    divisors = {
            3: 'Pling',
            5: 'Plang',
            7: 'Plong',
            }

    # List of strings corresponding to the divisors.
    divisor_strings = [divisors[i] for i in divisors if number % i == 0]

    # If nothing divided, then return the input as a string.
    if not divisor_strings:
        return str(number)

    # Otherwise join the list of matched strings.
    return ''.join(divisor_strings)


# Original version:
# - slow string concatenation
# - not flexible with future changes to divisor/output pairs
def raindrops_orig(number):
    # This seems deceptively simple..

    output = []

    if number % 3 == 0:
        output.append('Pling')

    if number % 5 == 0:
        output.append('Plang')

    if number % 7 == 0:
        output.append('Plong')

    if not output:
        return str(number)

    return ''.join(output)
