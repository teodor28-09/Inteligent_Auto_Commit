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
        res = self.git(["status","--porcelain"])
        return bool(res.stdout.strip())

    def auto_commit(self):
        if self.is_modified():
            print(self.git(["add", "."]).stdout)
            commit = self.git(["commit", "-m", "Auto Commit"])
            push = self.git(["push"])

            print(commit.stdout)
            print(push.stdout)

            if commit.returncode != 0 or push.returncode != 0:
                raise RuntimeError("Git commit or push failed")
            print("Auto Commit")
            return True
        else:
            print("Up to date")
            return False



def notify(title, message):
    subprocess.run(["notify-send", title, message])