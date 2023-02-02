from pelangiApp.pelangi import God,Interface

if __name__ == "__main__":
    god = God()
    ui = Interface(god)
    ui.start()