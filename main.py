
import rich
from rich.console import Console # library to console in terminal
from rich.table import Table # library for table in terminal

def main():
    
    while True:
        
        console = Console()
        table = Table(title="Encode or Decode")
        table.add_column("OPTION 1", style="steel_blue1")
        table.add_column("OPTION 2", style="sea_green1")
        table.add_row("Encode", "Decode")
        console.print(table)
        
        option = input("Enter the option: ")
        
        if option == '1':            
            table = Table(title="Methods")
            table.add_column("OPTION A", style="khaki1")
            table.add_column("OPTION B", style="khaki1")
            table.add_column("OPTION C", style="khaki1")
            table.add_column("OPTION D", style="khaki1")
            table.add_row("Golomb", "Elias-Gamma", "Fibonacci", "Huffman")
            console.print(table)
            
            option_encode = input("Choose an option to encode: ")
            
            if option_encode == 'A':
                print('Golomb')
            elif option_encode == 'B':
                print('Elias-Gamma')
            elif option_encode == 'C':
                print('Fibonacci')
            elif option_encode == 'D':
                print('Huffman')
            else:
                print('[bold red]Invalid Option![/bold red]') 
            
        elif option == '1': 
            option_decode = input("Choose an option to decode: ")
            
            if option_decode == 'A':
                print('Golomb')
            elif option_decode == 'B':
                print('Elias-Gamma')
            elif option_decode == 'C':
                print('Fibonacci')
            elif option_decode == 'D':
                print('Huffman')
            else:
                print('[bold red]Invalid Option![/bold red]')
            
        else:
            print('[bold red]Invalid Option![/bold red]')
    
if __name__ == '__main__':
    main()