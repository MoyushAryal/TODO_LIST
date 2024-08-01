''' 
To-Do List
Build a command-line to-do list application where users can add tasks, view tasks, mark tasks as completed, and delete tasks.
You can use a list to store the tasks.
'''

tasks=[]

def add_task(task):
    tasks.append(task)

def view_tasks():
    for task in tasks:
        print(task)

def delete_task(positon):
    tasks.pop(positon)

hold=True
choice=0

while(hold!=False):
    print('What task do you want to perform ?')
    print('1.Add new task')
    print('2.Delete a task ')
    print('3.View your tasks ')
    print('4.Mark task as complete')
    choice=int(input('Enter the task you want to perform : '))
    if choice ==1:
        inp_task=input('Enter the task you want to Add :')
        add_task(inp_task)
    elif choice==2:
        del_inp=int(input('Enter the task you want to delete :'))
        delete_task(del_inp-1)
    elif choice==3:
        view_tasks()
    elif choice==4:
        comp=int(input('Enter the task that is complete '))
        tasks[comp-1]=(f'{tasks[comp-1]} is completed.')
    conti=input('Do you want to continue ? (Y/N) ').upper()
    if conti=='N':
        hold=False

