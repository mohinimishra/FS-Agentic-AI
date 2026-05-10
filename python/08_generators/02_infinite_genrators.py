def sereve_infinite():
    count =1
    while True:
        yield f"Count: {count}"
        count += 1
    
serve = sereve_infinite()
serve2 = sereve_infinite()

for _ in range(5):
    print(next(serve))
    
for _ in range(2):
    print(next(serve2))
        