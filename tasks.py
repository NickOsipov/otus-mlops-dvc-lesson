from invoke import task


@task
def setup(ctx):
    """Install dependencies."""
    ctx.run("uv python install 3.11.11", pty=True)
    ctx.run("uv sync", pty=True)