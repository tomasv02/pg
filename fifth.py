
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
    with open(file_name, "rb") as file_name: 
        header_length = file_name.read(8) #přečte prvních 8 bajtů z hlavičky souboru [.jpeg = 3 bytes; .gif = 6 bytes; .png = 8 bytes]

    return header_length


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))

    if jpeg_header in header:  #vyhodnoť zda je soubor jpeg
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
    if gif_header1 in header: #vyhodnoť zda je soubor gif
        return True
    elif gif_header2 in header: #vyhodnoť zda je soubor gif2
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
    if png_header in header: #vyhodnoť zda je soubor png
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
    try: 
        file_name = sys.argv[1]
        print_file_type(file_name)

    except FileNotFoundError:
        print(f'Soubor {sys.argv[1]} nenalezen.')

    except Exception:
        print("Byla vyvolána výjimka")
   