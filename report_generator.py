import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models?sort=downloads"
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json()
        top_models = models[:10]
        return top_models
    else:
        raise Exception("Failed to fetch data from Hugging Face API")

def generate_report(models):
    report = "Top 10 Downloaded Models on Hugging Face:\n\n"
    for i, model in enumerate(models, 1):
        report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n"
    return report

def save_report(report):
    with open("top_models_report.txt", "w") as file:
        file.write(report)

def main():
    top_models = fetch_top_models()
    report = generate_report(top_models)
    save_report(report)
    print("Report generated and saved as 'top_models_report.txt'.")

if __name__ == "__main__":
    main()
