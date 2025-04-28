import sys

lines = []
# check if file is valid
try:
    if len(sys.argv) < 2:
        print("Usage: python3 interpreter.py <filename.txt>")
        sys.exit(1)
    fileName = sys.argv[1]
    with open(fileName, 'r', encoding='utf-8') as file:
        raw_lines = file.read().split("\n")

    # Filter out empty lines
    lines = [line for line in raw_lines if line.strip()]

except Exception as e:
    print(f"Error while opening or reading file:\n{e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

stack = []
pc = 0  # Program Count


def err(message):
    """Prints an error message with the current line number and exits."""
    print(f"\nError on line {pc + 1}: {message}")
    sys.exit(1)


def pop(index=-1):
    """Pops a value from the stack. Handles underflow."""
    if not stack:
        err("Stack underflow - cannot pop from empty stack.")
    try:
        # Only allow reg pop from the top
        if index != -1:
            err(f"Invalid index for pop: {index}. Only popping from top is standard.")
        return stack.pop(index)
    except IndexError:
        # if stack is empty
        err("Internal error during pop.")


print(f"--- Running {fileName} ---")

while 0 <= pc < len(lines):
    current_pc_for_error = pc  # Capture pc before execution/potential jump
    line = lines[pc]
    parts = line.split(" ")
    instr = parts[0].upper()  # converts to uppercase either way

    try:
        # Syntax
        if instr == "SHYIRAMO":
            if len(parts) < 2:
                err(f"Missing argument for SHYIRAMO")
            try:
                stack.append(int(parts[1]))
            except ValueError:
                err(f"Invalid number argument for SHYIRAMO: {parts[1]}")

        elif instr == "KURAMO":
            pop()

        elif instr == "DUPRIKASIYO":
            val = pop()
            stack.append(val)
            stack.append(val)

        elif instr == "HINDURA":
            if len(stack) < 2:
                err(f"Stack underflow - HINDURA requires at least two items.")
            a = pop()
            b = pop()
            stack.append(a)
            stack.append(b)

        elif instr == "TERANYA":
            if len(stack) < 2:
                err(f"Stack underflow - TERANYA requires at least two items.")
            a = pop()
            b = pop()
            stack.append(b + a)

        elif instr == "GABANYA":
            if len(stack) < 2:
                err(f"Stack underflow - GABANYA requires at least two items.")
            a = pop()
            b = pop()
            stack.append(b - a)

        elif instr == "KUBA":
            if len(stack) < 2:
                err(f"Stack underflow - KUBA requires at least two items.")
            a = pop()
            b = pop()
            stack.append(b * a)

        elif instr == "SOMA":
            try:
                char_input = sys.stdin.read(1)
                if char_input:
                    stack.append(ord(char_input))
                else:
                    stack.append(0)  # Push 0 on EOF
            except Exception as e:
                err(f"Error during input for SOMA: {e}")

        elif instr == "ANDIKA_INYUGUTI":
            val = pop()
            try:
                print(chr(val), end="", flush=True)
            except ValueError:
                err(f"Invalid ASCII value for ANDIKA_INYUGUTI: {val}")

        elif instr == "ANDIKA_UMUBARÉ":
            val = pop()
            try:
                print(int(val), end="", flush=True)
            except ValueError:
                err(f"Invalid value for ANDIKA_UMUBARÉ (must be number): {val}")

        # JMP
        elif instr == "SIMBUKA":
            if len(parts) < 2:
                err(f"Missing Line Number argument for SIMBUKA")
            try:
                target_line_1_based = int(parts[1])
                target_pc = target_line_1_based - 1  # Convert to 0-based index
                if not (0 <= target_pc < len(lines)):
                    print(f"\nError on line {current_pc_for_error + 1}: Invalid jump target {target_line_1_based} for SIMBUKA. Must be between 1 and {len(lines)}.")
                    sys.exit(1)
                pc = target_pc
                continue  # Skip the pc inc
            except ValueError:
                err(f"Invalid line number argument for SIMBUKA: '{parts[1]}'")

        elif instr == "SIMBUKA_UBUSA":
            if len(parts) < 2:
                err(f"Missing Line Number argument for SIMBUKA_UBUSA")
            val = pop()
            if val == 0:
                try:
                    target_line_1_based = int(parts[1])
                    target_pc = target_line_1_based - 1  # Convert to 0-based index
                    if not (0 <= target_pc < len(lines)):
                        print(f"\nError on line {current_pc_for_error + 1}: Invalid jump target {target_line_1_based} for SIMBUKA_UBUSA. Must be between 1 and {len(lines)}.")
                        sys.exit(1)
                    pc = target_pc
                    continue  # Skip the pc inc
                except ValueError:
                    err(f"Invalid line number argument for SIMBUKA_UBUSA: '{parts[1]}'")
            

        elif instr == "HAGARARA":
            break  # Exits

        else:
            # Handle if instruction is not found
            err(f"Unknown instruction: '{instr}'")

    # Debugging for annoying errors
    except SystemExit:
        raise  #
    except Exception as e:
        print(f"\nRuntime error on line {current_pc_for_error + 1} during instruction '{instr}': {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # inc pc
    pc += 1


print('\n--- Execution finished ---')
