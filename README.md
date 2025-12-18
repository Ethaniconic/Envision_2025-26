# Envision - Grey Market Product Detection

A comprehensive web scraping and machine learning project to identify counterfeit and grey market products from e-commerce platforms.

## Project Overview

This project scrapes product listings from e-commerce websites (Snapdeal) and uses machine learning techniques to classify products as legitimate or grey market (counterfeit/replica) items. The classifier analyzes product titles, pricing anomalies, and seller information to detect suspicious listings.

## Features

- **Automated Web Scraping**: Collects product data including titles, prices, MRP, review counts, and product links
- **Grey Market Detection**: Automatically labels suspicious products based on keyword analysis and pricing patterns
- **Data Processing**: Cleans and preprocesses raw scraping data for ML model training
- **Duplicate Prevention**: Avoids collecting duplicate products using unique product links
- **Polite Scraping**: Implements random delays between requests to avoid IP blocking

## Project Structure

```
Envision/
├── 1-Scraper.ipynb              # Main scraping and data processing notebook
├── general_market_analysis.csv   # Generated dataset (sample output)
├── snapdeal_mass_dataset.csv     # Final scraped dataset with labels
├── env/                          # Python virtual environment
└── README.md                     # This file
```

## Setup

### Prerequisites

- Python 3.8+
- Windows/Linux/macOS

### Installation

1. Navigate to the project directory:
```bash
cd c:\Users\Lenovo\Documents\Envision
```

2. Activate the virtual environment:
```bash
# Windows
env\Scripts\activate

# Linux/macOS
source env/bin/activate
```

3. Install required packages (if not already installed):
```bash
pip install requests beautifulsoup4 pandas numpy selenium
```

## Usage

### Running the Scraper

Open `1-Scraper.ipynb` in Jupyter Notebook or VS Code:

```bash
jupyter notebook 1-Scraper.ipynb
```

Or run directly in VS Code's notebook interface.

### Scraper Configuration

Edit the `keywords` list in the notebook to target different product categories:

```python
keywords = [
    "first copy watches",
    "replica shoes",
    "imported headphones",
    "analog watch men",
    "running shoes"
]
```

The scraper will collect up to 100 items per keyword from Snapdeal.

## Data Schema

The generated CSV contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `Search_Term` | string | Product search keyword |
| `Product_Title` | string | Product name/title |
| `Selling_Price` | float | Listed price in rupees |
| `MRP` | float | Maximum retail price |
| `Discount_Pct` | float | Discount percentage |
| `Review_Count` | string | Number of customer reviews |
| `Product_Link` | string | Direct product URL |
| `Is_Grey_Market` | int | Target variable (0=Legitimate, 1=Grey Market) |

## Grey Market Detection Logic

Products are flagged as suspicious based on:

1. **Keyword Analysis**: Presence of terms like 'copy', 'replica', 'compatible with', '7a', 'import'
2. **Price Anomalies**: 
   - Watches priced below ₹400
   - Suspiciously high discounts (>80% off)
3. **Risk Score**: Products with cumulative risk score ≥ 30 are labeled as grey market

## Output Files

- **snapdeal_mass_dataset.csv**: Main output file containing all scraped products with grey market labels
- **general_market_analysis.csv**: Alternative dataset format for analysis

## Technical Details

### Dependencies

- **requests**: HTTP library for making web requests
- **BeautifulSoup4**: HTML/XML parsing
- **pandas**: Data manipulation and CSV handling
- **numpy**: Numerical computations
- **Selenium**: Browser automation (optional, for JavaScript-heavy sites)

### Key Functions

- `check_suspicious()`: Determines if a product is likely grey market based on heuristics
- Main scraping loop: Iterates through keywords, paginating with offset parameter

## Performance Notes

- Each keyword collection target: 100 items
- Random delay between requests: 2-4 seconds
- Snapdeal pagination: 20 items per page
- Estimated scraping time: ~30-45 minutes for full dataset

## Limitations & Considerations

⚠️ **Important**: 
- This scraper is for educational purposes only
- Always check the website's `robots.txt` and terms of service before scraping
- Excessive scraping may result in IP blocking
- Use responsibly with appropriate delays between requests

## Future Enhancements

- [ ] Implement Selenium for JavaScript-rendered content
- [ ] Add support for multiple e-commerce platforms
- [ ] Build ML classification model (Random Forest, XGBoost)
- [ ] Create web dashboard for results visualization
- [ ] Implement caching to avoid re-scraping
- [ ] Add proxy rotation for better reliability

## Contributing

To contribute or modify the scraper:

1. Test changes in a isolated environment
2. Update relevant sections in this README
3. Ensure no hardcoded credentials are committed

## License

Educational use only. Use responsibly and ethically.

## Support

For issues or questions:
- Check the notebook for detailed comments and logic
- Verify internet connection and target website accessibility
- Ensure all dependencies are correctly installed

---

**Last Updated**: December 18, 2025  
**Version**: 1.0