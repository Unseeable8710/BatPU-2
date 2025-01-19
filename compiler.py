import sys

def compile_bc(batcode_filename, assembly_filename):
  batcode_file = open(batcode_filename, 'r')
  assembly_file = open(assembly_filename, 'w')
  lines = (line.strip() for line in assembly_file)

  # Remove comments and blanklines
  for comment_symbol in ['//', '/', '#']:
    lines = [line.split(comment_symbol)[0] for line in lines]
  lines = [line for line in lines if line.strip()]
  opcodes = ['nop', 'hlt', 'add', 'sub', 'nor', 'and', 'xor', 'rsh', 'ldi', 'adi', 'jmp', 'brh', 'cal', 'ret', 'lod', 'str']

  # Populate Batcode symbol table

  symbols = {}

  operations = ['null', 'stop()', '+', '-', '!||', '&&', '|', '', 'loadimm()', '<<', '++', 'jump()', 'branch()', 'call()', 'return()', 'load()', 'store()']
  for index, symbol in enumerate(operations):
    symbols[symbol] = index
  
  registers = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15']

  # Populate assembly symbol table
  as_symbols = {}

  opcodes = ['nop', 'hlt', 'add', 'sub', 'nor', 'and', 'xor', 'rsh', 'ldi', 'adi', 'jmp', 'brh', 'cal', 'ret', 'lod', 'str']
  for index, symbol in enumerate(opcodes):
    as_symbols[symbol] = index
  
  regs = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
  for index, symbol in enumerate(regs):
    as_symbols[symbol] = index
  
  condition1 = 'z'
  condition2 = 'nz'
  condition3 = 'c'
  condition4 = 'nc'
  for index, symbol in enumerate(condition1):
    as_symbols[symbol] = index
  for index, symbol in enumerate(condition2):
    as_symbols[symbol] = index
  for index, symbol in enumerate(condition3):
    as_symbols[symbol] = index
  for index, symbol in enumerate(condition4):
    as_symbols[symbol] = index

