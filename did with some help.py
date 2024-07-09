def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words[:])
    for each_word in words:
        if root_word in each_word:
            same_words.append(each_word)
        if each_word in root_word:
            same_words.append(each_word)
    return same_words


        
result1 = single_root_words('rich','richest','orichalum', 'cheers','richies'.capitalize())
result2 = single_root_words('disablement', 'able', 'mable', 'disable', 'bagel'.capitalize())
    
print(result1)
print(result2)