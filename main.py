from flask import Flask, render_template, request, redirect
app = Flask(__name__)  #instacia flask no aplicativo

#lista
contatos = []

agendas = []


@app.route('/')
def index():
    return render_template('index.html', contatos=contatos, agendas=agendas)


@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    """
    Rota para adicionar um novo contato.
    Se o método for POST, adiciona o novo contato à lista.
    Se não, exibe o formulário para adicionar um novo contato.
    """
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nomeanimal, especie, raca, peso, nometutor, telefone])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_contato.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        telefone = request.form['telefone']
        contatos[codigo] = [codigo, nomeanimal, especie, raca, peso, nometutor, telefone]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)  # Renderiza o formulário de edição


@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    del contatos[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial


@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        nomea = request.form['nomea']
        nomet = request.form['nomet']
        data = request.form['data']
        sintomas = request.form['sintomas']
        codigo = len(agendas)
        agendas.append([codigo, nomea, nomet, data, sintomas])
        return redirect('/')
    else:
        return render_template('agenda.html')


@app.route('/apagar_agenda/<int:codigo>')
def apagar_agenda(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del agendas[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial


@app.route('/calculadoram')
def calculadoram():
    return render_template('calculadoram.html', resultado="")


@app.route('/resultad', methods=['POST'])
def resultad():
    pesoanimal = float(request.form['peso'])
    graudesidrata = request.form['desidratação']

    if pesoanimal > 0:
        if graudesidrata.upper() == 'LEVE':
            soroml = pesoanimal * 50
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        elif graudesidrata.upper() == 'MODERADA':
            soroml = pesoanimal * 75
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        elif graudesidrata.upper() == 'GRAVE':
            soroml = pesoanimal * 100
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        else:
            quantidade = 'Isso não é um grau válido'

    else:
        quantidade = f'Isso não é um peso válido'

    return render_template('calculadoram.html', resultado=f'{quantidade}')


@app.route('/calculadoramp')
def calculadoramp():
    return render_template('calculadoramp.html', resultado="")


@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        peso_animal = float(request.form['peso'])
        dose_rec = int(request.form['dose_r'])
        dose = peso_animal * dose_rec

        return render_template('calculadoramp.html', resultado=f"A dose a ser administrada ao animal é de {dose} mg/kg.")


@app.route('/calculadoraa')
def calculadoraa():
    return render_template('calculadoraa.html', resultado="")


@app.route('/result', methods=['POST'])
def result():
    idadeanimal = int(request.form['idade'])
    esp = request.form['especie']

    if esp.upper() == "CACHORRO":

        if idadeanimal == 1:
            idade = 15
            mensagem = f"Seu cachorro tem {idade} anos humanos."
        elif (idadeanimal >= 2) and (idadeanimal <= 7):
            idade = 4 * idadeanimal + 16
            mensagem = f"Seu cachorro tem {idade} anos humanos."
        elif idadeanimal > 7:
            idade = 44 + ((idadeanimal - 7)*5)
            mensagem = f"Seu cachorro tem {idade} anos humanos."
        else:
            mensagem = f"Valor inválido"

    elif esp.upper() == "GATO":

        if idadeanimal == 1:
            idade = 15
            mensagem = f"Seu gato tem {idade} anos humanos."
        elif idadeanimal > 1:
            idade = 4*idadeanimal + 16
            mensagem = f"Seu gato tem {idade} anos humanos."
        else:
            mensagem = f"Valor inválido"

    return render_template('calculadoraa.html', resultado=f'{mensagem}')


if __name__ == '__main__':
    app.run(debug=True)  #executa o aplicativo flask
