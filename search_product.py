from playwright.async_api import async_playwright

async def search_product(product_name):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto('https://www.kabum.com.br/busca')
            
            await page.fill('input#input-busca', product_name)
            await page.press('input#input-busca', 'Enter')

            await page.wait_for_selector('main.sc-1be01e1c-9')

            products = await page.locator('[data-testid="tooltip"] span').all()
            product_to_click = None
            for product in products:
                if product_name in await product.inner_text():
                    product_to_click = product
                    break

            if product_to_click:
                await product_to_click.click()
            else:
                raise Exception('Produto não encontrado na lista de resultados.')

            await page.wait_for_selector('h1.brTtKt')

            product_url = page.url

            product_name = await page.locator('h1.brTtKt').inner_text()
            old_price = float((await page.locator('.oldPrice').inner_text()).replace('R$', '').replace(',', '.').strip())
            new_price = float((await page.locator('.finalPrice').inner_text()).replace('R$', '').replace(',', '.').strip())
            installment_price = float((await page.locator('.regularPrice').inner_text()).replace('R$', '').replace(',', '.').strip())

            await browser.close()

            message = f'Produto: {product_name}\n'
            message += f'Preço Antigo: R$ {old_price:.2f}\n' if old_price else 'Preço Antigo: Não disponível\n'
            message += f'Preço Novo: R$ {new_price:.2f}\n' if new_price else 'Preço Novo: Não disponível\n'
            message += f'Preço em Parcelas: R$ {installment_price:.2f}\n' if installment_price else 'Preço em Parcelas: Não disponível\n'
            message += f'Link do Produto: {product_url}'

            return message

    except Exception as e:
        return f'Erro durante a automação: {str(e)}'
