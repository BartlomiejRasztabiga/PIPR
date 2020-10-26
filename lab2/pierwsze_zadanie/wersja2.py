import sys

"""

łóręm ipśum ðółór śit ąmęt, ćóńśęćtętur ąðipiśćińg ęłit, śęð ðó ęiuśmóð tęmpór
ińćiðiðuńt ut łąbórę ęt ðółórę mągńą ąłiquą. Ut ęńim ąð mińim vęńiąm, quiś
ńóśtruð ęxęrćitątióń ułłąmćó łąbóriś ńiśi ut ąłiquip ęx ęą ćómmóðó ćóńśęquąt.
ðuiś ąutę irurę ðółór iń rępręhęńðęrit iń vółuptątę vęłit ęśśę ćiłłum ðółórę
ęu fugiąt ńułłą pąriątur. ęxćęptęur śińt óććąęćąt ćupiðątąt ńóń próiðęńt, śuńt
iń ćułpą qui óffićią ðęśęruńt mółłit ąńim ið ęśt łąbórum.

śęð ut pęrśpićiątiś uńðę ómńiś iśtę ńątuś ęrrór śit vółuptątęm ąććuśąńtium
ðółóręmquę łąuðąńtium, tótąm ręm ąpęriąm, ęąquę ipśą quąę ąb iłłó ińvęńtórę
vęritątiś ęt quąśi ąrćhitęćtó bęątąę vitąę ðićtą śuńt ęxpłićąbó. ńęmó ęńim ipśąm
vółuptątęm quią vółuptąś śit ąśpęrńątur ąut óðit ąut fugit, śęð quią ćóńśęquuńtur
mągńi ðółóręś ęóś qui rątióńę vółuptątęm śęqui ńęśćiuńt. ńęquę pórró quiśquąm
ęśt, qui ðółóręm ipśum quią ðółór śit ąmęt, ćóńśęćtętur, ąðipiśći vęłit, śęð quią
ńóń ńumquąm ęiuś móði tęmpórą ińćiðuńt ut łąbórę ęt ðółórę mągńąm ąłiquąm quąęrąt
vółuptątęm. Ut ęńim ąð mińimą vęńiąm, quiś ńóśtrum ęxęrćitątióńęm ułłąm ćórpóriś
śuśćipit łąbórióśąm, ńiśi ut ąłiquið ęx ęą ćómmóði ćóńśęquątur? Quiś ąutęm vęł
ęum iurę rępręhęńðęrit qui iń ęą vółuptątę vęłit ęśśę quąm ńihił mółęśtiąę
ćóńśęquątur, vęł iłłum qui ðółóręm ęum fugiąt quó vółuptąś ńułłą pąriątur?

Fuśćę tińćiðuńt ćómmóðó fęłiś vitąę ćómmóðó. ńąm vęhićułą ęłęmęńtum ńęquę. Iń
hęńðręrit łibęró śęð prętium fęrmęńtum. ńąm ułłąmćórpęr ąłiquęt ąłiquąm. Mąuriś
fąćiłiśiś, łigułą ą ćóńśęćtętur śóðąłęś, óðió ęrąt ðigńiśśim quąm, śęð łućtuś
ðółór urńą quiś mąuriś.
"""


def die(why: str, exit_code: int = 1) -> None:
    """
    Print `why` msg and close program with return value `exit_code`.

    Args:
        why: Message which will be printed.
        exit_code: Exit value of program.
    """
    print(why, file=sys.stderr)
    sys.exit(exit_code)


def main():
    with open(__file__, "r") as file_handler:
        num_of_bytes = len(file_handler.read())

    if len(sys.argv) != 2:
        die("Usage: {} <number of lines>".format(sys.argv[0]))

    first_argument = sys.argv[1]
    if not first_argument.isnumeric():
        die("Provided argument must be an integer.")

    if int(first_argument) != num_of_bytes:
        die("Wrong guess!")
    else:
        print("Good job!")


if __name__ == "__main__":
    main()
