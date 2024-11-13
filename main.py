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
        message = await search_product(product_name)
        await send_telegram_message(message)

if __name__ == '__main__':
    asyncio.run(main())
