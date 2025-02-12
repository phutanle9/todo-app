# from functions import get_todos, write_todos
# from scipy.special import functions
# import functions
import functions

while True:
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip()

        if user_action.startswith("add"):
            todo = user_action[4:]
            # todo = input("Enter a todo: ") + "\n"

            todos= functions.get_todos("todos.txt")

            todos.append(todo + '\n')

            functions.write_todos(todos)

        elif user_action.startswith("show"):
            todos= functions.get_todos("todos.txt")

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index}-{item}"
                print(row)
        elif user_action.startswith("edit"):
            # number = int(input("Number of the todo to edit"))
            # number = number-1
            # with open('todos.txt','r') as file:
            #     todos= file.readlines()
            # print('Here is todos existing ',todos)
            #
            # new_todo = input("Enter new todo:")
            # todos[number] = new_todo + '\n'
            #
            # print("Here is how it will be", todos)
            #
            # with open('todos.txt', 'w') as file:
            #      file.writelines(todos)
            try:
                number = int(user_action[5:])
                print(number)

                number = number -1

                todos = functions.get_todos()

                new_todo = input("Enter new todo:")
                todos[number] = new_todo + '\n'
                functions.write_todos(todos)
            except ValueError:
                print("Your command is not valid.")
                continue


        elif user_action.startswith("complete"):
            try:
                number = int(user_action[9:])

                with open('todos.txt', 'r') as file:
                    todos = file.readlines()
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                message = f"Todo {todo_to_remove} was removed from the list"
                print(message)
            except IndexError:
                print("There is no item with that number")
                continue
        elif user_action.startswith("exit"):
            break
        else:
            print("Command is not valid")
print("Bye!")

        # match user_action:
        #     case 'add':
        #         todo = input("Enter a todo: ") + "\n"
        #
        #         with open('todos.txt', 'r') as file:
        #             todos = file.readlines()
        #
        #         todos.append(todo)
        #
        #         with open('todos.txt', 'w') as file:
        #             file.writelines(todos)
        #
        #     case 'show':
        #         file = open('todos.txt', 'r')
        #         todos = file.readlines()
        #         file.close()
        #
        #         for index, item in enumerate(todos):
        #             item = item.strip('\n')
        #             row = f"{index}-{item}"
        #             print(row)
        #     case 'edit':
        #         number = int(input("Number of the todo to edit"))
        #         number = number - 1
        #         with open('todos.txt', 'r') as file:
        #             todos = file.readlines()
        #         print('Here is todos existing ', todos)
        #
        #         new_todo = input("Enter new todo:")
        #         todos[number] = new_todo + '\n'
        #
        #         print("Here is how it will be", todos)
        #
        #         with open('todos.txt', 'w') as file:
        #             file.writelines(todos)
        #
        #     case 'complete':
        #         number = int(input("Number of the todo to complete"))
        #
        #         with open('todos.txt', 'r') as file:
        #             todos = file.readlines()
        #         index = number - 1
        #         todo_to_remove = todos[index].strip('\n')
        #         todos.pop(index)
        #
        #         with open('todos.txt', 'w') as file:
        #             file.writelines(todos)
        #
        #         message = f"Todo {todo_to_remove} was removed from the list"
        #         print(message)
        #     case 'exit':
        #         break

print("Bye")



