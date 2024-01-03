input = "banana"

def problem(input):
    count = 0 
    def palindromeCount(input):

        if input == input[::-1]:
            count += 1


    for i in range(len(input)):
        for j in range(i,len(input)):
            palindromeCount(input[i:j])


    return count


print(problem(input))
    