# ListDomains
ListDomains is a subdomain enumeration tool, using passive techniques.

# Version
- 0.2
- New Api: Urlscan
- Updated Banner

# Instalation
```sh
git clone https://github.com/yHunterDep/listdomains/
cd listdomains
bash setup.sh
```

# Help of Tool
```
python3 listdomains.py -h
```
```
usage: listdomains.py [-h] -d DOMAIN [-subs] [-s] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        coloque o domínio
  -subs, --subs         pegar apenas subdomínios do alvo.
  -s, --silent          não mostrar o banner
  -o OUTPUT, --output OUTPUT
                        salvar resultados em um arquivo de texto. ex: -o subs.txt
```
