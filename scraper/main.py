
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os


excel_file_path = 'Scrapping Python Assigment- Flair Insights.xlsx'
df = pd.read_excel(excel_file_path, header=None)  


output_folder = 'scraped_data'
os.makedirs(output_folder, exist_ok=True)

# Function to scrape data
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information
        title = soup.title.string if soup.title else ''
        text = soup.get_text()
        
        images = [img['src'] if img.get('src') else '' for img in soup.find_all('img')]
        links = [link['href'] for link in soup.find_all('a', href=True)]
        
        return {
            'URL': url,
            'Title': title,
            'Text': text,
            'Images': images,
            'Links': links
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Scrape data for each website
scraped_data = []
for index, row in df.iterrows():
    website_url = row[0]  
    data = scrape_website(website_url)
    if data:
        scraped_data.append(data)

# Save the scraped data to a CSV file
output_file_path = os.path.join(output_folder, 'scraped_data.csv')
df_output = pd.DataFrame(scraped_data)
df_output.to_csv(output_file_path, index=False)

# # Save the scraped data to a JSON file
# output_file_path = os.path.join(output_folder, 'scraped_data.json')
# with open(output_file_path, 'w') as json_file:
#     json.dump(scraped_data, json_file, indent=4)

print(f"Scraped data saved to {output_file_path}")


