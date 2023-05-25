"""
Module for running the .fem files in optistruct
"""
import subprocess


def run_optistruct(path: str) -> None:
    """
    Function that runs the .fem file using optistruct. It should be the same as given for MACAnalysis.write()
    """
    # Code that runs the .fem file using optistruct
    subprocess.run([r"C:\Program Files\Altair\2022-edu\hwsolvers\scripts\optistruct.bat", path])
