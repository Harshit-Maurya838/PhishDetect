import pandas as pd
import os

def prepare_data():
    print("Loading raw datasets... (This might take a few seconds for 1M rows)")
    
    # 1. Load the raw data
    phish_df = pd.read_csv('../data/raw/phishtank.csv')
    legit_df = pd.read_csv('../data/raw/legitimate.csv')

    # Drop any random empty rows just to be safe
    phish_df = phish_df.dropna(subset=['url'])
    legit_df = legit_df.dropna(subset=['url'])

    # 2. The Undersampling Fix
    num_phish = len(phish_df)
    print(f"Found {num_phish} phishing URLs. Sampling legitimate URLs to match...")
    
    # We randomly grab 'num_phish' amount of rows from the 1 million legitimate URLs
    legit_sampled = legit_df.sample(n=num_phish, random_state=42)

    # 3. Isolate and Label Phishing Data
    phish_clean = pd.DataFrame()
    phish_clean['url'] = phish_df['url']
    phish_clean['label'] = 1

    # 4. Isolate, Fix, and Label Legitimate Data
    legit_clean = pd.DataFrame()
    # The hotfix to append 'https://' to domains that are missing it
    legit_clean['url'] = legit_sampled['url'].apply(lambda x: f"https://{x}" if not str(x).startswith('http') else x)
    legit_clean['label'] = 0

    # 5. Concatenate and Shuffle
    print("Merging and shuffling datasets...")
    master_df = pd.concat([phish_clean, legit_clean], ignore_index=True)
    master_df = master_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # 6. Save the processed master dataset
    output_path = '../data/processed/master_dataset.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    master_df.to_csv(output_path, index=False)
    
    print(f"Success! Master dataset saved to {output_path}")
    print(f"Total balanced rows ready for training: {len(master_df)}")

if __name__ == "__main__":
    prepare_data()