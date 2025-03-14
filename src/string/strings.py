class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = texto.replace(" ", "").lower()
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)
    
    def contar_consonantes(self, texto): # pendiente
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        consonantes = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
        return sum(1 for char in texto if char in consonantes)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()
        return sorted(texto1) == sorted(texto2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        return ' '.join(word.capitalize() for word in texto.split(' '))
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        palabras = texto.split(' ')
        palabras_sin_duplicados = [palabra for palabra in palabras if palabra != '']
        return ' '.join(palabras_sin_duplicados)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        try:
            int(texto)
            return True
        except ValueError:
            return False
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        cifrado = ""
        for char in texto:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                cifrado += chr((ord(char) - shift + desplazamiento) % 26 + shift)
            else:
                cifrado += char
        return cifrado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        for caracter in texto:
            if 'A' <= caracter <= 'Z':  # Mayúsculas
                nueva_letra = chr((ord(caracter) - ord('A') - desplazamiento) % 26 + ord('A'))
            elif 'a' <= caracter <= 'z':  # Minúsculas
                nueva_letra = chr((ord(caracter) - ord('a') - desplazamiento) % 26 + ord('a'))
            else:
                nueva_letra = caracter  # Otros caracteres no se modifican

        resultado += nueva_letra

        return resultado
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []
        len_texto = len(texto)
        len_subcadena = len(subcadena)

        for i in range(len_texto - len_subcadena + 1):
            if texto[i:i + len_subcadena] == subcadena:
                posiciones.append(i) 
        return posiciones