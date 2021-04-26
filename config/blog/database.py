def create(request):
    
    completion_state = False

    try:
        f= open(user_db_path + str() + ".txt", "x")
        
    except FileExistsError:
        print('User already created')
       # delete(account_number)
        #delete user if already exiit
        #check content of file exist before deletinh
        return False
    else:
        f.write(str(user_detail))
        completion_state=True
    finally:   
        f.close()
        return completion_state
