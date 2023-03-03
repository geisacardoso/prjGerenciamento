from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QStyle
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
import sys
import os #importa a biblioteca necessária para manipulação do S.O.
import mysql.connector #Importa o conector para o python se comunicar com o BD
#####Comando abaixo só é necessário executar uma única vez
os.system("pip install mysql-connector-python") #Faz a instalação do conector MySQL

def conectarBD(host, usuario, senha, bigfast_db): # função para conexão com o banco
    connection = mysql.connector.connect( #Informando os dados para conexão com o BD
        host = host, #ip do servidor do BD
        user = usuario, #Usuário do MySQL 
        password = senha, #Senha do usuário do MySQL
        database = bigfast_db  #nome do DB criado
    ) #Define o banco de dados usado

    return connection

def insertVeiculo(): #função insert para novos veiculos
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    valor = telaVeiculo.txtValor.text()
    marca = telaVeiculo.txtMarca.text()
    cor = telaVeiculo.txtCor.text()
    modelo = telaVeiculo.txtModelo.text()
    ano = telaVeiculo.txtAno.text()
    km = telaVeiculo.txtKm.text()
    combustivel = telaVeiculo.txtCombustivel.text()

    sql = "insert into veiculos (valor, marca, cor, modelo, ano, km, combustivel) values (%s, %s, %s, %s, %s, %s, %s)"
    data = (
    valor,
    marca,
    cor,
    modelo,
    ano,
    km,
    combustivel
    
    )

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    veiculoid = cursor.lastrowid #Obtém o último ID cadastrado

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o BD

    QtWidgets.QMessageBox.about(telaVeiculo, 'Cadastrado.', "Foi cadastrado o novo veiculo! ID " + str(veiculoid))

def insertFuncionario(): #função insert para novos funcionarios
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    nome = telaFuncionario.txtNome.text()
    rg = telaFuncionario.txtRg.text()
    cpf = telaFuncionario.txtCpf.text()
    data_nasc = telaFuncionario.txtDataNasc.text()
    celular = telaFuncionario.txtCelular.text()
    email = telaFuncionario.txtEmail.text()

    sql = "insert into funcionarios (nome, rg, cpf, data_nasc, celular, email) value (%s, %s, %s, %s, %s, %s)"
    data = (
    nome,
    rg,
    cpf,
    data_nasc,
    celular,
    email
    )

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    funcionarioid = cursor.lastrowid #Obtém o último ID cadastrado

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o BD

    QtWidgets.QMessageBox.about(telaFuncionario, 'Cadastrado.', "Foi cadastrado o novo funcionário! ID " + str(funcionarioid))

def updateVeiculo(): #função update para veiculos ja cadastrados
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    
    valor = telaAtualizarVeiculo.txtValor.text()
    marca = telaAtualizarVeiculo.txtMarca.text()
    cor = telaAtualizarVeiculo.txtCor.text()
    modelo = telaAtualizarVeiculo.txtModelo.text()
    ano = telaAtualizarVeiculo.txtAno.text()
    km = telaAtualizarVeiculo.txtKm.text()
    combustivel = telaAtualizarVeiculo.txtCombustivel.text()
    veiculoid = telaAtualizarVeiculo.txtId.text()
    

    sql = "update veiculos set valor = %s, marca = %s, cor = %s, modelo = %s, ano = %s, km = %s, combustivel = %s where id_veiculo = %s"
    data = (valor,
            marca,
            cor,
            modelo,
            ano,
            km,
            combustivel,
            veiculoid
    )

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit()  #Efetua as modificações

    ##recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    ##QtWidgets.QMessageBox.about(telaVeiculoAtualizar, 'Atualizado.', recordsaffected, "registros alterados")
    QtWidgets.QMessageBox.about(telaAtualizarVeiculo, 'Atualizado.', "Foi atualizado o veículo de ID: " + str(veiculoid))

def updateFuncionario(): #funcao para atualizar funcionarios ja cadastrados
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    nome = telaAtualizarFuncionario.txtNome.text()
    rg = telaAtualizarFuncionario.txtRg.text()
    cpf = telaAtualizarFuncionario.txtCpf.text()
    data_nasc = telaAtualizarFuncionario.txtDataNasc.text()
    celular = telaAtualizarFuncionario.txtTelefone.text()
    email = telaAtualizarFuncionario.txtEmail.text()
    idfuncionario = telaAtualizarFuncionario.txtId.text()

    sql = "update funcionarios set nome = %s, rg = %s, cpf = %s, data_nasc = %s, celular = %s, email = %s where id_funcionario = %s"
    data = (nome,
            rg,
            cpf,
            data_nasc,
            celular,
            email,
            idfuncionario
    )

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit()  #Efetua as modificações

    ##recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    ##QtWidgets.QMessageBox.about(telaVeiculoAtualizar, 'Atualizado.', recordsaffected, "registros alterados")
    QtWidgets.QMessageBox.about(telaAtualizarFuncionario, 'Atualizado.', "Foi atualizado o funcionário de ID: " + str(idfuncionario))
    
def deleteVeiculo(): #função para deletar veiculos
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    id_veiculo = telaExcluirVeiculo.txtId.text()

    sql = "delete from veiculos where id_veiculo = %s"
    data = (id_veiculo,)

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    ##recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    QtWidgets.QMessageBox.about(telaExcluirVeiculo, 'Excluido.', "Foi excluído o veículo de ID: " + str(id_veiculo))

def deleteFuncionario(): #função para deletarfuncionarios
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    id_funcionario = telaExcluirFuncionario.txtId.text()

    sql = "delete from funcionarios WHERE id_funcionario = %s"
    data = (id_funcionario,)

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    ##recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    QtWidgets.QMessageBox.about(telaExcluirFuncionario, 'Excluido.', "Foi excluído o funcionário de ID: " + str(id_funcionario))

def selecionarVeiculo():
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    print("chegou aqui")

    sql = "select * from veiculos" #Realizando um select para mostrar todas as linhas e colunas da tabela

    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtém todas as linhas no conjunto de resultados da consulta
    
    cursor.close() #fecha o cursor
    connection.close()
    
    linha=0
    telaSelecionarVeiculo.tableProd.setRowCount(0)
    for result in results: #Ler os registros existentes com o select
        print(result)
        telaSelecionarVeiculo.tableProd.setRowCount(len(results))
        telaSelecionarVeiculo.tableProd.setColumnCount(8)
        telaSelecionarVeiculo.tableProd.setItem(linha,0, QTableWidgetItem(str(result[0])))
        telaSelecionarVeiculo.tableProd.setItem(linha,1, QTableWidgetItem(str(result[1])))
        telaSelecionarVeiculo.tableProd.setItem(linha,2, QTableWidgetItem(str(result[2])))
        telaSelecionarVeiculo.tableProd.setItem(linha,3, QTableWidgetItem(str(result[3])))
        telaSelecionarVeiculo.tableProd.setItem(linha,4, QTableWidgetItem(str(result[4])))
        telaSelecionarVeiculo.tableProd.setItem(linha,5, QTableWidgetItem(str(result[5])))
        telaSelecionarVeiculo.tableProd.setItem(linha,6, QTableWidgetItem(str(result[6])))
        telaSelecionarVeiculo.tableProd.setItem(linha,7, QTableWidgetItem(str(result[7])))
        
        linha+=1

def selecionarFuncionario():
    connection = conectarBD("localhost","root","1234","bigfast_db") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    print("chegou aqui")

    sql = "select * from funcionarios" #Realizando um select para mostrar todas as linhas e colunas da tabela

    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtém todas as linhas no conjunto de resultados da consulta
    print("Carregando tablewidget")
    cursor.close() #fecha o cursor
    connection.close() #Fecha a conexão com o banco
    linha=0
    telaSelecionarFuncionario.tableFunc.setRowCount(0)
    for result in results: #Ler os registros existentes com o select
        print(result)
        telaSelecionarFuncionario.tableFunc.setRowCount(len(results))
        telaSelecionarFuncionario.tableFunc.setColumnCount(7)
        telaSelecionarFuncionario.tableFunc.setItem(linha,0, QTableWidgetItem(str(result[0])))
        telaSelecionarFuncionario.tableFunc.setItem(linha,1, QTableWidgetItem(str(result[1])))
        telaSelecionarFuncionario.tableFunc.setItem(linha,2, QTableWidgetItem(str(result[2])))
        telaSelecionarFuncionario.tableFunc.setItem(linha,3, QTableWidgetItem(str(result[3])))
        telaSelecionarFuncionario.tableFunc.setItem(linha,4, QTableWidgetItem(str(result[4])))
        telaSelecionarFuncionario.tableFunc.setItem(linha,5, QTableWidgetItem(str(result[5])))
        telaSelecionarFuncionario.tableFunc.setItem(linha,6, QTableWidgetItem(str(result[6])))
        
        linha+=1

def AbrircadastroVeiculo(): #função abrir tela de cadastro de veiculos
    telaVeiculo.show()
    telaPrincipal.close()

def AbrircadastroFuncionario(): #função abrir tela de cadastro de funcionarios
    telaFuncionario.show()
    telaPrincipal.close()

def AbriratualizarVeiculo(): #função abrir tela atualizar veiculos
    telaAtualizarVeiculo.show()
    telaVeiculo.close()

def AbriratualizarFuniconario(): #função abrir tela atualizar veiculos
    telaAtualizarFuncionario.show()
    telaFuncionario.close()

def AbrirexcluirVeiculo(): #função abrir tela excluir veiculo
    telaExcluirVeiculo.show()
    telaVeiculo.close() 

def AbrirexcluirFuncionario(): #função abrir tela excluir Funcionario
    telaExcluirFuncionario.show()
    telaFuncionario.close()

def AbrirselecionarVeiculo(): #função abrir tela selecionar veiculo
    telaSelecionarVeiculo.show()
    telaVeiculo.close()
    selecionarVeiculo()

def AbrirselecionarFuncionario(): #função abrir tela selecionar funcionario
    telaSelecionarFuncionario.show()
    telaFuncionario.close()
    selecionarFuncionario()

def inAtualizar_AbririnserirFuncionario(): #função em atualizar abrir tela inserir funcionario
    telaFuncionario.show()
    telaAtualizarFuncionario.close()
    selecionarFuncionario()

def inAtualizar_AbrirvertodosFuncionarios(): #função em atualizar abrir tela ver todos funcionario
    telaSelecionarFuncionario.show()
    telaAtualizarFuncionario.close()
    selecionarFuncionario()

def inAtualizar_AbrirExcluirFuncionarios(): #função em atualizar abrir tela excluir funcionario
    telaExcluirFuncionario.show()
    telaAtualizarFuncionario.close()
    selecionarFuncionario()

def inverTodos_AbririnserirFuncionario(): #função em vertodos abrir tela inserir funcionario
    telaFuncionario.show()
    telaSelecionarFuncionario.close()

def inverTodos_AbrirAtualizarFuncionarios(): #função em vertodos abrir tela atualizar funcionario
    telaAtualizarFuncionario.show()
    telaSelecionarFuncionario.close()

def inverTodos_AbrirExcluirFuncionarios(): #função em vertodos abrir tela excluir funcionario
    telaExcluirFuncionario.show()
    telaSelecionarFuncionario.close()
    selecionarFuncionario()

def inExcluir_AbririnsertFuncionarios(): #função em excluir abrir tela inserir funcionario
    telaFuncionario.show()
    telaExcluirFuncionario.close()
    selecionarFuncionario()

def inExcluir_AbriratualizarFuncionarios(): #função em excluir abrir tela inserir funcionario
    telaAtualizarFuncionario.show()
    telaExcluirFuncionario.close()
    selecionarFuncionario()

def inExcluir_AbrirvertodosFuncionarios(): #função em excluir abrir tela inserir funcionario
    telaSelecionarFuncionario.show()
    telaExcluirFuncionario.close()
    selecionarFuncionario()

def inAtualizar_AbririnserirVeiculos(): #função em atualizar abrir tela inserir veiculos
    telaVeiculo.show()
    telaAtualizarVeiculo.close()

def inAtualizar_AbrirvertodosVeiculos(): #função em atualizar abrir tela ver todos veiculos
    telaSelecionarVeiculo.show()
    telaAtualizarVeiculo.close()
    selecionarVeiculo()

def inAtualizar_AbrirExcluirVeiculos(): #função em atualizar abrir tela excluir veiculos
    telaExcluirVeiculo.show()
    telaAtualizarVeiculo.close()

def inverTodos_AbririnserirVeiculos(): #função em vertodos abrir tela inserir veiculos
    telaVeiculo.show()
    telaSelecionarVeiculo.close()
    selecionarVeiculo()

def inverTodos_AbrirAtualizarVeiculos(): #função em vertodos abrir tela atualizar veiculo
    telaAtualizarVeiculo.show()
    telaSelecionarVeiculo.close()
    selecionarVeiculo()

def inverTodos_AbrirExcluirVeiculos(): #função em vertodos abrir tela excluir veiculo
    telaExcluirVeiculo.show()
    telaSelecionarVeiculo.close()

def inExcluir_AbririnsertVeiculos(): #função em excluir abrir tela inserir veiculo
    telaVeiculo.show()
    telaExcluirVeiculo.close()

def inExcluir_AbriratualizarVeiculos(): #função em excluir abrir tela inserir veiculo
    telaAtualizarVeiculo.show()
    telaExcluirVeiculo.close()
    selecionarVeiculo()

def inExcluir_AbrirvertodosVeiculos(): #função em excluir abrir tela inserir veiculo
    telaSelecionarVeiculo.show()
    telaExcluirVeiculo.close()
    selecionarVeiculo()

def cadastroVeiculo_backacessar(): #função em inserir veiculo voltar ao menu principal 
    telaPrincipal.show()
    telaVeiculo.close()

def cadastroFuncionario_backacessar(): #função em inserir Funcionario voltar ao menu principal 
    telaPrincipal.show()
    telaFuncionario.close()

def inAtualizarVeiculo_backacessar(): #função em atualizar veiculo voltar ao menu principal
    telaPrincipal.show()
    telaAtualizarVeiculo.close()

def inAtualizarFuncionario_backacessar(): #função em atualizar Funcionario voltar ao menu principal
    telaPrincipal.show()
    telaAtualizarFuncionario.close()

def inverTodosFuncionario_backacessar(): #função em verTodos Funcionario voltar ao menu principal
    telaPrincipal.show()
    telaSelecionarFuncionario.close()

def inverTodosVeiculo_backacessar(): #função em verTodos veiculo voltar ao menu principal
    telaPrincipal.show()
    telaSelecionarFuncionario.close()

def inExcluirFuncionario_backacessar(): #função em Excluir Funcionairo voltar ao menu principal
    telaPrincipal.show()
    telaSelecionarFuncionario.close()

def inExcluirVeiculo_backacessar(): #função em Excluir veiculo voltar ao menu principal
    telaPrincipal.show()
    telaSelecionarVeiculo.close()

def telaAcessar():
    telaPrincipal.show()

app = QtWidgets.QApplication(sys.argv)

#carregando arquivos de interface nas variaveis
telaPrincipal = uic.loadUi('acessar.ui')
telaVeiculo = uic.loadUi('inserirProduto.ui')
telaFuncionario = uic.loadUi('inserirFuncionario.ui')
telaAtualizarVeiculo = uic.loadUi('atualizarProduto.ui')
telaAtualizarFuncionario = uic.loadUi('atualizarFuncionario.ui')
telaExcluirFuncionario = uic.loadUi('excluirFuncionario.ui')
telaExcluirVeiculo = uic.loadUi('excluirProduto.ui')
telaSelecionarVeiculo = uic.loadUi('selecionarProduto.ui')
telaSelecionarFuncionario = uic.loadUi('selecionarFuncionario.ui')

telaPrincipal.show() #abrindo a tela inicial do projeto

telaPrincipal.btnprod.clicked.connect(AbrircadastroVeiculo) #abre o cadastro de veiculos
telaPrincipal.btnfunc.clicked.connect(AbrircadastroFuncionario) #abre o cadastro de funcionarios

telaVeiculo.btnConfirmar.clicked.connect(insertVeiculo) #realiza o insert dos dados do veiculo
telaVeiculo.back.clicked.connect(cadastroVeiculo_backacessar) #volta ao home

telaFuncionario.btnConfirmar.clicked.connect(insertFuncionario) #realiza o insert dos dados do funcionario
telaFuncionario.back.clicked.connect(cadastroFuncionario_backacessar) #volta ao home

telaVeiculo.btnAtualizar.clicked.connect(AbriratualizarVeiculo) #abre o atualizar dados do veiculos
telaFuncionario.btnAtualizar.clicked.connect(AbriratualizarFuniconario) #abre o atualizar dados do funcionario

##Função dos botões laterais de transição entre as telas (funcionarios)
telaAtualizarFuncionario.btnInserir.clicked.connect(inAtualizar_AbririnserirFuncionario) #função em atualizar abrir tela inserir funcionarios
telaAtualizarFuncionario.btnverTodos.clicked.connect(inAtualizar_AbrirvertodosFuncionarios) #função em atualizar abrir tela ver todos funcionarios
telaAtualizarFuncionario.btnExcluir.clicked.connect(inAtualizar_AbrirExcluirFuncionarios) #função em atualizar abrir tela excluir funcionarois
telaAtualizarFuncionario.back.clicked.connect(inAtualizarFuncionario_backacessar) #volta ao home

telaSelecionarFuncionario.btnInserir.clicked.connect(inverTodos_AbririnserirFuncionario) #função em ver todos abrir tela inserir funcionarios
telaSelecionarFuncionario.btnAtualizar.clicked.connect(inverTodos_AbrirAtualizarFuncionarios) #função em ver todos abrir tela excluir funcionarios
telaSelecionarFuncionario.btnExcluir.clicked.connect(inverTodos_AbrirExcluirFuncionarios) #função em ver todos abrir tela excluir funcionarios
telaSelecionarFuncionario.back.clicked.connect(inverTodosFuncionario_backacessar) #volta ao home

telaExcluirFuncionario.btnInserir.clicked.connect(inExcluir_AbririnsertFuncionarios) #função em excluir abrir tela inserir funcionarios
telaExcluirFuncionario.btnAtualizar.clicked.connect(inExcluir_AbriratualizarFuncionarios) #função em excluir abrir tela atualizar funcionarios
telaExcluirFuncionario.btnverTodos.clicked.connect(inExcluir_AbrirvertodosFuncionarios) #função em excluir abrir tela ver todos funcionarios
telaExcluirFuncionario.back.clicked.connect(inExcluirFuncionario_backacessar) #volta ao home

##Função dos botões laterais de transição entre as telas (produtos)
telaAtualizarVeiculo.btnInserir.clicked.connect(inAtualizar_AbririnserirVeiculos) #função em atualizar abrir tela inserir funcionarios
telaAtualizarVeiculo.btnverTodos.clicked.connect(inAtualizar_AbrirvertodosVeiculos) #função em atualizar abrir tela ver todos funcionarios
telaAtualizarVeiculo.btnExcluir.clicked.connect(inAtualizar_AbrirExcluirVeiculos) #função em atualizar abrir tela excluir funcionarois
telaAtualizarVeiculo.back.clicked.connect(inAtualizarVeiculo_backacessar) #volta ao home

telaSelecionarVeiculo.btnInserir.clicked.connect(inverTodos_AbririnserirVeiculos) #função em ver todos abrir tela inserir funcionarios
telaSelecionarVeiculo.btnAtualizar.clicked.connect(inverTodos_AbrirAtualizarVeiculos) #função em ver todos abrir tela excluir funcionarios
telaSelecionarVeiculo.btnExcluir.clicked.connect(inverTodos_AbrirExcluirVeiculos) #função em ver todos abrir tela excluir funcionarios
telaSelecionarVeiculo.back.clicked.connect(inverTodosVeiculo_backacessar) #volta ao home

telaExcluirVeiculo.btnInserir.clicked.connect(inExcluir_AbririnsertVeiculos) #função em excluir abrir tela inserir funcionarios
telaExcluirVeiculo.btnAtualizar.clicked.connect(inExcluir_AbriratualizarVeiculos) #função em excluir abrir tela atualizar funcionarios
telaExcluirVeiculo.btnverTodos.clicked.connect(inExcluir_AbrirvertodosVeiculos) #função em excluir abrir tela ver todos funcionarios

telaExcluirVeiculo.back.clicked.connect(inExcluirVeiculo_backacessar) #volta ao home

telaAtualizarVeiculo.btnConfirmar.clicked.connect(updateVeiculo) #atualiza as informações do veiculo
telaAtualizarFuncionario.btnConfirmar.clicked.connect(updateFuncionario) #atualiza as informações do funcionario

telaVeiculo.btnExcluir.clicked.connect(AbrirexcluirVeiculo) #abre o excluir veiculo
telaFuncionario.btnExcluir.clicked.connect(AbrirexcluirFuncionario) #abre o excluir funcionario

telaExcluirVeiculo.btnExcluirConfirm.clicked.connect(deleteVeiculo)#deleta o veiculo por id
telaExcluirFuncionario.btnExcluirConfirm.clicked.connect(deleteFuncionario)#deleta o funcionario por id

telaVeiculo.btnverTodos.clicked.connect(AbrirselecionarVeiculo)#abre o selecionar veiculo por id
telaFuncionario.btnverTodos.clicked.connect(AbrirselecionarFuncionario)#abre o seleiconar funcionario por id

app.exec()