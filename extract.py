import subprocess
import json
import os
import lizard

def extract(filepath):
    analysis = lizard.analyze_file(filepath)
    functions = analysis.function_list
    avg_complexity = 0
    if functions: 
        avg_complexity = sum(f.cyclomatic_complexity for f in functions) / len(functions)

    try:
        cloc_cmd = ["cloc", "--json", filepath]
        cloc_out = subprocess.check_output(cloc_cmd)
        cloc_data = json.loads(cloc_out.decode("utf-8"))

        langs = [lang for lang in cloc_data.keys() if lang != "header"]
        lang = langs[0] if langs else "Unknown"
        code = cloc_data[lang]["code"]
        comments = cloc_data[lang]["comment"]

    except Exception as e:
        print(f"Error running cloc: {e}")
        lang, code, comments = "Unknown", 0, 0

    return {
        "file": os.path.basename(filepath),
        "language": lang,
        "loc": code,
        "comments": comments,
        "comment_ratio": comments / (code + 1),
        "avg_complexity": avg_complexity,
        "num_functions": len(functions)
    }