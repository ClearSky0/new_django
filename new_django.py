import os

root = input("\n\nLocation for new Django Project?\n"
    "(NB. This is the directory above the project directory, current '.' is default) ") or '.'
try:
    os.chdir(root)
except Exception as e:
    print(e)
    exit()

project = input("\n\nWhat is the name for the new project? ")
try:
    os.mkdir(project)
except FileExistsError:
    print(f"\n\nWarning '{project}' already exists, in '{root}'.")
    check = input("Continue anyway? (y/n)")
    if check.lower() != 'y':
        exit()
except Exception as e:
    print(e)
    exit()

try:
    os.chdir(project)
except Exception as e:
    print(e)
    exit()

project_folder = os.getcwd()
print(f"\nProject folder created at: {project_folder}")

app = input(f"\n\nWhat is the name of the first app within '{project}'?\n"
    "('core' will be created regardless, blank for none) ")
if app == '':
    app_command = '@echo Not creating an app'
else:
    app_command = f'python manage.py startapp {app}'

all_auth_required = input("\n\nDo you want All_Auth installing? (y/n) ")
if all_auth_required.lower() == 'y':
    install_aa = 'pip install django-allauth'
else:
    install_aa = ''

command = 'python -m venv venv' # Create the virtual env
try:
    print('\n', '*' * 5, 'Running', '*' * 5, '\n\t', command, '\n\n')
    os.system(command)
except Exception as e:
    print(e)
    exit()

activate = 'venv\\Scripts\\activate' # Activate the venv
try:
    print('\n', '*' * 5, 'Running', '*' * 5, '\n\t', activate, '\n\n')
    os.system(activate)
except Exception as e:
    print(e)
    exit()

commands = [
    'python -m pip install --upgrade pip', # Upgrade pip
    'pip install django', # Install Django
    install_aa, # All_Auth if required
    'copy ' + os.path.dirname(os.path.abspath(__file__)) + '\.gitignore .', # Copy .gitignore 
    'pip freeze > requirements.txt', # Freeze as is to create requirements file
    'django-admin.exe startproject core .', # start the project with core, for settings
    app_command, # start the project with the frontend app of the dev's choice
    'python manage.py migrate', # start the database
    'git init', # Initialise git
    f'code {project_folder}', # open vscode in the project folder
    # 'python manage.py runserver', # run the server
]

# Subsequent commands need to have the venv activated as each call to os.system is a new cmd shell

for command in commands:
    if command:
        command = activate + ' & ' + command
        try:
            print('\n', '*' * 5, 'Running', '*' * 5, '\n\t', command, '\n\n')
            os.system(command)
            # process = subprocess.run(command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            # print(process.stdout)

        except Exception as e:
            print(e)
            exit()
