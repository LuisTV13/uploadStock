def read_Cred():
    objeto = {
        "BDF" : {
        "correo" : "alertas.stock.bdf@gmail.com",
        "password": "Invernalia@!",
      }
    }
    return objeto


def getCred(Corporativo):
    objeto  = read_Cred()
    correo  = objeto[Corporativo]["correo"]
    password  = objeto[Corporativo]["password"]

    return correo,password

