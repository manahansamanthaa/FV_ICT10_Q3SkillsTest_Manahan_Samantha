from pyscript import document, display

def account_creation(e): #we put e for event handling
    document.getElementById('output').innerHtml = ' '
    Username = document.getElementById('username').value
    Username_length = len(username)

    if username_length < 7:
        display(f'Your user is too short, add {7 - Username_length}', target = 'output')
    else:
        display(f'okay', target = 'output')




    
    













