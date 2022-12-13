class Pessoa:
    def __init__(self, nome, matricula, CPF, curso):
        self.nome = nome
        self.matricula = matricula
        self.CPF = CPF
        self.curso = curso


class Cursos:
    def __init__(self, nomeCurso, duracao, idCurso):
        self.nomeCurso = nomeCurso
        self.duracao = duracao
        self.idCurso = idCurso
        

class Professores:
    def __init__(self, nomeProfessor, curso, salario, CPF):
        self.nomeProfessor = nomeProfessor
        self.curso = curso
        self.salario = salario
        self.CPF = CPF