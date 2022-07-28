from flask import Flask

app= Flask(__name__)

#criar a 1ª pagina do site
#route -> linkdosite.com/  
#função -> o que você quer exibir naquela página
@app.route("/")
def homepage():
    return "Esse é meu primeiro site"

#colocar o site no ar
app.run()