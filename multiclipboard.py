import sys, clipboard, json, os


os.system("cls")


SAVED_DATA = "multiclipboard.json"



def load_data() -> dict :
    
    try :
        with open(SAVED_DATA, "r") as my_file :
            data = json.load(my_file)
            return data

    except :

        with open(SAVED_DATA, "w") as my_file :
            
            my_file.write("{ }")

        load_data()



def save_data(data : dict) :
    with open(SAVED_DATA, "w") as my_file :
        json.dump(data, my_file)



def save(data : dict) :
    key = input("Digite uma chave para salvar o valor de sua clipboard: ")
    value = clipboard.paste()

    data[key] = value
    save_data(data)
    print("Dado salvo!")


def load(data : None):
    key = input("Qual chave você deseja pegar o valor? ")
    
    if key in load_data() :
        value = load_data()[key]

        clipboard.copy(value)
        print("Valor copiado para sua clipboard")

    else :
        print("Esse valor não existe entre os salvos")



def list(data : None) :

    for key, value in load_data().items() :
        print(f"O campo {key} tem o valor {value}")




if len(sys.argv) == 2 :

    commandsAccepted = ["save", "load", "list"]
    command = sys.argv[1]

    data = load_data()

    if command in commandsAccepted :
        globals()[command](data)

    else :
        print("Digite algum comando aceito, sendo esses: save, load e list")

else :
    print("Esse programa é feito para rodar por CLI. Tente rodar o arquivo utilizando algum desses parâmetros: save, load, list")