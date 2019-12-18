import re

word1 = 'Litigation, tax and other regulated payments'
word2 = 'Media and Marketing'
word3 = 'Total HR costs'
# print(len(word1))
# print(len(word2))
# print(len(word3))

index = []
shift_1 = 14
shift_2 = 28


def formated_word(word, shift):
    spaces_list = []
    for space in re.finditer(' ', word):
        spaces_list.append(space.start())
    # print(spaces_list)

    comparison = []
    for space in spaces_list:
        gap = abs(shift - space)
        # print(gap)
        comparison.append((gap, space))
    end_line = sorted(comparison)[0][1]
    # print(sorted(comparison))
    # print(end_line)
    return end_line

# formated_word(word1, shift_1)
# formated_word(word1, shift_2)
# print('')
# formated_word(word2, shift_1)
# formated_word(word2, shift_2)
# print('')
# formated_word(word3, shift_1)
# formated_word(word3, shift_2)
# print('')

print(word1[:formated_word(word1, shift_1)] + '\n' + word1[formated_word(word1, shift_1):formated_word(word1, shift_2)].strip() + '\n' + word1[formated_word(word1, shift_2):].strip())
print('')
print(word2[:formated_word(word2, shift_1)] + '\n' + word2[formated_word(word2, shift_1):].strip())
print('')
print(word3)


