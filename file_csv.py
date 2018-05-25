
# Возьмите словарь с ответами из функции get_answer
# Запишите его содержимое в формате csv в формате: "ключ"; "значение". 
# Каждая пара ключ-значение должна располагаться на отдельной строке
import csv

answers=[]

# Функция добавляет новую строку Вопрос:Ответ в словарь
def set_answer():
    q=input("Введите вопрос в словарь: ")
    a=input("Введите ответ в словарь: ")
    dct={"question":"","answer":""}
    dct["question"]=q
    dct["answer"]=a
    answers.append(dct)

# Пройти в цикле cnt_qst кол-во раз и заполнить файл answers.csv
def write_csv(cnt_qst):
    with open('answers.csv','w',encoding='utf-8') as f:
        fields=['question', 'answer']
        writer=csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for s in range(cnt_qst):
            set_answer()
        for i in answers:
            writer.writerow(i)

# Запуск программы
if __name__=='__main__':
# Указывается кол-во строчек добавляемых в файл
    cnt_qst=int(input("Введите кол-во вопросов попавших в словарь: "))
    write_csv(cnt_qst)