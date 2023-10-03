# Eventex 

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com python
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/patresio/wttd.git
cd wttd
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?