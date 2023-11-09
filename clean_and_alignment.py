from collections import Counter
import json

# Load the JSONL file
def get_clean_word(file_path,top_words=None):
    file_path = 'output_labels_list.jsonl'

    # Read and parse the JSONL file
    with open(file_path, 'r') as file:
        # Read the lines in the file
        lines = file.readlines()
        # Parse each line as a JSON object
        data = [json.loads(line) for line in lines]

    # Initialize a Counter object to hold the word frequencies
    word_freq = Counter()

    import nltk
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet

    # Download necessary NLTK resources
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('omw-1.4')

    # Initialize the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()
    sum_list=[]
    for entry in data:
        word_list = entry['word_list']
        sum_list.extend(word_list)
        # Update the word frequencies
        word_freq.update(word_list)
    # all_word_list_before_clean_num = sum(1 for word, freq in word_freq.items() if freq == 1)
    # print(all_word_list_before_clean_num)
    def get_wordnet_pos(treebank_tag):
        """
        Convert the part-of-speech naming convention
        from the Penn Treebank tag to a WordNet lemmatizer compatible tag.
        """
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            # As default pos in lemmatization is NOUN
            return wordnet.NOUN

    # Create a new Counter to hold the normalized word frequencies

    def simple_normalize(word):
        word = word.lower()
        if word.endswith('s') and not word.endswith("ss"):
            return word.rstrip('s')
        else:
            return word

    # Create a new Counter to hold the simplified normalized word frequencies
    simplified_normalized_word_freq = Counter()

    # Iterate over each word in the original word frequency Counter
    for word, freq in word_freq.items():
        # Apply the simple normalization function
        normalized_word = simple_normalize(word)
        # Update the simplified normalized word frequency Counter
        simplified_normalized_word_freq[normalized_word] += freq
    # Get the most common 50 normalized words

    non_repeat=[]
    print(len(simplified_normalized_word_freq.keys()),"simplified_normalized_word_freq.items()")
    for word, freq in simplified_normalized_word_freq.items():
        if word not in non_repeat:
            non_repeat.append(word)
    print(non_repeat,"non_repeat")
    print(len(non_repeat))
    if top_words==None:
        top_words=len(non_repeat)
    normalized_top_50_words = simplified_normalized_word_freq.most_common(top_words)
    print(normalized_top_50_words)

    # all_word_list=list(simplified_normalized_word_freq.keys())
    print(len(normalized_top_50_words))
    word_list = []
    phrase_list = [item[0] for item in normalized_top_50_words]

    return phrase_list


# print(get_clean_word(""))