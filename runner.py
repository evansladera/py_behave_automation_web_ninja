# from behave import __main__ as behave_executable
#
# # Define el comando que se ejecutará en la terminal
# command_args = ['behave',
#                 '--format', 'pretty',
#                 '--no-capture',
#                 '--tags', 'not @wip',
#                 '--logging-level', 'INFO',
#                 '--no-capture-stderr',
#                 '--junit',
#                 '--junit-directory', 'reports',
#                 '--stop',
#                 'features/']
#
# # Ejecuta el comando usando el runner Behave
# behave_executable.main(command_args)


import subprocess

if __name__ == '__main__':
    # command line args along with error capture on failure with check true
    s = subprocess.run('behave', shell=True, check=True)
