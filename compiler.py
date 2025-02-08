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

  # Populate symbol table

  symbols = {}

  operations = ['null', 'stop()', '+', '-', '!||', '&&', '|', '', 'loadimm()', '<<', '++', 'jump()', 'branch()', 'call()', 'return()', 'load()', 'store()', 'print()', 'clear()']
  for index, symbol in enumerate(operations):
    symbols[symbol] = index
  
  registers = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8','r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
  for index, symbol in enumerate(registers):
    symbols[symbol] = index
  
  condition1 = 'zero'
  condition2 = '!zero'
  condition3 = 'carry'
  condition4 = '!carry'
  for index, symbol in enumerate(condition1):
    symbols[symbol] = index
  for index, symbol in enumerate(condition2):
    symbols[symbol] = index
  for index, symbol in enumerate(condition3):
    symbols[symbol] = index
  for index, symbol in enumerate(condition4):
    symbols[symbol] = index

  ports = ['pixel_x', 'pixel_y', 'draw_pixel', 'clear_pixel', 'load_pixel', 'buffer_screen', 'clear_screen_buffer', 'write_char', 'buffer_chars', 'clear_chars_buffer', 'show_number', 'clear_number', 'signed_mode', 'unsigned_mode', 'rng', 'controller_input']
  for index, symbol in enumerate(ports):
    as_symbols[symbol] = index + 240

  # Extract definitions and labels

  def is_definition(word):
    return word == ('var' or 'const') 

  def is_label(word):
    return word == 'function'

  pc = 0
  instructions = []

  for index, line in enumerate(lines):
    words = [word.lower() for word in line.split()]

    if is_definition(words[0]):
      symbols[words[1]] = int(words[2])
    elif is_label(words[0]):
      symbols[words[0]] = pc
      if len(words) > 1:
        pc += 1
        instructions.append(words[1:])
    else:
      pc += 1
      instructions.append(words)

  # Generate assembly code
    
  def resolve(word):
    if word[0] in '-0123456789':
      return int(word, 0)
    if symbols.get(word) is None:
      exit(f'Could not resolve {word}')
    return symbols[word]

  for pc, words in enumerate(instructions):
    # Resolve psuedo-instructions
    if words[0] == '':
      words
