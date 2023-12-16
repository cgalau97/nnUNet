import json
import pandas as pd

def extract_summary_information(json_path: str) -> pd.DataFrame:
    """This functions extracts the information from foreground_mean and mean. Then, the infomration is stored in a dictionary"""

    # Read json file
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Extract information
    summary = {}
    summary["all_lesions"] = data['foreground_mean']
    summary["noSEL"] = data["mean"]["1"]
    summary["SEL"] = data["mean"]["2"]
    

    return summary

def metrics_creator(summary: dict, key: str) -> dict:
    """This function creates a dictionary with the metrics of recall, precision, f1-score and accuracy.
    We also return the DICE coefficient which is already a key field in the summary dictionary.
    
    Every summary contains the TN, TP, FN and FP as keys.
    """

    # Create dictionary
    metrics = {}

    # Calculate metrics
    metrics["recall"] = summary[key]["TP"] / (summary[key]["TP"] + summary[key]["FN"])
    metrics["precision"] = summary[key]["TP"] / (summary[key]["TP"] + summary[key]["FP"])
    metrics["f1_score"] = 2 * metrics["recall"] * metrics["precision"] / (metrics["recall"] + metrics["precision"])
    metrics["accuracy"] = (summary[key]["TP"] + summary[key]["TN"]) / (summary[key]["TP"] + summary[key]["TN"] + summary[key]["FP"] + summary[key]["FN"])
    metrics["dice"] = summary[key]["Dice"]

    return metrics


if __name__ == "__main__":
    # Path to json files
    json_path = "./data/summary.json"
    summary = extract_summary_information(json_path)

    # Extract metrics for SEL and noSEL
    
    metrics_SEL = metrics_creator(summary, "SEL")
    metrics_noSEL = metrics_creator(summary, "noSEL")
    print(f"SEL: {metrics_SEL}")
    print(f"Non SEL: {metrics_noSEL}")

    # All lesions
    metrics_all = metrics_creator(summary, "all_lesions")
    print(f"All lesions: {metrics_all}")

