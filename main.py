from flask import Flask, render_template # Importa a biblioteca

app = Flask(__name__,template_folder='template') # Inicializa a aplicação

@app.route('/auth/') # Cria uma rota
def auth():
  return render_template('index.html')

@app.route('/client/') # Cria uma rota
def client():
  return render_template('pag2Cliente.html')

@app.route('/table/') # Cria uma rota
def table():
  return render_template('tabela.html')

@app.route('/boletim1/') # Cria uma rota
def boletim1():
  return render_template('Boletim1.html')

@app.route('/boletim2/') # Cria uma rota
def boletim2():
  return render_template('Boletim2.html')

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação