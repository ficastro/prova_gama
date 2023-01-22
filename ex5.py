from pymongo import MongoClient

url_conexao = 'mongodb+srv://provagama:prova123@cluster0.8d7ssyq.mongodb.net/test'
colecao = 'produto'

def obter_colecao_mondogb(url_conexao,colecao):
    client = MongoClient(url_conexao)
    db = client[colecao]