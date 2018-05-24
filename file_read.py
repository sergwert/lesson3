def file_read():
    cnt_word=0
    cnt_line=0
    with open ('referat.txt', 'r', encoding='utf-8') as f:
        for ln in f:
            arr=ln.replace("\n",'').replace(".",'').replace(",","").split(' ')
            #print(arr)
            if arr[0] !='':
                cnt_word=cnt_word+len(arr)
            cnt_line=cnt_line+1
        print("Кол-во слов: ", cnt_word)
        print("Кол-во строк: ", cnt_line)

if __name__=='__main__':
    file_read()