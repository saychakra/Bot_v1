import wikipedia
#### changing language
lang = input("Enter the language you wish to read in: ")
wikipedia.set_lang(lang)
while True:
    my_input = input("Question: ")
    # print(wikipedia.summary(my_input))
    
    #### reducing the answer to 3 sentences
    # print(wikipedia.summary(my_input, sentences=3))
    
    #### other attributes of the api
    # val = wikipedia.page(my_input)
    # print("Wikipedia Page Title: ", val.title)
    # print("Wikipedia URL: ", val.url)
    # print("Wikipedia Content: ", val.content)

    # print(wikipedia.search(my_input))
    print(wikipedia.summary(my_input, sentences=3))

    