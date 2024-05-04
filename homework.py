
python_reviews = [ "This product is really good. I'm impressed with its quality.",
                   "The performance of this product is excellent. Highly recommended!",
                     "I had a bad experience with this product. It didn't meet my expectations.", 
                     "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."
                ]

review_words = ["good", "excellent", "bad", "poor"]
for sentence in python_reviews:
    for word in review_words:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
    print(sentence)


python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]
reviews = " ".join(python_reviews)
print(reviews)

for word in keywords:
    reviews = reviews.replace(word, word.upper())
    reviews = reviews.replace(word.title(), word.upper())
print(reviews)



        

