import wolframalpha
app_id = "L84P2L-AU2XYJQXJ4"
client = wolframalpha.Client(app_id)
my_input = input("Question: ")
res = client.query(my_input)
answer = next(res.results).text
print(answer)