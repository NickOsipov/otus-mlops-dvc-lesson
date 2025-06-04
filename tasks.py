from dotenv import load_dotenv
from invoke import task


load_dotenv()

@task
def setup(ctx):
    """Install dependencies."""
    ctx.run("uv python install 3.11.11", pty=True)
    ctx.run("uv sync", pty=True)

@task
def test(ctx):
    """Run tests."""
    ctx.run("echo $TEST_ENV")

@task
def setup_dvc(ctx):
    """Setup DVC."""
    ctx.run("bash setup-dvc.sh", pty=True)