import requests, json, os

def downloadcode():
    print('Getting Code from GuiltlessCodeProvider...\n')
    codeurl = requests.get('https://guiltlesscodeprovider.raghavbhai4545.repl.co/agentcode')
    with open("agent.py",'wb') as e:
        e.write(codeurl.content)

    requirementsurl = requests.get('https://guiltlesscodeprovider.raghavbhai4545.repl.co/requirements')
    with open("requirements.txt",'wb') as r:
        r.write(requirementsurl.content)

    # poetryurl = requests.get('https://guiltlesscodeprovider.raghavbhai4545.repl.co/poetry')
    # with open("poetry.lock",'wb') as f:
    #     f.write(poetryurl.content)

    # pyprojecturl = requests.get('https://guiltlesscodeprovider.raghavbhai4545.repl.co/pyproject')
    # with open("pyproject.toml",'wb') as g:
    #     g.write(pyprojecturl.content)
    
downloadcode()
print('Got Code Now Installing Required Modules...\n')
os.system('pip install -r requirements.txt')
print('Now Running Agent...\n')

exec(open('agent.py').read())