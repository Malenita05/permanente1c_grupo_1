#diccionario completo
web = {'https://ucsp.edu.pe/cs111/index.html': """<html>
<body>
<h1>Algoritmo CS111</h1>
<p>
Aqui encontraremos más información al respecto:
<ul>
<li> <a href="https://ucsp.edu.pe/cs111/pseudocodigo.html">Pseudocódigo</a>
<li> <a href="https://ucsp.edu.pe/cs111/implementacion.html">Implementación del algoritmo</a>
<li> <a href="https://ucsp.edu.pe/cs111/python.html">Documentación de Python</a>
</ul>
Podemos revisar comentarios adicional al respecto: 
<a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a> 
y <a href="https://ucsp.edu.pe/cs111/peter.html">Peter Norvig</a>.
</body>
</html>
""",

   'https://ucsp.edu.pe/cs111/peter.html': """<html>
<body>
<h1>Peter Norvig</h1>
<p>
Peter Norvig es un científico estadounidense, investigador en ciencias de la computación. Actualmente 
es director de investigación de la empresa Google. Ha publicado unos cincuenta artículos científicos 
sobre informática, en particular en el campo de la inteligencia artificial, el procesamiento automático 
del lenguaje natural , la recuperación de información y el diseño de software.
Con muchos años de expiencia en el lenguaje <a href="https://ucsp.edu.pe/cs111/python.html">Python</a>, 
creado por <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
</body>
</html>
""",

   'https://ucsp.edu.pe/cs111/guido.html': """<html>
<body>
<h1>Guido van Rossum</h1>
<p>
El es el creador de 
<a href="https://ucsp.edu.pe/cs111/python.html">Python</a>
</body>
</html>
""",

   'https://ucsp.edu.pe/cs111/python.html': """<html>
<body>
<h1>
Lenguaje de Programación Python
</h1>
<p>
<ol>
<li> Python 2.
<li> Python 3.
</ol>
</body>
</html>
""",

   'https://ucsp.edu.pe/cs111/implementacion.html': """<html>
<body>
<h1>
La Implementación del algoritmo
</h1>
<p>
<ol>
<li> En el siguiente link <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
<li> Cree las variables de manera correcta, siguiendo los estandares.
</ol>
</body>
</html>
""",

   'https://ucsp.edu.pe/cs111/pseudocodigo.html': """<html>
<body>
<h1>
Pseudocódigo
</h1>
<p>
<ol>
<li> 'https://ucsp.edu.pe/cs111/implementacion.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
</ol>
</body>
</html>
"""}

#diccionario reducido 
h=[]
r=[]
j=[]
for i,v in web.items():
   f=v.split('"')
   h.append(f)
   j.append(i)
for p in h:
   for x in p:
      if "https" in x:
         pass
      else:
         p.remove(x)
   r.append(p)
web2={j[i]:str(r[i])for i in range(len(j))}

#usando el diccionario reducido
#codigo
#variables 
r = [] #lista para almacenar los datos del rank y la pagina
#dar el rango a cada pagina
for x,y in web2.items(): 
    e = 0 #varible 
    s = y.count("https")+1
    #hallar las entrantes
    for i,t in web2.items(): 
        j = t.count(x)
        e += j
    #evitar el error de la divicion en 0
    rank = round(e/s,1)
    r.append([rank,x,e,s])
#ordenar e invertit lista
a = sorted(r)[::-1]
print("\n########usando el diccionario reducido#######")
print("\n\t\t############Ranking##############")
#imprimir en patalla
for i in range(10): 
    try: 
        print(f"{i+1}.- entrantes = {a[i][2]}, saliente = {a[i][3]}  puntaje: {a[i][0]} ----- url: {a[i][1]}")
    except IndexError:
        break