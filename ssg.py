import typer
from ssg.site import Site

def main(content, dist):
    config ={"source":source, "dest": dest}

    Site(**config).build()

typer.run(main)
