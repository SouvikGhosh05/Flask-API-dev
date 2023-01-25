from flask import Flask, request

app=Flask(__name__)

@app.get('/')
def query_records():
    try:
        with open("records.txt", 'r') as rec:
            return rec.read()
    except FileNotFoundError:
        return "No resource found!"

@app.post('/')
def new_records():
    with open("records.txt", 'a') as rec:
        if request.data.decode('UTF-8'):
            rec.write(f"{request.data.decode('UTF-8')} \n")
        else:
            return "Input is empty!"
    return "Resource is added"

@app.delete('/')
def delete_records():
    if stripped:=request.data.decode('UTF-8').strip():
        with open("records.txt", 'r') as rec:
            lines= rec.readlines()
            stp_lst=[line.strip() for line in lines]
            if stripped in stp_lst:
                with open("records.txt", 'w') as rec:
                    rev_stp_list=list(reversed(stp_lst))
                    for rev in rev_stp_list:
                        if rev==stripped:
                            get_index=rev_stp_list.index(stripped)
                            del lines[len(lines)-get_index-1]
                            rec.writelines(lines)
                            break
                    else:
                        return "Resourse not found"
                    return "Resource deleted"
            else:
                return "Invalid resource"         
    else:
        return "Input is empty!"
            
app.run()