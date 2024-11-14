import asyncio
from search_product import search_product
from send_telegram_message import send_telegram_message

async def main():
    products = [
        'Memória RAM XPG Spectrix D35G, RGB, 16GB, 3200MHz, DDR4, CL16, Preto',
        'SSD Corsair 1TB MP600 Elite, M.2 NVMe, Leitura 7000MB/s e Gravação 6200MB/s, Para PS5, Branco'
        # Adicionar outros produtos
    ]

    for product_name in products:
        product_info = await search_product(product_name)

        message = f'Produto: {product_info["nome"]}\n'
        message += f'Preço Antigo: R$ {product_info["preco_antigo"]}\n'
        message += f'Preço Novo: R$ {product_info["preco_novo"]}\n'
        message += f'Preço em Parcelas: R$ {product_info["preco_parcelas"]}\n'
        message += f'Link do Produto: {product_info["link"]}'

        await send_telegram_message(message)

if __name__ == '__main__':
    asyncio.run(main())
