from tinydb import TinyDB, Query
from models import Pessoa, Cursos, Professores


# Alunos
bd = TinyDB("Pessoas.json")
pessoa = Query()

def inserirPessoa(model: Pessoa):
    bd.insert({"nome":model.nome
               ,"matricula":model.matricula
               ,"CPF":model.CPF
               ,"curso":model.curso})

def mostrarPessoas():
    todos = bd.all()
    return todos

def deletarPessoa(cpf: int):
    if bd.search(pessoa.CPF==str(cpf)):
        bd.remove(pessoa.CPF==str(cpf))
        print(pessoa)
    else:
        print("Usuário não encontrado")

def atualizarPessoa(cpf: int, model: Pessoa):
    if bd.search(pessoa.CPF == cpf):
        bd.remove(pessoa.CPF == cpf)
        inserirPessoa(model)
    else:
        print('Esse usuario não existe')

def buscarPorCPF(cpf):
    return bd.search(pessoa.CPF==str(cpf))

# Cursos

bdCursos = TinyDB("Cursos.json")
curso = Query()

def inserirCurso(model: Cursos):
    bdCursos.insert({"nomeCurso":model.nomeCurso,
                     "duracao":model.duracao,
                     "idCurso":model.idCurso})
    

def mostrarCursos():
    todosCursos = bdCursos.all()
    return todosCursos

def deletarCurso(idCurso: int):
    if bdCursos.search(curso.idCurso == str(idCurso)):
        bdCursos.remove(curso.idCurso == str(idCurso))  
    else:
        print("Não encontrado")
        
        
def atualizarCurso(idCurso: int, model:Cursos):
    print(idCurso)
    if bdCursos.search(curso.idCurso == idCurso):
        bdCursos.remove(curso.idCurso == idCurso)
        inserirCurso(model)
    else:
        print('Esse usuario não existe')
        
        

def buscarPorIdCurso(idCurso):
    return bdCursos.search(curso.idCurso == str(idCurso))



# Professor


bdProf = TinyDB("Professores.json")
profes = Query()

def inserirProfessor(model: Professores):
    bdProf.insert({"nomeProfessor":model.nomeProfessor,
                     "curso":model.curso,
                     "salario":model.salario,
                     "CPF":model.CPF})
    
def mostrarProfessores():
    todosProfessores = bdProf.all()
    return todosProfessores

def deletarProfessores(CPF: int):
    if bdProf.search(profes.CPF == str(CPF)):
        bdProf.remove(profes.CPF == str(CPF))  
    else:
        print("Não encontrado")
        
        
def atualizarProfes(CPF: int, model:Professores):
    if bdProf.search(profes.CPF == CPF):
        bdProf.remove(profes.CPF == CPF)
        inserirProfessor(model)
    else:
        print('Esse usuario não existe')
        
        
        
def buscarPorProf(CPF):
    return bdProf.search(profes.CPF == str(CPF))