from flask import Flask, render_template, request, redirect, url_for
from funcoes import *

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
  if not tasks:
    lines = ler_arquivo()

    for line in lines:
      tasks.append(line.strip())
      
  return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
  
    if task:
        tasks.append(task)
        salvar_arquivo(tasks)
      
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        excluir_tarefa(tasks)
      
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
  
