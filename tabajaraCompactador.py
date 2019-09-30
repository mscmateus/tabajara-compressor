import pickle
import os

#CAMINHO_ABSOLUTO = os.getcwd()+"/"
#função para exibir ajuda
def ajuda():
    print("                           Ajuda\n"
          "Para compactar:"
          "encode -i nomeArquivoDeEntrada.txt -o nomeArquivoDeSaida.bin\n"
          "Para descompactar:"
          "decode -i nomeArquivoDeEntrada.bin -o nomeArquivoDeSaida.txt\n"
          "Para encerrar execução:"
          "exit")
#função responsavel por transformar o arquivo txt em bin
def compacta(arquivo, nomeSaida):
    print("Iniciano compactação...")
    #inicialização dos vetores do dicionario e de ocorrencia
    dicionario = []
    ocorrencia = []
    #adicionando a pulada de linha ao dicionario
    dicionario.append("\n")
    #leitura das linhas do arquivo passado como parametro
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            try:
                codigo = dicionario.index(palavra)
                ocorrencia.append(codigo)
            except ValueError:
                dicionario.append(palavra)
                ocorrencia.append(len(dicionario)-1)
        ocorrencia.append(0)
    #vetor para armazenar o tamenho do dicionario
    tamanhoDicionario = []
    tamanhoDicionario.append(len(dicionario))
    #junção do vetor de dicionario como o vetor de ocorrencias
    dicionario += ocorrencia
    #junção do vetor de tamanho do dicionario 
    dicionario = tamanhoDicionario + dicionario
    #abrindo o stream do arquivo de saida no mode de escrita binaria
    arquivoSaida = open(nomeSaida, "wb")
    #escrevendo o vetor de dicionario no arquivo em binario
    pickle.dump(dicionario, arquivoSaida)
    #fechando arquivo
    arquivoSaida.close()
    arquivoSaida = open(nomeSaida)
    print("Compactação concluida!")
    #Calculando e exibindo a quantidade em bytes reduzida
    print("Reduzido: "+str(os.path.getsize(arquivo.name)-os.path.getsize(arquivoSaida.name))+" bytes")
    #fechando arquivos
    arquivo.close()
    arquivoSaida.close()
#função responsavel por transformar o arquivo bin em txt
def descompacta(arquivo, nomeSaida):
    print("Iniciano descompactação...")
    #pegando o dicionario do arquivo binario
    informacao = pickle.load(arquivo)
    #pegando o tamano do dicionario
    tamanhoDicionario = informacao[0]
    #iniciando variavel que vai receber o texto decodificado
    texto=""
    #iniciando o dicionario
    dicionario = []
    for i in range(1, len(informacao)):
        #caso pertença ao dicionario
        if i <= tamanhoDicionario:
            dicionario.append(informacao[i])
        #decodificação para o texto
        elif i == tamanhoDicionario+1:
            texto += dicionario[informacao[i]]
        else:
            #Para organizar os espaços e pulada de linha
            if dicionario[informacao[i-1]] == "\n":
                texto += dicionario[informacao[i]]
            else:
                texto += " "+dicionario[informacao[i]]
    #abrindo arquivo para escrita
    arquivoSaida = open(nomeSaida, "w")
    #escrevendo o texto decodificado no arquivo
    arquivoSaida.write(texto)
    arquivo.close()
    arquivoSaida.close()
    print("Descompactação concluida!")

print("    Tabajara Compressor 2019, todos os direitos reservados\n\n"
      "Desenvolvido para a diciplina de Sistemas Multimídia do Curso de\n"
      "Bacharalado em Sistemas de Informação da Universidade Federal do Acre")


entrada = input("<tabja> ")

while entrada != "exit":
    entrada = entrada.split()
    #opção que inicia a compactação
    try:
        if entrada[0] == "encode":

            #caso o arquivo exista ele é compactado
            try:
                arquivoEntrada = open(entrada[2])
                if entrada[1] != "-i" or entrada[3] != "-o":
                    print("Erro! verifique a entrada e tente novamente, entre com ajuda para receber instruções.")
                else:
                    compacta(arquivoEntrada, entrada[4])
            except IOError:
                print("Erro! Arquivo não encontrado")

        #caso a entrada seja para a descompactação
        elif entrada[0] == "decode":

            try:
                arquivoEntrada = open(entrada[2], "rb")
                if entrada[1] != "-i" or entrada[3] != "-o":
                    print("Erro! verifique a entrada e tente novamente, entre com \"ajuda\" para receber instruções.")
                else:
                    descompacta(arquivoEntrada, entrada[4])
            except IOError:
                print("Erro! Arquivo não encontrado")
        else:
            # Em caso de entrada incompativel exiir ajuda
            ajuda()
    except IndexError:
        #Em caso de entrada incompativel exiir ajuda
        ajuda()
    entrada = input("<tabja> ")





