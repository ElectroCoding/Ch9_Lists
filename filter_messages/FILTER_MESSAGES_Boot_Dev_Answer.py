def filter_messages(messages):
    filtered_messages = []
    words_removed = []
    for message in messages:
        words = message.split()
        new_words = []
        removed = 0
        for word in words:
            if word == "dang":
                removed += 1
            else:
                new_words.append(word)
        filtered_messages.append(" ".join(new_words))
        words_removed.append(removed)

    return filtered_messages, words_removed
