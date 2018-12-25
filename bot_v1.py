import wikipedia
import wolframalpha

while True:
    my_input = input("Question: ")
    my_input = my_input.lower()
    if (my_input == "bye" or my_input == "goodbye"):
        break
    try:
        #wolframalpha code here
        app_id = "L84P2L-AU2XYJQXJ4" # please get your own API man, its free!! 
        client = wolframalpha.Client(app_id)
        res = client.query(my_input)
        answer = next(res.results).text 
        print(answer)

    except:
        #wikipedia code here
        print(wikipedia.summary(my_input, sentences=2))