from mystack import myStack

def check_bracket(str_for_check):
    
    compare = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    string_test = myStack(str_for_check)
    string_temp = myStack('')  

    while(string_test.isEmpty()):
        current_item = string_test.pop() 
        if (string_test.isEmpty()):
            if (compare[current_item] == string_test.peek()):
                string_test.pop()
            else:
                string_temp.push(current_item)
        else:
            string_temp.push(current_item)
    return str(string_temp)

def check_balanced_string(str_for_check):
    
    size = len(str_for_check)
    
    if (size % 2 == 0):
        for i in range(size // 2): 
            str_for_check = check_bracket(str_for_check)
        if str_for_check == '':
            return "Сбалансированная строка"
        else:
            return "Несбалансированная строка"   
    else:
        return "Несбалансированная строка"
    
    
if __name__ == '__main__':
    print('*' * 50)
    test = '((((([{}])))))'
    # test = '[([])((([[[]]])))]{()}'
    # test = '{{[(])]}}'
   
    print(check_balanced_string(test))
