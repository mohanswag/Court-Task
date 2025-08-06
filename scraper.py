def fetch_case_data(case_type, case_number, filing_year):
    # Dummy scraped data (replace with actual scraping later)
    data = {
        'parties': 'Ramesh vs Suresh',
        'filing_date': '2024-01-10',
        'next_hearing': '2025-09-15',
        'latest_order': 'https://example.com/latest-order.pdf'
    }
    raw_html = '<html>Mock court site HTML...</html>'
    return data, raw_html
