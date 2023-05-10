"""
Main module for the Metamaterial Analysis Code (MAC) package. It represents the whole analysis.
"""

from os import remove

from .MACModel import MACModel
from .MACGlobals import MAC_VERSION
from datetime import date


class MACAnalysis:
    """
    Main class for the Metamaterial Analysis Code (MAC) package. It represents the whole analysis.

    Attributes:
        Model: MACModel of the model
        Subcases:
        LoadCases:
        Parameters:
    """

    def __init__(self, model: MACModel, subcases: list, loadcases: list, parameters: list):
        """
        Constructor for MACAnalysis class
        """
        self.__model = model
        self.__subcases = subcases
        self.__loadcases = loadcases
        self.__parameters = parameters

    def write_fem(self, path: str) -> None:
        """
        Writes the .fem file for the analysis in the specified path. It overwrites the file if it already exists.
        """

        if path[-4:] != ".fem":
            path += ".fem"

        if path.exists(path):
            remove(path)
            print(f"File {path} already exists. It has been overwritten.")

        today = date.today().strftime("%d/%m/%Y")
        analysis_name = path.split("\\")[-1].split(".")[0]
        macverlen = 79 - (len(MAC_VERSION) + len("# MAC version: "))
        analysis_namelen = 79 - (len(analysis_name) + len("# Analysis Name: "))

        header = "#" * 80 + "\n" + \
                 "#" * 13 + "  File generated by Metamaterial Analysis Code (MAC)  " + "#" * 13 + "\n" + \
                 "#" * 80 + "\n" + \
                 "#" + " " * 78 + "#" + "\n" + \
                 "# Escuela Tecnica Superior de Ingenieria Aeronautica" + " " * 27 + "#" + "\n" + \
                 "#" + " " * 78 + "#" + "\n" + \
                 f"# MAC version: {MAC_VERSION}" + " " * macverlen + "#" + "\n" + \
                 "#" + " " * 78 + "#" + "\n" + \
                 f"# Date: {today}" + " " * 61 + "#" "\n" + \
                 "#" + " " * 78 + "#" + "\n" + \
                f"# Analysis Name: {analysis_name}" + " " * analysis_namelen + "#" + "\n" + \
                 "#" + " " * 78 + "#" + "\n" + \
                 "#" * 80 + "\n"

        with open(path, "a") as w:
            w.writelines(header)
            w.writelines(str(self.__subcases))
            w.writelines(str(self.__loadcases))
            w.writelines(str(self.__parameters))

        # Write model calling the model method. header=False to avoid writing the header again.
        self.__model.write_fem(path, writeheader=False)


def set_analysis(model: MACModel, subcases: list, loadcases: list, parameters: list) -> MACAnalysis:
    """
    Function to set the analysis. It returns a MACAnalysis object.
    """
    analysis = MACAnalysis(model, subcases, loadcases, parameters)

    return analysis
