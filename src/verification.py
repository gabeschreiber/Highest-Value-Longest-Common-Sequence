def verify(sequence, alphabet):
    sum = 0
    vString = "Val(" + sequence + "): "
    for i in range(len(sequence)):
        if 0 < i <= len(sequence) - 1:
            vString += " + "
        sum += alphabet[sequence[i]]
        vString += str(alphabet[sequence[i]])

    vString += " = " + str(sum)

    return vString
