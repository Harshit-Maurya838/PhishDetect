import pandas as pd
import re
from urllib.parse import urlparse
import os

def check_features(url):
    # Initialize our dictionary to hold the 6 feature values
    features = {}
    
    # Convert to string just in case pandas grabbed a null/float value
    url = str(url)
    
    # Safely isolate the domain using Python's built-in URL parser
    try:
        domain = urlparse(url).netloc
        if not domain:
            domain = url.split('/')[2] if '//' in url else url.split('/')[0]
    except:
        domain = ""

    # 1. Have_IP
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        features['Have_IP'] = 1
    else:
        features['Have_IP'] = 0
        
    # 2. URL_Length (Paper flags URLs longer than 54 characters)
    if len(url) > 54:
        features['URL_Length'] = 1
    else:
        features['URL_Length'] = 0
        
    # 3. Redirection (Checks if '//' appears past the 7th character)
    if url.rfind('//') > 7: 
        features['Redirection'] = 1
    else:
        features['Redirection'] = 0
        
    # 4. HTTPS_Domain (Checks if 'http' or 'https' is in the domain part)
    if 'http' in domain:
        features['https_Domain'] = 1
    else:
        features['https_Domain'] = 0
        
    # 5. TinyURL (Checks against common URL shorteners)
    shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd', 'buff.ly', 'tiny.cc']
    if any(shortener in url for shortener in shorteners):
        features['TinyURL'] = 1
    else:
        features['TinyURL'] = 0
        
    # 6. Prefix/Suffix (Checks for a hyphen in the domain)
    if '-' in domain:
        features['Prefix/Suffix'] = 1
    else:
        features['Prefix/Suffix'] = 0
        
    return pd.Series(features)

def run_extraction():
    input_path = '../data/processed/master_dataset.csv'
    output_path = '../data/processed/extracted_features.csv'
    
    print(f"Loading master dataset from {input_path}...")
    df = pd.read_csv(input_path)
    
    print(f"Extracting features for {len(df)} URLs. This may take a minute or two...")
    
    # Apply our feature extraction function to every URL in the dataframe
    # This creates a new dataframe containing only our 6 feature columns
    features_df = df['url'].apply(check_features)
    
    # We append the original raw URL text and the 'label' (answer key) to our features
    features_df['url'] = df['url']
    features_df['label'] = df['label']
    
    # Save the strictly numerical dataset ready for the Neural Network
    features_df.to_csv(output_path, index=False)
    
    print(f"Success! Numerical features saved to {output_path}")
    print(features_df.head())

if __name__ == "__main__":
    run_extraction()