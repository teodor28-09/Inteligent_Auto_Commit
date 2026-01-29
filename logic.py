import subprocess


class AutoCommit:
    def __init__(self,repo):
        self.repo = repo

    def git(self,cmd):
        return subprocess.run(
            ["git"] + cmd,
            cwd=self.repo,
            capture_output=True,
            text=True
        )

    def is_modified(self):
        res = self.git(["status"]).stdout
        if "modified" in res:
            return True #este modificat
        else :
            return False #nu este modificat

    def auto_commit(self):
        if self.is_modified() == True:
            print(self.git(["add", "."]).stdout)
            print(self.git(["commit", "-m", "Auto Commit"]).stdout)
            print(self.git(["push"]).stdout)
            print("Auto Commit")
        else:
            print("Up to date")


repos = "/home/teodor/Git_Test"
git = AutoCommit(repos)

git.auto_commit()