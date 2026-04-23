import json
import os


with open("reflection-tree.json", "r") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}


state = {
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"others": 0, "self": 0},
    "answers": {}
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def record_signal(signal):
    if not signal:
        return
    axis, pole = signal.split(":")
    state[axis][pole] += 1

def get_dominant(axis):
    scores = state[axis]
    winner = max(scores, key=scores.get)
    return winner

def interpolate(text):
    # Replace {A1_Q1.answer}
    for node_id, answer in state["answers"].items():
        text = text.replace("{" + node_id + ".answer}", answer)
    # Replace {axis1.dominant} etc
    for axis in ["axis1", "axis2", "axis3"]:
        dominant = get_dominant(axis)
        text = text.replace("{" + axis + ".dominant}", dominant)
    return text

def fill_summary_labels(node, text):
    if "dominantLabels" not in node:
        return text
    labels = node["dominantLabels"]
    for axis, poles in labels.items():
        dominant = get_dominant(axis)
        label = poles.get(dominant, dominant)
        text = text.replace("{" + axis + ".dominant}", label)
    for node_id, answer in state["answers"].items():
        text = text.replace("{" + node_id + ".answer}", answer)
    return text

def press_enter():
    input("\n  [ Press Enter to continue ] ")

def print_banner():
    print("\n" + "="*55)
    print("       DAILY REFLECTION TREE")
    print("="*55)


def run_start(node):
    clear()
    print_banner()
    print(f"\n  {node['text']}\n")
    press_enter()
    return node["next"]

def run_question(node):
    clear()
    print_banner()
    print(f"\n  {node['text']}\n")
    options = node["options"]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt['label']}")
    print()
    while True:
        try:
            choice = int(input("  Your answer (enter number): "))
            if 1 <= choice <= len(options):
                selected = options[choice - 1]
                state["answers"][node["id"]] = selected["label"]
                record_signal(selected.get("signal"))
                return selected["next"]
            else:
                print(f"  Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("  Please enter a valid number.")

def run_decision(node):
    for condition in node["conditions"]:
        expr = condition["if"]
        # Parse "axis1.internal > axis1.external" style conditions
        parts = expr.split()
        left_val  = eval_expr(parts[0])
        operator  = parts[1]
        right_val = eval_expr(parts[2])
        if operator == ">" and left_val > right_val:
            return condition["next"]
        if operator == ">=" and left_val >= right_val:
            return condition["next"]
    return node["conditions"][-1]["next"]

def eval_expr(expr):
    axis, pole = expr.split(".")
    return state[axis][pole]

def run_reflection(node):
    clear()
    print_banner()
    text = interpolate(node["text"])
    print(f"\n  {text}\n")
    press_enter()
    return node["next"]

def run_bridge(node):
    clear()
    print_banner()
    print(f"\n  ── {node['text']} ──\n")
    press_enter()
    return node["next"]

def run_summary(node):
    clear()
    print_banner()
    print("\n  YOUR REFLECTION SUMMARY\n")
    print("  " + "-"*45)

    # Print axis scores
    for axis in ["axis1", "axis2", "axis3"]:
        dominant = get_dominant(state[axis] if isinstance(state[axis], dict) else {})
        scores = state[axis]
        print(f"\n  {axis.upper()}: {scores}")

    print("\n  " + "-"*45)
    text = fill_summary_labels(node, node["text"])
    print(f"\n  {text}\n")
    print("  " + "-"*45)
    press_enter()
    return node["next"]

def run_end(node):
    clear()
    print_banner()
    print(f"\n  {node['text']}\n")
    print("="*55 + "\n")


def run():
    current_id = "START"

    while current_id:
        node = nodes[current_id]
        node_type = node["type"]

        if node_type == "start":
            current_id = run_start(node)
        elif node_type == "question":
            current_id = run_question(node)
        elif node_type == "decision":
            current_id = run_decision(node)
        elif node_type == "reflection":
            current_id = run_reflection(node)
        elif node_type == "bridge":
            current_id = run_bridge(node)
        elif node_type == "summary":
            current_id = run_summary(node)
        elif node_type == "end":
            run_end(node)
            break
        else:
            print(f"Unknown node type: {node_type}")
            break

if __name__ == "__main__":
    run()
