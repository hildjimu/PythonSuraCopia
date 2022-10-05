def generarHTML(tabla,nombreArchivo):
    html=tabla.to_html()
    archivo=open(nombreArchivo,"w")
    archivo.write(html)
    archivo.close()


    