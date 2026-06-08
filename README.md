# ⚽ SofaScore Multi-Season Football Data Scraping Pipeline

An automated Python-based data pipeline that extracts historical football player statistics from SofaScore using the **ScraperFC** library.

The tool allows you to collect player performance data across multiple leagues and seasons in a single run, making it ideal for:

* Football Analytics
* Player Scouting
* Data Visualization
* Machine Learning Projects
* Performance Analysis

---

## 🚀 Features

### 🌍 Multi-League & Multi-Season Support

Extract data from multiple leagues and seasons at once through a simple command-line interface.

### 📊 Automatic Metadata Tracking

Every record is automatically tagged with:

* League Name
* Season

This makes it easy to combine and analyze data across competitions.

### 🛡️ Data Quality Protection

The pipeline automatically removes duplicate columns before merging datasets, preventing common dataframe errors.

### ⏱️ Safe Scraping

Built-in delays between requests help reduce server load and lower the risk of temporary blocking.

### 📈 BI-Friendly Output

Exports data in **UTF-8-SIG** format, ensuring player names and special characters display correctly in:

* Power BI
* Tableau
* Excel

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Armaan7781/SofaScore-Web-Scraping.git
cd SofaScore-Web-Scraping
```

## 2️⃣ Install Dependencies

```bash
pip install pandas ScraperFC
```

---

# ▶️ How to Run

Launch the script and provide the league(s) and season(s) you want to scrape.

Example:

```text
============================================================
🚀 WELCOME TO THE HISTORICAL FOOTBALL DATA EXTRACTION PIPELINE
============================================================

⚽ Enter league(s):
Spain La Liga, England Premier League

📅 Enter season(s):
23/24, 24/25
```

The pipeline will automatically:

1. Extract data for each league
2. Extract data for each season
3. Merge all datasets
4. Export a master CSV file

Example Output:

```text
🏆 Processing League: Spain La Liga
📥 Pulling player stats for 23/24...
✅ Successfully processed 540 records.

🏆 Processing League: England Premier League
📥 Pulling player stats for 24/25...
✅ Successfully processed 589 records.

🎉 PIPELINE EXECUTION SUCCESS
Master file saved successfully.
Total dataset volume: 2243 player-season records.
```

---

# 📂 Output

The scraper generates a consolidated CSV dataset containing player statistics across all selected leagues and seasons.

Typical columns include:

| Column      | Description               |
| ----------- | ------------------------- |
| player_name | Player Name               |
| team_name   | Club Name                 |
| league_name | Competition Name          |
| season_year | Season                    |
| goals       | Goals Scored              |
| assists     | Assists                   |
| ...         | 50+ additional statistics |

---

# 📋 Supported Competitions

### Domestic Leagues

* England Premier League
* England EFL Championship
* Spain La Liga
* Spain La Liga 2
* Germany Bundesliga
* Germany 2. Bundesliga
* Italy Serie A
* Italy Serie B
* France Ligue 1
* France Ligue 2
* Netherlands Eredivisie
* Portugal Primeira Liga
* Saudi Arabia Pro League
* MLS
* Liga MX
* And many more...

### International Competitions

* FIFA World Cup
* FIFA Women's World Cup
* UEFA Champions League
* UEFA Europa League
* UEFA Conference League
* UEFA European Championship
* CONMEBOL Copa Libertadores
* CONCACAF Gold Cup

---

# 📊 Use Cases

* Football Performance Analysis
* Player Scouting
* Recruitment Models
* Dashboard Development
* Statistical Research
* Machine Learning Feature Engineering

---

# 🛠 Tech Stack

* Python
* Pandas
* ScraperFC
* SofaScore Data

---

# ⚠️ Disclaimer

This project is intended for educational, research, and football analytics purposes only.

Please use responsible scraping practices and respect the terms and limitations of public data sources.

---

## ⭐ Support

If you find this project useful, consider giving the repository a star.

Contributions, suggestions, and improvements are always welcome.
