# Automação das máquinaas da WEB - luiz.lima
import os
import subprocess

machines = None
whiteListCommands = [
    'up',
    'destroy',
    'reload',
    'ssh',
    'full-provision',
    'install',
]
blacklistMachines = [
    'desktop.ini',
    'corporativo-meu',
    'hubspot',
    'redhat',
    'slides-ead',
    'talisma',
    'universo-ead',
    'universo-ead2.0',
    'media-server',
    'moodle-presencial',
    'iis'
]


def printColored(text, color):
    os.system('echo|set /p=\033[0{0}m'.format(color))
    print(text)
    os.system('echo|set /p=\033[97m')


def exec(command):
    global machines

    if command not in whiteListCommands:
        raise
    machinesPath = os.path.join('D:','vagrant', 'machines')
    machines = os.listdir(machinesPath)
    if type(machines) is not list or machines is None:
        print('Erro ao listar diretórios/máquinas')
        raise
    if len(os.sys.argv) > 2:
        if os.sys.argv[2] in machines:
            machines.clear()
            machines.append(os.sys.argv[2])
        else:
            raise
    elif len(os.sys.argv) == 2:
        print('Máquinas:\n {0}'.format(machines))
        accept = input('\nExecutar todas as máquinas?[s/n]').lower()
        if accept not in ('s', 'sim'):
            os.system('cls || clear')
            print('Saindo...')
            raise
    if command == 'install':
        commandPath = os.path.join('commands','environment')
    else:
        commandPath = 'commands'
    for i in (j for j in machines if j not in blacklistMachines):
        printColored('Executando {0} para {1}'.format(command, (i+'...')), 92)
        fullCommand = os.path.join(machinesPath, i, commandPath, '{0}.lnk'.format(command))
        subprocess.Popen([fullCommand], shell=True)

try:
    os.system('cls || clear')
    exec(os.sys.argv[1])
except:
    printColored('Argumentos inválidos:', 91)
    printColored('Exemplo de sintaxe: python {} <comando> <máquina>'.format(__file__), 93)
    printColored('Comandos:', 92)
    for i in whiteListCommands:
        print('\t{0}'.format(i))
    if machines is not None:
        validMachines = list(k for k in machines if k not in blacklistMachines)
        printColored('Máquinas:', 92)
        for i in validMachines:
            end = '| ' if i != validMachines[-1] else ''
            print('{0} '.format(i), end=end)
    print()
    os.system('echo|set /p=\033[0m')
    os.sys.exit()