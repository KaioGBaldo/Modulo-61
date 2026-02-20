# 🛒 Django MVT Architecture - Sistema de Listagem de Produtos

Este projeto consolida o uso do padrão de arquitetura **MVT (Model-View-Template)** do Django. O foco foi a criação de uma lógica de visualização dinâmica que processa dados do back-end e os renderiza em templates HTML, utilizando contextos para comunicação entre camadas.

---

# 📝 Resumo (Resume)
Neste projeto, implementei o fluxo completo de uma requisição Django. Configurei o `settings.py` com foco em localização (**PT-BR** e fuso horário de **São Paulo**) e estruturei o roteamento modular de URLs. Desenvolvi uma **View** funcional que organiza dados em um dicionário de contexto e utiliza o método `render` para entregar uma interface dinâmica ao usuário. A estrutura também conta com um modelo relacional robusto (Produto e Estoque), preparando o terreno para a migração de dados estáticos para dados persistidos no banco de dados SQLite3.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 📋 Funcionalidades em Destaque
* **Padrão MVT Completo:** Separação clara entre a lógica de dados (Models), lógica de negócio (Views) e apresentação (Templates).
* **Renderização Dinâmica:** Uso de contextos para passar listas de dicionários e variáveis para o HTML, permitindo interfaces que reagem aos dados do servidor.
* **Localização e i18n:** Configuração do projeto para o padrão brasileiro (`pt-br`), garantindo que datas e moedas sejam tratadas corretamente pelo framework.
* **Roteamento Hierárquico:** Uso de `include()` no arquivo de URLs principal para manter o projeto organizado e modularizado por apps.
* **Gerenciamento de Contexto:** Estruturação de dados complexos (listas de produtos com atributos de preço e disponibilidade) para consumo no front-end.
* **Infraestrutura ASGI/WSGI:** Configurações prontas para deploy, suportando tanto comunicações síncronas quanto assíncronas.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco é o **Back-End com Python**, dominar o padrão MVT é essencial para entender como os dados trafegam do banco até o navegador do cliente. Minha experiência com **React** facilita muito a compreensão de como os templates do Django funcionam, mas agora tenho o controle total do lado do servidor, gerenciando o estado e a lógica de negócio de forma centralizada e segura.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para consolidar a integração entre lógica de servidor e renderização de templates no ecossistema Django.*
