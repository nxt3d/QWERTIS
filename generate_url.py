import base64
import urllib.parse

def create_data_url():
    # Read files
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    with open('favicon.svg', 'r', encoding='utf-8') as f:
        svg_content = f.read()
        
    # Create Favicon Data URL
    svg_b64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    favicon_data_url = f"data:image/svg+xml;base64,{svg_b64}"
    
    # Embed Favicon in HTML
    html_content = html_content.replace('href="favicon.svg"', f'href="{favicon_data_url}"')
    
    # Create HTML Data URL (Base64 encoded for safety/compactness)
    html_b64 = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    full_data_url = f"data:text/html;base64,{html_b64}"
    
    # Write to file
    with open('game_data_url.txt', 'w', encoding='utf-8') as f:
        f.write(full_data_url)
        
    print(f"Data URL generated! Length: {len(full_data_url)} characters")
    print("Created 'game_data_url.txt'")

if __name__ == "__main__":
    create_data_url()
