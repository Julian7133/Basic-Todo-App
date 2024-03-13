from flask import Flask, render_template, redirect, url_for, request

app = Flask(
    __name__,
    template_folder='templates/'
    )


todos = [{'task': 'Test task 1', 'done':False}]

#{'todo_name': 'Test task 1', 'Done':False}


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template ('index.html', todos=todos)



# add Todo
@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, 'done':False})
    return redirect(url_for('index'))



#edit ToDo
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form["todo"]
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', todo=todo, index=index)

        
# check off todo
@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('index'))

    


# delete todo
@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)