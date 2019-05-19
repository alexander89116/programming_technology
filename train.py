import sys
import string
import json
import collections

from main import caesar, caesar_calc

len_ascii_lowercase = len(string.ascii_lowercase)

def train(args):
    text = args.text_file.read()
    json.dump(get_model(text), args.model_file)


def get_model(text: str):
    count = collections.Counter(symbol for symbol in text.lower() if symbol.isalpha() and symbol.isascii())
    letters_count = sum(count.values())
    result = {'coincidence_index': 0}

    for letter in string.ascii_lowercase:
        result[letter] = count[letter] / letters_count
        if letters_count > 1:
            result['coincidence_index'] += (count[letter] * (count[letter] - 1)) / \
                                           (letters_count * (letters_count - 1))
    return result


def hack(args):
    try:
        model = json.load(args.model_file)
    except json.JSONDecodeError:
        raise Exception('Bad model file')

    text = args.input_file.read()
    result = caesar_hack(model, text)
    args.output_file.write(result)


def caesar_hack(model, text: str):
    result = [0 for i in range(len_ascii_lowercase)]
    shift_result = 0
    current_model = get_model(text)
    for shift in range(len_ascii_lowercase):

        for letter in string.ascii_lowercase:
            new_letter = caesar_calc(letter, shift)
            result[shift] += (model[letter] - current_model[new_letter]) ** 2

        if result[shift] < result[shift_result]:
            shift_result = shift

    return caesar(shift_result, text)
