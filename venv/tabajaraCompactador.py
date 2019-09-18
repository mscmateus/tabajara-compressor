import pickle
import os

CAMINHO_ABSOLUTO = os.getcwd()+"/"

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
    dicionario = []
    ocorrencia = []
    dicionario.append("\n")
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
    tamanhoDicionario = []
    tamanhoDicionario.append(len(dicionario))
    dicionario += ocorrencia
    dicionario = tamanhoDicionario + dicionario
    arquivoSaida = open(CAMINHO_ABSOLUTO+nomeSaida, "wb")
    pickle.dump(dicionario, arquivoSaida)
    arquivo.close()
    arquivoSaida.close()
    print("Compactação concluida!")

def descompacta(arquivo, nomeSaida):
    print("Iniciano descompactação...")
    informacao = pickle.load(arquivo)
    tamanhoDicionario = informacao[0]
    texto=""
    dicionario = []
    for i in range(1, len(informacao)):
        if i <= tamanhoDicionario:
            dicionario.append(informacao[i])
        elif i == tamanhoDicionario+1:
            texto += dicionario[informacao[i]]
        else:
            if dicionario[informacao[i-1]] == "\n":
                texto += dicionario[informacao[i]]
            else:
                texto += " "+dicionario[informacao[i]]

    arquivoSaida = open(CAMINHO_ABSOLUTO + nomeSaida, "w")
    arquivoSaida.write(texto)
    arquivo.close()
    arquivoSaida.close()
    print("Descompactação concluida!")

print("    Tabajara Compressor 2019, todos os direitos reservados\n\n"
      "Desenvolvido para a diciplina de Sistemas Multimídia do Curso de\n"
      "bacaheralado em Sistemas de Informação da Universidade Federal do Acre")

#testes
#encode -i teste.txt -o binario.bin
#decode -i binario.bin -o texto.txt

entrada = input("<tabja> ")

while entrada != "exit":
    entrada = entrada.split()
    #opção que inicia a compactação
    try:
        if entrada[0] == "encode":

            #caso o arquivo exista ele é compactado
            try:
                arquivoEntrada = open(CAMINHO_ABSOLUTO+""+entrada[2])
                if entrada[1] != "-i" or entrada[3] != "-o":
                    print("Erro! verifique a entrada e tente novamente, entre com ajuda para receber instruções.")
                else:
                    compacta(arquivoEntrada, entrada[4])
            except IOError:
                print("Erro! Arquivo não encontrado")

        #caso a entrada seja para a descompactação
        elif entrada[0] == "decode":

            try:
                arquivoEntrada = open(CAMINHO_ABSOLUTO+""+entrada[2], "rb")
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





