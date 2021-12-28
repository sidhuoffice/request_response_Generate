def userinput():
    what_generate = str(input("what u need 1.request or 2.response: "))
    variableInput = "Wrong Input"
    if what_generate == '1':
        variableInput = str(input("enter varialbes: ")).replace(" ","")
        request(variableInput.split("="))
    elif what_generate == '2':
        variableInput = str(input("enter varialbes: ")).replace(" ","")
        response(variableInput.split("="))
    else:
        print(variableInput)
def request(userInput):
    request_INIT(userInput)
    print("\n\n")
    for i in userInput:
        request_out = f"""def get_{i}(self):\n\treturn self.{i}"""
        print(request_out)

def response(userInput):
    for i in userInput:
        response_out = f"""def set_{i}(self,{i}):\n\tself.{i}={i}"""
        print(response_out)



def request_INIT(userInput):
    for index,i in enumerate(userInput,start=0):
        if index == 0:
            init_out = f"""def __init__(self,data):"""
            print(init_out)
        if_out = f"""\tif '{i}' in data:\n\tself.{i}=data['{i}']"""
        print(if_out)



userinput()