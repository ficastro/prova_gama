sku = input("Insira o SKU: ")

estoque = input("Insira a quantidade do estoque: ")
while str(estoque).isnumeric() != True:
    estoque = input("\nInsira um número inteiro: ")


def ajustar_estoque(self, sku, estoque):
    collection = self.db['produto']
    result = collection.update({
        "_id.sku": sku
    },
    {
        "estoque": int(estoque)
    })