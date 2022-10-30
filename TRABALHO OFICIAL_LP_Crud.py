#VARIAVÉIS
nome='vazio'
fm=1
z=''
x=0

#MENU
z=input("Pressione Enter para iniciar:")
while z!='t01':
	print('-'*50)
	v=0
	print("MENU: \n1-Cadastrar \n2-Ler \n3-Deletar \n4-Atualizar \n5-Sair")
	v=int(input('\nEscolha a opção: '))
	x=v
	z='t01'
	
	#SAIR DO PROGRAMA
	while x==5:
		print('-'*50)
		print('Deseja sair do Programa?\n 1-Sim\n 2-Não')
		fm=int(input())
		if fm==2:
			z=''
			x=0
		elif fm==1:
			v=5
			x=3
		else:
			print('Opção inválida!')
			
	#OPÇOES
	while v!=5:
		
		#OPÇÃO INVÁLIDA
		if v>5 or v==0:
			print("#"*25,"NÃO EXISTE ESSA OPÇÃO!","#"*25,'\n')
			z=input('Pressione Enter pra voltar ao menu: ')
			v=5
		
		#CADASTRAR
		elif v==1:
			print('='*25,'CADASTRO','='*25)
			nome=input('Cadastre seu nome: ')
			email=input("Cadastre seu email: ")
			senha=input("Cadastre sua senha: ")
			cpf=int(input("Cadastre seu cpf: "))
			telefone=int(input("Cadastre seu número de telefone: "))
			print('-'*50)
			print('DADOS: \nNome: %s \nEmail: %s \nSenha: %s \nCpf: %d \nN° de telefone: %d '% (nome,email,senha,cpf,telefone))
			print('-'*50)
			print('Confirmar dados?\n 1-Sim\n 2-Não')
			cfm=int(input())
			if cfm==1:
				v=5
				x=5
				z=''
			elif cfm>2:
				print('Opção invalida! \n')
				cfm=2
			
		#LER
		elif v==2:
			if nome=='vazio':
				print("\nÉ necessario fazer o cadastro!")
				v=1
			else:
				print('='*21,'Dados cadastrados','='*20)
				print('Nome de usuário: ',nome,' \nEmail: ',email,'\nSenha: ',senha,' \nCpf: ',cpf,' \nN° de telefone: ',telefone)
				z=input("Pressione Enter para voltar ao Menu:")
				v=5
		
		#DELETAR
		elif v==3:
			if nome=='vazio':
				print('\nNenhum cadastro foi efetuado!')
				v=5
				z=''
			else:
				print('='*21,'Dados cadastrados','='*20)
				print('1 - Nome de usuário: ',nome,' \n2 - Email: ',email,' \n3 - Senha: ',senha,' \n4 - Cpf: ',cpf,' \n5 - N° de telefone: ',telefone)
				print('\n6 - Apagar todos os dados \n')
				campo=int(input('Qual campo você deseja deletar? '))
				if campo==1:
					nome=''
				elif campo==2:
					email=''
				elif campo==3:
					senha=''
				elif campo==4:
					cpf=''
				elif campo==5:
					telefone=''
				elif campo==6:
					nome=email=senha=cpf=telefone=''
				
				if campo>6 or campo==0:
					print('\nOpção inválida! \n')
					v=3
					z='t'
				else:
					print('\nDELETADO!')
					v=5
					z=''
		
		#ATUALIZAR
		elif v==4:
			if nome=='vazio':
				print('\nEfetue o cadastro!')
				v=5
				z=''
			else:
				print('='*21,'Dados cadastrados','='*20)
				print('1 - Nome de usuário: ',nome,' \n2 - Email: ',email,' \n3 - Senha: ',senha,' \n4 - Cpf: ',cpf,' \n5 - N° de telefone: ',telefone)
				print('\n6 - Atualizar todos os dados \n')
				atual=int(input('Qual campo você deseja atualizar? '))
			
				#Variaveis para recuperação
				anome=nome
				aemail=email
				asenha=senha
				acpf=cpf
				atelefone=telefone
			
				if atual==1:
					nome=input('Novo nome: ')
				elif atual==2:
					email=input('Novo email: ')
				elif atual==3:
					senha=input('Nova senha: ')
				elif atual==4:
					cpf=int(input('Novo Cpf: '))
				elif atual==5:
					telefone=int(input('Novo N° de Telefone: '))
				elif atual==6:
					nome=input('Novo nome: ')
					email=input("Novo email: ")
					senha=input("Nova senha: ")
					cpf=int(input("Novo cpf: "))
					telefone=int(input("Novo N° de Telefone: "))
				
				#Dados atualizados ou não
				print('\nAtualizar dados?\n 1-Sim\n 2-Não')
				at=int(input())
				if at==1:
					v=5
					z=''
				elif at==2:
					nome=anome
					senha=asenha
					email=aemail
					cpf=acpf
					telefone=atelefone
					v=5
					z=''
				else:
					print('\nAtualizar dados?\n 1-Sim\n 2-Não')
					at=int(input())
z=''