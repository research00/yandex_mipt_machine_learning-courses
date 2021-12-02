import re
from scipy.spatial.distance import cosine


def unique_elements(a):
    ret = []
    for item in a:
        if item not in ret and item != '':
            ret.append(item)
    return ret


if __name__ == '__main__':
    # you need to place a file named "sentences.txt" in the same folder with the .py file you will run
    # the file should contain sentences separated by "\n"
    with open("sentences.txt", "r") as file:
        lines = file.read()
    lines = lines.lower()
    print(f'{lines}\n\n')
    sentences = lines.split('\n')
    words = unique_elements(re.split('[^a-z]', lines))
    print(f'{words}\n\n')
    words_dict = dict(enumerate(words))
    d = len(words)
    n = len(sentences) - 1
    matrix = []

    for i in range(len(sentences)):
        sentences[i] = sentences[i].replace(",", '').replace(".", '').split()
    for i in range(n):
        temp = [0] * d
        for j in range(d):
            counter = 0
            if words[j] in sentences[i]:
                for k in range(len(sentences[i])):
                    if words[j] == sentences[i][k]:
                        counter += 1
            temp[j] = counter
        matrix.append(temp)
        print(matrix[i])

    cos_distance = []
    vector_sum = []
    print("\n")
    for i in range(n):
        cos_distance.append(cosine(matrix[0], matrix[i]))
        print(f"{i}: {cos_distance[i]}")
