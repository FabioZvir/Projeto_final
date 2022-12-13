from connect import atualizarCurso, atualizarPessoa, atualizarProfes, buscarPorCPF, buscarPorIdCurso, buscarPorProf, deletarCurso, deletarPessoa, deletarProfessores, inserirCurso, inserirPessoa, inserirProfessor, mostrarCursos, mostrarPessoas, mostrarProfessores
from models import Cursos, Pessoa, Professores
from flask import Flask, render_template, redirect
from flask.globals import request



app = Flask(__name__)
@app.route('/')
def index():
    result = mostrarPessoas()
    cursos = mostrarCursos()
    return  render_template("index.html", result = result, cursos = cursos)

@app.route('/cursos')
def cursos():
    cursos = mostrarCursos()
    return render_template("cursos.html", cursos = cursos)

@app.route('/professores')
def professores():
    cursos = mostrarCursos()
    prof = mostrarProfessores()
    return render_template("professores.html", prof = prof, cursos = cursos)


@app.route('/cadastrar', methods=["POST", "GET"])
def cadastrar():
    nomeAluno = request.form["nome-aluno"]
    matricula = request.form["matricula"]
    cpf = request.form["cpf"]
    curso = request.form["curso"]
    pessoa = Pessoa(nomeAluno, matricula, cpf, curso)
    inserirPessoa(pessoa)
    return redirect("/")

@app.route('/deletar/<int:cpf>')
def deletar(cpf):
    try:
        deletarPessoa(cpf)
        return redirect("/")
    except:
        return "Algo de errado aconteceu"
    

@app.route('/atualizar/<int:cpf>', methods=["POST", "GET"])
def atualizar(cpf):
    if request.method == 'POST':
        nomeAluno = request.form["nome-aluno"]
        matricula = request.form["matricula"]
        cpf = request.form["cpf"]
        curso = request.form["curso"]
        pessoa = Pessoa(nomeAluno, matricula, cpf, curso)
        try:
            atualizarPessoa(cpf, pessoa)
            return redirect('/')
        except:
            return 'algo deu errado'
    else:
        print('foi')
        result = mostrarPessoas()
        pessoa = buscarPorCPF(cpf)
        print(pessoa)
        return render_template('index.html', result = result, pessoa = pessoa)


# Cursos

@app.route('/cadastrar/cursos', methods=["POST", "GET"])
def cadastrarCursos():
    nomeCurso =  request.form["nome-curso"]
    duracao = request.form["duracao"]
    idCurso = request.form["id-curso"]
    curso = Cursos(nomeCurso, duracao, idCurso)
    inserirCurso(curso)
    return redirect("/cursos")


@app.route('/cursoDel/<int:idcurso>')
def deletandoCurso(idcurso):
    try:
        deletarCurso(idcurso)
        return redirect("/cursos")
    except:
        return "Algo de errado aconteceu"

    
@app.route('/atualizando/<int:idCurso>', methods=["POST", "GET"])
def atualizandoCurso(idCurso):
    if request.method == 'POST':
        nomeCurso =  request.form["nome-curso"]
        duracao = request.form["duracao"]
        idCurso = request.form["id-curso"]
        curso = Cursos(nomeCurso, duracao, idCurso)
        try:
            atualizarCurso(idCurso, curso)
            return redirect('/cursos')
        except:
            return 'algo deu errado'
    else:
        cursos = mostrarCursos()
        curso = buscarPorIdCurso(idCurso)
        print(curso)
        return render_template('cursos.html', cursos = cursos, curso = curso)


#Professores

@app.route('/cadastrar/professores', methods=["POST", "GET"])
def cadastrarProfessores():
    nomeProfessor =  request.form["nome-professor"]
    cursoProfessor = request.form["cursoProfessor"]
    salario = request.form["salario"]
    CPF = request.form["CPF"]
    profess = Professores(nomeProfessor, cursoProfessor, salario, CPF)
    inserirProfessor(profess)
    return redirect("/professores")


@app.route('/professorDel/<int:cpf>')
def deletarProfessor(cpf):
    try:
        deletarProfessores(cpf)
        return redirect("/professores")
    except:
        return "Algo de errado aconteceu"



@app.route('/atualizandoProfessores/<int:CPF>', methods=["POST", "GET"])
def atualizandoProfessores(CPF):
    if request.method == 'POST':
        nomeProfessor =  request.form["nome-professor"]
        cursoProfessor = request.form["cursoProfessor"]
        salario = request.form["salario"]
        CPF = request.form["CPF"]
        profess = Professores(nomeProfessor, cursoProfessor, salario, CPF)
        try:
            atualizarProfes(CPF, profess)
            return redirect('/professores')
        except:
            return 'algo deu errado'
    else:
        prof = mostrarProfessores()
        profess = buscarPorProf(CPF)
        print(profess)
        return render_template('professores.html', prof = prof, profess = profess)
    


if __name__ == '__main__':
    app.run(debug=True)