import json 

park = {
    'age' : 26,
    'uni' : "jbnu",
    'gender' : 'male',
}
# javascript 객체형 설명해주기

print(park)
print(type(park))

test1 = json.dumps(park) # dumps 는 json 파일로 변환

print(test1)
print(type(test1))

test2 = json.loads(test1)   