# Objective:
# The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]
keywords= ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    word_list=review.split()
    new_review=[]
    for word in word_list:
        word_stripped = word.strip(".")
        if word_stripped.lower() in keywords:
            new_review.append(word.upper())
        else:
            new_review.append(word)
    
    print(" ".join(new_review))


# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in reviews:
    word_list=review.split()
    positive_counter=0
    negative_counter=0
    for word in word_list:
        word_stripped = word.strip(".")
        if word_stripped.lower() in positive_words:
            positive_counter+=1
        elif word_stripped.lower() in negative_words:
            negative_counter+=1
    
    print(f"Positive Words: {positive_counter} Negative Words: {negative_counter}")


# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

for review in reviews:
    word_list=review.split()
    char_counter=0
    summary = []
    for word in word_list:
        #+1 for space after the word. spaces are chars
        char_counter+=len(word)+1
        summary.append(word)
        if(char_counter>=30):
            break
    # if the summary is equal or more then it is not a summary thus doesnt need ...
    summary_text=" ".join(summary)
    if len(summary)<len(word_list):
        #dont need 3 periods if the summary ends with one period already
        if summary_text[-1] == ".":
            summary_text += ".."
        else:
            summary_text += "..."
    
    print(summary_text)

