# COVID-19 Global Data Tracker

## Project Description
A data analysis and reporting project that tracks global COVID-19 trends. The project analyzes cases, deaths, recoveries, and vaccinations across countries and time, using real-world data. It provides visualizations and insights suitable for presentation or publishing.

## Objectives
- Import and clean COVID-19 global data
- Analyze time trends (cases, deaths, vaccinations)
- Compare metrics across countries/regions
- Visualize trends with charts and maps
- Communicate findings in a Jupyter Notebook or PDF report

## Tools and Libraries Used
- Python 3.x
- pandas
- matplotlib
- seaborn
- ipywidgets (for interactivity in Jupyter)
- streamlit (for optional dashboard)

## How to Run/View the Project
1. **Clone the repository and navigate to the project folder.**
2. **Install dependencies:**
   ```bash
   pip install pandas matplotlib seaborn ipywidgets streamlit
   ```
3. **Download the latest COVID-19 data:**
   ```bash
   curl -L -o owid-covid-data.csv https://covid.ourworldindata.org/data/owid-covid-data.csv
   ```
4. **To run the analysis and view visualizations:**
   - Open `main.py` as a script, or convert it to a Jupyter Notebook for a more interactive experience.
   - For interactive widgets, use Jupyter Notebook.
   - For the dashboard, run:
     ```bash
     streamlit run main.py
     ```

## Insights & Reflections
- The project demonstrates how different countries experienced and responded to the COVID-19 pandemic.
- Visualizations reveal trends in cases, deaths, and vaccination rollouts.
- The analysis highlights the importance of data-driven decision making in public health.
- The project can be extended with more interactivity, additional metrics (e.g., hospitalizations), or more advanced visualizations (e.g., choropleth maps). 