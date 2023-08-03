import os
import webbrowser

# Crie uma pasta para o site
os.mkdir("website")

# Crie um arquivo index.html na pasta
with open("website/index.html", "w") as f:
    f.write("<html>\n<head>\n<title>Meu site</title>\n</head>\n<body>\n<h1>Olá, mundo!</h1>\n</body>\n</html>")

# Crie um arquivo css para o site
with open("website/style.css", "w") as f:
    f.write("body { font-family: sans-serif; }\n")

# Crie um arquivo 404.html para o site
with open("website/404.html", "w") as f:
    f.write("<html>\n<head>\n<title>404 Not Found</title>\n</head>\n<body>\n<h1>Página não encontrada</h1>\n</body>\n</html>")

# Crie um arquivo robots.txt para o site
with open("website/robots.txt", "w") as f:
    f.write("User-agent: *\nDisallow: /")

# Abra o site no navegador
webbrowser.open("http://localhost:8000/")
