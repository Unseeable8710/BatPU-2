from compiler import compile_bc
from assembler import assemble
from schematic import make_schematic

def main():
  program = input('Enter the filename (without the extension): ')
    
  bat_filename = f'programs/{program}.bc'
  as_filename = f'programs/{program}.as'
  mc_filename = f'programs/{program}.mc'
  schem_filename = f'programs/{program}program.schem'

  compile_bc(bat_filename, as_filename)
  assemble(as_filename, mc_filename)
  make_schematic(mc_filename, schem_filename)

if __name__ == '__main__':
  main()