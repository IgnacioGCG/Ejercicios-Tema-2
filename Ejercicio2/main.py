class Conversacion:
    def __init__(self, texto):
        """Inicializa la conversación con el texto en bruto."""
        self.texto = texto
        self.partes = self.texto.split("#")  # Dividimos el texto en fragmentos
    
    def formatear(self):
        """Formatea el texto en una conversación legible."""
        conversacion = [self.partes[0].capitalize() + "..."]  # Primera frase con "..."
        
        for linea in self.partes[1:]:
            conversacion.append(linea.capitalize() + ".")  # Capitaliza y añade punto final
        
        return "\n\n".join(conversacion)  # Une con saltos de línea para legibilidad
    
    def mostrar(self):
        """Imprime la conversación formateada."""
        print(self.formatear())

# Texto original
texto_original = ("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje"
                  "#lo que se mueve es el viento -respondió otro monje"
                  "#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")

# Crear una instancia de la clase y mostrar el resultado
conversacion = Conversacion(texto_original)
conversacion.mostrar()
