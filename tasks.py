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

@task
def add_train_stage(ctx):
    """Add train stage to DVC."""
    ctx.run(
        "dvc stage add -n train -d train.py -d data -o models/model.joblib -M metrics.csv python3 train.py"
    )
