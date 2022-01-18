def convertToDigit(n, suffix):

	if n == 0:
		return EMPTY

	if n > 19:
		return Y[n // 10] + X[n % 10] + suffix
	else:
		return X[n] + suffix


def convert(n):
    result=[]
    out = []
    result.append(convertToDigit((n // 100000000000) % 100, 'lakhs  '))
    result.append(convertToDigit((n // 1000000000) % 100, 'hundred  '))
    result.append(convertToDigit((n // 10000000) % 100, 'crore '))
    result.append(convertToDigit(((n // 100000) % 100), 'lakh '))
    result.append(convertToDigit(((n // 1000) % 100), 'thousand '))
    result.append(convertToDigit(((n // 100) % 10), 'hundred  '))
    result.append(convertToDigit((n % 100), ' '))
    for i in result:
        if i:
            out.append(i)
    # print(out)
    if len(out)==1:
        return ''.join(result)
    for i in range(len(result)-1,0,-1):
        if result[i]:
            result[i] = " and " + result[i]
            break
    result=''.join(result)
    return result

	

if __name__ == '__main__':
	EMPTY = ''

	X = [EMPTY, 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ',
		'eight ', 'nine ', 'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ',
		'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']

	Y = [EMPTY, EMPTY, 'twenty ', 'thirty ', 'forty ', 'fifty ',
		'sixty ', 'seventy ', 'eighty ', 'ninety ']
n=int(input())
print(convert(n))

	
