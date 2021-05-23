# Cellular Automation Simulation
# Simran Hundal
import matplotlib.pyplot as plt


# function to make a dictionary for a given rule
def makerule(num):
    # convert number to 8bit binary
    num = '{0:08b}'.format(num)
    # index binary number to make dictionary
    return {'111': num[0], '110': num[1], '101': num[2], '100': num[3],
            '011': num[4], '010': num[5], '001': num[6], '000': num[7], }


# making a new line of the simulation
def makenextline(rule, line):
    # add padding to line up in display
    line = '0' + line + '0'
    # look at the string in groups of 3 then look up in dictionary
    # and apply relevant rule to the new line
    return ''.join([rule[line[i:i + 3]] for i in range(len(line) - 2)])


# make initial line for a given number of iterations
def makeinit(size):
    string = '0'
    for i in range(size-2):
        string += '0'
    return string + '1' + string


# perfrom simulation given rule and how many iterations
def simulate(rule, iterations):
    # make inital line
    init = makeinit(iterations)
    # make label for figure being displayed
    label = "Rule " + str(rule) + " with " + str(iterations) + " iterations"
    # make relevant rule
    rule = makerule(rule)
    result = [list(map(int, init))]
    # apply new line
    for i in range(iterations - 1):
        init = makenextline(rule, init)
        result.append(list(map(int, init)))
    # display figure
    plt.figure(figsize=(15, 9)).suptitle(label)
    plt.imshow(result, cmap='binary')
    plt.show()
    return result



simulate(75, 50)

# simulate(4, 50)
# simulate(110, 50)
# simulate(50, 50)
# simulate(54, 50)
# simulate(126, 50)
# simulate(182, 50)
# simulate(220, 50)
# simulate(222, 50)
# simulate(60, 50)
# simulate(102, 50)



