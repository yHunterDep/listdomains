#!/usr/bin/python3

import argparse, requests, pyfiglet, json, re

subs_total = []

vermelho = "\033[31m"
verde = "\033[32m"
laranja = "\033[33m"
reset = "\033[0;0m"

criador = "HunterDep"
versão = "0.2"
github = "https://github.com/yHunterDep"
apis = "HackerTarget, AlienVault, Urlscan, Crtsh"

def banner():
        print(verde + pyfiglet.figlet_format("ListDomains", font="slant"))
        print(f"Coded by {vermelho + criador + verde}")
        print(f"Versão: {vermelho + versão + verde}")
        print(f"Github: {laranja + github + verde}")
        print(f"Apis: {laranja}{apis}\n")

def hacker_target(domain):
        try:
                req = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}")
                ht = req.text
                ht = ht.split()
                for i in ht:
                        p = re.findall(",\d+\.?\d+\.?\d+\.?\d+", i)
                        p = "".join(p)
                        i = i.replace(p, "")
                        subs_total.append(i)
        except:pass

def alien_vault(domain):
        try:
                req = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns")
                alien = req.json()
                alien = json.dumps(alien)
                alien = json.loads(alien)

                lists = alien["passive_dns"]

                for list in lists:
                        subs = list["hostname"]
                        subs_total.append(subs)
        except:pass

def urlscan(domain):
        try:
                req = requests.get(f"https://urlscan.io/api/v1/search/?q=domain:{domain}")
                urlscan = req.json()
                urlscan = json.dumps(urlscan)
                urlscan = json.loads(urlscan)
                results = urlscan["results"]

                for result in results:
                        result = result["task"]["domain"]
                        subs_total.append(result)

        except Exception as x:print(x)

def crtsh(domain):
        try:
                req = requests.get(f"https://crt.sh/?q={domain}&output=json")
                crt = req.json()
                crt = json.dumps(crt)
                crt = json.loads(crt)

                for index in crt:
                        common_name = index["common_name"]
                        name_value = index["name_value"]
                        subs_total.append(common_name)
                        subs_total.append(name_value)
        except:pass

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="coloque o domínio")
parser.add_argument("-subs", "--subs", help="pegar apenas subdomínios do alvo.", action="store_true")
parser.add_argument("-s", "--silent", help="não mostrar o banner", action="store_true")
parser.add_argument("-o", "--output", help="salvar resultados em um arquivo de texto. ex: -o subs.txt")
args = parser.parse_args()

domain = args.domain
subs = args.subs
sil = args.silent
output = args.output

if not sil:
        banner()

hacker_target(domain)
alien_vault(domain)
crtsh(domain)
urlscan(domain)

subs_total = [x for x in subs_total if x is not None]
subs_total = [x.lower() for x in subs_total]
subs_total = [x.strip().split("\n") for x in subs_total]
subs_total = [parte for item in subs_total for parte in item]

if subs:
        subs_total = [x for x in subs_total if x.endswith(domain)]

subs_total = set(subs_total)
subs_total = "\n".join(subs_total)
print(subs_total)

if output:
        try:
                file = open(output, 'a+')
                file.write(subs_total)
        except:
                pass
