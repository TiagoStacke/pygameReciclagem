import cx_Freeze
executables = [cx_Freeze.Executable(
    script = "reciclagem.py", icon = "imagens/lixeira.ico")]

cx_Freeze.setup(
    name = "Jogo da Reciclagem: Os pneus mortais!",
    options = {"build_exe": {
        "packages":["pygame"],
        "include_files":["imagens"]
    }},
    executables = executables
)
