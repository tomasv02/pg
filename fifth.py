
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

#28.11.2024 VRBAT - implementation
def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    try:
        with open("kitten.jpeg", "rb") as file_name: #načtení prvních dvou bajtů z hlavičky bin souboru (definuje, o jaký formát se jedná)
            header_length = file_name.read(2)

    except FileNotFoundError:
        print("Soubor neexistuje")
    
    return header_length


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))
    if header == jpeg_header:  #vyhodnoť zda je soubor jpeg
        return True
    else:
        return False
  

def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    #.gif má dva standardy pro zápis formátu v bin
    header = read_header(file_name, len(gif_header1))
    if header == gif_header1: #vyhodnoť zda je soubor gif
        return True
    elif header == gif_header2: #vyhodnoť zda je soubor gif2
        return True
    else:
        return False
    


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    # vyhodnoť zda je soubor png
    header = read_header(file_name, len(png_header))
    if header == png_header_header: #vyhodnoť zda je soubor png
        return True
    else:
        return False


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    # přidej try-catch blok, odchyť obecnou vyjímku Exception a vypiš ji
    file_name = sys.argv[1]
    print_file_type(file_name)
