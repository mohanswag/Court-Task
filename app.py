from flask import Flask, render_template, request
from scraper import fetch_case_data
from models import log_case_query

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']
        
        data, raw_html = fetch_case_data(case_type, case_number, filing_year)
        log_case_query(case_type, case_number, filing_year, raw_html)
        
        return render_template('result.html', data=data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
