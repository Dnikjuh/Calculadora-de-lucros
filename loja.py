print("--- SISTEMA DE GESTÃO DA VENCESLAU COSMÉTICOS ---")
nome_produto = input("Qual é o nome do produto? (Ex: Base Matte)?")
preco_custo = float(
    input("Quanto é que pagou por ele? R$")
)
preco_venda = float(input("Por quanto é que o vai vender? R$"))
lucro_unitario = preco_venda - preco_custo
margem_lucro = (lucro_unitario / preco_custo) * 100
print("\n--- RELATÓRIO DO PRODUTO ---")
print(f"Produto: {nome_produto}")
print(f"Lucro por unidade: R$ {lucro_unitario:.2f}")
print(f"Margem de lucro: {margem_lucro:.1f}%")
if lucro_unitario > 0:
    print("Situação: Este produto está a dar lucro! Excelente escolha.")
else:
    print(
        "Atenção: Vai ter prejuízo ou vender pelo preço de custo! Reveja o" "preço."
    )