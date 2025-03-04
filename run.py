from app import create_app #nos traemos lo de la carpeta de app, desde el init

app=create_app()

if __name__ == "__main__":
    app.run(debug=True) #corremos la aplicacion, poniendo el debug para que nos enseñe los errores, la pinche exibisionista esa