import subprocess as cmd

def git_push_automation():
    try:
        cp = cmd.run(".", check=True, shell=True)
        print("cp", cp)

        cmd.run('pip freeze > requirements.txt', check=True, shell=True)
        cmd.run('python manage.py test', check=True, shell=True)
        print("Done running tests!"              )

        cmd.run('git add .', check=True, shell=True)

        commit_message = input('Enter commit message: ')
        commit_message = f'git commit -m "{commit_message}"'
        cmd.run(commit_message, check=True, shell=True)

        branch_name = input('Enter branch name: ')
        push = f'git push origin {branch_name}'

        print(f"Pushing to {branch_name} branch ...")

        cmd.run(push, check=True, shell=True)

        print(f"Successfully Pushed to {branch_name} branch")
        return True
    except:
        print("Error git automation")
        return False

if __name__ == '__main__':
    git_push_automation()