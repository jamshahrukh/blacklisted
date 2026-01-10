import importlib
import sys

MENU = {
    1: ("tool", "main_menu", "Main Tool"),
    2: ("tool1", "main", "Tool 1"),
    3: ("tool2", "main_jam", "Tool 2"),
    4: ("tool3", "main", "Tool 3"),
    5: ("tool4", "main", "Tool 4"),
    6: ("tool5", "main", "Tool 5"),
    7: ("tool6", "main", "Tool 6"),
    8: ("tool7", "main", "Tool 7"),
    9: ("tool8", "main", "Tool 8"),
    10: ("tool9", "main", "Tool 9"),
    11: ("tool10", "main", "Tool 10"),
}

def main():
    print("\n======= TOOL MENU =======\n")

    for num, (_, _, name) in MENU.items():
        print(f"[{num}] {name}")

    try:
        choice = int(input("\nSelect option (1–11): ").strip())
    except ValueError:
        print("❌ Please enter a number")
        sys.exit(1)

    if choice not in MENU:
        print("❌ Invalid selection")
        sys.exit(1)

    module_name, func_name, _ = MENU[choice]

    try:
        module = importlib.import_module(module_name)
        getattr(module, func_name)()
    except Exception as e:
        print(f"❌ Failed to run {module_name}")
        print(e)

if __name__ == "__main__":
    main()
