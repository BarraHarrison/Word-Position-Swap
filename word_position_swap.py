def manipulate_sentence(sentence: str) -> str:
    # Step 1: Split the sentence into words
    words = sentence.split()
    

    # Step 2: Swap the first and last words
    if len(words) > 1:
        words[0], words[-1] = words[-1], words[0]
    

    # Step 3: Manipulate the seocnd character of each word
    for i in range(len(words)):
        if len(words[i]) > 1:
            words[i] = words[i][0] + words[i][1].upper() + words[i][2:]
    
    # Step 4: Reconstruct and return modified sentences
    modified_sentence = " ".join(words)
    return modified_sentence

sentence = "Korean is a difficult langauge to learn"
result = manipulate_sentence(sentence)
print(result)