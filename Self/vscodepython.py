'''
Write a function that:
Takes a list of sentences
Returns a list of sentences that contain the word "python" (case-insensitive)
'''

def sentence_with_python(sentences):
    result = []
    for sentence in sentences:
        if "python" in sentence.lower():
            result.append(sentence)
    return result

sentences = ["Python is fun", "I like Java", "python is easy"]
print(sentence_with_python(sentences))

