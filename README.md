# Phishing para captura de senhas do Facebook

### Ferramentas

- Kali Linux
- setoolkit
- Python

### Configurando o Phishing no Kali Linux

- Acesso root: ``` sudo su ```
- Iniciando o setoolkit: ``` setoolkit ```
- Tipo de ataque: ``` 1 - Social-Engineering Attacks ```
- Vetor de ataque: ``` 2 - Web Site Attack Vectors ```
- Método de ataque: ``` 3 - Credential Harvester Attack Method ```
- Método de ataque: ``` 2 - Site Cloner ```
- Obtendo o endereço da máquina: ``` ifconfig ```
- URL para clone: facebook.com
- Executar script para modificar código fonte da página clonada. A alteração serve para não ocorrer a criptografia da senha e o POST request ser feito em texto claro. ``` python3 config_index.py ```

### Resutados

![Alt text](./result.png "resultado do POST request")
